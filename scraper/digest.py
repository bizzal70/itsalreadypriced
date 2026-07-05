"""
Weekly Issue generator — pulls the past 7 days of articles from SQLite,
sends them to Claude, writes an IAW-structured Jekyll post to _posts/.

Run: python digest.py    Requires: ANTHROPIC_API_KEY
"""

import os
import sqlite3
import subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path
import anthropic
from resources import build_resources_section, validate_sources

DB_PATH = Path(__file__).parent / "articles.db"
POSTS_DIR = Path(__file__).parent.parent / "_posts"
ISSUE_TRACKER = Path(__file__).parent / "issue_number.txt"


def get_issue_number():
    n = int(ISSUE_TRACKER.read_text().strip()) + 1 if ISSUE_TRACKER.exists() else 1
    ISSUE_TRACKER.write_text(str(n))
    return n


def get_weeks_articles(conn):
    since = (datetime.now(timezone.utc) - timedelta(days=7)).isoformat()
    return conn.execute("""
        SELECT title, url, source, category, summary, published_at
        FROM articles
        WHERE published_at >= ? AND used_in_digest = 0
        ORDER BY published_at DESC
        LIMIT 150
    """, (since,)).fetchall()


def mark_used(conn, urls):
    for url in urls:
        conn.execute("UPDATE articles SET used_in_digest = 1 WHERE url = ?", (url,))
    conn.commit()


def build_prompt(articles):
    lines = []
    for title, url, source, category, summary, published_at in articles:
        lines.append(f"[{category.upper()}] {published_at[:10]} | {source}\nTitle: {title}\nURL: {url}\nSummary: {summary}\n")
    articles_text = "\n---\n".join(lines)

    return f"""You are the anonymous author of "It's Already Priced." — a weekly crypto security and markets intelligence digest. Security leads; markets are context. Your voice is dry, world-weary, and authoritative, allergic to hype, shilling, and price targets. You read the block explorer, not the timeline. The running thesis: by the time it is news, it is already priced in.

Below are this week's crypto articles (security incidents, exploits, protocol news, markets, regulation). Write the weekly Issue in Markdown.

Use exactly these section headers (## ...), in this order:
1. **This Week's Verdict** — 2 to 3 sentences capturing the week's theme with dry wit
2. **The Breaches** — the exploits, drains, and thefts that moved real money; name the protocols and amounts
3. **Vulnerabilities Worth Your Attention** — a short bulleted list with bold lead-ins; disclosed flaws, bug-bounty saves, systemic risks
4. **Threat Actors & Campaigns** — who is active (Lazarus/DPRK, drainer crews, etc.) and how
5. **The Bigger Picture** — the market, regulatory, and adoption moves that actually shift the board

Rules:
- Be specific: name protocols, chains, dollar amounts, threat actors, and standards
- Bold the named entities. Mix prose and short lists naturally, no bullet-point soup
- Under 1200 words. Do NOT write a Resources or Sources section (it is appended automatically)
- Do not mention that you used AI to write this
- Do not use em dashes anywhere. Use periods, commas, or parentheses
- If a claim cannot be tied to one of the articles below, leave it out

Output format:
- FIRST line: "SUMMARY: <one dry sentence for the blog index>"
- Then the post body (the five sections above)
- LAST line: "SOURCES: <comma-separated URLs, copied verbatim from the articles below, of the specific items you actually drew from>"

---

ARTICLES THIS WEEK:

{articles_text}
"""


def write_post(issue_number, title, summary, content):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = POSTS_DIR / f"{today}-issue-{issue_number:03d}.md"
    safe_summary = summary.replace('"', "'")
    frontmatter = f"""---
layout: post
title: "Issue #{issue_number:03d} — {title}"
date: {today}
issue: "{issue_number}"
summary: "{safe_summary}"
---

"""
    filename.write_text(frontmatter + content, encoding="utf-8")
    print(f"Post written: {filename}")
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
    articles = get_weeks_articles(conn)
    if not articles:
        print("No new articles this week. Run scraper.py first.")
        conn.close()
        return

    print(f"Generating Issue from {len(articles)} articles...")
    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=2500,
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
    sources = validate_sources(sources_line, input_urls)
    content = content + "\n\n" + build_resources_section(content, sources)

    issue_number = get_issue_number()
    title = f"Week of {datetime.now().strftime('%B %d, %Y')}"
    filepath = write_post(issue_number, title, summary, content)

    mark_used(conn, input_urls)
    conn.close()

    if not os.environ.get("GITHUB_ACTIONS"):
        git_push(filepath)


if __name__ == "__main__":
    main()
