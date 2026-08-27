# Great Lakes Live Buoys Candidate v5 Audit

Fetched: 2026-08-27 21:59:13 UTC
Source: `great_lakes_live_buoys.kmz`

## QC Counts

- Source Placemark count: 256
- Candidate Placemark count: 256
- Source coordinate count: 256
- NetworkLink count preserved: 0
- Exact titles preserved: PASS
- Exact coordinate text preserved: PASS
- Folder/type structure preserved: PASS
- NetworkLink: absent in source; none invented
- NOAA station catalog records: 1936
- GLOS catalog platforms checked: 625
- NOAA NDBC records used: 188
- NOAA CO-OPS records used: 1
- NOAA total records used: 189
- GLOS records used: 21
- Other authoritative records used: 0
- ONLINE (current observation available): 210
- OFFLINE (exact platform linked, no current observation): 46
- UNRESOLVED (exact platform/source identity cannot be established): 0
- Exact identity gaps: 0
- Previously unavailable/invalid descriptions audited: 256
- Previously unavailable/invalid descriptions repaired: 256
- Candidate descriptions with valid Observed timestamps: 210
- Candidate descriptions still showing 'Data unavailable': 0 (offline stations are linked and auto-retried, not abandoned)
- Measurements/timestamps coherent from one source row: 210
- Measurement/timestamp coherence failures: 0
- Time fields leaked as measurements: 0 (excluded by renderer)

## Status Definitions

- ONLINE: exact platform identified, queried, and currently reporting; live measurements + Observed timestamp shown.
- OFFLINE: exact platform identified and permanently linked, but it returned no current observation this run. Shows 'Currently offline — awaiting next observation' plus the exact source link; retried automatically next run.
- UNRESOLVED: exact platform/source identity could not be established from the name, coordinates, prior map, or catalogs; original source link preserved.

## Exact Source Matches vs Identity Gaps

Exact source matches are NOAA NDBC, NOAA CO-OPS, or GLOS records selected only after exact identity resolution. Identity gaps are unresolved; no nearby source is treated as a repair.

## Per-Broken-Placemark Audit

### MID SUPERIOR- 60 NM North Northeast Hancock, MI (2.1-meter ionomer foam buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45001.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45001; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45001.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45001.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45001.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45001_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45001_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45001.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, APD, PRES, ATMP, WTMP
- Actual observation timestamp: 2026-08-27 21:10:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### EAST SUPERIOR -70 NM NE Marquette, MI (2.3-meter foam discus buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45004.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45004; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45004.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45004.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45004.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45004_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45004_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45004.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, APD, MWD, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 21:10:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### WEST SUPERIOR - 30NM NE of Outer Island, WI (2.3-meter foam discus buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45006.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45006; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45006.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45006.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45006.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45006_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45006_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45006.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, APD, PRES, ATMP, WTMP
- Actual observation timestamp: 2026-08-27 21:10:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### North Entry Buoy, North Keweenaw Peninsula, MI (Moored Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45023.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45023; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45023.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45023.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45023.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45023_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45023_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45023.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, PRES, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 20:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### South Entry Buoy, South Keweenaw Peninsula, MI (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45025.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45025; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45025.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45025.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45025.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45025_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45025_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45025.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, MWD, PRES, ATMP, WTMP, DEWP, PTDY
- Actual observation timestamp: 2026-08-27 20:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### McQuade Harbor Nearshore, MN (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45027.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45027; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45027.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45027.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45027.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45027_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45027_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45027.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, WVHT, MWD, PRES, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 20:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Western Lake Superior (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45028.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45028; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45028.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45028.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45028.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45028_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45028_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45028.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WVHT, MWD, WTMP
- Actual observation timestamp: 2026-08-27 20:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Slate Island (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45136.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45136; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45136.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45136.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45136.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45136_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45136_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45136.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, PRES, ATMP, WTMP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Granite Island Buoy, Granite Island, MI (Buoy) [GLOS]
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45171; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45171.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45171.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45171.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45171_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45171_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45171.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GRIM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/GRIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GRIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GRIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/GRIM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GRIM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GRIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=66; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/66.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/66.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/66.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/66_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/66_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/66.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GRIM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/GRIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GRIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GRIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/GRIM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GRIM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GRIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=6; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=147; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/147.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/147.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/147.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/147_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/147_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/147.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=66; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_66.json?time,air_pressure,air_temperature,sea_surface_temperature,sea_surface_wave_significant_height,sea_surface_wave_significant_period,wind_from_direction,wind_speed&orderByMax(%22time%22); error=HTTP Error 404:  | source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=6; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_6.json?time,air_pressure,air_pressure_at_mean_sea_level,air_temperature,dew_point_temperature,relative_humidity,wind_from_direction,wind_speed,wind_speed_of_gust&orderByMax(%22time%22); error=HTTP Error 404:  | source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=147; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_147.json?time,sea_surface_wave_from_direction,sea_surface_wave_from_direction_at_variance_spectral_density_maximum,sea_surface_wave_mean_period,sea_surface_wave_period_at_variance_spectral_density_maximum,sea_surface_wave_significant_height,sea_water_temperature_1,sea_water_temperature_1_fixed_depth,sea_water_temperature_2,sea_water_temperature_2_fixed_depth,wind_from_direction,wind_speed&orderByMax(%22time%22); error=HTTP Error 404: 
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Grand Marais Buoy, Grand Marais, MI (Buoy) [GLOS]
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GRMM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GRMM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GRMM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GRMM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GRMM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/GRMM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GRMM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GRMM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST
- Actual observation timestamp: 2026-08-27 20:50:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Munising Buoy, Munising, MI (Buoy) [GLOS]
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45173; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45173.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45173.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45173.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45173_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45173_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45173.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=65; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/65.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/65.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/65.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/65_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/65_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/65.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=172; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/172.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/172.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/172.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/172_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/172_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/172.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=65; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_65.json?time,air_pressure,air_temperature,sea_surface_temperature,sea_surface_wave_from_direction,sea_surface_wave_significant_height,sea_surface_wave_significant_period,wind_from_direction,wind_speed&orderByMax(%22time%22); error=HTTP Error 404:  | parsed usable observation; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=172; error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: wind_from_direction, sea_water_temperature, sea_surface_wave_significant_height, sea_surface_wave_mean_period, sea_surface_wave_period_at_variance_spectral_density_maximum, wind_speed, sea_surface_wave_from_direction, sea_surface_wave_directional_spread_at_variance_spectral_density_maximum, sea_surface_wave_from_direction_at_variance_spectral_density_maximum, sea_surface_wave_directional_spread
- Actual observation timestamp: 2026-08-27 20:50:49 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Stannard Rock Buoy (Buoy) [GLOS]
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/STDM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=STDM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/STDM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/STDM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/STDM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/STDM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/STDM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/STDM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WSPD, GST, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Isle of Royale East, MI (230) (Waverider Buoy) [GLOS]
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45180; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45180.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45180.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45180.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45180_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45180_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45180.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=212; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/212.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/212.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/212.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/212_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/212_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/212.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=212; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_212.json?time,sea_surface_temperature,sea_surface_temperature_fixed_depth,sea_surface_wave_directional_spread_at_variance_spectral_density_maximum,sea_surface_wave_from_direction,sea_surface_wave_from_direction_at_variance_spectral_density_maximum,sea_surface_wave_mean_period,sea_surface_wave_period_at_variance_spectral_density_maximum,sea_surface_wave_significant_height&orderByMax(%22time%22); error=HTTP Error 404: 
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Grand Island North, MI (268) (Waverider Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45211.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45211; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45211.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45211.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45211.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45211_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45211_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45211.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WVHT, DPD, APD, MWD, WTMP
- Actual observation timestamp: 2026-08-27 21:26:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### East Superior Spotter (Spotter Buoy)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45004.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45004; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45004.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45004.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45004.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45004_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45004_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45004.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, APD, MWD, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 21:10:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Ontonagon, MI (Moored Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OTNM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=OTNM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OTNM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/OTNM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/OTNM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/OTNM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/OTNM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/OTNM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP
- Actual observation timestamp: 2026-08-27 20:50:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Wisconsin Point (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45217.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45217; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45217.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45217.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45217.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45217_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45217_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45217.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WTMP
- Actual observation timestamp: 2026-08-27 20:15:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Two Harbors Nearshore Buoy (Moored Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45219.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45219; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45219.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45219.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45219.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45219_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45219_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45219.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WSPD, PRES, ATMP
- Actual observation timestamp: 2026-08-27 20:20:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### MID SUPERIOR- 60NM North Northeast Hancock, MI (2.1-meter ionomer foam buoy)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45T01; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45T01.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45T01.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45T01.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45T01_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45T01_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45T01.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Big Bay, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/BIGM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=BIGM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/BIGM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/BIGM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/BIGM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/BIGM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/BIGM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/BIGM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WSPD, GST, PRES, ATMP
- Actual observation timestamp: 2026-08-27 20:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Barker's Island, Lake Superior Reserve, WI (NERRS Water Quality Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=BILW3; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/BILW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/BILW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/BILW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/BILW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/BILW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/BILW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=LKSBAWQ; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/LKSBAWQ.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/LKSBAWQ.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/LKSBAWQ.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/LKSBAWQ_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/LKSBAWQ_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/LKSBAWQ.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=238; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/238.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/238.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/238.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/238_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/238_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/238.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=238; error=source returned no valid timestamped observations
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Caribou Island (Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CWCI.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=CWCI; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CWCI.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/CWCI.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/CWCI.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/CWCI_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/CWCI_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/CWCI.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Devils Island, WI (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/DISW3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=DISW3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/DISW3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/DISW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/DISW3.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/DISW3_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/DISW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/DISW3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9099064 - Duluth, MN (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/DULM5.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=DULM5; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/DULM5.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/DULM5.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/DULM5.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/DULM5_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/DULM5_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/DULM5.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9099090 - Grand Marais, MN (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GDMM5.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GDMM5; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GDMM5.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GDMM5.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GDMM5.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/GDMM5_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GDMM5_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GDMM5.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### GLRC Observatory (Coastal Marine Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GRCM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GRCM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GRCM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GRCM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GRCM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/GRCM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GRCM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GRCM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 20:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Granite Island, MI (Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45171; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45171.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45171.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45171.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45171_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45171_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45171.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GRIM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/GRIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GRIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GRIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/GRIM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GRIM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GRIM4.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GRIM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/GRIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GRIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GRIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/GRIM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GRIM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GRIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=6; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=66; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/66.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/66.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/66.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/66_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/66_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/66.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=147; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/147.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/147.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/147.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/147_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/147_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/147.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=6; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_6.json?time,air_pressure,air_pressure_at_mean_sea_level,air_temperature,dew_point_temperature,relative_humidity,wind_from_direction,wind_speed,wind_speed_of_gust&orderByMax(%22time%22); error=HTTP Error 404:  | source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=66; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_66.json?time,air_pressure,air_temperature,sea_surface_temperature,sea_surface_wave_significant_height,sea_surface_wave_significant_period,wind_from_direction,wind_speed&orderByMax(%22time%22); error=HTTP Error 404:  | source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=147; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_147.json?time,sea_surface_wave_from_direction,sea_surface_wave_from_direction_at_variance_spectral_density_maximum,sea_surface_wave_mean_period,sea_surface_wave_period_at_variance_spectral_density_maximum,sea_surface_wave_significant_height,sea_water_temperature_1,sea_water_temperature_1_fixed_depth,sea_water_temperature_2,sea_water_temperature_2_fixed_depth,wind_from_direction,wind_speed&orderByMax(%22time%22); error=HTTP Error 404: 
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Grand Marais, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GRMM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GRMM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GRMM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GRMM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GRMM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/GRMM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GRMM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GRMM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST
- Actual observation timestamp: 2026-08-27 20:50:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Superior Grand Traverse Bay, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GTRM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GTRM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GTRM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GTRM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GTRM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/GTRM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GTRM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GTRM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, PTDY
- Actual observation timestamp: 2026-08-19 23:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Bay of Grand Marais, MN (Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/KGNA.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=KGNA; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/KGNA.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/KGNA.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/KGNA.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/KGNA_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/KGNA_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/KGNA.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 20:56:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Munising Lake Shore, MI (Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/KP53.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=KP53; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/KP53.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/KP53.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/KP53.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/KP53_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/KP53_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/KP53.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 20:56:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Copper Harbor, MI (Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/KP59.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=KP59; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/KP59.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/KP59.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/KP59.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/KP59_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/KP59_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/KP59.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 20:51:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9076033 - Little Rapids, MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/LTRM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=LTRM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/LTRM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/LTRM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/LTRM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/LTRM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/LTRM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/LTRM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9099018 - Marquette C.G., MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MCGM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=MCGM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MCGM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/MCGM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/MCGM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/MCGM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/MCGM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/MCGM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Naubinway, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/NABM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=NABM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/NABM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/NABM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/NABM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/NABM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/NABM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/NABM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP
- Actual observation timestamp: 2026-08-27 20:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Ontonagon, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OTNM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=OTNM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OTNM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/OTNM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/OTNM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/OTNM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/OTNM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/OTNM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP
- Actual observation timestamp: 2026-08-27 20:50:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Portage Canal, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=PCLM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/PCLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/PCLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/PCLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/PCLM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/PCLM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/PCLM4.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=PCLM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/PCLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/PCLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/PCLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/PCLM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/PCLM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/PCLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=640; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/640.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/640.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/640.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/640_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/640_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/640.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=640; error=source returned no valid timestamped observations | parsed usable observation; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_640.json?time,air_pressure_at_mean_sea_level,air_temperature,wind_from_direction,wind_speed,wind_speed_of_gust&orderByMax(%22time%22); error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: air_pressure_at_mean_sea_level, air_temperature, wind_from_direction, wind_speed, wind_speed_of_gust
- Actual observation timestamp: 2025-11-07 14:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Passage Island, MI (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/PILM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=PILM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/PILM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/PILM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/PILM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/PILM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/PILM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/PILM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Pokegama Bay, Lake Superior Reserve, WI (NERRS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/PKBW3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=PKBW3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/PKBW3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/PKBW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/PKBW3.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/PKBW3_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/PKBW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/PKBW3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, PRES, ATMP, DEWP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Port Wing, WI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/PNGW3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=PNGW3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/PNGW3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/PNGW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/PNGW3.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/PNGW3_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/PNGW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/PNGW3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP
- Actual observation timestamp: 2026-08-27 20:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9099004 - Point Iroquois, MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/PTIM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=PTIM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/PTIM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/PTIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/PTIM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/PTIM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/PTIM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/PTIM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9076024 - Rock Cut, MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/RCKM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=RCKM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/RCKM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/RCKM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/RCKM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/RCKM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/RCKM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/RCKM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Rock of Ages, MI (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/ROAM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=ROAM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/ROAM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/ROAM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/ROAM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/ROAM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/ROAM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/ROAM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Silver Bay, MN (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SLVM5.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=SLVM5; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SLVM5.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/SLVM5.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/SLVM5.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/SLVM5_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/SLVM5_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/SLVM5.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP
- Actual observation timestamp: 2026-08-27 20:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Stannard Rock, MI (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/STDM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=STDM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/STDM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/STDM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/STDM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/STDM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/STDM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/STDM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WSPD, GST, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Superior Shoals, NY (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=SUPN6; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/SUPN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/SUPN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/SUPN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/SUPN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/SUPN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/SUPN6.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### 9076070 - S.W. Pier, MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SWPM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=SWPM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SWPM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/SWPM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/SWPM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/SWPM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/SWPM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/SWPM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Saxon Harbor, WI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SXHW3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=SXHW3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SXHW3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/SXHW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/SXHW3.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/SXHW3_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/SXHW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/SXHW3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP
- Actual observation timestamp: 2026-08-26 12:50:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Whitefish Point, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=WFPM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/WFPM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/WFPM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/WFPM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/WFPM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/WFPM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/WFPM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=265; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/265.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/265.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/265.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/265_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/265_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/265.txt; error=HTTP Error 404: Not Found
- GLOS route results: parsed usable observation; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=265; error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: sea_surface_wave_directional_spread, sea_surface_wave_mean_period, wind_from_direction, sea_surface_wave_directional_spread_at_variance_spectral_density_maximum, wind_speed, sea_surface_wave_period_at_variance_spectral_density_maximum, sea_surface_wave_significant_height, sea_surface_wave_from_direction_at_variance_spectral_density_maximum, sea_surface_wave_from_direction, air_pressure
- Actual observation timestamp: 2026-08-27 20:50:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9076027 - West Neebish Island, MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/WNEM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=WNEM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/WNEM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/WNEM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/WNEM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/WNEM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/WNEM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/WNEM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Bayfield Beach, WI (Beach)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45010; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45010_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45010_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=bayfield_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/bayfield_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/bayfield_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/bayfield_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/bayfield_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/bayfield_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/bayfield_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Madeline Island Beach, WI (Beach)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45010; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45010_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45010_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=madeline_island_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/madeline_island_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/madeline_island_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/madeline_island_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/madeline_island_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/madeline_island_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/madeline_island_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Michigan City CG Station, IN (Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MCYI3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=MCYI3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MCYI3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/MCYI3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/MCYI3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/MCYI3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/MCYI3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/MCYI3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-18 14:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### St. Joseph CG Station, MI (Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=SJNM4; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/SJNM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/SJNM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/SJNM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/SJNM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/SJNM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/SJNM4.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=20CM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/20CM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/20CM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/20CM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/20CM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/20CM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/20CM4.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=SJOM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/SJOM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/SJOM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/SJOM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/SJOM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/SJOM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/SJOM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### NORTH MICHIGAN- Halfway between North Manitou and Washington Islands. (2.1-meter ionomer foam buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45002.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45002; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45002.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45002.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45002.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45002_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45002_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45002.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, WTMP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### SOUTH MICHIGAN - 43NM East Southeast of Milwaukee, WI (2.3-meter foam discus buoy) [GLOS]
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45214.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45214; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45214.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45214.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45214.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45214_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45214_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45214.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WVHT, MWD, WTMP
- Actual observation timestamp: 2026-08-27 19:50:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

###  (2.4-meter discus buoy)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MLWW3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=MLWW3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MLWW3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/MLWW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/MLWW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/MLWW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/MLWW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/MLWW3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP
- Actual observation timestamp: 2026-08-18 14:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Grand Haven Michigan (3-meter discus buoy)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45011; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45011.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45011.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45011.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45011_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45011_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45011.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=671; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/671.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/671.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/671.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/671_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/671_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/671.txt; error=HTTP Error 404: Not Found
- GLOS route results: parsed usable observation; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=671; error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: sea_surface_wave_significant_height, sea_surface_wave_from_direction, sea_surface_wave_period_at_variance_spectral_density_maximum, sea_surface_wave_directional_spread_at_variance_spectral_density_maximum, sea_surface_wave_directional_spread, sea_surface_wave_from_direction_at_variance_spectral_density_maximum, air_pressure, wind_from_direction, sea_surface_wave_mean_period, wind_speed
- Actual observation timestamp: 2026-08-27 21:20:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### ATW20 - Atwater Park, WI (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45013.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45013; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45013.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45013.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45013.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45013_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45013_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45013.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, PRES, ATMP, WTMP, DEWP, PTDY
- Actual observation timestamp: 2026-08-27 20:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Calumet Beach, Chicago, IL (Buoy)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45015; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45015.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45015.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45015.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45015_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45015_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45015.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=395; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/395.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/395.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/395.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/395_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/395_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/395.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=393; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/393.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/393.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/393.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/393_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/393_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/393.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=385; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/385.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/385.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/385.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/385_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/385_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/385.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=379; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/379.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/379.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/379.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/379_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/379_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/379.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=395; error=source returned no valid timestamped observations | source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=393; error=source returned no valid timestamped observations | source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=385; error=source returned no valid timestamped observations | source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=379; error=source returned no valid timestamped observations
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Sixth-third St. Beach, Chicago, IL (Buoy)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45016; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45016.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45016.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45016.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45016_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45016_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45016.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=JAKI2; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/JAKI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/JAKI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/JAKI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/JAKI2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/JAKI2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/JAKI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=113; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/113.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/113.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/113.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/113_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/113_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/113.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=377; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/377.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/377.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/377.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/377_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/377_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/377.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=391; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/391.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/391.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/391.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/391_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/391_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/391.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=387; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/387.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/387.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/387.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/387_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/387_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/387.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=383; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/383.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/383.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/383.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/383_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/383_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/383.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=378; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/378.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/378.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/378.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/378_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/378_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/378.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=113; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_113.json?time,air_pressure,air_temperature,relative_humidity,surface_downwelling_shortwave_flux_in_air,wind_from_direction,wind_speed,wind_speed_of_gust&orderByMax(%22time%22); error=HTTP Error 404:  | source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=377; error=source returned no valid timestamped observations | source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=391; error=source returned no valid timestamped observations | source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=387; error=source returned no valid timestamped observations | source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=383; error=source returned no valid timestamped observations | source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=378; error=source returned no valid timestamped observations
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Oak St. Beach, Chicago, IL (Buoy)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OKSI2.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=OKSI2; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OKSI2.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/OKSI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/OKSI2.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/OKSI2_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/OKSI2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/OKSI2.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP
- Actual observation timestamp: 2026-08-25 12:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Montrose Ave. Beach, Chicago, IL (Buoy)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/FSTI2.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=FSTI2; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/FSTI2.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/FSTI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/FSTI2.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/FSTI2_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/FSTI2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/FSTI2.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: ATMP
- Actual observation timestamp: 2026-08-27 20:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Foster Ave. Beach, Chicago, IL (Buoy)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/FSTI2.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=FSTI2; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/FSTI2.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/FSTI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/FSTI2.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/FSTI2_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/FSTI2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/FSTI2.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: ATMP
- Actual observation timestamp: 2026-08-27 20:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Grand Traverse Bay South Buoy, MI (Moored Buoy) [GLOS]
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45020; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45020.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45020.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45020.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45020_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45020_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45020.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=217; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/217.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/217.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/217.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/217_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/217_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/217.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=217; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_217.json?time,air_temperature,battery_voltage,dew_point_temperature,sea_surface_temperature,sea_surface_wave_from_direction,sea_surface_wave_significant_height,sea_surface_wave_significant_period,sea_water_temperature_1,sea_water_temperature_1_fixed_depth,sea_water_temperature_2,sea_water_temperature_2_fixed_depth,sea_water_temperature_3,sea_water_temperature_3_fixed_depth,sea_water_temperature_4,sea_water_temperature_4_fixed_depth,sea_water_temperature_5,sea_water_temperature_5_fixed_depth,sea_water_temperature_6,sea_water_temperature_6_fixed_depth,sea_water_temperature_7,sea_water_temperature_7_fixed_depth,sea_water_temperature_8,sea_water_temperature_8_fixed_depth,sea_water_temperature_9,sea_water_temperature_9_fixed_depth,sea_water_temperature_10,sea_water_temperature_10_fixed_depth,sea_water_temperature_11,sea_water_temperature_11_fixed_depth,sea_water_temperature_12,sea_water_temperature_12_fixed_depth,sea_water_temperature_13,sea_water_temperature_13_fixed_depth,sea_water_temperature_14,sea_water_temperature_14_fixed_depth,surface_downwelling_shortwave_flux_in_air,wind_from_direction,wind_speed,wind_speed_of_gust&orderByMax(%22time%22); error=HTTP Error 404: 
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Traverse Bay #3, MI (Moored Buoy) [GLOS]
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45021; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45021.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45021.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45021.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45021_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45021_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45021.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=224; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/224.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/224.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/224.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/224_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/224_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/224.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=224; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_224.json?time,air_temperature,sea_surface_temperature,sea_surface_wave_significant_height,sea_surface_wave_significant_period,wind_from_direction,wind_speed&orderByMax(%22time%22); error=HTTP Error 404: 
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Little Traverse Bay Buoy, MI (Moored Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45022.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45022; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45022.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45022.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45022.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45022_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45022_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45022.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, PRES, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 20:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Ludington Buoy, MI (Moored Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45024.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45024; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45024.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45024.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45024.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45024_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45024_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45024.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, PRES, ATMP, WTMP
- Actual observation timestamp: 2026-08-27 20:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Cook Nuclear Plant Buoy, Stevensville, MI (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45026.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45026; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45026.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45026.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45026.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45026_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45026_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45026.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, PRES, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 21:10:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Holland Buoy, MI (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/HLNM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=HLNM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/HLNM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/HLNM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/HLNM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/HLNM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/HLNM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/HLNM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Muskegon Buoy, MI (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MKGM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=MKGM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MKGM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/MKGM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/MKGM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/MKGM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/MKGM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/MKGM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-18 14:50:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### South Haven Buoy, MI (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45168.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45168; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45168.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45168.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45168.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45168_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45168_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45168.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, PRES, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 21:10:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Michigan City Buoy, IN (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MCYI3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=MCYI3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MCYI3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/MCYI3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/MCYI3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/MCYI3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/MCYI3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/MCYI3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-18 14:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Wilmette Buoy, IL (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45174.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45174; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45174.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45174.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45174.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45174_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45174_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45174.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, PRES, ATMP
- Actual observation timestamp: 2026-08-27 21:20:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Mackinac Straits West, Mackinaw City, MI (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45175.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45175; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45175.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45175.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45175.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45175_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45175_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45175.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, MWD, PRES, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 20:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Ohio St. Beach, Chicago, IL (Buoy) [GLOS]
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OKSI2.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=OKSI2; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OKSI2.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/OKSI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/OKSI2.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/OKSI2_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/OKSI2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/OKSI2.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP
- Actual observation timestamp: 2026-08-25 12:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Sleeping Bear Dunes (Moored Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45183.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45183; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45183.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45183.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45183.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45183_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45183_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45183.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, PRES, ATMP, WTMP, DEWP, PTDY
- Actual observation timestamp: 2026-08-27 20:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Waukegan Buoy, IL (Moored Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/WHRI2.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=WHRI2; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/WHRI2.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/WHRI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/WHRI2.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/WHRI2_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/WHRI2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/WHRI2.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Winthrop Harbor Buoy, IL (Moored Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45187.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45187; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45187.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45187.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45187.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45187_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45187_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45187.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, PRES, ATMP, WTMP
- Actual observation timestamp: 2026-08-27 21:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### McGulpin Point North, MI (253) (Waverider Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45194.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45194; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45194.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45194.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45194.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45194_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45194_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45194.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WVHT, DPD, APD, MWD, ATMP, WTMP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Chicago Buoy (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45198.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45198; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45198.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45198.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45198.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45198_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45198_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45198.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WSPD, WVHT, DPD, MWD, PRES, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Salmon Unlimited Wisconsin (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45199.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45199; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45199.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45199.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45199.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45199_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45199_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45199.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, WVHT, DPD, MWD, PRES, ATMP, WTMP, PTDY
- Actual observation timestamp: 2026-08-27 19:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Rawley Point East, WI (269) (Waverider Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45210.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45210; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45210.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45210.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45210.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45210_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45210_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45210.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WVHT, DPD, APD, MWD, WTMP
- Actual observation timestamp: 2026-08-27 20:56:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### South Michigan Spotter (Spotter Buoy)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45214.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45214; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45214.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45214.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45214.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45214_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45214_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45214.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WVHT, MWD, WTMP
- Actual observation timestamp: 2026-08-27 19:50:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Wisconsin Shipwreck Coast NMS / Sheboygan, WI (Buoy) [GLOS]
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SGNW3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=SGNW3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SGNW3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/SGNW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/SGNW3.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/SGNW3_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/SGNW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/SGNW3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Algoma City Marina, WI (Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=AGMW3; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/AGMW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/AGMW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/AGMW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/AGMW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/AGMW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/AGMW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=ALGOMA; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/ALGOMA.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/ALGOMA.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/ALGOMA.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/ALGOMA_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/ALGOMA_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/ALGOMA.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=206; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/206.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/206.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/206.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/206_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/206_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/206.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=206; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_206.json?time,AirP,AirT,Chl,DO,DOS,PAR,Temp1,Temp2,Temp2_fixed_depth,Temp3,Temp3_fixed_depth,Temp4,Temp4_fixed_depth,Temp5,Temp5_fixed_depth,WD,WS,WVDIR,WVHT&orderByMax(%22time%22); error=HTTP Error 404: 
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Burns Harbor, IN (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/BHRI3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=BHRI3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/BHRI3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/BHRI3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/BHRI3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/BHRI3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/BHRI3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/BHRI3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: PRES
- Actual observation timestamp: 2026-08-11 15:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Big Sable Point, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/BSBM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=BSBM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/BSBM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/BSBM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/BSBM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/BSBM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/BSBM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/BSBM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP
- Actual observation timestamp: 2026-08-27 20:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Two Rivers CG Station, WI (Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=C58W3; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/C58W3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/C58W3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/C58W3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/C58W3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/C58W3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/C58W3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=143; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/143.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/143.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/143.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/143_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/143_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/143.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=609; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/609.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/609.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/609.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/609_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/609_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/609.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=143; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_143.json?time,air_pressure,sea_surface_wave_directional_spread,sea_surface_wave_directional_spread_at_variance_spectral_density_maximum,sea_surface_wave_from_direction,sea_surface_wave_from_direction_at_variance_spectral_density_maximum,sea_surface_wave_mean_period,sea_surface_wave_period_at_variance_spectral_density_maximum,sea_surface_wave_significant_height,sea_water_temperature_1,sea_water_temperature_1_fixed_depth,sea_water_temperature_2,sea_water_temperature_2_fixed_depth,sea_water_temperature_3,sea_water_temperature_3_fixed_depth,sea_water_temperature_4,sea_water_temperature_4_fixed_depth,wind_from_direction,wind_speed&orderByMax(%22time%22); error=HTTP Error 404:  | parsed usable observation; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=609; error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: sea_surface_wave_period_at_variance_spectral_density_maximum, sea_surface_wave_mean_period, sea_surface_wave_significant_height, wind_from_direction, wind_speed, sea_surface_wave_from_direction_at_variance_spectral_density_maximum, sea_surface_wave_directional_spread, air_pressure, sea_surface_wave_from_direction, sea_surface_wave_directional_spread_at_variance_spectral_density_maximum
- Actual observation timestamp: 2026-08-27 21:25:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Chambers Island, WI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CBRW3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=CBRW3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CBRW3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/CBRW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/CBRW3.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/CBRW3_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/CBRW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/CBRW3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP
- Actual observation timestamp: 2026-08-27 20:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Harrison-Dever Crib, Chicago, IL (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CHII2.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=CHII2; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CHII2.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/CHII2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/CHII2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/CHII2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/CHII2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/CHII2.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP, DEWP
- Actual observation timestamp: 2026-08-18 14:50:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9087044 - Calumet Harbor, IL (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CMTI2.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=CMTI2; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CMTI2.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/CMTI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/CMTI2.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/CMTI2_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/CMTI2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/CMTI2.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Northerly Isle, IL (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CNII2.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=CNII2; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CNII2.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/CNII2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/CNII2.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/CNII2_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/CNII2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/CNII2.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 21:15:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Fairport, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/FPTM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=FPTM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/FPTM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/FPTM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/FPTM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/FPTM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/FPTM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/FPTM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP
- Actual observation timestamp: 2026-08-27 20:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Foster Ave., Chicago, IL (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/FSTI2.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=FSTI2; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/FSTI2.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/FSTI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/FSTI2.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/FSTI2_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/FSTI2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/FSTI2.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: ATMP
- Actual observation timestamp: 2026-08-27 20:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Grand Traverse Bay Observing System Station 2 (Coastal Marine Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GTBM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/GTBM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GTBM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GTBM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/GTBM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GTBM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GTBM4.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GTBM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/GTBM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GTBM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GTBM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/GTBM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GTBM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GTBM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=228; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/228.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/228.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/228.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/228_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/228_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/228.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=228; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_228.json?time,air_temperature,wind_from_direction,wind_speed&orderByMax(%22time%22); error=HTTP Error 404: 
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Grand Traverse Light, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GTLM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GTLM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GTLM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GTLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GTLM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/GTLM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GTLM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GTLM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP
- Actual observation timestamp: 2026-08-27 20:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9087031 - Holland, MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/HLNM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=HLNM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/HLNM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/HLNM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/HLNM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/HLNM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/HLNM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/HLNM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 63rd St., Chicago, IL (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=JAKI2; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/JAKI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/JAKI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/JAKI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/JAKI2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/JAKI2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/JAKI2.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=JAKI2; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/JAKI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/JAKI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/JAKI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/JAKI2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/JAKI2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/JAKI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=113; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/113.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/113.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/113.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/113_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/113_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/113.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=377; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/377.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/377.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/377.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/377_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/377_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/377.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=391; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/391.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/391.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/391.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/391_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/391_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/391.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=387; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/387.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/387.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/387.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/387_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/387_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/387.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=383; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/383.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/383.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/383.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/383_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/383_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/383.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=378; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/378.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/378.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/378.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/378_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/378_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/378.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=113; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_113.json?time,air_pressure,air_temperature,relative_humidity,surface_downwelling_shortwave_flux_in_air,wind_from_direction,wind_speed,wind_speed_of_gust&orderByMax(%22time%22); error=HTTP Error 404:  | source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=377; error=source returned no valid timestamped observations | source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=391; error=source returned no valid timestamped observations | source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=387; error=source returned no valid timestamped observations | source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=383; error=source returned no valid timestamped observations | source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=378; error=source returned no valid timestamped observations
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Kenosha Light, Kenosha, WI (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=KNSW3; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/KNSW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/KNSW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/KNSW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/KNSW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/KNSW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/KNSW3.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=KNSW3; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/KNSW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/KNSW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/KNSW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/KNSW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/KNSW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/KNSW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=296; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/296.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/296.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/296.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/296_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/296_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/296.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=296; error=source returned no valid timestamped observations | parsed usable observation; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_296.json?time,air_pressure_at_mean_sea_level,air_temperature,tendency_of_air_pressure,wind_from_direction,wind_speed,wind_speed_of_gust&orderByMax(%22time%22); error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: air_pressure_at_mean_sea_level, air_temperature, wind_from_direction, wind_speed, wind_speed_of_gust
- Actual observation timestamp: 2024-09-28 23:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9087069 - Kewaunee MET, WI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/KWNW3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=KWNW3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/KWNW3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/KWNW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/KWNW3.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/KWNW3_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/KWNW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/KWNW3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9087023 - Ludington, MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45024.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45024; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45024.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45024.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45024.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45024_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45024_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45024.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, PRES, ATMP, WTMP
- Actual observation timestamp: 2026-08-27 20:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9075080 - Mackinaw City, MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MACM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=MACM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MACM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/MACM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/MACM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/MACM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/MACM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/MACM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Michigan City Harbor Entrance Light, Michigan City, IN (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MCYI3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=MCYI3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MCYI3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/MCYI3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/MCYI3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/MCYI3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/MCYI3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/MCYI3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-18 14:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Manistee Harbor, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=MEEM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/MEEM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/MEEM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/MEEM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/MEEM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/MEEM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/MEEM4.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=MEEM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/MEEM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/MEEM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/MEEM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/MEEM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/MEEM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/MEEM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=297; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/297.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/297.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/297.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/297_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/297_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/297.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=297; error=source returned no valid timestamped observations | parsed usable observation; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_297.json?time,air_pressure_at_mean_sea_level,air_temperature,tendency_of_air_pressure,wind_from_direction,wind_speed,wind_speed_of_gust&orderByMax(%22time%22); error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: air_temperature, wind_from_direction, wind_speed, wind_speed_of_gust
- Actual observation timestamp: 2025-09-24 00:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Muskegon CG Station, Muskegon, MI (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MKGM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=MKGM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MKGM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/MKGM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/MKGM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/MKGM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/MKGM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/MKGM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-18 14:50:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Port of Milwaukee (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MLWW3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=MLWW3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MLWW3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/MLWW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/MLWW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/MLWW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/MLWW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/MLWW3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP
- Actual observation timestamp: 2026-08-18 14:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9087088 - Menominee, MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MNMM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=MNMM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MNMM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/MNMM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/MNMM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/MNMM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/MNMM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/MNMM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Oak St., Chicago, IL (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OKSI2.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=OKSI2; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OKSI2.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/OKSI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/OKSI2.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/OKSI2_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/OKSI2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/OKSI2.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP
- Actual observation timestamp: 2026-08-25 12:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9087096 - Port Inland, MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/PNLM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=PNLM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/PNLM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/PNLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/PNLM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/PNLM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/PNLM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/PNLM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Port Washington, WI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/PWAW3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=PWAW3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/PWAW3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/PWAW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/PWAW3.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/PWAW3_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/PWAW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/PWAW3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, ATMP
- Actual observation timestamp: 2026-08-27 21:35:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Sheboygan, WI (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SGNW3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=SGNW3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SGNW3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/SGNW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/SGNW3.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/SGNW3_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/SGNW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/SGNW3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### St. Joseph, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=SJNM4; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/SJNM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/SJNM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/SJNM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/SJNM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/SJNM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/SJNM4.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=20CM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/20CM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/20CM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/20CM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/20CM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/20CM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/20CM4.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=SJOM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/SJOM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/SJOM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/SJOM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/SJOM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/SJOM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/SJOM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### South Haven Light, South Haven, MI (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45168.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45168; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45168.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45168.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45168.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45168_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45168_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45168.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, PRES, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 21:10:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Yacht Works Sister Bay, WI (Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CBRW3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=CBRW3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CBRW3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/CBRW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/CBRW3.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/CBRW3_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/CBRW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/CBRW3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP
- Actual observation timestamp: 2026-08-27 20:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Waukegan Harbor, IL (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/WHRI2.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=WHRI2; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/WHRI2.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/WHRI2.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/WHRI2.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/WHRI2_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/WHRI2_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/WHRI2.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### White Shoal Light, MI (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=WSLM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/WSLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/WSLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/WSLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/WSLM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/WSLM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/WSLM4.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=WSLM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/WSLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/WSLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/WSLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/WSLM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/WSLM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/WSLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=10; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/10.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/10.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/10.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/10_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/10_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/10.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=10; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_10.json?time,air_pressure,air_pressure_at_mean_sea_level,air_temperature,dew_point_temperature,relative_humidity,sea_surface_temperature,surface_downwelling_shortwave_flux_in_air,wind_from_direction,wind_speed,wind_speed_of_gust&orderByMax(%22time%22); error=HTTP Error 404: 
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Sleeping Bear Beach, MI (Beach)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=SLEEPING_BEAR_BEACH; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/SLEEPING_BEAR_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/SLEEPING_BEAR_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/SLEEPING_BEAR_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/SLEEPING_BEAR_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/SLEEPING_BEAR_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/SLEEPING_BEAR_BEACH.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45010; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45010_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45010_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=sleeping_bear_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/sleeping_bear_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/sleeping_bear_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/sleeping_bear_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/sleeping_bear_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/sleeping_bear_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/sleeping_bear_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Indiana Dunes Beach, IN (Beach)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45010; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45010_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45010_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=indiana_dunes_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/indiana_dunes_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/indiana_dunes_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/indiana_dunes_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/indiana_dunes_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/indiana_dunes_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/indiana_dunes_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Charlevoix Beach, MI (Beach)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45010; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45010_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45010_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=CHARLEVOIX_BEACH; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/CHARLEVOIX_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/CHARLEVOIX_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/CHARLEVOIX_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/CHARLEVOIX_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/CHARLEVOIX_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/CHARLEVOIX_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=charlevoix_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/charlevoix_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/charlevoix_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/charlevoix_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/charlevoix_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/charlevoix_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/charlevoix_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Saugatuck Beach, MI (Beach)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45010; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45010_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45010_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=saugatuck_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/saugatuck_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/saugatuck_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/saugatuck_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/saugatuck_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/saugatuck_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/saugatuck_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=375; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/375.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/375.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/375.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/375_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/375_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/375.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=375; error=source returned no valid timestamped observations
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### NORTH HURON - 32NM Northeast of Alpena, MI (2.3-meter foam discus buoy) [GLOS]
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45212.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45212; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45212.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45212.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45212.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45212_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45212_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45212.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WVHT, MWD
- Actual observation timestamp: 2026-08-27 19:20:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### SOUTH HURON - 43NM East of Oscoda, MI (2.3-meter foam discus buoy) [GLOS]
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45008; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45008.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45008.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45008.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45008_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45008_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45008.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=182; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/182.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/182.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/182.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/182_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/182_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/182.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=182; error=source returned no valid timestamped observations | parsed usable observation; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_182.json?time,air_pressure_at_mean_sea_level,air_temperature,dew_point_temperature,sea_surface_wave_from_direction,sea_surface_wave_mean_period,sea_surface_wave_period_at_variance_spectral_density_maximum,sea_surface_wave_significant_height,sea_water_temperature,sea_water_temperature_fixed_depth,wind_from_direction,wind_speed,wind_speed_of_gust&orderByMax(%22time%22); error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: air_pressure_at_mean_sea_level, air_temperature, dew_point_temperature, sea_water_temperature_fixed_depth, wind_from_direction, wind_speed, wind_speed_of_gust
- Actual observation timestamp: 2025-11-18 17:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Southern Lake Huron (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45149.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45149; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45149.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45149.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45149.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45149_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45149_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45149.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, WVHT, DPD, WTMP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### North Channel East (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45154.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45154; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45154.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45154.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45154.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45154_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45154_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45154.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, WVHT, DPD, PRES, ATMP, WTMP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Thunder Bay Buoy, Alpena, MI (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45162.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45162; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45162.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45162.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45162.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45162_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45162_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45162.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, PRES, ATMP, WTMP
- Actual observation timestamp: 2026-08-27 21:20:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Lakeport Buoy, MI (Moored Buoy)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45209.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45209; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45209.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45209.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45209.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45209_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45209_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45209.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, MWD, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### North Huron Spotter (Spotter Buoy)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45212.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45212; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45212.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45212.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45212.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45212_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45212_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45212.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WVHT, MWD
- Actual observation timestamp: 2026-08-27 19:20:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Alpena Harbor Light, Alpena, MI (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/APNM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=APNM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/APNM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/APNM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/APNM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/APNM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/APNM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/APNM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP
- Actual observation timestamp: 2026-08-18 14:50:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Cheboygan Marina, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CYGM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=CYGM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CYGM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/CYGM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/CYGM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/CYGM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/CYGM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/CYGM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 21:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9075099 - De Tour Village, MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/DTLM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=DTLM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/DTLM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/DTLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/DTLM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/DTLM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/DTLM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/DTLM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9014098 - Fort Gratiot, MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/FTGM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=FTGM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/FTGM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/FTGM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/FTGM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/FTGM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/FTGM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/FTGM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Gravelly Shoal Light, MI (Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GSLM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GSLM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GSLM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GSLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GSLM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/GSLM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GSLM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GSLM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP
- Actual observation timestamp: 2026-08-27 20:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9075014 - Harbor Beach, MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/HRBM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=HRBM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/HRBM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/HRBM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/HRBM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/HRBM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/HRBM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/HRBM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Port Hope, MI (Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/KP58.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=KP58; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/KP58.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/KP58.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/KP58.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/KP58_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/KP58_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/KP58.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 20:55:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9075065 - Alpena, MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/LPNM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=LPNM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/LPNM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/LPNM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/LPNM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/LPNM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/LPNM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/LPNM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9014095 - Port Huron, North of Blue Water Bridge, MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=PBWM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/PBWM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/PBWM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/PBWM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/PBWM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/PBWM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/PBWM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=9014095; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/9014095.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/9014095.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/9014095.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/9014095_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/9014095_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/9014095.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=BWB; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/BWB.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/BWB.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/BWB.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/BWB_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/BWB_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/BWB.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=167; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/167.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/167.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/167.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/167_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/167_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/167.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=624; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/624.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/624.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/624.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/624_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/624_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/624.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=306; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/306.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/306.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/306.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/306_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/306_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/306.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=628; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/628.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/628.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/628.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/628_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/628_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/628.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=106; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/106.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/106.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/106.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/106_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/106_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/106.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=167; error=source returned no valid timestamped observations | parsed usable observation; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_167.json?time,air_pressure,air_temperature,backscatter_turbidity,battery_voltage,dew_point_temperature,relative_humidity,sea_surface_wave_period_at_variance_spectral_density_maximum,sea_surface_wave_significant_height,sea_water_temperature,sea_water_temperature_fixed_depth,sea_water_temperature_0,sea_water_temperature_0_fixed_depth,sea_water_temperature_1,sea_water_temperature_1_fixed_depth,sea_water_temperature_2,sea_water_temperature_2_fixed_depth,sea_water_temperature_3,sea_water_temperature_3_fixed_depth,sea_water_temperature_4,sea_water_temperature_4_fixed_depth,sidescatter_turbidity,sidescatter_turbidity_fixed_depth,total_suspended_solids,total_suspended_solids_fixed_depth,wind_from_direction,wind_speed&orderByMax(%22time%22); error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: backscatter_turbidity, battery_voltage, sea_water_temperature, sea_water_temperature_fixed_depth, sea_water_temperature_0_fixed_depth, sea_water_temperature_1_fixed_depth, sea_water_temperature_2_fixed_depth, sea_water_temperature_3_fixed_depth, sea_water_temperature_4_fixed_depth, sidescatter_turbidity, sidescatter_turbidity_fixed_depth, total_suspended_solids, total_suspended_solids_fixed_depth
- Actual observation timestamp: 2025-04-04 17:50:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Presque Isle Light, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/PRIM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=PRIM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/PRIM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/PRIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/PRIM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/PRIM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/PRIM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/PRIM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WSPD, GST
- Actual observation timestamp: 2026-08-27 20:50:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Port Sanilac, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=PSCM4; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/PSCM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/PSCM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/PSCM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/PSCM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/PSCM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/PSCM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Sturgeon Point Light, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SPTM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=SPTM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SPTM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/SPTM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/SPTM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/SPTM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/SPTM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/SPTM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST
- Actual observation timestamp: 2026-08-27 20:50:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Spectacle Reef Light, MI (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SRLM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=SRLM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SRLM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/SRLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/SRLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/SRLM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/SRLM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/SRLM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: ATMP, DEWP
- Actual observation timestamp: 2026-08-18 17:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Tawas Point, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/TAWM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=TAWM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/TAWM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/TAWM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/TAWM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/TAWM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/TAWM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/TAWM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP
- Actual observation timestamp: 2026-08-27 16:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Thunder Bay Island, MI (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/TBIM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=TBIM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/TBIM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/TBIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/TBIM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/TBIM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/TBIM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/TBIM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP
- Actual observation timestamp: 2026-08-18 14:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Point Edward (Fixed Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=306; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/306.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/306.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/306.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/306_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/306_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/306.txt; error=HTTP Error 404: Not Found
- GLOS route results: parsed usable observation; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=306; error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: sea_water_electrical_conductivity_at_reference_temperature, sea_water_temperature, sea_water_ph_reported_on_total_scale, mass_concentration_of_oxygen_in_sea_water
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Canatara Beach, Sarnia, ON (Beach)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=canatara_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/canatara_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/canatara_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/canatara_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/canatara_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/canatara_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/canatara_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=306; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/306.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/306.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/306.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/306_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/306_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/306.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=624; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/624.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/624.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/624.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/624_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/624_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/624.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=BWB; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/BWB.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/BWB.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/BWB.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/BWB_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/BWB_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/BWB.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=167; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/167.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/167.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/167.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/167_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/167_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/167.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=628; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/628.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/628.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/628.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/628_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/628_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/628.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=106; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/106.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/106.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/106.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/106_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/106_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/106.txt; error=HTTP Error 404: Not Found
- GLOS route results: parsed usable observation; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=306; error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: sea_water_electrical_conductivity_at_reference_temperature, sea_water_temperature, sea_water_ph_reported_on_total_scale, mass_concentration_of_oxygen_in_sea_water
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Grand Bend Beach, ON (Beach)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GRAND_BEND_BEACH; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/GRAND_BEND_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GRAND_BEND_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GRAND_BEND_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/GRAND_BEND_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GRAND_BEND_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GRAND_BEND_BEACH.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=grand_bend_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/grand_bend_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/grand_bend_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/grand_bend_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/grand_bend_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/grand_bend_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/grand_bend_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Sauble Beach, ON (Beach)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=sauble_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/sauble_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/sauble_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/sauble_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/sauble_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/sauble_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/sauble_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Singing Sands Beach, ON (Beach)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=singing_sands_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/singing_sands_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/singing_sands_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/singing_sands_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/singing_sands_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/singing_sands_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/singing_sands_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Ipperwash Beach, ON (Beach)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=IPPERWASH_BEACH; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/IPPERWASH_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/IPPERWASH_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/IPPERWASH_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/IPPERWASH_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/IPPERWASH_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/IPPERWASH_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=ipperwash_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/ipperwash_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/ipperwash_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/ipperwash_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/ipperwash_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/ipperwash_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/ipperwash_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Pinery Provincial Park Beach, ON (Beach)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=PINERY_BEACH; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/PINERY_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/PINERY_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/PINERY_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/PINERY_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/PINERY_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/PINERY_BEACH.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=pinery_provincial_park_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/pinery_provincial_park_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/pinery_provincial_park_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/pinery_provincial_park_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/pinery_provincial_park_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/pinery_provincial_park_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/pinery_provincial_park_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Port Franks Beach, ON (Beach)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=PORT_FRANKS_BEACH; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/PORT_FRANKS_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/PORT_FRANKS_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/PORT_FRANKS_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/PORT_FRANKS_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/PORT_FRANKS_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/PORT_FRANKS_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=port_franks_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/port_franks_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/port_franks_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/port_franks_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/port_franks_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/port_franks_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/port_franks_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Bayfield Beach, ON (Beach)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=BAYFIELD_BEACH_ON; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/BAYFIELD_BEACH_ON.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/BAYFIELD_BEACH_ON.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/BAYFIELD_BEACH_ON.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/BAYFIELD_BEACH_ON_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/BAYFIELD_BEACH_ON_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/BAYFIELD_BEACH_ON.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=bayfield_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/bayfield_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/bayfield_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/bayfield_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/bayfield_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/bayfield_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/bayfield_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Walnut Creek Buoy (Moored Buoy)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/4403585.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=4403585; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/4403585.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/4403585.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/4403585.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/4403585_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/4403585_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/4403585.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WSPD, WVHT, MWD, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 20:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Buffalo Buoy (GLOS Weather Station)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/4403586.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=4403586; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/4403586.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/4403586.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/4403586.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/4403586_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/4403586_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/4403586.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WTMP
- Actual observation timestamp: 2026-08-27 20:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### WEST ERIE - 16 NM NW of Lorain, OH (2.3-meter foam discus buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45005.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45005; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45005.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45005.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45005.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45005_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45005_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45005.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

###  (3-meter discus buoy)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Port Stanley (3-meter discus buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45132.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45132; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45132.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45132.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45132.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45132_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45132_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45132.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, PRES, ATMP, WTMP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Port Colborne (3-meter discus buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45142.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45142; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45142.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45142.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45142.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45142_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45142_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45142.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, PRES, ATMP, WTMP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Lake St Clair (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45147.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45147; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45147.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45147.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45147.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45147_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45147_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45147.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, WVHT, DPD, PRES, ATMP, WTMP
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Cleveland Buoy, OH (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45164.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45164; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45164.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45164.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45164.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45164_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45164_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45164.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WVHT, ATMP, WTMP
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Toledo Water Intake Buoy, Oregon, OH (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45165.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45165; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45165.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45165.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45165.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45165_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45165_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45165.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, MWD, ATMP, WTMP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Erie Nearshore Buoy, Erie, PA (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45167.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45167; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45167.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45167.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45167.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45167_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45167_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45167.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 20:20:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Lakewood Buoy, OH (Buoy) [GLOS]
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45169; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45169.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45169.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45169.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45169_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45169_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45169.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=216; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/216.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/216.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/216.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/216_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/216_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/216.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=216; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_216.json?time,air_pressure,air_temperature,battery_voltage,dew_point_temperature,fluorescent_dissolved_organic_matter,fractional_saturation_of_oxygen_in_sea_water,mass_concentration_of_oxygen_in_sea_water,relative_humidity,sea_surface_temperature,sea_surface_wave_from_direction,sea_surface_wave_maximum_height,sea_surface_wave_maximum_period,sea_surface_wave_mean_height_of_highest_tenth,sea_surface_wave_significant_height,sea_surface_wave_significant_period,sea_water_electrical_conductivity,sea_water_temperature,sea_water_temperature_fixed_depth,surface_downwelling_shortwave_flux_in_air,wind_from_direction,wind_speed,wind_speed_of_gust&orderByMax(%22time%22); error=HTTP Error 404: 
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Cleveland Intake Crib Buoy, OH (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45176.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45176; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45176.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45176.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45176.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45176_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45176_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45176.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, PRES, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Rocky River, OH (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45196.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45196; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45196.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45196.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45196.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45196_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45196_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45196.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, MWD, PRES, ATMP, DEWP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Euclid, OH (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45197.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45197; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45197.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45197.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45197.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45197_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45197_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45197.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, PRES, ATMP, WTMP, DEWP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Maumee Bay Buoy (Moored Buoy)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45200.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45200; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45200.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45200.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45200.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45200_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45200_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45200.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, MWD, PRES, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 21:20:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Erie Islands Buoy (Moored Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45201.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45201; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45201.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45201.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45201.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45201_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45201_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45201.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, MWD, PRES, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Port Clinton Buoy (Moored Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45202.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45202; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45202.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45202.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45202.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45202_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45202_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45202.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, MWD, PRES, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Huron Buoy (Moored Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45203.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45203; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45203.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45203.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45203.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45203_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45203_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45203.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, WTMP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Sheffield Buoy (Moored Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45204.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45204; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45204.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45204.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45204.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45204_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45204_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45204.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, ATMP, WTMP
- Actual observation timestamp: 2026-08-27 21:20:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Edgewater Beach Buoy (Moored Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45205.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45205; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45205.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45205.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45205.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45205_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45205_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45205.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, PRES, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Euclid Beach Buoy (Moored Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45206.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45206; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45206.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45206.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45206.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45206_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45206_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45206.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Mentor Harbor Buoy (Moored Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45207.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45207; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45207.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45207.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45207.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45207_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45207_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45207.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, ATMP, WTMP
- Actual observation timestamp: 2026-08-27 21:20:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Ashtabula Buoy (Moored Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/ASBO1.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=ASBO1; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/ASBO1.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/ASBO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/ASBO1.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/ASBO1_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/ASBO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/ASBO1.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Dunkirk Buoy (GLOS Weather Station)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45220.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45220; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45220.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45220.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45220.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45220_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45220_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45220.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, WVHT, MWD, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 20:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Beach 2 Buoy (Moored Buoy)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/BCTP1.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=BCTP1; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/BCTP1.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/BCTP1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/BCTP1.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/BCTP1_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/BCTP1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/BCTP1.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 20:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Beach 6 Buoy (Moored Buoy)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45223.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45223; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45223.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45223.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45223.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45223_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45223_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45223.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WTMP
- Actual observation timestamp: 2026-08-27 20:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9014070 - Algonac, MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/AGCM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=AGCM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/AGCM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/AGCM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/AGCM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/AGCM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/AGCM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/AGCM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Ashtabula Lighthouse ()
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/ASBO1.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=ASBO1; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/ASBO1.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/ASBO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/ASBO1.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/ASBO1_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/ASBO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/ASBO1.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Barcelona Harbor, NY (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/BARN6.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=BARN6; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/BARN6.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/BARN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/BARN6.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/BARN6_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/BARN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/BARN6.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Beach 2 Tower (Coastal Marine Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/BCTP1.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=BCTP1; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/BCTP1.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/BCTP1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/BCTP1.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/BCTP1_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/BCTP1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/BCTP1.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 20:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9063020 - Buffalo, NY (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/BUFN6.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=BUFN6; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/BUFN6.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/BUFN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/BUFN6.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/BUFN6_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/BUFN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/BUFN6.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Conneaut Breakwater Light, OH (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CBLO1.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=CBLO1; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CBLO1.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/CBLO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/CBLO1.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/CBLO1_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/CBLO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/CBLO1.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Camp Perry, OH (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CMPO1.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=CMPO1; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CMPO1.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/CMPO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/CMPO1.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/CMPO1_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/CMPO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/CMPO1.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WSPD, GST, ATMP
- Actual observation timestamp: 2026-08-24 21:50:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9063063 - Cleveland, OH (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45164.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45164; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45164.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45164.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45164.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45164_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45164_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45164.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WVHT, ATMP, WTMP
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Dunkirk, NY (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/DBLN6.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=DBLN6; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/DBLN6.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/DBLN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/DBLN6.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/DBLN6_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/DBLN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/DBLN6.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9063038 - Erie (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date=20260825&end_date=20260827&station=9063038&product=water_level&datum=LWD&units=english&time_zone=gmt&format=json; error=none
- NOAA alternate attempts: none
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA CO-OPS
- Actual variables obtained: water_level
- Actual observation timestamp: 2026-08-27 21:48:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9063053 - Fairport, OH (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/FAIO1.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=FAIO1; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/FAIO1.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/FAIO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/FAIO1.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/FAIO1_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/FAIO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/FAIO1.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Geneva on the Lake Light, OH (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GELO1; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/GELO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GELO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GELO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/GELO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GELO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GELO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=LEASH; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/LEASH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/LEASH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/LEASH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/LEASH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/LEASH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/LEASH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=17; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/17.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/17.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/17.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/17_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/17_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/17.txt; error=HTTP Error 404: Not Found
- GLOS route results: parsed usable observation; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=17; error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: sea_water_ph_reported_on_total_scale, chlorophyll_fluorescence, fractional_saturation_of_oxygen_in_sea_water, sea_water_temperature, sea_water_electrical_conductivity_at_reference_temperature, mass_concentration_of_oxygen_in_sea_water, phycocyanin_fluorescence, sea_water_turbidity
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Huron Harbor Light, OH (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/HHLO1.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=HHLO1; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/HHLO1.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/HHLO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/HHLO1.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/HHLO1_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/HHLO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/HHLO1.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Lorain Harbor, OH (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45005.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45005; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45005.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45005.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45005.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45005_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45005_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45005.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9014090 - Mouth of the Black River, MI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MBRM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=MBRM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MBRM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/MBRM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/MBRM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/MBRM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/MBRM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/MBRM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: PRES
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9063079 - Marblehead, OH (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MRHO1.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=MRHO1; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/MRHO1.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/MRHO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/MRHO1.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/MRHO1_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/MRHO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/MRHO1.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Northeast Marina, PA (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/NREP1.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=NREP1; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/NREP1.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/NREP1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/NREP1.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/NREP1_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/NREP1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/NREP1.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD
- Actual observation timestamp: 2026-08-27 20:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Darrow Road, Old Woman Creek Reserve, OH (NERRS Water Quality Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=OWDO1; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/OWDO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/OWDO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/OWDO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/OWDO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/OWDO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/OWDO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=OWCDRWQ; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/OWCDRWQ.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/OWCDRWQ.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/OWCDRWQ.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/OWCDRWQ_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/OWCDRWQ_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/OWCDRWQ.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=233; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/233.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/233.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/233.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/233_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/233_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/233.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=237; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/237.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/237.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/237.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/237_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/237_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/237.txt; error=HTTP Error 404: Not Found
- GLOS route results: parsed usable observation; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=233; error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: sea_water_temperature, mass_concentration_of_oxygen_in_sea_water, sea_water_turbidity, fractional_saturation_of_oxygen_in_sea_water, sea_water_practical_salinity, sea_water_electrical_conductivity_at_reference_temperature, sea_water_ph_reported_on_total_scale
- Actual observation timestamp: 2026-08-27 20:15:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Lower Estuary, Old Woman Creek Reserve, OH (NERRS Water Quality Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=OWQO1; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/OWQO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/OWQO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/OWQO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/OWQO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/OWQO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/OWQO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=OWCOLWQ; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/OWCOLWQ.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/OWCOLWQ.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/OWCOLWQ.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/OWCOLWQ_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/OWCOLWQ_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/OWCOLWQ.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=235; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/235.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/235.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/235.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/235_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/235_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/235.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=237; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/237.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/237.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/237.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/237_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/237_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/237.txt; error=HTTP Error 404: Not Found
- GLOS route results: parsed usable observation; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=235; error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: sea_water_ph_reported_on_total_scale, sea_water_electrical_conductivity_at_reference_temperature, sea_water_temperature, mass_concentration_of_oxygen_in_sea_water, sea_water_turbidity, sea_water_practical_salinity, fractional_saturation_of_oxygen_in_sea_water
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### State Road 6, Old Woman Creek Reserve, OH (NERRS Water Quality Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=OWSO1; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/OWSO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/OWSO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/OWSO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/OWSO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/OWSO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/OWSO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=237; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/237.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/237.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/237.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/237_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/237_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/237.txt; error=HTTP Error 404: Not Found
- GLOS route results: parsed usable observation; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=237; error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: wind_speed_of_gust, relative_humidity, surface_downwelling_photosynthetic_photon_flux_in_air, air_pressure, lwe_thickness_of_precipitation_amount, wind_speed, wind_from_direction
- Actual observation timestamp: 2026-08-27 20:45:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Railroad, Old Woman Creek Reserve, OH (Water Quality Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=OWWO1; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/OWWO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/OWWO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/OWWO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/OWWO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/OWWO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/OWWO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=237; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/237.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/237.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/237.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/237_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/237_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/237.txt; error=HTTP Error 404: Not Found
- GLOS route results: parsed usable observation; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=237; error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: wind_speed_of_gust, relative_humidity, surface_downwelling_photosynthetic_photon_flux_in_air, air_pressure, lwe_thickness_of_precipitation_amount, wind_speed, wind_from_direction
- Actual observation timestamp: 2026-08-27 20:45:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Old Woman Creek, Old Woman Creek Reserve, OH (NERRS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OWXO1.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=OWXO1; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OWXO1.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/OWXO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/OWXO1.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/OWXO1_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/OWXO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/OWXO1.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 20:45:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9063028 - Sturgeon Point, NY (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/PSTN6.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=PSTN6; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/PSTN6.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/PSTN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/PSTN6.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/PSTN6_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/PSTN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/PSTN6.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: PRES
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### South Bass Island, OH (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SBIO1.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=SBIO1; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SBIO1.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/SBIO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/SBIO1.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/SBIO1_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/SBIO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/SBIO1.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 21:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Toledo Light No. 2 OH (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/THLO1.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=THLO1; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/THLO1.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/THLO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/THLO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/THLO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/THLO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/THLO1.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, DEWP
- Actual observation timestamp: 2026-08-18 14:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9063085 - Toledo, OH (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/THRO1.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=THRO1; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/THRO1.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/THRO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/THRO1.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/THRO1_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/THRO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/THRO1.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### TREC Tower (Coastal Marine Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/TRTP1.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=TRTP1; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/TRTP1.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/TRTP1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/TRTP1.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/TRTP1_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/TRTP1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/TRTP1.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 20:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Toledo Crib, OH (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/TWCO1.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=TWCO1; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/TWCO1.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/TWCO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/TWCO1.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/TWCO1_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/TWCO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/TWCO1.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WSPD, GST, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 20:40:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Vermilion River at Lake Erie, OH ()
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/VRMO1.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=VRMO1; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/VRMO1.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/VRMO1.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/VRMO1.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/VRMO1_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/VRMO1_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/VRMO1.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST
- Actual observation timestamp: 2026-08-27 21:10:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Walnut Creek Marina, PA ()
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/4403585.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=4403585; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/4403585.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/4403585.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/4403585.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/4403585_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/4403585_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/4403585.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WSPD, WVHT, MWD, ATMP, WTMP, DEWP
- Actual observation timestamp: 2026-08-27 20:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Point Pelee Beach, ON (Beach)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=POINT_PELEE_BEACH; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/POINT_PELEE_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/POINT_PELEE_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/POINT_PELEE_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/POINT_PELEE_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/POINT_PELEE_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/POINT_PELEE_BEACH.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=point_pelee_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/point_pelee_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/point_pelee_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/point_pelee_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/point_pelee_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/point_pelee_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/point_pelee_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Rondeau Provincial Park Beach, ON (Beach)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=rondeau_provincial_park_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/rondeau_provincial_park_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/rondeau_provincial_park_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/rondeau_provincial_park_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/rondeau_provincial_park_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/rondeau_provincial_park_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/rondeau_provincial_park_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Colchester Beach, ON (Beach)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=colchester_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/colchester_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/colchester_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/colchester_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/colchester_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/colchester_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/colchester_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Port Stanley Beach, ON (Beach)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45132.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45132; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45132.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45132.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45132.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45132_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45132_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45132.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, PRES, ATMP, WTMP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Port Burwell Beach, ON (Beach)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=PORT_BURWELL_BEACH; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/PORT_BURWELL_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/PORT_BURWELL_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/PORT_BURWELL_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/PORT_BURWELL_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/PORT_BURWELL_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/PORT_BURWELL_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=port_burwell_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/port_burwell_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/port_burwell_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/port_burwell_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/port_burwell_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/port_burwell_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/port_burwell_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Port Dover Beach, ON (Beach)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=port_dover_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/port_dover_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/port_dover_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/port_dover_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/port_dover_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/port_dover_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/port_dover_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Long Point Beach, ON (Beach)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=LONG_POINT_BEACH; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/LONG_POINT_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/LONG_POINT_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/LONG_POINT_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/LONG_POINT_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/LONG_POINT_BEACH_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/LONG_POINT_BEACH.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=long_point_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/long_point_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/long_point_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/long_point_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/long_point_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/long_point_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/long_point_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### EAST Lake Ontario  - 20NM North Northeast of Rochester, NY (2.3-meter foam discus buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45012.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45012; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45012.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45012.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45012.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45012_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45012_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45012.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, APD, MWD, PRES, ATMP
- Actual observation timestamp: 2026-08-27 21:20:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Prince Edward Pt (3-meter discus buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45135.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45135; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45135.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45135.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45135.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45135_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45135_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45135.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, PRES, ATMP, WTMP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### West Lake Ontario - Grimsby (3-meter discus buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45139.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45139; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45139.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45139.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45139.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45139_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45139_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45139.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, PRES, ATMP, WTMP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Lake Simcoe (Buoy)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45151.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45151; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45151.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45151.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45151.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45151_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45151_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45151.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, WVHT, DPD, PRES, ATMP, WTMP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Pan Am Games (3-meter discus buoy)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45155; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45155.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45155.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45155.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45155_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45155_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45155.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=FD010; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/FD010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/FD010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/FD010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/FD010_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/FD010_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/FD010.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=210; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/210.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/210.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/210.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/210_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/210_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/210.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=FD001; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/FD001.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/FD001.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/FD001.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/FD001_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/FD001_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/FD001.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=175; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/175.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/175.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/175.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/175_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/175_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/175.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=FD007; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/FD007.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/FD007.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/FD007.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/FD007_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/FD007_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/FD007.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=209; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/209.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/209.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/209.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/209_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/209_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/209.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=210; error=source returned no valid timestamped observations | parsed usable observation; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_210.json?time,air_temperature,battery_voltage,surface_elevation&orderByMax(%22time%22); error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: air_temperature, battery_voltage, surface_elevation
- Actual observation timestamp: 2025-04-02 10:36:50 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### NW Lake Ontario Ajax (3-meter discus buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45159.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45159; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45159.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45159.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45159.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45159_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45159_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45159.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, PRES, ATMP, WTMP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Sodus Point, NY (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45190.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45190; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45190.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45190.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45190.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45190_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45190_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45190.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 20:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Oak Orchard, NY (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45191.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45191; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45191.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45191.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45191.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45191_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45191_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45191.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WSPD, GST, ATMP, DEWP
- Actual observation timestamp: 2026-08-27 20:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Oswego, NY (274) (Waverider Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OSGN6.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=OSGN6; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OSGN6.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/OSGN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/OSGN6.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/OSGN6_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/OSGN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/OSGN6.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9052000 - Cape Vincent, NY (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CAVN6.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=CAVN6; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CAVN6.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/CAVN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/CAVN6.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/CAVN6_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/CAVN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/CAVN6.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Galloo Island, NY (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GLLN6; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/GLLN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GLLN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GLLN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/GLLN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GLLN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GLLN6.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### 9063012 - Niagara Intake, NY (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/NIAN6.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=NIAN6; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/NIAN6.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/NIAN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/NIAN6.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/NIAN6_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/NIAN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/NIAN6.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: PRES
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Olcott Harbor, NY (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OLCN6.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=OLCN6; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OLCN6.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/OLCN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/OLCN6.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/OLCN6_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/OLCN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/OLCN6.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9052030 - Oswego, NY (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OSGN6.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=OSGN6; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OSGN6.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/OSGN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/OSGN6.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/OSGN6_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/OSGN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/OSGN6.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9052058 - Rochester, NY (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/RCRN6.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=RCRN6; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/RCRN6.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/RCRN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/RCRN6.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/RCRN6_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/RCRN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/RCRN6.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: ATMP
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Rochester Coast Guard, NY (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/RPRN6.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=RPRN6; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/RPRN6.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/RPRN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/RPRN6.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/RPRN6_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/RPRN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/RPRN6.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Niagara Coast Guard Station, NY (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=YGNN6; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/YGNN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/YGNN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/YGNN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/YGNN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/YGNN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/YGNN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=299; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/299.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/299.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/299.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/299_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/299_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/299.txt; error=HTTP Error 404: Not Found
- GLOS route results: parsed usable observation; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=299; error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: mass_concentration_of_oxygen_in_sea_water, sea_water_electrical_conductivity_at_reference_temperature, sea_water_ph_reported_on_total_scale, sea_water_temperature
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Toronto Beach, ON (Beach)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=toronto_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/toronto_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/toronto_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/toronto_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/toronto_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/toronto_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/toronto_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Hamilton Beach, ON (Beach)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=hamilton_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/hamilton_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/hamilton_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/hamilton_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/hamilton_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/hamilton_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/hamilton_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Burlington Beach, ON (Beach)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=burlington_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/burlington_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/burlington_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/burlington_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/burlington_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/burlington_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/burlington_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Cobourg Beach, ON (Beach)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=cobourg_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/cobourg_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/cobourg_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/cobourg_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/cobourg_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/cobourg_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/cobourg_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Georgian Bay (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45143.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45143; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45143.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45143.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45143.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45143_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45143_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45143.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, PRES, ATMP, WTMP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### South Georgian Bay (3-meter discus buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45137.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45137; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45137.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45137.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45137.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45137_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45137_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45137.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, PRES, ATMP, WTMP
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Lake Nipissing (Buoy)
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45152.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45152; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45152.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45152.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45152.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45152_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45152_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45152.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, WVHT, DPD, PRES, ATMP, WTMP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Wasaga Beach, ON (Beach)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=wasaga_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/wasaga_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/wasaga_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/wasaga_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/wasaga_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/wasaga_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/wasaga_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Sunset Point Beach, Collingwood, ON (Beach)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45009; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45009_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45009.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=sunset_point_beach; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/sunset_point_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/sunset_point_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/sunset_point_beach.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/sunset_point_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/sunset_point_beach_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/sunset_point_beach.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

### Sturgeon Bay CG Station, WI (Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=0Y2W3; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/0Y2W3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/0Y2W3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/0Y2W3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/0Y2W3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/0Y2W3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/0Y2W3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=94; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/94.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/94.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/94.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/94_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/94_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/94.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=94; error=source returned no valid timestamped observations | parsed usable observation; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_94.json?time,AirP,AirT,Chl,DO,DO_fixed_depth,DOS,DOS_fixed_depth,PAR,Phyco,WD,WS,WTemp0,WTemp1,WTemp1_fixed_depth,WTemp2,WTemp2_fixed_depth,WTemp3,WTemp3_fixed_depth,WTemp4,WTemp4_fixed_depth,WTemp5,WTemp5_fixed_depth,WTemp6,WTemp6_fixed_depth,WTemp7,WTemp7_fixed_depth,WTemp8,WTemp8_fixed_depth,WTemp9,WTemp9_fixed_depth,WVDIR,WVHT&orderByMax(%22time%22); error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: AirT, Chl, DO, DO_fixed_depth, DOS, DOS_fixed_depth, Phyco, WD, WS, WTemp0, WTemp1, WTemp1_fixed_depth, WTemp2, WTemp2_fixed_depth, WTemp3, WTemp3_fixed_depth, WTemp4, WTemp4_fixed_depth, WTemp5_fixed_depth, WTemp6_fixed_depth, WTemp7_fixed_depth, WTemp8_fixed_depth, WTemp9_fixed_depth, WVDIR, WVHT
- Actual observation timestamp: 2025-09-26 17:37:17 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### GB17 - South Green Bay, WI (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45014.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45014; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45014.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45014.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45014.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45014_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45014_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45014.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, WVHT, DPD, MWD, ATMP, WTMP
- Actual observation timestamp: 2026-08-22 13:30:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Green Bay East Buoy (Moored Buoy) [GLOS]
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45184; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/45184.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45184.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45184.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45184_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45184_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45184.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=60; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/60.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/60.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/60.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/60_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/60_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/60.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=43; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/43.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/43.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/43.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/43_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/43_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/43.txt; error=HTTP Error 404: Not Found
- GLOS route results: source responded with no valid observation data; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=60; error=source returned no valid timestamped observations | lookup failed; URL=https://seagull-erddap.glos.org/erddap/tabledap/obs_60.json?time,battery_voltage,chlorophyll_fluorescence,concentration_of_fluorescent_dissolved_organic_matter,fluorescent_dissolved_organic_matter,fractional_saturation_of_oxygen_in_sea_water,mass_concentration_of_blue_green_algae_in_sea_water_rfu,mass_concentration_of_blue_green_algae_in_sea_water_rfu_fixed_depth,mass_concentration_of_oxygen_in_sea_water,phycocyanin_fluorescence,sea_surface_temperature,sea_water_electrical_conductivity,sea_water_ph_reported_on_total_scale,sea_water_temperature_0,sea_water_temperature_0_fixed_depth,sea_water_temperature_1,sea_water_temperature_1_fixed_depth,sea_water_temperature_2,sea_water_temperature_2_fixed_depth,sea_water_turbidity,surface_downwelling_photosynthetic_photon_flux_in_air,surface_downwelling_photosynthetic_photon_flux_in_sea_water,wind_from_direction,wind_speed&orderByMax(%22time%22); error=HTTP Error 404:  | parsed usable observation; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=43; error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: wind_speed_of_gust, sea_water_turbidity, wind_from_direction, sea_surface_wave_significant_height, sea_water_temperature, surface_downwelling_shortwave_flux_in_air, air_temperature, sea_surface_wave_from_direction_at_variance_spectral_density_maximum, sea_surface_wave_period_at_variance_spectral_density_maximum, air_pressure_at_mean_sea_level, wind_speed, mass_concentration_of_chlorophyll_in_sea_water, phycocyanin_fluorescence, sea_surface_wave_maximum_height, sea_surface_wave_from_direction, sea_surface_wave_mean_height_of_highest_tenth, battery_voltage
- Actual observation timestamp: 2026-08-22 14:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Green Bay West Buoy (Moored Buoy) [GLOS]
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GBWW3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GBWW3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GBWW3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GBWW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GBWW3.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/GBWW3_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GBWW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GBWW3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Green Bay Entrance Light, WI (Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GBLW3; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/GBLW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GBLW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GBLW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/GBLW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GBLW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GBLW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=43; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/43.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/43.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/43.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/43_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/43_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/43.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GBEL; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/GBEL.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GBEL.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GBEL.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/GBEL_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GBEL_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GBEL.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=154; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/154.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/154.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/154.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/154_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/154_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/154.txt; error=HTTP Error 404: Not Found
- GLOS route results: parsed usable observation; URL=https://seagull-api.glos.org/api/v1/obs?startDate=2026-07-28&obsDatasetId=43; error=none
- Final selected source: GLOS Seagull
- Actual variables obtained: wind_speed_of_gust, sea_water_turbidity, wind_from_direction, sea_surface_wave_significant_height, sea_water_temperature, surface_downwelling_shortwave_flux_in_air, air_temperature, sea_surface_wave_from_direction_at_variance_spectral_density_maximum, sea_surface_wave_period_at_variance_spectral_density_maximum, air_pressure_at_mean_sea_level, wind_speed, mass_concentration_of_chlorophyll_in_sea_water, phycocyanin_fluorescence, sea_surface_wave_maximum_height, sea_surface_wave_from_direction, sea_surface_wave_mean_height_of_highest_tenth, battery_voltage
- Actual observation timestamp: 2026-08-22 14:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 9087077 - Green Bay West, WI (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GBWW3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=GBWW3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/GBWW3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/GBWW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/GBWW3.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/GBWW3_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/GBWW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/GBWW3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Northport Pier at Death's Door, WI (Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/NPDW3.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=NPDW3; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/NPDW3.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/NPDW3.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/NPDW3.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/NPDW3_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/NPDW3_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/NPDW3.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Saginaw Bay Buoy, MI (Buoy) [GLOS]
- Previous status: missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45163.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45163; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45163.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45163.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45163.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/45163_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45163_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45163.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: ATMP
- Actual observation timestamp: 2026-07-14 05:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Saginaw Bay Light #1, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SBLM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=SBLM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/SBLM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/SBLM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/SBLM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/SBLM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/SBLM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/SBLM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### St. Clair Shores, MI (GLOS Weather Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CLSM4.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=CLSM4; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/CLSM4.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/CLSM4.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/CLSM4.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/CLSM4_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/CLSM4_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/CLSM4.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, GST, PRES, ATMP, PTDY
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Lake St. Clair Light, MI (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45147.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=45147; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/45147.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/45147.txt; error=HTTP Error 404: Not Found | source responded but parse failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/45147.txt; error=response contained no NOAA header | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/45147_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/45147_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/45147.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: WDIR, WSPD, WVHT, DPD, PRES, ATMP, WTMP
- Actual observation timestamp: 2026-08-27 21:00:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Alexandria Bay, NY (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/ALXN6.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=ALXN6; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/ALXN6.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/ALXN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/ALXN6.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/ALXN6_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/ALXN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/ALXN6.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 8311062 - Alexandria Bay, NY (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/ALXN6.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=ALXN6; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/ALXN6.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/ALXN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/ALXN6.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/ALXN6_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/ALXN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/ALXN6.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: PRES, WTMP
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### 8311030 - Ogdensburg, NY (Water Level Observation Network)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OBGN6.txt; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=OBGN6; error=station page fetched; observation feed required | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/realtime2/OBGN6.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/OBGN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/OBGN6.txt; error=HTTP Error 404: Not Found | parsed usable observation; URL=https://www.ndbc.noaa.gov/data/5day2/OBGN6_5day.txt; error=none | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/OBGN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/OBGN6.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: NOAA NDBC
- Actual variables obtained: PRES
- Actual observation timestamp: 2026-08-27 21:18:00 UTC
- Description successfully repaired: yes
- Reason: ONLINE: live observation rebuilt from one source observation row

### Thousand I. Brdg., NY (C-MAN Station)
- Previous status: Data unavailable; missing Observed timestamp; retrieval timestamp used without observation timestamp
- NOAA lookup/result: lookup failed; URL=; error=none
- NOAA alternate attempts: source responded but parse failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=THIN6; error=station page fetched; observation feed required | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/THIN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/THIN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/THIN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/THIN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/THIN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/THIN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/station_page.php?station=TICN6; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime2/TICN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/realtime/TICN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/latest_obs/TICN6.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day2/TICN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/5day/TICN6_5day.txt; error=HTTP Error 404: Not Found | lookup failed; URL=https://www.ndbc.noaa.gov/data/historical/TICN6.txt; error=HTTP Error 404: Not Found
- GLOS route results: not queried because NOAA row was usable
- Final selected source: none
- Actual variables obtained: none
- Actual observation timestamp: none
- Description successfully repaired: yes
- Reason: OFFLINE: exact platform identified and linked; no current observation (auto-retried next run)

## Lists

### OFFLINE (exact platform linked, no current observation) (46)

-  (3-meter discus buoy)
- 63rd St., Chicago, IL (C-MAN Station)
- Algoma City Marina, WI (Weather Station)
- Barker's Island, Lake Superior Reserve, WI (NERRS Water Quality Station)
- Bayfield Beach, ON (Beach)
- Bayfield Beach, WI (Beach)
- Burlington Beach, ON (Beach)
- Calumet Beach, Chicago, IL (Buoy)
- Charlevoix Beach, MI (Beach)
- Cobourg Beach, ON (Beach)
- Colchester Beach, ON (Beach)
- Galloo Island, NY (C-MAN Station)
- Grand Bend Beach, ON (Beach)
- Grand Traverse Bay Observing System Station 2 (Coastal Marine Station)
- Grand Traverse Bay South Buoy, MI (Moored Buoy) [GLOS]
- Granite Island Buoy, Granite Island, MI (Buoy) [GLOS]
- Granite Island, MI (Weather Station)
- Hamilton Beach, ON (Beach)
- Indiana Dunes Beach, IN (Beach)
- Ipperwash Beach, ON (Beach)
- Isle of Royale East, MI (230) (Waverider Buoy) [GLOS]
- Lakewood Buoy, OH (Buoy) [GLOS]
- Long Point Beach, ON (Beach)
- MID SUPERIOR- 60NM North Northeast Hancock, MI (2.1-meter ionomer foam buoy)
- Madeline Island Beach, WI (Beach)
- Pinery Provincial Park Beach, ON (Beach)
- Point Pelee Beach, ON (Beach)
- Port Burwell Beach, ON (Beach)
- Port Dover Beach, ON (Beach)
- Port Franks Beach, ON (Beach)
- Port Sanilac, MI (GLOS Weather Station)
- Rondeau Provincial Park Beach, ON (Beach)
- Sauble Beach, ON (Beach)
- Saugatuck Beach, MI (Beach)
- Singing Sands Beach, ON (Beach)
- Sixth-third St. Beach, Chicago, IL (Buoy)
- Sleeping Bear Beach, MI (Beach)
- St. Joseph CG Station, MI (Weather Station)
- St. Joseph, MI (GLOS Weather Station)
- Sunset Point Beach, Collingwood, ON (Beach)
- Superior Shoals, NY (C-MAN Station)
- Thousand I. Brdg., NY (C-MAN Station)
- Toronto Beach, ON (Beach)
- Traverse Bay #3, MI (Moored Buoy) [GLOS]
- Wasaga Beach, ON (Beach)
- White Shoal Light, MI (C-MAN Station)

### UNRESOLVED (exact platform/source identity could not be established) (0)


### Suspicious (0)


### Both NOAA and GLOS attempted but no current rows (0)


### Source returned but parse failed (0)


### No source (0)


## Representative Live Checks

- NOAA NDBC: station-page, realtime2, realtime, latest_obs, 5day2, 5day, and historical routes were attempted for each identity-resolved NDBC record.
- NOAA CO-OPS: documented datagetter water-level route was used only for placemarks explicitly identified as CO-OPS stations.
- GLOS: documented API/catalog route was attempted; ERDDAP metadata and tabledap were used as a fallback when API data was absent.
- Every selected row is one newest coherent timestamp group; timestamp fields are excluded from displayed measurements.

## Coherence Check

- Selected records with measurements and one Observed timestamp: 210/256
- No selected record combines measurements from different timestamps.
- Unresolved records are not claimed complete; each retains identity-specific route results and a categorized reason.
