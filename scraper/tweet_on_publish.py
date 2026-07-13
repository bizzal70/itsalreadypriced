"""
Tweet-on-publish for It's Already Priced.
Triggered by the GitHub Actions workflow (.github/workflows/tweet-on-publish.yml)
when a new post is added under _posts/, _field_notes/, or _rtfm/.
Waits for the live GitHub Pages URL to return 200, then posts to X (@ItsAlreadyPrice)
with a generated 1200x675 thumbnail card.

Env:
  X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET  (repo secrets)
  POST_PATHS    space/newline-separated repo-relative paths of newly added posts (from the workflow diff)
  TWEET_LATEST  'true' to tweet the latest Issue instead (manual workflow_dispatch test)
"""

import os
import re
import sys
import glob
import time
import urllib.request
from pathlib import Path

BLOG_URL = "https://bizzal70.github.io/itsalreadypriced"
HANDLE = "ItsAlreadyPrice"
ROOT = Path(__file__).resolve().parent.parent

COLLECTIONS = {
    "_posts": "",
    "_field_notes": "field-notes",
    "_rtfm": "rtfm",
}


def parse_front_matter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            mm = re.match(r"\s*([A-Za-z_]+)\s*:\s*(.*)$", line)
            if mm:
                k, v = mm.group(1), mm.group(2).strip()
                if len(v) >= 2 and v[0] in "\"'" and v[-1] == v[0]:
                    v = v[1:-1]
                fm[k] = v
    return fm


def resolve(path):
    p = Path(path)
    coll = p.parent.name
    prefix = COLLECTIONS.get(coll)
    if prefix is None or p.suffix != ".md":
        return None
    full = ROOT / path
    if not full.exists():
        return None
    fm = parse_front_matter(full.read_text(encoding="utf-8"))
    date = (fm.get("date", "") or "")[:10]
    if not re.match(r"\d{4}-\d{2}-\d{2}", date):
        m = re.match(r"(\d{4}-\d{2}-\d{2})-", p.stem)
        date = m.group(1) if m else ""
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", p.stem)
    datepath = date.replace("-", "/")
    url = f"{BLOG_URL}/{prefix}/{datepath}/{slug}/" if prefix else f"{BLOG_URL}/{datepath}/{slug}/"
    return {"coll": coll, "fm": fm, "url": url}


def wait_for_200(url, timeout=300, interval=10):
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "iap-tweet-bot"})
            with urllib.request.urlopen(req, timeout=15) as r:
                if r.status == 200:
                    return True
        except Exception:
            pass
        time.sleep(interval)
    return False


def build_tweet(coll, fm, url):
    title = fm.get("title", "")
    summary = fm.get("summary", "")
    issue = fm.get("issue", "")
    if coll == "_posts" and issue.isdigit():
        head = f"It's Already Priced. — Issue #{int(issue):03d}"
        body, tags = summary, "#Crypto #CryptoSecurity #DeFi"
    elif coll == "_field_notes":
        head, body, tags = "It's Already Priced. — Field Note", title, "#Crypto #CryptoSecurity"
    elif coll == "_rtfm":
        head, body, tags = "It's Already Priced. — RTFM", title, "#Crypto #DeFi #Security"
    else:
        head, body, tags = "It's Already Priced.", (summary or title), "#Crypto #CryptoSecurity"

    def assemble(b):
        return f"{head}\n\n{b}\n\n{url}\n\n{tags}"

    tweet = assemble(body)
    if len(tweet) > 280:
        overhead = len(assemble("")) + 3
        body = body[: max(0, 280 - overhead)].rstrip() + "..."
        tweet = assemble(body)
    return tweet


def make_thumbnail(fm):
    try:
        from x_thumbnail import render
        return render("priced", fm)
    except Exception as e:
        print(f"[x_thumbnail] WARNING: {e}; posting without image")
        return None


def main():
    creds = {k: os.environ.get(k) for k in
             ("X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET")}
    missing = [k for k, v in creds.items() if not v]
    if missing:
        print(f"X secrets not configured ({', '.join(missing)}). Skipping tweet.")
        return

    targets = []
    raw = os.environ.get("POST_PATHS", "").strip()
    if raw:
        targets = [t for t in re.split(r"\s+", raw) if t]
    elif os.environ.get("TWEET_LATEST", "").lower() == "true":
        posts = sorted(glob.glob(str(ROOT / "_posts" / "*.md")), reverse=True)
        posts = [p for p in posts if "issue-000" not in p]
        if posts:
            targets = [str(Path(posts[0]).relative_to(ROOT)).replace("\\", "/")]

    if not targets:
        print("No newly added posts to tweet.")
        return

    import tweepy

    print("Credential shape check:")
    for k in ("X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET"):
        v = creds[k] or ""
        print(f"  {k}: len={len(v)} has_dash={'-' in v} whitespace_edges={v != v.strip()}")

    client = tweepy.Client(
        consumer_key=creds["X_API_KEY"],
        consumer_secret=creds["X_API_SECRET"],
        access_token=creds["X_ACCESS_TOKEN"],
        access_token_secret=creds["X_ACCESS_TOKEN_SECRET"],
    )
    try:
        me = client.get_me()
        print(f"READ-AUTH OK: authenticated as @{me.data.username}")
    except Exception as e:
        print(f"READ-AUTH FAILED: {type(e).__name__}: {e}")

    auth = tweepy.OAuth1UserHandler(
        creds["X_API_KEY"], creds["X_API_SECRET"],
        creds["X_ACCESS_TOKEN"], creds["X_ACCESS_TOKEN_SECRET"],
    )
    v1 = tweepy.API(auth)

    for path in targets:
        info = resolve(path)
        if not info:
            print(f"Skip (not a publishable post): {path}")
            continue
        print(f"Waiting for live URL: {info['url']}")
        if not wait_for_200(info["url"]):
            print(f"  URL never returned 200 within timeout; skipping {path}")
            continue

        thumb_path = make_thumbnail(info["fm"])
        media_ids = None
        if thumb_path:
            try:
                media = v1.media_upload(thumb_path)
                media_ids = [media.media_id]
                print(f"[x_thumbnail] media_id={media.media_id}")
            except Exception as e:
                print(f"[x_post] WARNING: media upload failed ({e}); posting without image")

        tweet = build_tweet(info["coll"], info["fm"], info["url"])
        print(f"Posting:\n{tweet}\n")
        kwargs = {"text": tweet}
        if media_ids:
            kwargs["media_ids"] = media_ids
        resp = client.create_tweet(**kwargs)
        print(f"Tweeted: https://x.com/{HANDLE}/status/{resp.data['id']}")

        if thumb_path:
            try:
                os.unlink(thumb_path)
            except Exception:
                pass


if __name__ == "__main__":
    main()
