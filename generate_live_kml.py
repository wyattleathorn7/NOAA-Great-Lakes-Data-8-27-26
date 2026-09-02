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
    # Add shared buoy style: native Point via standard icon, Small icon/label, no custom PNG
    # Use explicit href so Google Earth Web renders icon (no href = no icon in data layer mode)
    # Keep Small sizes (scale 0.7) as requested, preserve native Point appearance
    buoy_style = ET.Element(f"{{{KML_NS}}}Style", id="buoyStyle")
    icon_style = ET.SubElement(buoy_style, f"{{{KML_NS}}}IconStyle")
    icon_scale = ET.SubElement(icon_style, f"{{{KML_NS}}}scale")
    icon_scale.text = "1.0"
    icon = ET.SubElement(icon_style, f"{{{KML_NS}}}Icon")
    icon_href = ET.SubElement(icon, f"{{{KML_NS}}}href")
    icon_href.text = "icons/noaa_buoy_512.png"
    label_style = ET.SubElement(buoy_style, f"{{{KML_NS}}}LabelStyle")
    label_color = ET.SubElement(label_style, f"{{{KML_NS}}}color")
    label_color.text = "ffffffff"
    label_scale = ET.SubElement(label_style, f"{{{KML_NS}}}scale")
    label_scale.text = "0.7"
    # Insert as first child of Document
    doc_elem = root.find(f"{{{KML_NS}}}Document")
    if doc_elem is not None:
        doc_elem.insert(0, buoy_style)
    else:
        root.insert(0, buoy_style)
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
    audit = {"used_noaa": [], "used_glos": [], "offline": [], "unresolved": [],
             "identity_failures": [], "both_failed": [], "no_source": []}

    def resolve(index, placemark):
        return G.resolve_placemark(index, placemark, fetcher, stations, platforms,
                                  parameter_names, prior_map, audit)

    with ThreadPoolExecutor(max_workers=16) as pool:
        jobs = [pool.submit(resolve, i, p) for i, p in enumerate(placemarks)]
        for job in as_completed(jobs):
            index, name, result, attempts = job.result()
            records[index] = (name, result or {"raw": False, "parsed": False, "record": {}}, attempts or {})

    previous_descriptions = {
        index: G.text_of(placemark.find(f"{{{KML_NS}}}description"))
        for index, placemark in enumerate(placemarks)
    }

    for index, placemark in enumerate(placemarks):
        name, result, attempts = records[index]
        description = placemark.find(f"{{{KML_NS}}}description")
        if description is None:
            description = ET.SubElement(placemark, f"{{{KML_NS}}}description")
        original_link = G.extract_original_link(previous_descriptions[index])
        body = G.render_description(name, result, attempts, fetched_at, original_link)
        description.text = body
        # Ensure each Placemark uses the shared buoyStyle (native Point, Small icon/label)
        style_url = placemark.find(f"{{{KML_NS}}}styleUrl")
        if style_url is None:
            style_url = ET.Element(f"{{{KML_NS}}}styleUrl")
            placemark.insert(0, style_url)
        style_url.text = "#buoyStyle"

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

    # NetworkLink KML pointing at the public URL — mirrors AIS NetworkLink (300s, onInterval, never).
    netlink = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
        "  <NetworkLink>\n"
        "    <name>Great Lakes Live Buoys (auto-refresh)</name>\n"
        "    <Link>\n"
        f"      <href>{html.escape(base_url.rstrip('/'))}/live_buoys.kml</href>\n"
        "      <refreshMode>onInterval</refreshMode>\n"
        "      <refreshInterval>300</refreshInterval>\n"
        "      <viewRefreshMode>never</viewRefreshMode>\n"
        "    </Link>\n"
        "  </NetworkLink>\n"
        "</kml>\n"
    )
    NETLINK_KML.write_text(netlink, encoding="utf-8")

    print(f"Created {LIVE_KML}")
    print(f"Created {NETLINK_KML}")
    online = sum(records[i][1].get("status") == "online" for i in range(len(placemarks)))
    offline = sum(records[i][1].get("status") == "offline" for i in range(len(placemarks)))
    unresolved = sum(records[i][1].get("status") == "unresolved" for i in range(len(placemarks)))
    print(f"Placemark/coordinate counts: {len(placemarks)}/{len(candidate_coords)}; NetworkLinks in source: {len(links)}")
    print(f"ONLINE: {online}; OFFLINE: {offline}; UNRESOLVED: {unresolved}")
    print(f"Titles preserved: {'PASS' if candidate_names == original_names else 'FAIL'}; "
          f"Coordinates preserved: {'PASS' if candidate_coords == original_coords else 'FAIL'}; "
          f"Folders preserved: {'PASS' if candidate_folders == original_folders else 'FAIL'}")
    print(f"NetworkLink points to: {base_url.rstrip('/')}/live_buoys.kml")


if __name__ == "__main__":
    base = os.environ.get("KML_BASE_URL", "REPLACE_WITH_YOUR_GITHUB_PAGES_URL")
    run(base, force=True)
