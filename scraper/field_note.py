"""
Daily Field Note generator — pulls the last 24h of high-signal articles,
sends them to Claude, writes a short tactical Jekyll post to _field_notes/.

Run: python field_note.py    Requires: ANTHROPIC_API_KEY
"""

import os
import sqlite3
import subprocess
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
from pathlib import Path
import anthropic
from resources import build_resources_section, validate_sources, build_related_section
from scraper import init_db

DB_PATH = Path(__file__).parent / "articles.db"
NOTES_DIR = Path(__file__).parent.parent / "_field_notes"
MT = ZoneInfo("America/Denver")


def get_todays_articles(conn):
    since = (datetime.now(timezone.utc) - timedelta(hours=24)).isoformat()
    return conn.execute("""
        SELECT title, url, source, category, summary, published_at
        FROM articles
        WHERE published_at >= ? AND used_in_fieldnote = 0
        ORDER BY published_at DESC
        LIMIT 60
    """, (since,)).fetchall()


def mark_used(conn, urls):
    for url in urls:
        conn.execute("UPDATE articles SET used_in_fieldnote = 1 WHERE url = ?", (url,))
    conn.commit()


def build_prompt(articles):
    lines = []
    for title, url, source, category, summary, published_at in articles:
        lines.append(f"[{category.upper()}] {source}\nTitle: {title}\nURL: {url}\nSummary: {summary}\n")
    articles_text = "\n---\n".join(lines)

    return f"""You are the anonymous author of "It's Already Priced." — a crypto security and markets digest. This is a "Field Note": a short, tactical daily entry, distinct from the weekly Issue. Same dry, world-weary, authoritative voice, but tighter and more operational, like a note scrawled between drains.

Below are the last day's crypto articles. Pick the 1 to 3 highest-signal items (an active exploit, a confirmed theft with real losses, a disclosed protocol flaw, a drainer campaign, or a genuinely board-moving market/regulatory event). Skip shilling, price-action noise, and PR. Write a Field Note in Markdown with exactly this structure:

## Today's Field Note
One tight paragraph (3 to 5 sentences) in voice: what happened and why it matters right now.

## Today's Move
A short list (3 to 5 items) of concrete, specific things a crypto holder or builder should do today in response (revoke approvals, rotate keys, exit a pool, patch, watch an address, etc.).

Rules:
- Name the protocols, chains, amounts, and actors specifically
- No shilling, no fear-mongering, no price targets
- Under 300 words. Do not mention that you used AI to write this
- Do not use em dashes. Use periods, commas, or parentheses

Output format:
- FIRST line: "SUMMARY: <one dry sentence for the blog index>"
- Then the content (the two sections above)
- LAST line: "SOURCES: <comma-separated URLs, verbatim from the articles below, of the items you drew from>"

If nothing today is genuinely high-signal, output exactly "SUMMARY: SKIP" and nothing else.

---

TODAY'S ARTICLES:

{articles_text}
"""


def write_note(title, summary, content):
    today = datetime.now(MT).strftime("%Y-%m-%d")
    filename = NOTES_DIR / f"{today}-field-note.md"
    safe_summary = summary.replace('"', "'")
    frontmatter = f"""---
layout: field_note
title: "{title}"
date: {today}
summary: "{safe_summary}"
---

"""
    cta = (
        "\n\n---\n\n*Daily field notes, weekly Issues. Follow "
        "[@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*"
    )
    NOTES_DIR.mkdir(exist_ok=True)
    related = build_related_section(NOTES_DIR.parent, filename.name)
    filename.write_text(
        frontmatter + content + ("\n\n" + related if related else "") + cta,
        encoding="utf-8",
    )
    print(f"Field Note written: {filename}")
    return filename


def git_push(filepath):
    repo_root = Path(__file__).parent.parent
    subprocess.run(["git", "add", str(filepath)], cwd=repo_root, check=True)
    subprocess.run(["git", "commit", "-m", f"Add {filepath.name}"], cwd=repo_root, check=True)
    subprocess.run(["git", "push"], cwd=repo_root, check=True)


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit("ERROR: set ANTHROPIC_API_KEY")

    conn = sqlite3.connect(DB_PATH)
    init_db(conn)
    articles = get_todays_articles(conn)
    if not articles:
        print("No new articles today. Skipping Field Note.")
        conn.close()
        return

    print(f"Generating Field Note from {len(articles)} articles...")
    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=900,
        messages=[{"role": "user", "content": build_prompt(articles)}],
    )
    raw = response.content[0].text.strip()

    summary, sources_line, body = "", "", []
    for line in raw.splitlines():
        if line.startswith("SUMMARY:"):
            summary = line.replace("SUMMARY:", "").strip()
        elif line.startswith("SOURCES:"):
            sources_line = line
        else:
            body.append(line)
    content = "\n".join(body).strip()

    input_urls = [a[1] for a in articles]
    mark_used(conn, input_urls)
    conn.close()

    if summary == "SKIP" or not content:
        print("Nothing high-signal today. Skipping Field Note.")
        return

    sources = validate_sources(sources_line, input_urls)
    content = content + "\n\n" + build_resources_section(content, sources)

    title = f"Field Note — {datetime.now(MT).strftime('%B %d, %Y')}"
    filepath = write_note(title, summary, content)

    if not os.environ.get("GITHUB_ACTIONS"):
        git_push(filepath)


if __name__ == "__main__":
    main()
