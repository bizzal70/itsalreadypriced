# It's Already Priced.

Crypto security and markets for people who already know how this ends. A shadow-published weekly digest. Security-led, markets-aware.

Sister site to [It's Already When.](https://github.com/bizzal70/itsalreadywhen) (cyber) and [It's Already Written.](https://github.com/bizzal70/itsalreadywritten) (TTRPG).

- **Site:** https://bizzal70.github.io/itsalreadypriced/
- **Stack:** Jekyll + GitHub Pages + GitHub Actions (+ Claude API for generation, planned)

## Sections

| Section | Cadence | Description |
|---|---|---|
| Issues | Weekly | Roundup of major hacks, exploits, and market/regulatory news |
| Field Notes | Daily | One exploit, on-chain event, or security habit |
| RTFM | Weekly (Wed) | Long-form technical deep dives: keys, wallets, DeFi mechanics |

## Content rules

- No em dashes in generated prose (AI tell).
- No mention of AI authorship.
- Token references resolve to deterministic CoinGecko coin pages (`coingecko.com/en/coins/{id}`), never LLM-generated links.
- Exploit and theft references link to deterministic block-explorer addresses/txs and incident trackers, never LLM-generated.
- Every post ends with a Sources section. If it can't be sourced, it doesn't run.

## Layout

```
_config.yml            site config
_layouts/              default, post (Issues), field_note, rtfm
_posts/                Issues
_field_notes/          daily Field Notes collection
_rtfm/                 weekly RTFM collection
index.html             Issues list
field-notes.html       Field Notes list
rtfm.html              RTFM list
*-feed.xml             per-section Atom feeds
assets/css/style.css   theme (trading-terminal green/gold)
.github/workflows/     deploy.yml (Pages)
```

Content generators (Python + Claude API) to be added in a follow-up build, mirroring the It's Already When pipeline.
