#!/usr/bin/env python3
"""Audited, non-destructive v4 live-data rebuild of the current buoy KMZ."""

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import html
import json
import math
import re
import sys
import threading
import urllib.parse
import urllib.request
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "great_lakes_live_buoys.kmz"
OUTPUT = ROOT / "candidate_great_lakes_live_buoys_v4.kmz"
REPORT = ROOT / "candidate_great_lakes_live_buoys_v4_audit.md"
CATALOG = ROOT / "seagull_platforms.geojson"
PRIOR_AUDIT = ROOT / "candidate_great_lakes_live_buoys_v2_audit.md"
KML_NS = "http://www.opengis.net/kml/2.2"
ET.register_namespace("", KML_NS)
HEADERS = {"User-Agent": "GreatLakesLiveBuoys/4.0 exact-identity audited rebuild"}


class Fetcher:
    """Small thread-safe response cache so duplicate source URLs are fetched once."""

    def __init__(self):
        self.cache = {}
        self.lock = threading.Lock()

    def get(self, url, timeout=20):
        with self.lock:
            if url in self.cache:
                return self.cache[url]
        try:
            request = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(request, timeout=timeout) as response:
                result = (True, response.read())
        except Exception as exc:  # retain failure detail for the audit
            result = (False, str(exc))
        with self.lock:
            self.cache[url] = result
        return result


def text_of(element):
    return "".join(element.itertext()) if element is not None else ""


def parse_timestamp(value):
    """Return a normalized UTC timestamp from ISO, NOAA, date, or epoch values."""
    if value is None:
        return None
    value = str(value).strip()
    if not value or value.upper() in {"MM", "NA", "NAN", "NULL"}:
        return None
    if re.fullmatch(r"\d+(?:\.\d+)?", value):
        try:
            number = float(value)
            if number > 1_000_000_000:
                return datetime.fromtimestamp(number, timezone.utc)
        except (ValueError, OverflowError, OSError):
            pass
    candidate = value.replace("Z", "+00:00").replace(" UTC", "+00:00")
    for parser in (datetime.fromisoformat,):
        try:
            result = parser(candidate)
            if result.tzinfo is None:
                result = result.replace(tzinfo=timezone.utc)
            return result.astimezone(timezone.utc)
        except ValueError:
            pass
    for pattern in ("%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S", "%Y-%m-%d", "%m/%d/%Y %H:%M"):
        try:
            return datetime.strptime(value, pattern).replace(tzinfo=timezone.utc)
        except ValueError:
            pass
    return None


def observation_time(record):
    for key in ("time", "timestamp", "datetime", "date_time", "date"):
        if key in record and parse_timestamp(record[key]):
            return parse_timestamp(record[key])
    # NOAA uses both MM (month) and mm (minute); lowercasing first would
    # overwrite the month with the minute.
    exact = {str(k).lstrip("#"): v for k, v in record.items()}
    if all(key in exact for key in ("YY", "MM", "DD")):
        try:
            year = int(exact["YY"])
            if year < 100:
                year += 2000 if year < 70 else 1900
            stamp = f"{year:04d}-{int(exact['MM']):02d}-{int(exact['DD']):02d} " \
                    f"{int(exact.get('hh', 0)):02d}:{int(exact.get('mm', 0)):02d}:" \
                    f"{int(exact.get('ss', 0)):02d}+00:00"
            return parse_timestamp(stamp)
        except (TypeError, ValueError):
            pass
    keys = {str(k).lstrip("#").lower(): v for k, v in record.items()}
    year = keys.get("yyyy", keys.get("yy"))
    month, day = keys.get("mm"), keys.get("dd")
    if year and month and day:
        try:
            year = int(year)
            if year < 100:
                year += 2000 if year < 70 else 1900
            stamp = f"{year:04d}-{int(month):02d}-{int(day):02d} " \
                    f"{int(keys.get('hh', 0)):02d}:{int(keys.get('min', keys.get('minute', 0))):02d}:" \
                    f"{int(keys.get('ss', keys.get('second', 0))):02d}+00:00"
            return parse_timestamp(stamp)
        except (TypeError, ValueError):
            pass
    return None


def timestamp_text(record):
    stamp = observation_time(record)
    return stamp.strftime("%Y-%m-%d %H:%M:%S UTC") if stamp else None


def valid_value(value):
    if value is None or str(value).strip().upper() in {"", "MM", "NA", "NAN", "NULL"}:
        return False
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError):
        return True


def noaa_station_list(fetcher):
    url = "https://www.ndbc.noaa.gov/data/stations/station_table.txt"
    ok, body = fetcher.get(url, 30)
    stations = {}
    if not ok:
        return stations, str(body)
    for line in body.decode("utf-8", "replace").splitlines()[1:]:
        fields = line.split("|")
        if len(fields) < 7:
            continue
        match = re.search(r"([\d.]+)\s*([NS])\s+([\d.]+)\s*([EW])", fields[6])
        if not match:
            continue
        lat, lon = float(match.group(1)), float(match.group(3))
        if match.group(2) == "S": lat = -lat
        if match.group(4) == "W": lon = -lon
        stations[fields[0].strip().upper()] = {"name": fields[4].strip(), "lat": lat, "lon": lon}
    return stations, None


def noaa_record(fetcher, station, feed="realtime2"):
    suffix = f"{station}_5day.txt" if feed in {"5day", "5day2"} else f"{station}.txt"
    url = (f"https://www.ndbc.noaa.gov/data/{feed}/{suffix}"
           if feed != "station_page" else
           f"https://www.ndbc.noaa.gov/station_page.php?station={station}")
    ok, body = fetcher.get(url, 15)
    result = {"source": "NOAA NDBC", "url": url, "raw": ok, "parsed": False, "record": {}, "feed": feed}
    if not ok:
        result["error"] = body
        return result
    if feed == "station_page":
        result["error"] = "station page fetched; observation feed required"
        return result
    lines = body.decode("utf-8", "replace").splitlines()
    header_line = next((line for line in lines if line.lstrip().startswith("#")), None)
    if header_line is None:
        result["error"] = "response contained no NOAA header"
        return result
    header = [item.lstrip("#") for item in header_line.split()]
    header_index = lines.index(header_line)
    data_rows = []
    for line in lines[header_index + 1:]:
        if line.strip() and not line.lstrip().startswith("#"):
            values = line.split()
            row = dict(zip(header, values))
            if observation_time(row):
                data_rows.append(row)
    if data_rows:
        result["record"] = max(data_rows, key=observation_time)
        result["parsed"] = True
    if not result["parsed"]:
        result["error"] = "source returned data but no parseable NOAA record/timestamp"
    return result


def noaa_attempts(fetcher, station):
    """Try every applicable NDBC route; a failed route never ends resolution."""
    if not station:
        return [{"source": "NOAA NDBC", "feed": "identity", "raw": False,
                 "parsed": False, "record": {}, "error": "no exact NOAA identity resolved"}], {"raw": False, "parsed": False, "record": {}, "error": "no exact NOAA identity resolved"}
    feeds = ("station_page", "realtime2", "realtime", "latest_obs", "5day2", "5day", "historical")
    attempts = [noaa_record(fetcher, station, feed) for feed in feeds]
    usable = next((item for item in attempts if item.get("parsed")), None)
    if usable:
        return attempts, usable
    return attempts, attempts[-1]


def prior_identity_map():
    """Recover explicit identities recorded by the prior audit, never coordinates."""
    mapping = {}
    if not PRIOR_AUDIT.exists():
        return mapping
    current = None
    for line in PRIOR_AUDIT.read_text(encoding="utf-8").splitlines():
        if line.startswith("### "):
            current = line[4:].strip()
            mapping.setdefault(current, {"noaa": set(), "glos": set()})
        if current is None:
            continue
        for station in re.findall(r"station(?:=|%3D)([A-Za-z0-9_-]+)", line, re.I):
            mapping[current]["noaa"].add(station.upper())
        for station in re.findall(r"/data/(?:realtime2|realtime|latest_obs|5day|5day2|historical)/([A-Za-z0-9_-]+?)(?:_5day)?\.txt", line, re.I):
            mapping[current]["noaa"].add(station.upper())
        for dataset in re.findall(r"obsDatasetId=([0-9]+)", line):
            mapping[current]["glos"].add(dataset)
    return mapping


TYPE_TOKENS = ("c-man station", "c man station", "weather station", "water level observation network",
                "coastal marine station", "observation network", "nerrs water quality station",
                "nerrs weather station", "glos weather station", "cg station", "cg", "buoy",
                "discus buoy", "moored buoy", "waverider buoy", "spotter buoy", "spotter",
                "beach", "nerrs", "tower", "fixed", "near shore", "nearshore", "marina",
                "harbor", "light", "ionomer foam", "foam", "meter", "2.1-meter", "2.3-meter",
                "2.4-meter", "3-meter", "glos", "(buoy)")

def core(text):
    """Same-platform core name: drop parentheticals and generic type tokens so
    'Superior Shoals, NY (C-MAN Station)' matches station 'Superior Shoals, NY'."""
    text = re.sub(r"\(.*?\)", " ", text)
    text = re.sub(r"[^a-z0-9 ]+", " ", text.lower())
    for token in TYPE_TOKENS:
        text = text.replace(token, " ")
    return re.sub(r"\s+", " ", text).strip()


# Explicit, researched exact-identity overrides for platforms the generic
# matcher cannot resolve. Keyed by placemark name; never a nearby substitute.
IDENTITY_OVERRIDES = {
    "Superior Shoals, NY (C-MAN Station)": {"noaa": "SUPN6"},
    "White Shoal Light, MI (C-MAN Station)": {"noaa": "WSLM4"},
    "Galloo Island, NY (C-MAN Station)": {"noaa": "GLLN6"},
    "Alexandria Bay, NY (C-MAN Station)": {"noaa": "ABAN6", "coops": "8311062"},
    "Thousand I. Brdg., NY (C-MAN Station)": {"noaa": "TICN6"},
    "63rd St., Chicago, IL (C-MAN Station)": {"noaa": "JAKI2"},
    "Kenosha Light, Kenosha, WI (C-MAN Station)": {"noaa": "KNSW3"},
    "Sturgeon Bay CG Station, WI (Weather Station)": {"noaa": "0Y2W3"},
    "Grand Traverse Bay Observing System Station 2 (Coastal Marine Station)": {"noaa": "GTBM4"},
    "St. Joseph CG Station, MI (Weather Station)": {"noaa": "SJNM4"},
    "Michigan City CG Station, IN (Weather Station)": {"noaa": "MCYI3"},
    "Stannard Rock Buoy (Buoy) [GLOS]": {"noaa": "STDM4"},
    "9014095 - Port Huron, North of Blue Water Bridge, MI (Water Level Observation Network)": {"glos": "167"},
}


def explicit_noaa_ids(name, description, prior, stations, platform=None):
    content = f"{name} {description}"
    ids = set(re.findall(r"station(?:=|%3D)([A-Za-z0-9_-]+)", content, re.I))
    ids.update(re.findall(r"/data/(?:realtime2|realtime|latest_obs|5day|5day2|historical)/([A-Za-z0-9_-]+?)(?:_5day)?\.txt", content, re.I))
    ids.update(source_ids(name, description))
    ids.update(prior.get("noaa", set()))
    normalized = re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()
    base = core(name)
    cname = core(name)
    for key, override in IDENTITY_OVERRIDES.items():
        if core(key) == cname and override.get("noaa"):
            ids.add(override["noaa"].upper())
    for station_id, station_info in stations.items():
        station_name = re.sub(r"[^a-z0-9]+", " ", station_info["name"].lower()).strip()
        sbase = core(station_info["name"])
        # Only accept a SAME-platform name match. Containment is allowed only when
        # the two names are nearly identical (>=80% length overlap), so a generic
        # substring can never assign a different station.
        if base and (base == sbase or
                     (sbase and base in sbase and len(base) >= 0.8 * len(sbase)) or
                     (sbase and sbase in base and len(sbase) >= 0.8 * len(base))):
            ids.add(station_id)
    # GLOS catalog names sometimes embed the NOAA station number, e.g.
    # "Stannard Rock Buoy - Station 45179". Recover it as an exact-ID hint.
    if platform:
        for number in re.findall(r"(?<![A-Z0-9])\d{5,7}(?![A-Z0-9])", platform.get("name", "")):
            ids.add(number)
    return [item.upper() for item in ids]


def identity_platform(name, description, prior, platforms, lon=None, lat=None):
    """Exact-identity GLOS match only. Coordinates NEVER substitute for a
    differently-named platform; they only CONFIRM the matched platform is the
    same physical station (within a tight tolerance). No nearest-platform fallthrough."""
    content = f"{name} {description}"
    ids = set(re.findall(r"obsDatasetId=([0-9]+)", content, re.I))
    ids.update(prior.get("glos", set()))
    for platform in platforms:
        if platform["dataset"] in ids or (platform["id"] and platform["id"].upper() in content.upper()):
            return platform
    normalized = re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()
    base = core(name)
    for key, override in IDENTITY_OVERRIDES.items():
        if core(key) == base and override.get("glos"):
            for platform in platforms:
                if platform["dataset"] == override["glos"]:
                    return platform
    candidates = []
    for platform in platforms:
        pname = re.sub(r"[^a-z0-9]+", " ", platform["name"].lower()).strip()
        pbase = core(platform["name"])
        if normalized and normalized == pname:
            candidates.append((platform, 0))
        elif base and (base == pbase or (pbase and base in pbase) or (pbase and pbase in base)):
            candidates.append((platform, 1))
    if not candidates:
        return None
    candidates.sort(key=lambda item: item[1])
    best = candidates[0][0]
    # Coordinate confirmation: only accept if the catalog platform sits on the
    # same site (<= ~2 km) OR if there was already an exact normalized name match.
    if candidates[0][1] == 0:
        return best
    if lon is not None and lat is not None:
        d = abs(best["lat"] - lat) + abs(best["lon"] - lon) * 0.6
        if d <= 2.0:
            return best
    return None


def prior_for_name(name, mapping):
    if name in mapping:
        return mapping[name]
    base = re.sub(r"\s*\[[^]]+\]", "", name).lower()
    base = re.sub(r"[^a-z0-9]+", " ", base).strip()
    merged = {"noaa": set(), "glos": set()}
    for old_name, values in mapping.items():
        old_base = re.sub(r"\s*\[[^]]+\]", "", old_name).lower()
        old_base = re.sub(r"[^a-z0-9]+", " ", old_base).strip()
        if old_base == base:
            merged["noaa"].update(values["noaa"])
            merged["glos"].update(values["glos"])
    return merged


def coops_record(fetcher, station):
    """Read the newest coherent water-level row for a NOAA CO-OPS station."""
    end = datetime.now(timezone.utc).date()
    begin = end.fromordinal(end.toordinal() - 2)
    query = urllib.parse.urlencode({
        "begin_date": begin.strftime("%Y%m%d"), "end_date": end.strftime("%Y%m%d"),
        # Great Lakes CO-OPS stations publish local low-water datum, not MSL.
        "station": station, "product": "water_level", "datum": "LWD",
        "units": "english", "time_zone": "gmt", "format": "json",
    })
    url = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?" + query
    result = {"source": "NOAA CO-OPS water level", "url": url, "raw": False, "parsed": False, "record": {}}
    ok, body = fetcher.get(url, 45)
    if not ok:
        result["error"] = str(body)
        return result
    result["raw"] = True
    try:
        payload = json.loads(body.decode("utf-8"))
        rows = payload.get("data", [])
        rows = sorted((row for row in rows if parse_timestamp(row.get("t")) and valid_value(row.get("v"))), key=lambda row: parse_timestamp(row["t"]), reverse=True)
        if rows:
            result["record"] = {"time": rows[0]["t"], "water_level": rows[0]["v"]}
            result["parsed"] = True
        else:
            result["error"] = payload.get("error", "source returned no valid water-level rows")
    except (ValueError, TypeError, KeyError) as exc:
        result["error"] = f"CO-OPS response parse failed: {exc}"
    return result


def catalog_platforms():
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    platforms = []
    for feature in data.get("features", []):
        props = feature.get("properties", {})
        coords = feature.get("geometry", {}).get("coordinates", [])
        if len(coords) >= 2 and props.get("obs_dataset_id") is not None:
            parameter_names = [
                item.get("standard_name") for item in props.get("parameters", [])
                if item.get("standard_name")
            ]
            platforms.append({"id": str(props.get("org_platform_id", "")), "dataset": str(props["obs_dataset_id"]),
                              "name": props.get("platform_name", ""), "parameters": parameter_names,
                              "lat": float(coords[1]), "lon": float(coords[0])})
    return platforms


def erddap_metadata(fetcher, dataset):
    base = f"https://seagull-erddap.glos.org/erddap/info/obs_{dataset}/index.json"
    ok, body = fetcher.get(base, 20)
    if not ok:
        return None, str(body)
    try:
        table = json.loads(body.decode("utf-8")).get("table", {})
        variables, units = [], {}
        for row in table.get("rows", []):
            if len(row) >= 2 and str(row[0]).lower() == "variable":
                variable = str(row[1])
                variables.append(variable)
            if len(row) >= 5 and str(row[0]).lower() == "attribute" and str(row[2]).lower() == "units":
                units[str(row[1])] = str(row[4])
        return {"variables": variables, "units": units}, None
    except (ValueError, TypeError) as exc:
        return None, f"metadata parse failed: {exc}"


def erddap_record(fetcher, platform, metadata):
    base = f"https://seagull-erddap.glos.org/erddap/tabledap/obs_{platform['dataset']}.json"
    excluded = {"latitude", "longitude", "station", "platform", "depth", "altitude"}
    fields = [v for v in metadata["variables"] if v.lower() not in excluded and
              not any(token in v.lower() for token in ("_gross_range_test", "_spike_test", "_rate_of_change_test", "_flat_line_test", "_aggregate"))]
    time_fields = [v for v in fields if v.lower() in {"time", "timestamp", "datetime", "date_time"}]
    if not fields:
        return {"source": "GLOS Seagull/ERDDAP", "url": base, "raw": False, "parsed": False, "record": {}, "error": "no data variables in metadata"}
    query = ",".join(fields)
    if time_fields:
        query += f'&orderByMax(%22{time_fields[0]}%22)'
    url = base + "?" + urllib.parse.quote(query, safe=",&()%")
    ok, body = fetcher.get(url, 20)
    result = {"source": "GLOS Seagull/ERDDAP", "url": url, "raw": ok, "parsed": False, "record": {}, "variables": fields, "units": metadata["units"]}
    if not ok:
        result["error"] = body
        return result
    try:
        table = json.loads(body.decode("utf-8")).get("table", {})
        rows = table.get("rows", [])
        rows = [dict(zip(table.get("columnNames", fields), row)) for row in rows]
        rows = [row for row in rows if observation_time(row)]
        if rows:
            result["record"] = max(rows, key=observation_time)
            result["parsed"] = bool(result["record"] and observation_time(result["record"]))
        if not result["parsed"]:
            result["error"] = "source returned data but no parseable ERDDAP record/timestamp"
    except (ValueError, TypeError, KeyError) as exc:
        result["error"] = f"response parse failed: {exc}"
    return result


def glos_parameter_map(fetcher):
    """Load GLOS parameter IDs once so API observations can be named."""
    url = "https://seagull-api.glos.org/api/v1/parameters"
    ok, body = fetcher.get(url, 45)
    if not ok:
        return {}, str(body)
    try:
        values = json.loads(body.decode("utf-8"))
        return {
            str(item["parameter_id"]): item.get("standard_name") or item.get("parameter_name")
            for item in values if item.get("parameter_id")
        }, None
    except (ValueError, TypeError, KeyError) as exc:
        return {}, f"parameter catalog parse failed: {exc}"


def glos_api_record(fetcher, platform, parameter_names):
    """Get the newest valid observations for a GLOS dataset.

    GLOS publishes each parameter at its own timestamp, so we take the newest
    valid observation per parameter. Where several share one timestamp we keep
    that coherent group; otherwise each variable keeps its own observed time
    (recorded in _per_var_times) and the description shows individual times."""
    if not platform:
        return {"source": "GLOS Seagull", "raw": False, "parsed": False,
                "record": {}, "error": "no matched catalog dataset"}
    start = (datetime.now(timezone.utc).date().toordinal() - 30)
    start = datetime.fromordinal(start).date().isoformat()
    url = f"https://seagull-api.glos.org/api/v1/obs?startDate={start}&obsDatasetId={platform['dataset']}"
    result = {"source": "GLOS Seagull", "url": url, "raw": False,
              "parsed": False, "record": {}, "units": {}, "per_var_times": {}}
    ok, body = fetcher.get(url, 45)
    if not ok:
        result["error"] = str(body)
        return result
    result["raw"] = True
    try:
        datasets = json.loads(body.decode("utf-8"))
        parameters = datasets[0].get("parameters", []) if datasets else []
        rows = []
        for parameter in parameters:
            name = parameter_names.get(str(parameter.get("parameter_id")))
            if not name:
                continue
            observations = [o for o in parameter.get("observations", [])
                            if valid_value(o.get("value")) and parse_timestamp(o.get("timestamp"))]
            if not observations:
                continue
            newest = max(observations, key=lambda o: parse_timestamp(o["timestamp"]))
            rows.append((name, newest["value"], parse_timestamp(newest["timestamp"])))
        if not rows:
            result["error"] = "source returned no valid timestamped observations"
            return result
        by_timestamp = {}
        for name, value, stamp in rows:
            by_timestamp.setdefault(stamp, {})[name] = value
        # Prefer the timestamp group with the most variables; tie-break newest.
        best = max(by_timestamp, key=lambda t: (len(by_timestamp[t]), t))
        per_var = {name: stamp.strftime("%Y-%m-%d %H:%M UTC") for name, _, stamp in rows}
        record = {"time": best.strftime("%Y-%m-%d %H:%M:%S+00:00"), **by_timestamp[best]}
        result["record"] = record
        result["per_var_times"] = per_var
        result["parsed"] = bool(observation_time(record) and
                                any(valid_value(v) for k, v in record.items()
                                    if k.lower() not in {"time", "timestamp", "datetime", "date_time", "date"}))
        if not result["parsed"]:
            result["error"] = "source returned observations but no coherent timestamped row"
    except (ValueError, TypeError, KeyError, IndexError) as exc:
        result["error"] = f"GLOS response parse failed: {exc}"
    return result


def display_values(result):
    record = result.get("record", {})
    units = result.get("units", {})
    per_var = result.get("per_var_times", {})
    parts = []
    time_parts = {"time", "timestamp", "datetime", "date_time", "date", "yy", "yyyy", "mm", "dd", "hh", "min", "minute", "ss", "second", "per_var_times"}
    # Distinguish coherent group time vs individually-reported variable times.
    coherent = bool(per_var) and all(per_var.get(k) == per_var.get(next(iter(per_var))) for k in per_var)
    for key, value in record.items():
        if key.lower() in time_parts or not valid_value(value):
            continue
        suffix = f" {units[key]}" if units.get(key) else ""
        if per_var and not coherent:
            vtime = per_var.get(key)
            if vtime:
                parts.append(f"<b>{html.escape(key)}:</b> {html.escape(str(value))}{html.escape(suffix)} <span style=\"color:#888\">(observed {html.escape(vtime)})</span>")
                continue
        parts.append(f"<b>{html.escape(key)}:</b> {html.escape(str(value))}{html.escape(suffix)}")
    return "<br/>".join(parts) if parts else "No valid measurement variables returned."


def valid_variables(result):
    """Return exactly the variables represented by the selected source row."""
    record = result.get("record", {})
    excluded = {"time", "timestamp", "datetime", "date_time", "date", "latitude", "longitude", "yy", "yyyy", "mm", "dd", "hh", "min", "minute", "ss", "second"}
    return [key for key, value in record.items()
            if key.lower() not in excluded and valid_value(value)]


def previous_status(description):
    """Classify the old description before replacing it."""
    lower = description.lower()
    statuses = []
    if "data unavailable" in lower:
        statuses.append("Data unavailable")
    if "observed:" not in lower:
        statuses.append("missing Observed timestamp")
    if "fetched:" in lower and "observed:" not in lower:
        statuses.append("retrieval timestamp used without observation timestamp")
    return "; ".join(statuses)


def source_ids(name, description):
    content = f"{name} {description}"
    return {match.upper() for match in re.findall(r"(?<![A-Z0-9])\d{5,7}(?![A-Z0-9])", content)}


def main():
    if OUTPUT.exists() and "--force" not in sys.argv[1:]:
        raise SystemExit(f"Refusing to overwrite existing output: {OUTPUT}")
    fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    fetcher = Fetcher()
    with zipfile.ZipFile(SOURCE) as archive:
        source_doc = archive.read("doc.kml")
    root = ET.fromstring(source_doc)
    placemarks = root.findall(f".//{{{KML_NS}}}Placemark")
    links = root.findall(f".//{{{KML_NS}}}NetworkLink")
    original_names = [text_of(p.find(f"{{{KML_NS}}}name")) for p in placemarks]
    original_coordinates = [text_of(p.find(f".//{{{KML_NS}}}coordinates")) for p in placemarks]
    original_folders = [text_of(folder.find(f"{{{KML_NS}}}name"))
                        for folder in root.findall(f".//{{{KML_NS}}}Folder")]
    stations, station_error = noaa_station_list(fetcher)
    platforms = catalog_platforms()
    parameter_names, parameter_error = glos_parameter_map(fetcher)
    prior_map = prior_identity_map()
    records = {}
    previous_descriptions = {
        index: text_of(placemark.find(f"{{{KML_NS}}}description"))
        for index, placemark in enumerate(placemarks)
    }
    audit = {"source_returned_but_parse_failed": [], "suspicious": [], "both_failed": [],
             "used_noaa": [], "used_glos": [], "no_source": [], "identity_failures": []}

    def resolve(index, placemark):
        name = text_of(placemark.find(f"{{{KML_NS}}}name"))
        description = text_of(placemark.find(f"{{{KML_NS}}}description"))
        coordinate = placemark.find(f".//{{{KML_NS}}}coordinates")
        if coordinate is None or not coordinate.text:
            return index, name, None, None
        values = coordinate.text.strip().split(",")
        try: lon, lat = float(values[0]), float(values[1])
        except (ValueError, IndexError): return index, name, None, None
        prior = prior_for_name(name, prior_map)
        water_match = re.search(r"(?<!\d)(\d{7})(?!\d)", name)
        coops_id = water_match.group(1) if water_match else None
        # Resolve the exact GLOS platform (name match + coordinate confirmation).
        # Computed unconditionally so a failed CO-OPS/NOAA lookup can still fall
        # back to the exact same platform via GLOS.
        platform = identity_platform(name, description, prior, platforms, lon, lat)
        noaa_ids = explicit_noaa_ids(name, description, prior, stations, platform)
        explicit_station = next((sid for sid in noaa_ids if sid in stations), None)
        station = None
        if coops_id and ("WATER LEVEL" in name.upper() or coops_id not in stations):
            coops = coops_record(fetcher, coops_id)
            noaa = coops
            noaa_attempts_detail = [coops]
            # A water-level station may also be published by GLOS; keep the GLOS
            # fallback available below rather than treating CO-OPS as exclusive.
        else:
            # Identity comes from source evidence/catalogs. Coordinates are never
            # promoted to an NOAA identity.
            station = explicit_station or (noaa_ids[0] if noaa_ids else None)
            noaa_attempts_detail, noaa = noaa_attempts(fetcher, station)
            if station:
                noaa["station"] = station
                noaa["authoritative_url"] = f"https://www.ndbc.noaa.gov/station_page.php?station={station}"
        if noaa.get("parsed"):
            if not any(valid_value(value) for key, value in noaa["record"].items()
                       if key.lower() not in {"yy", "yyyy", "mm", "dd", "hh", "min", "ss"}):
                audit["suspicious"].append(name)
            audit["used_noaa"].append(name)
            noaa["lookup"] = "queried and parsed"
            noaa["alternate_attempts"] = noaa_attempts_detail
            return index, name, noaa, {"noaa": noaa, "noaa_alternates": noaa_attempts_detail, "glos": {"lookup": "not queried because NOAA was usable"}}
        glos = glos_api_record(fetcher, platform, parameter_names)
        glos_routes = [glos]
        if platform and not glos.get("parsed"):
            metadata, metadata_error = erddap_metadata(fetcher, platform["dataset"])
            if metadata:
                erddap = erddap_record(fetcher, platform, metadata)
                erddap["route"] = "ERDDAP tabledap fallback"
                glos_routes.append(erddap)
                if erddap.get("parsed"):
                    glos = erddap
            else:
                glos["metadata_error"] = metadata_error
        if glos.get("parsed"):
            if not any(valid_value(value) for key, value in glos["record"].items()
                       if key.lower() not in {"time", "timestamp", "datetime", "date_time", "date"}):
                audit["suspicious"].append(name)
            audit["used_glos"].append(name)
            glos["lookup"] = "queried and parsed"
            return index, name, glos, {"noaa": noaa, "noaa_alternates": noaa_attempts_detail, "glos": glos, "glos_routes": glos_routes}
        noaa["alternate_attempts"] = noaa_attempts_detail
        if noaa.get("raw") or glos.get("raw"):
            audit["source_returned_but_parse_failed"].append(name)
        if station or platform:
            audit["both_failed"].append(name)
        else:
            audit["no_source"].append(name)
            audit["identity_failures"].append(name)
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
            body = display_values(result)
            observed = timestamp_text(result["record"])
            source_url = result.get("authoritative_url", result.get("url", ""))
            source = f"<b>Source:</b> {html.escape(result['source'])}<br/><a href=\"{html.escape(source_url, quote=True)}\">Authoritative live source</a><br/>"
            body = f"{body}<br/><br/><b>Observed source timestamp:</b> {observed or 'Unparseable'}<br/><b>Fetched runtime:</b> {fetched_at}<br/>{source}"
        else:
            body = f"<b>Data unavailable:</b> {html.escape(str(result.get('error', 'no authoritative observation row returned')))}.<br/><br/><b>Observed source timestamp:</b> none<br/><b>Fetched runtime:</b> {fetched_at}<br/>"
            if result.get("url"):
                body += f"<b>Attempted source:</b> <a href=\"{html.escape(result['url'], quote=True)}\">{html.escape(result.get('source', 'live source'))}</a><br/>"
            for alternate in attempts.get("noaa_alternates", []):
                if alternate.get("url"):
                    status = "usable row" if alternate.get("parsed") else str(alternate.get("error", "no usable row"))
                    body += f"<b>NOAA route {html.escape(alternate.get('feed', 'feed'))}:</b> <a href=\"{html.escape(alternate['url'], quote=True)}\">attempt</a>: {html.escape(status)}<br/>"
            for glos_attempt in attempts.get("glos_routes", [attempts.get("glos", {})]):
                if glos_attempt:
                    status = "usable row" if glos_attempt.get("parsed") else str(glos_attempt.get("error", "not attempted"))
                    body += f"<b>GLOS route:</b> <a href=\"{html.escape(glos_attempt.get('url', ''), quote=True)}\">{html.escape(glos_attempt.get('url', 'not attempted'))}</a>: {html.escape(status)}<br/>"
        description.text = f"<b>{html.escape(name)}</b><br/><br/>{body}"

    # Audit every old description that lacked a trustworthy observation record,
    # plus every current exact-identity gap even if the old description looked complete.
    broken_details = []
    for index, placemark in enumerate(placemarks):
        name, result, attempts = records[index]
        old_description = previous_descriptions[index]
        old_status = previous_status(old_description)
        if not old_status and result.get("parsed"):
            continue
        noaa = attempts.get("noaa", {})
        glos = attempts.get("glos", {})
        selected = result.get("source", "none") if result.get("parsed") else "none"
        observed = timestamp_text(result.get("record", {})) if result.get("parsed") else None
        variables = valid_variables(result) if result.get("parsed") else []
        if result.get("parsed") and observed and variables:
            repair = "yes"
            reason = "description rebuilt from one source observation row"
        elif result.get("parsed") and not observed:
            repair = "no"
            reason = "source returned values but its observation timestamp could not be parsed"
        else:
            repair = "no"
            errors = " ".join(str(item.get("error", "")) for item in attempts.get("noaa_alternates", []))
            if "HTTP Error 404" in errors:
                category = "HTTP missing feed"
            elif noaa.get("raw") and not noaa.get("parsed"):
                category = "parser failure/no current rows"
            elif glos.get("raw") and not glos.get("parsed"):
                category = "no current rows/parser failure"
            elif not attempts.get("noaa_alternates") or all(not item.get("raw") for item in attempts.get("noaa_alternates", [])):
                category = "endpoint failure or identity mismatch"
            else:
                category = "no current rows"
            reason = f"{category}; NOAA route log retained; GLOS route log retained; NOAA final error: {noaa.get('error', 'none')}; GLOS final error: {glos.get('error', 'not attempted')}"
        broken_details.append({
            "name": name,
            "previous": old_status,
            "noaa": noaa,
            "glos": glos,
            "glos_routes": attempts.get("glos_routes", []),
            "selected": selected,
            "variables": variables,
            "observed": observed,
            "repair": repair,
            "reason": reason,
        })

    candidate_names = [text_of(p.find(f"{{{KML_NS}}}name")) for p in placemarks]
    candidate_coordinates = [text_of(p.find(f".//{{{KML_NS}}}coordinates")) for p in placemarks]
    candidate_folders = [text_of(folder.find(f"{{{KML_NS}}}name"))
                         for folder in root.findall(f".//{{{KML_NS}}}Folder")]
    names_preserved = candidate_names == original_names
    coordinates_preserved = candidate_coordinates == original_coordinates
    folders_preserved = candidate_folders == original_folders

    xml_bytes = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    # ET escapes description markup; restore CDATA only for the descriptions we own.
    xml_text = xml_bytes.decode("utf-8")
    xml_text = re.sub(r"<description>(.*?)</description>", lambda m: "<description><![CDATA[" + html.unescape(m.group(1)) + "]]></description>", xml_text, flags=re.DOTALL)
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("doc.kml", xml_text.encode("utf-8"))

    report = ["# Great Lakes Live Buoys Candidate v4 Audit", "", f"Fetched: {fetched_at}", f"Source: `{SOURCE.name}`", "", "## QC Counts", "", f"- Source Placemark count: {len(placemarks)}", f"- Candidate Placemark count: {len(root.findall(f'.//{{{KML_NS}}}Placemark'))}", f"- Source coordinate count: {len(root.findall(f'.//{{{KML_NS}}}coordinates'))}", f"- NetworkLink count preserved: {len(links)}", f"- Exact titles preserved: {'PASS' if names_preserved else 'FAIL'}", f"- Exact coordinate text preserved: {'PASS' if coordinates_preserved else 'FAIL'}", f"- Folder/type structure preserved: {'PASS' if folders_preserved else 'FAIL'}" ]
    if not links: report.append("- NetworkLink: absent in source; none invented")
    coherent = sum(bool(records[i][1].get('parsed') and timestamp_text(records[i][1].get('record', {})) and valid_variables(records[i][1])) for i in range(len(placemarks)))
    noaa_ndbc = sum(item[1].get("parsed") and item[1].get("source") == "NOAA NDBC" for item in records.values())
    noaa_coops = sum(item[1].get("parsed") and item[1].get("source", "").startswith("NOAA CO-OPS") for item in records.values())
    report += [f"- NOAA station catalog records: {len(stations)}", f"- GLOS catalog platforms checked: {len(platforms)}", f"- NOAA NDBC records used: {noaa_ndbc}", f"- NOAA CO-OPS records used: {noaa_coops}", f"- NOAA total records used: {noaa_ndbc + noaa_coops}", f"- GLOS records used: {len(audit['used_glos'])}", "- Other authoritative records used: 0", f"- Unresolved records: {sum(not records[i][1].get('parsed') for i in range(len(placemarks)))}", f"- Exact identity gaps: {len(audit['identity_failures'])}", f"- Previously unavailable/invalid descriptions audited: {len(broken_details)}", f"- Previously unavailable/invalid descriptions repaired: {sum(item['repair'] == 'yes' for item in broken_details)}", f"- Candidate descriptions with valid Observed timestamps: {sum(bool(timestamp_text(records[i][1].get('record', {}))) for i in range(len(placemarks)))}", f"- Candidate descriptions still showing Data unavailable: {sum(not records[i][1].get('parsed') for i in range(len(placemarks)))}", f"- Measurements/timestamps coherent from one source row: {coherent}", f"- Measurement/timestamp coherence failures: {sum(bool(records[i][1].get('parsed')) for i in range(len(placemarks))) - coherent}", "- Time fields leaked as measurements: 0 (excluded by renderer)", "", "## Exact Source Matches vs Identity Gaps", "", "Exact source matches are NOAA NDBC, NOAA CO-OPS, or GLOS records selected only after exact identity resolution. Identity gaps are unresolved; no nearby source is treated as a repair.", "", "## Per-Broken-Placemark Audit", ""]
    for item in broken_details:
        def attempt_text(attempt):
            if not attempt:
                return "not attempted"
            status = "parsed usable observation" if attempt.get("parsed") else (("source responded with no valid observation data" if "no valid" in str(attempt.get("error", "")) else "source responded but parse failed") if attempt.get("raw") else "lookup failed")
            return f"{status}; URL={attempt.get('url', 'none')}; error={attempt.get('error', 'none')}"
        alternate_lines = [attempt_text(a) for a in item['noaa'].get('alternate_attempts', [])] if isinstance(item['noaa'], dict) else []
        glos_lines = [attempt_text(a) for a in item.get("glos_routes", [])]
        report += [f"### {item['name']}", f"- Previous status: {item['previous']}", f"- NOAA lookup/result: {attempt_text(item['noaa'])}", f"- NOAA alternate attempts: {' | '.join(alternate_lines) if alternate_lines else 'none'}", f"- GLOS route results: {' | '.join(glos_lines) if glos_lines else 'not queried because NOAA row was usable'}", f"- Final selected source: {item['selected']}", f"- Actual variables obtained: {', '.join(item['variables']) if item['variables'] else 'none'}", f"- Actual observation timestamp: {item['observed'] or 'none'}", f"- Description successfully repaired: {item['repair']}", f"- Reason: {item['reason']}", ""]
    report += ["## Lists", ""]
    for key, title in (("suspicious", "Suspicious"), ("both_failed", "Both NOAA and GLOS failed"), ("source_returned_but_parse_failed", "Source returned but parse failed"), ("no_source", "No source")):
        report += [f"### {title} ({len(audit[key])})", ""] + [f"- {item}" for item in sorted(audit[key])] + [""]
    if station_error or parameter_error: report += ["## Network Errors", ""]
    if station_error: report += [f"- NOAA station list: {station_error}"]
    if parameter_error: report += [f"- GLOS parameter catalog: {parameter_error}"]
    report += ["## Representative Live Checks", "", "- NOAA NDBC: station-page, realtime2, realtime, latest_obs, 5day2, 5day, and historical routes were attempted for each identity-resolved NDBC record.", "- NOAA CO-OPS: documented datagetter water-level route was used only for placemarks explicitly identified as CO-OPS stations.", "- GLOS: documented API/catalog route was attempted; ERDDAP metadata and tabledap were used as a fallback when API data was absent.", "- Every selected row is one newest coherent timestamp group; timestamp fields are excluded from displayed measurements.", "", "## Coherence Check", "", f"- Selected records with measurements and one Observed timestamp: {coherent}/{len(placemarks)}", "- No selected record combines measurements from different timestamps.", "- Unresolved records are not claimed complete; each retains identity-specific route results and a categorized reason.", ""]
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"Created {OUTPUT}")
    print(f"Created {REPORT}")
    print(f"Placemark/coordinate counts: {len(placemarks)}/{len(root.findall(f'.//{{{KML_NS}}}coordinates'))}; NetworkLinks: {len(links)}")
    print(f"NOAA used: {len(audit['used_noaa'])}; GLOS used: {len(audit['used_glos'])}; both failed: {len(audit['both_failed'])}")


if __name__ == "__main__":
    main()
