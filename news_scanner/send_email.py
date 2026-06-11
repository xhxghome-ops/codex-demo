#!/usr/bin/env python3
"""Email the most recent work design news report.

Reads the latest markdown report from reports/, converts it to simple
HTML, and sends it over SMTP. Configuration comes from environment
variables:

    MAIL_USERNAME  SMTP login (e.g. your Gmail address)        [required]
    MAIL_PASSWORD  SMTP password (Gmail: an app password)      [required]
    MAIL_TO        Recipient address                           [required]
    SMTP_SERVER    SMTP host (default: smtp.gmail.com)
    SMTP_PORT      SMTP SSL port (default: 465)

Uses only the Python standard library.
"""

import os
import re
import smtplib
import ssl
import sys
from email.message import EmailMessage
from html import escape
from pathlib import Path

REPORTS_DIR = Path(__file__).resolve().parent.parent / "reports"

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def md_line_to_html(line):
    """Minimal markdown-to-HTML for the report format scan.py produces."""
    if not line.strip():
        return ""
    if line == "---":
        return "<hr>"

    def link(m):
        return f'<a href="{escape(m.group(2), quote=True)}">{escape(m.group(1))}</a>'

    # Escape everything except the links we rebuild ourselves.
    parts = []
    pos = 0
    for m in LINK_RE.finditer(line):
        parts.append(escape(line[pos : m.start()]))
        parts.append(link(m))
        pos = m.end()
    parts.append(escape(line[pos:]))
    text = "".join(parts)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"_([^_]+)_", r"<em>\1</em>", text)

    if line.startswith("## "):
        return f"<h3>{text[3:].lstrip()}</h3>"
    if line.startswith("# "):
        return f"<h2>{text[2:].lstrip()}</h2>"
    if line.startswith("- "):
        return f"<p style='margin:2px 0'>&bull; {text[2:]}</p>"
    return f"<p>{text}</p>"


def md_to_html(md):
    body = "\n".join(h for h in (md_line_to_html(l) for l in md.splitlines()) if h)
    return (
        "<html><body style='font-family:sans-serif;max-width:700px'>"
        f"{body}</body></html>"
    )


def main():
    username = os.environ.get("MAIL_USERNAME")
    password = os.environ.get("MAIL_PASSWORD")
    recipient = os.environ.get("MAIL_TO")
    server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
    port = int(os.environ.get("SMTP_PORT", "465"))

    missing = [
        name
        for name, value in [
            ("MAIL_USERNAME", username),
            ("MAIL_PASSWORD", password),
            ("MAIL_TO", recipient),
        ]
        if not value
    ]
    if missing:
        sys.exit(
            f"Missing required environment variables: {', '.join(missing)}. "
            "Set them as repository secrets (see news_scanner/README.md)."
        )

    reports = sorted(REPORTS_DIR.glob("*.md"))
    if not reports:
        sys.exit(f"No report found in {REPORTS_DIR}; run scan.py first.")
    report = reports[-1]
    markdown = report.read_text()

    msg = EmailMessage()
    msg["Subject"] = f"Work design news — {report.stem}"
    msg["From"] = username
    msg["To"] = recipient
    msg.set_content(markdown)
    msg.add_alternative(md_to_html(markdown), subtype="html")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(server, port, context=context) as smtp:
        smtp.login(username, password)
        smtp.send_message(msg)

    print(f"Emailed {report.name} to {recipient}")


if __name__ == "__main__":
    main()
