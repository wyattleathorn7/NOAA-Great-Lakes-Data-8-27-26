#!/usr/bin/env python3
"""Live Great Lakes buoy KML generator for GitHub Pages + NetworkLink refresh.

Reuses the exact-identity resolution logic from repair_live_buoys_candidate.py
(already audited: no nearby-platform substitution, per-platform variables,
Observed vs Fetched separation). It emits:

  docs/live_buoys.kml                 -> 256 placemarks, plain KML, live data
  docs/live_buoys_networklink.kml     -> NetworkLink to the public Pages URL

The public base URL is taken from the KML_BASE_URL environment variable
(the GitHub Actions workflow computes it from the repository). A placeholder is
used only for local testing and must be replaced by a real public HTTPS URL for
Google Earth Web/mobile to refresh.
"""

import html
import os
import re
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET

import repair_live_buoys_candidate as G

ROOT = Path(__file__).resolve().parent
SOURCE = G.SOURCE
DOCS = ROOT / "docs"
LIVE_KML = DOCS / "live_buoys.kml"
NETLINK_KML = DOCS / "live_buoys_networklink.kml"
KML_NS = G.KML_NS
ET = G.ET


def run(base_url, force=False):
    if LIVE_KML.exists() and not force and "--force" not in sys.argv[1:]:
        raise SystemExit(f"Refusing to overwrite existing output: {LIVE_KML}")
    fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    fetcher = G.Fetcher()
    DOCS.mkdir(exist_ok=True)
    with __import__("zipfile").ZipFile(SOURCE) as archive:
        source_doc = archive.read("doc.kml")
    root = ET.fromstring(source_doc)
    placemarks = root.findall(f".//{{{KML_NS}}}Placemark")
    links = root.findall(f".//{{{KML_NS}}}NetworkLink")
    original_names = [G.text_of(p.find(f"{{{KML_NS}}}name")) for p in placemarks]
    original_coords = [G.text_of(p.find(f".//{{{KML_NS}}}coordinates")) for p in placemarks]
    original_folders = [G.text_of(f.find(f"{{{KML_NS}}}name"))
                        for f in root.findall(f".//{{{KML_NS}}}Folder")]
    stations, _ = G.noaa_station_list(fetcher)
    platforms = G.catalog_platforms()
    parameter_names, _ = G.glos_parameter_map(fetcher)
    prior_map = G.prior_identity_map()
    records = {}
    audit = {"used_noaa": [], "used_glos": [], "both_failed": [], "no_source": []}

    def resolve(index, placemark):
        name = G.text_of(placemark.find(f"{{{KML_NS}}}name"))
        description = G.text_of(placemark.find(f"{{{KML_NS}}}description"))
        coordinate = placemark.find(f".//{{{KML_NS}}}coordinates")
        if coordinate is None or not coordinate.text:
            return index, name, None, None
        values = coordinate.text.strip().split(",")
        try:
            lon, lat = float(values[0]), float(values[1])
        except (ValueError, IndexError):
            return index, name, None, None
        prior = G.prior_for_name(name, prior_map)
        water_match = re.search(r"(?<!\d)(\d{7})(?!\d)", name)
        coops_id = water_match.group(1) if water_match else None
        platform = G.identity_platform(name, description, prior, platforms, lon, lat)
        noaa_ids = G.explicit_noaa_ids(name, description, prior, stations, platform)
        explicit_station = next((sid for sid in noaa_ids if sid in stations), None)
        station = None
        if coops_id and ("WATER LEVEL" in name.upper() or coops_id not in stations):
            coops = G.coops_record(fetcher, coops_id)
            noaa = coops
            noaa_attempts_detail = [coops]
        else:
            station = explicit_station or (noaa_ids[0] if noaa_ids else None)
            noaa_attempts_detail, noaa = G.noaa_attempts(fetcher, station)
            if station:
                noaa["station"] = station
                noaa["authoritative_url"] = f"https://www.ndbc.noaa.gov/station_page.php?station={station}"
        if noaa.get("parsed"):
            audit["used_noaa"].append(name)
            noaa["lookup"] = "queried and parsed"
            noaa["alternate_attempts"] = noaa_attempts_detail
            return index, name, noaa, {"noaa": noaa, "noaa_alternates": noaa_attempts_detail, "glos": {"lookup": "not queried because NOAA was usable"}}
        glos = G.glos_api_record(fetcher, platform, parameter_names)
        glos_routes = [glos]
        if platform and not glos.get("parsed"):
            metadata, _ = G.erddap_metadata(fetcher, platform["dataset"])
            if metadata:
                erddap = G.erddap_record(fetcher, platform, metadata)
                erddap["route"] = "ERDDAP tabledap fallback"
                glos_routes.append(erddap)
                if erddap.get("parsed"):
                    glos = erddap
        if glos.get("parsed"):
            audit["used_glos"].append(name)
            glos["lookup"] = "queried and parsed"
            return index, name, glos, {"noaa": noaa, "noaa_alternates": noaa_attempts_detail, "glos": glos, "glos_routes": glos_routes}
        noaa["alternate_attempts"] = noaa_attempts_detail
        if station or platform:
            audit["both_failed"].append(name)
        else:
            audit["no_source"].append(name)
        return index, name, noaa if noaa.get("raw") else glos, {"noaa": noaa, "noaa_alternates": noaa_attempts_detail, "glos": glos, "glos_routes": glos_routes}

    with ThreadPoolExecutor(max_workers=16) as pool:
        jobs = [pool.submit(resolve, i, p) for i, p in enumerate(placemarks)]
        for job in as_completed(jobs):
            index, name, result, attempts = job.result()
            records[index] = (name, result or {"raw": False, "parsed": False, "record": {}}, attempts or {})

    for index, placemark in enumerate(placemarks):
        name, result, attempts = records[index]
        description = placemark.find(f"{{{KML_NS}}}description")
        if description is None:
            description = ET.SubElement(placemark, f"{{{KML_NS}}}description")
        if result.get("parsed"):
            body = G.display_values(result)
            observed = G.timestamp_text(result["record"])
            source_url = result.get("authoritative_url", result.get("url", ""))
            source = f"<b>Source:</b> {html.escape(result['source'])}<br/><a href=\"{html.escape(source_url, quote=True)}\">Authoritative live source</a><br/>"
            body = f"{body}<br/><br/><b>Observed source timestamp:</b> {observed or 'Unparseable'}<br/><b>Fetched runtime:</b> {fetched_at}<br/>{source}"
        else:
            body = f"<b>Data unavailable:</b> {html.escape(str(result.get('error', 'no authoritative observation row returned')))}.<br/><br/><b>Observed source timestamp:</b> none<br/><b>Fetched runtime:</b> {fetched_at}<br/>"
            if result.get("url"):
                body += f"<b>Attempted source:</b> <a href=\"{html.escape(result['url'], quote=True)}\">{html.escape(result.get('source', 'live source'))}</a><br/>"
        description.text = f"<b>{html.escape(name)}</b><br/><br/>{body}"

    candidate_names = [G.text_of(p.find(f"{{{KML_NS}}}name")) for p in placemarks]
    candidate_coords = [G.text_of(p.find(f".//{{{KML_NS}}}coordinates")) for p in placemarks]
    candidate_folders = [G.text_of(f.find(f"{{{KML_NS}}}name"))
                         for f in root.findall(f".//{{{KML_NS}}}Folder")]

    # Plain KML (no ZIP) so GitHub Pages serves it directly over HTTPS.
    xml_bytes = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    xml_text = xml_bytes.decode("utf-8")
    xml_text = re.sub(r"<description>(.*?)</description>",
                      lambda m: "<description><![CDATA[" + html.unescape(m.group(1)) + "]]></description>",
                      xml_text, flags=re.DOTALL)
    LIVE_KML.write_text(xml_text, encoding="utf-8")

    # NetworkLink KML pointing at the public URL.
    netlink = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
        "  <NetworkLink>\n"
        "    <name>Great Lakes Live Buoys (auto-refresh)</name>\n"
        "    <Link>\n"
        f"      <href>{html.escape(base_url.rstrip('/'))}/live_buoys.kml</href>\n"
        "      <refreshMode>onInterval</refreshMode>\n"
        "      <refreshInterval>900</refreshInterval>\n"
        "      <viewRefreshMode>never</viewRefreshMode>\n"
        "    </Link>\n"
        "  </NetworkLink>\n"
        "</kml>\n"
    )
    NETLINK_KML.write_text(netlink, encoding="utf-8")

    print(f"Created {LIVE_KML}")
    print(f"Created {NETLINK_KML}")
    print(f"Placemark/coordinate counts: {len(placemarks)}/{len(candidate_coords)}; NetworkLinks in source: {len(links)}")
    print(f"NOAA used: {len(audit['used_noaa'])}; GLOS used: {len(audit['used_glos'])}; both failed: {len(audit['both_failed'])}")
    print(f"Titles preserved: {'PASS' if candidate_names == original_names else 'FAIL'}; "
          f"Coordinates preserved: {'PASS' if candidate_coords == original_coords else 'FAIL'}; "
          f"Folders preserved: {'PASS' if candidate_folders == original_folders else 'FAIL'}")
    print(f"NetworkLink points to: {base_url.rstrip('/')}/live_buoys.kml")


if __name__ == "__main__":
    base = os.environ.get("KML_BASE_URL", "REPLACE_WITH_YOUR_GITHUB_PAGES_URL")
    run(base, force=True)
