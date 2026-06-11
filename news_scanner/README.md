# Work design news scanner

Scans a configurable list of news websites every day for articles relevant
to **work design** and emails a digest to you.

## How it works

- `sources.json` lists the websites to scan (via their RSS/Atom feeds,
  plus Google News search feeds that cover the wider web).
- `scan.py` fetches every feed, keeps items published in the last 24 hours
  whose title or summary matches work-design keywords (work design, job
  design, job crafting, future of work, hybrid/remote/flexible work,
  four-day week, organizational design, etc.), de-duplicates them, and
  writes a markdown report to `reports/YYYY-MM-DD.md`.
- `send_email.py` emails the latest report (HTML with clickable links,
  plain-text fallback) over SMTP.
- `.github/workflows/daily-news-scan.yml` runs both every day at
  06:00 UTC. It can also be run on demand from the Actions tab
  (`workflow_dispatch`). Reports are emailed, not committed to the repo.

Both scripts use only the Python standard library.

## One-time setup: email credentials

The workflow sends mail through Gmail SMTP and needs two repository
secrets (**Settings → Secrets and variables → Actions → New repository
secret**):

| Secret | Value |
|---|---|
| `MAIL_USERNAME` | Your Gmail address (used as both sender and recipient) |
| `MAIL_PASSWORD` | A Gmail **app password** for that account |

To create an app password: enable 2-step verification on the Google
account, then go to <https://myaccount.google.com/apppasswords> and
generate one for "Mail". Regular account passwords will not work.

By default the digest is sent to the sending address itself. To deliver
somewhere else, set a `MAIL_TO` environment variable in the workflow's
email step. A different SMTP provider can be used via the optional
`SMTP_SERVER` and `SMTP_PORT` environment variables.

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
- **Change the recipient:** add a `MAIL_TO` env var to the email step in
  the workflow file (defaults to the sending address).

## Run locally

```bash
python3 news_scanner/scan.py
MAIL_USERNAME=you@gmail.com MAIL_PASSWORD=app-password \
  python3 news_scanner/send_email.py
```
