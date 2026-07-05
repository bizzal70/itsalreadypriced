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

TX = re.compile(r"0x[a-fA-F0-9]{64}")
ADDR = re.compile(r"0x[a-fA-F0-9]{40}")


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
