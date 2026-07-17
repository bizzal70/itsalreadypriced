"""
Weekly RTFM generator — picks the next unused topic from rtfm_topics.yml,
sends it to Claude, writes a long-form Jekyll post to _rtfm/.

Deliberately NOT sourced from the article database. RTFM is evergreen,
reference-grounded best-practice writing, distinct from Issues and Field Notes.

Run: python rtfm.py    Requires: ANTHROPIC_API_KEY
"""

import os
import re
import subprocess
import yaml
from datetime import datetime
from pathlib import Path
import anthropic
from resources import build_related_section

TOPICS_PATH = Path(__file__).parent / "rtfm_topics.yml"
RTFM_DIR = Path(__file__).parent.parent / "_rtfm"


def load_topics():
    with open(TOPICS_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_topics(topics):
    with open(TOPICS_PATH, "w", encoding="utf-8") as f:
        yaml.safe_dump(topics, f, sort_keys=False, allow_unicode=True, default_flow_style=False)


def next_topic(topics):
    for t in topics:
        if not t.get("used"):
            return t
    return None


def build_prompt(topic):
    return f"""You are the anonymous author of "It's Already Priced." — a crypto security and markets publication. This piece is for "RTFM": a weekly long-form, technical, reference-grounded article. It is deliberately NOT news-driven and must not reference recent exploits, specific hacks, or current events. That is what Issues and Field Notes are for. RTFM is the field manual: durable, technical, first-principles writing about the security practices crypto users and builders already know they should follow and routinely do not.

Same voice as the rest of the publication: dry, world-weary, authoritative, allergic to hype and shilling. Longer and more technical than the news sections, closer to a respected practitioner's essay than a digest entry.

Topic: {topic['topic']}
Grounding framework: {topic['framework']}
Angle: {topic['angle']}

Write the article in Markdown with this structure. Do NOT include a top-level title (no "# ..." line); the template renders the title. Start directly with the opening paragraph.
1. Open with a sharp, opinionated framing (2 to 4 sentences): why this obvious thing is still ignored in practice
2. ## The Standard — what the framework or mechanism actually requires, in plain language, citing it by name
3. ## Where It Breaks Down — the specific, concrete ways people and protocols fail at this (be technical: name mechanisms, contract patterns, wallet behaviors, not vague generalities)
4. ## Doing It Right — concrete, actionable guidance a holder or builder could actually implement
5. ## The Bottom Line — a short closing that ties back to the publication's fatalistic voice

Rules:
- Do not reference specific recent hacks or current events. Keep it evergreen
- Be technical and specific: name standards (EIPs), mechanisms, tooling categories
- 1000 to 1500 words. Do not mention that you used AI to write this
- Do not use em dashes. Use periods, commas, or parentheses
- End with a single italicized sign-off line that fits the brand voice

Also provide, on the very first line before the article, "SUMMARY: <one sentence for the blog index>".
"""


def write_post(topic, summary, content):
    today = datetime.now().strftime("%Y-%m-%d")
    slug = re.sub(r"[^a-z0-9]+", "-", topic["topic"].lower()).strip("-")
    filename = RTFM_DIR / f"{today}-{slug}.md"
    safe_summary = summary.replace('"', "'")
    frontmatter = f"""---
layout: rtfm
title: "{topic['topic']}"
date: {today}
summary: "{safe_summary}"
framework: "{topic['framework']}"
framework_url: "{topic['framework_url']}"
---

"""
    RTFM_DIR.mkdir(exist_ok=True)
    related = build_related_section(RTFM_DIR.parent, filename.name)
    filename.write_text(
        frontmatter + content + ("\n\n" + related if related else ""),
        encoding="utf-8",
    )
    print(f"RTFM written: {filename}")
    return filename


def git_push(filepaths):
    repo_root = Path(__file__).parent.parent
    for fp in filepaths:
        subprocess.run(["git", "add", str(fp)], cwd=repo_root, check=True)
    subprocess.run(["git", "commit", "-m", f"RTFM: {filepaths[0].stem}"], cwd=repo_root, check=True)
    subprocess.run(["git", "push"], cwd=repo_root, check=True)


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit("ERROR: set ANTHROPIC_API_KEY")

    topics = load_topics()
    topic = next_topic(topics)
    if not topic:
        print("No unused RTFM topics remain. Add more to rtfm_topics.yml.")
        return

    print(f"Generating RTFM: {topic['topic']}...")
    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=3000,
        messages=[{"role": "user", "content": build_prompt(topic)}],
    )
    raw = response.content[0].text.strip()

    summary, body = "", []
    for line in raw.splitlines():
        if line.startswith("SUMMARY:"):
            summary = line.replace("SUMMARY:", "").strip()
        else:
            body.append(line)
    content = "\n".join(body).strip()
    if content.startswith("# "):
        content = content.split("\n", 1)[1].lstrip() if "\n" in content else ""

    filepath = write_post(topic, summary, content)
    topic["used"] = True
    save_topics(topics)

    if not os.environ.get("GITHUB_ACTIONS"):
        git_push([filepath, TOPICS_PATH])


if __name__ == "__main__":
    main()
