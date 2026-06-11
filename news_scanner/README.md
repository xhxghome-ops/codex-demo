# Work design news scanner

Scans a configurable list of news websites every day for articles relevant
to **work design** and saves a markdown report to `reports/YYYY-MM-DD.md`.

## How it works

- `sources.json` lists the websites to scan (via their RSS/Atom feeds,
  plus Google News search feeds that cover the wider web).
- `scan.py` fetches every feed, keeps items published in the last 24 hours
  whose title or summary matches work-design keywords (work design, job
  design, job crafting, future of work, hybrid/remote/flexible work,
  four-day week, organizational design, etc.), de-duplicates them, and
  writes the report. It uses only the Python standard library.
- `.github/workflows/daily-news-scan.yml` runs the scan every day at
  06:00 UTC and commits the report back to the repository. It can also be
  run on demand from the Actions tab (`workflow_dispatch`).

## Note on scheduling

GitHub only triggers `schedule` workflows from the **default branch**, so
the daily run starts once this is merged into `main`.

## Customizing

- **Add/remove websites:** edit `news_scanner/sources.json`. Any RSS or
  Atom feed URL works.
- **Tune relevance:** edit the `KEYWORDS` list at the top of
  `news_scanner/scan.py`.
- **Change the schedule:** edit the `cron` expression in
  `.github/workflows/daily-news-scan.yml` (times are UTC).

## Run locally

```bash
python3 news_scanner/scan.py
```
