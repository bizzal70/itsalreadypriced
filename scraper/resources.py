"""
Builds the deterministic Resources section for Issues and Field Notes.

Crypto analog of IAW's CVE->NVD/Sigma helper. Links are constructed
programmatically, never LLM-generated, to avoid hallucinated URLs:
  - source reporting URLs are the real article links the generator fed to the
    model, filtered to the ones the model declared it drew from (SOURCES line),
    and validated to be a subset of the input set (any hallucinated URL is dropped)
  - any on-chain tx hash / address appearing in the prose is linked to a block explorer
  - the reference-standard incident trackers are always appended
"""

import re
from pathlib import Path

TX = re.compile(r"0x[a-fA-F0-9]{64}")
ADDR = re.compile(r"0x[a-fA-F0-9]{40}")

# GitHub Pages baseurl for this blog. Hardcoded (not `{{ site.baseurl }}`) so the
# internal links don't depend on Liquid being rendered inside post bodies.
_BASEURL = "/itsalreadypriced"
_FNAME_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})-(.+)\.md$")
# collection dir -> URL prefix (Issues have no prefix; the others are namespaced).
_COLLECTIONS = [("_posts", ""), ("_field_notes", "/field-notes"), ("_rtfm", "/rtfm")]


# --- topical "Related" ranking -------------------------------------------------
# Related used to be the 3 most-RECENT posts, which dead-ends readers on unrelated
# content. Now prior posts are ranked by keyword overlap with the current post
# (shared TITLE terms weighted), with recency only as a tiebreaker and to
# back-fill so the section is never short. Deterministic: reads real files.
_STOP = set(
    "the a an and or of to in on at for is are was were be been by from as with "
    "that this it its you your their they them we our not but if how why what "
    "which when while then than into about over after before more most some any "
    "all can will just like one two new today week weekly daily field note notes "
    "issue rtfm read follow subscribe rss related resources here there also only "
    "very much many made make using used".split()
)
_MD_LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")


def _keywords(text: str) -> dict:
    text = _MD_LINK.sub(r"\1", text or "")          # keep link text, drop URLs
    text = re.sub(r"`[^`]*`", " ", text)            # drop code spans
    out: dict = {}
    for w in re.findall(r"[a-zA-Z][a-zA-Z0-9\-']{2,}", text.lower()):
        w = w.strip("-'")
        if len(w) < 3 or w in _STOP:
            continue
        out[w] = out.get(w, 0) + 1
    return out


def _relevance(cur: dict, cand_title: str, cand_body: str) -> int:
    cb = _keywords(cand_body)
    for t in set(_keywords(cand_title)):
        cb[t] = cb.get(t, 0) + 2                     # a shared TITLE term counts more
    return sum(cb.get(t, 0) for t in cur if t in cb)


def _post_text(path: Path):
    """(title, body) for a post file; body is the markdown minus front-matter."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return "", ""
    m = re.search(r'^title:\s*"(.+?)"', text, re.M)
    title = m.group(1) if m else ""
    body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)
    return title, body


def build_related_section(root, current_filename: str, limit: int = 3,
                          current_text: str = "") -> str:
    """Link the `limit` most RELEVANT prior posts across every collection, plus
    the section indexes, so a reader has a path deeper into the site.

    Ranked by keyword overlap with `current_text` (the post being written);
    recency is the tiebreaker and back-fill. With no `current_text` this reduces
    to the old most-recent behavior. Deterministic: reads real files on disk, so
    no URL is ever invented.
    """
    root = Path(root)
    cur = _keywords(current_text)
    entries = []  # (score, filename_sortkey, url, title)
    for coll, prefix in _COLLECTIONS:
        try:
            files = list((root / coll).glob("*.md"))
        except OSError:
            files = []
        for p in files:
            if p.name == current_filename:
                continue
            m = _FNAME_RE.match(p.name)
            if not m:
                continue
            y, mo, d, slug = m.groups()
            url = f"{_BASEURL}{prefix}/{y}/{mo}/{d}/{slug}/"
            title, body = _post_text(p)
            title = title or slug.replace("-", " ").strip().capitalize()
            score = _relevance(cur, title, body) if cur else 0
            entries.append((score, p.name, url, title))

    if not entries:
        return ""
    # topical first (score desc), then recency (filename is date-prefixed).
    entries.sort(key=lambda e: (e[0], e[1]), reverse=True)
    picked = entries[:limit]

    out = ["## Related", ""]
    out += [f"- [{t}]({u})" for _, _, u, t in picked]
    out += [
        "",
        f"More: [Issues]({_BASEURL}/) · [Field Notes]({_BASEURL}/field-notes/) · [RTFM]({_BASEURL}/rtfm/)",
    ]
    return "\n".join(out) + "\n"


def build_resources_section(content, source_urls, heading="## Resources"):
    lines = [f"{heading}\n"]

    for url in source_urls:
        lines.append(f"- {url}")

    # on-chain references found in the prose (tx first, then non-tx addresses)
    txs = sorted(set(TX.findall(content)))
    content_wo_tx = TX.sub("", content)
    addrs = sorted(set(ADDR.findall(content_wo_tx)))
    for t in txs:
        lines.append(f"- On-chain tx: https://etherscan.io/tx/{t}")
    for a in addrs:
        lines.append(f"- On-chain address: https://etherscan.io/address/{a}")

    lines.append("- Incident trackers (reference standard): "
                 "[Rekt leaderboard](https://rekt.news/leaderboard/) "
                 "· [SlowMist Hacked](https://hacked.slowmist.io/)")
    return "\n".join(lines) + "\n"


def validate_sources(declared_line, input_urls):
    """Keep only declared source URLs that were actually in the input set."""
    if not declared_line:
        return []
    raw = declared_line.replace("SOURCES:", "", 1)
    candidates = [u.strip().strip(",") for u in re.split(r"[\s,]+", raw) if u.strip()]
    inset = set(input_urls)
    seen, out = set(), []
    for u in candidates:
        if u in inset and u not in seen:
            seen.add(u)
            out.append(u)
    return out
