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


def _post_title(path: Path) -> str | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    m = re.search(r'^title:\s*"(.+?)"', text, re.M)
    return m.group(1) if m else None


def build_related_section(root, current_filename: str, limit: int = 3) -> str:
    """Link the `limit` most recent prior posts across every collection, plus the
    section indexes, so a reader has a path deeper into the site.

    Deterministic: reads the actual files on disk, so no URL is ever invented.
    URLs are built per collection (Issues `/…`, Field Notes `/field-notes/…`,
    RTFM `/rtfm/…`). Returns "" if there are no prior posts.
    """
    root = Path(root)
    entries = []  # (filename_sortkey, url, title)
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
            title = _post_title(p) or slug.replace("-", " ").strip().capitalize()
            entries.append((p.name, url, title))

    entries.sort(key=lambda e: e[0], reverse=True)  # filename is date-prefixed
    picked = entries[:limit]
    if not picked:
        return ""

    out = ["## Related", ""]
    out += [f"- [{t}]({u})" for _, u, t in picked]
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
