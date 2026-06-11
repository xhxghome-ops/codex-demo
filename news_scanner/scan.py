#!/usr/bin/env python3
"""Scan configured news sources for today's articles relevant to work design.

Fetches each RSS/Atom feed listed in sources.json, keeps items published
today (UTC) whose title or summary matches the work-design keyword list,
and writes a markdown report to reports/YYYY-MM-DD.md.

Uses only the Python standard library so it can run anywhere without
installing dependencies.
"""

import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent
REPORTS_DIR = REPO_ROOT / "reports"

FETCH_TIMEOUT = 30
USER_AGENT = "Mozilla/5.0 (compatible; work-design-news-scanner/1.0)"

# An item is considered relevant if its title or summary matches any of these.
KEYWORDS = [
    r"work design",
    r"job design",
    r"work redesign",
    r"redesign(?:ing)? work",
    r"job craft\w*",
    r"organi[sz]ational design",
    r"future of work",
    r"hybrid work",
    r"remote work",
    r"flexible work",
    r"four[- ]day (?:work ?)?week",
    r"4[- ]day (?:work ?)?week",
    r"workplace design",
    r"job quality",
    r"work(?:er|force|place) wellbeing",
    r"employee experience",
    r"job demands",
    r"job autonomy",
]
KEYWORD_RE = re.compile("|".join(f"(?:{k})" for k in KEYWORDS), re.IGNORECASE)

ATOM_NS = "{http://www.w3.org/2005/Atom}"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
        return resp.read()


def text_of(elem):
    if elem is None:
        return ""
    return "".join(elem.itertext()).strip()


def parse_date(value):
    if not value:
        return None
    try:
        return parsedate_to_datetime(value)
    except (TypeError, ValueError):
        pass
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def parse_items(raw):
    """Yield (title, link, summary, published) from an RSS or Atom feed."""
    root = ET.fromstring(raw)

    for item in root.iter("item"):  # RSS
        link = text_of(item.find("link"))
        yield (
            text_of(item.find("title")),
            link,
            text_of(item.find("description")),
            parse_date(text_of(item.find("pubDate"))),
        )

    for entry in root.iter(f"{ATOM_NS}entry"):  # Atom
        link_el = entry.find(f"{ATOM_NS}link")
        link = link_el.get("href", "") if link_el is not None else ""
        published = text_of(entry.find(f"{ATOM_NS}published")) or text_of(
            entry.find(f"{ATOM_NS}updated")
        )
        yield (
            text_of(entry.find(f"{ATOM_NS}title")),
            link,
            text_of(entry.find(f"{ATOM_NS}summary")),
            parse_date(published),
        )


def clean(text):
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def scan():
    config = json.loads((BASE_DIR / "sources.json").read_text())
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=24)

    results = []
    errors = []
    seen_links = set()

    for source in config["sources"]:
        name, url = source["name"], source["url"]
        try:
            raw = fetch(url)
            items = list(parse_items(raw))
        except Exception as exc:  # noqa: BLE001 - one bad feed must not kill the run
            errors.append(f"{name}: {exc}")
            continue

        for title, link, summary, published in items:
            if published is None or published < cutoff:
                continue
            title, summary = clean(title), clean(summary)
            if not KEYWORD_RE.search(f"{title} {summary}"):
                continue
            if link in seen_links:
                continue
            seen_links.add(link)
            results.append(
                {
                    "source": name,
                    "title": title,
                    "link": link,
                    "summary": summary[:300],
                    "published": published.astimezone(timezone.utc),
                }
            )

    results.sort(key=lambda r: r["published"], reverse=True)
    return now, results, errors


def write_report(now, results, errors):
    REPORTS_DIR.mkdir(exist_ok=True)
    date_str = now.strftime("%Y-%m-%d")
    path = REPORTS_DIR / f"{date_str}.md"

    lines = [
        f"# Work design news — {date_str}",
        "",
        f"Scanned at {now.strftime('%Y-%m-%d %H:%M UTC')}. "
        f"{len(results)} relevant article(s) from the last 24 hours.",
        "",
    ]

    if not results:
        lines.append("_No relevant articles found today._")
    for r in results:
        lines.append(f"## [{r['title']}]({r['link']})")
        lines.append(
            f"*{r['source']} — {r['published'].strftime('%Y-%m-%d %H:%M UTC')}*"
        )
        if r["summary"]:
            lines.append("")
            lines.append(r["summary"])
        lines.append("")

    if errors:
        lines.append("---")
        lines.append("**Feeds that could not be fetched:**")
        lines.extend(f"- {e}" for e in errors)
        lines.append("")

    path.write_text("\n".join(lines))
    return path


def main():
    now, results, errors = scan()
    path = write_report(now, results, errors)
    print(f"Wrote {path} ({len(results)} articles, {len(errors)} feed errors)")
    if errors:
        for e in errors:
            print(f"  feed error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
