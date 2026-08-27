# Live Great Lakes Buoys — GitHub Pages Deployment

This implements the auto-refreshing Google Earth architecture:

```
Google Earth
  → NetworkLink (live_buoys_networklink.kml)
  → public GitHub Pages KML (https://<owner>.github.io/<repo>/live_buoys.kml)
  → GitHub Actions (every 15 min)
  → generate_live_kml.py
  → live NOAA / GLOS observations
  → regenerated placemark descriptions (Observed + Fetched)
```

The data generator (`generate_live_kml.py`) reuses the exact-identity resolution
from `repair_live_buoys_candidate.py`: no nearby-platform substitution, each
platform shows only its real variables, `Observed` = source time and `Fetched`
= generator runtime. All 256 placemarks and their coordinates are preserved.

---

## What is already built (local)

- `generate_live_kml.py` — produces `docs/live_buoys.kml` (256 placemarks, plain
  KML) and `docs/live_buoys_networklink.kml` (NetworkLink, 900 s refresh).
- `.github/workflows/publish.yml` — cron every 15 min, runs the generator with the
  computed Pages URL, deploys `docs/` to the `gh-pages` branch.
- `repair_live_buoys_candidate.py` + `seagull_platforms.geojson` — data sources.
- `great_lakes_live_buoys.kmz` — protected source of truth (read by the generator;
  never overwritten).

Verified locally: 256/256 placemarks, titles, coordinates, and folders preserved;
205 placemarks resolved with live data; NetworkLink file well-formed and points at
`<base>/live_buoys.kml` with `refreshInterval=900`.

## What YOU must do (no repo/auth exists in this environment)

### 1. Create the repository and push

```bash
cd "/Users/wyattleathorn/Documents/Projects/Open code/locks"
git init
git add generate_live_kml.py repair_live_buoys_candidate.py seagull_platforms.geojson \
        great_lakes_live_buoys.kmz .github/workflows/publish.yml
git commit -m "Live Great Lakes buoys: generator + GitHub Pages publish workflow"
gh repo create great-lakes-live-buoys --public --source=. --remote=origin
git push -u origin main
```

(Replace `great-lakes-live-buoys` with your preferred repo name. The workflow
computes the public URL from the repo, so the name flows through automatically.)

### 2. Enable GitHub Pages

- Repo **Settings → Pages → Build and deployment → Source**: `Deploy from a branch`.
- **Branch**: `gh-pages` (created by the first workflow run), **folder**: `/ (root)`.
- Save. The public URL becomes:

  `https://<your-github-username>.github.io/great-lakes-live-buoys/`

### 3. Run the workflow once

- **Actions → "Publish live buoys KML" → Run workflow** (or just wait for the
  15-minute cron). Wait until the `gh-pages` branch exists and Pages shows
  "Your site is live".

### 4. Verify the public KML is reachable (outside this machine)

```bash
curl -I "https://<your-github-username>.github.io/great-lakes-live-buoys/live_buoys.kml"
# Expect HTTP/2 200 and a content-type containing xml
curl "https://<your-github-username>.github.io/great-lakes-live-buoys/live_buoys.kml" | grep -c "<Placemark>"
# Expect 256
```

### 5. End-to-end live-refresh test (Thunder Bay Buoy, NOAA 45162)

1. Open the NetworkLink KML in Google Earth (Web or mobile):
   `https://<your-github-username>.github.io/great-lakes-live-buoys/live_buoys_networklink.kml`
2. Locate **Thunder Bay Buoy, Alpena, MI (Buoy) [GLOS]** and record its
   `Observed source timestamp` and measurements (e.g. `WTMP`, `WSPD`).
3. Note that the generator runs every 15 min. Wait for at least one refresh cycle
   (or trigger the workflow manually), and confirm the served KML changes:
   ```bash
   curl "https://<your-github-username>.github.io/great-lakes-live-buoys/live_buoys.kml" \
     | grep -A2 "Thunder Bay Buoy" | grep "Observed"
   ```
4. After a real source change (NOAA updates the observation), the next refresh
   must show a new `Observed` timestamp and updated measurements **inside the
   placemark description** — without you replacing the KMZ.

## Acceptance criterion

Successful when: Google Earth → NetworkLink → public GitHub Pages KML →
GitHub Action → live NOAA/GLOS data → regenerated description forms a working
chain, and the measurements/`Observed` timestamp inside the description change
after a refresh when the source data changes.

## Notes / limits

- The 15-minute `refreshInterval` on the NetworkLink and the 15-minute workflow
  cron mean updates propagate within roughly one cycle.
- ~50 placemarks currently have no current observation from their exact platform
  (confirmed: their GLOS dataset returns 0 rows via both API and ERDDAP, and
  NOAA realtime2 404s; beaches have no exact NOAA/GLOS source). These remain
  `Data unavailable` with full route logs and are not substituted with nearby
  platforms.
- The local candidate KMZs (`candidate_great_lakes_live_buoys_v*.kmz`) and the
  protected working KMZ are untouched by this live pipeline.
