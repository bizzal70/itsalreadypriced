# CLAUDE.md

## Project Overview
"It's Already Priced." — crypto security + markets blog, live at https://bizzal70.github.io/itsalreadypriced/. Jekyll + GitHub Pages, three content tiers, all Claude-generated and auto-tweeted. **This is live and actively publishing, not scaffolding** — 227 total Actions runs, the last 15+ all successful; 6 Issues, 30 daily Field Notes (no gaps through today), 4 RTFM posts actually published with real content.

- **Weekly Issue** (Sunday) — `digest.py`, 5-section structured post from the past 7 days of feed articles.
- **Daily Field Note** — `field_note.py`, 1-3 highest-signal items from the last 24h; can return `SUMMARY: SKIP` to decline a day rather than post filler.
- **Weekly RTFM** (Wednesday) — `rtfm.py`, long-form evergreen piece from a curated topic list, deliberately not sourced from the article database.

Content is **news-feed-driven, not market-data-API-driven** — there is no exchange/price API call anywhere; "market" content comes entirely from the RSS feed set (Cointelegraph, Hacker News, Bleeping Computer, Chainalysis, The Block, CoinDesk, Decrypt, The Defiant, r/CryptoCurrency). On-chain/resource links (Etherscan tx/address, Rekt leaderboard, SlowMist Hacked) are built deterministically via regex extraction, never fetched from a market-data provider.

## Tech Stack
- Jekyll + GitHub Pages (three collections: default posts = Issues, `field_notes`, `rtfm`)
- Claude API (`anthropic==0.40.0`), model constant `"claude-opus-4-8"` across all three generators
- `feedparser` — 10 RSS feeds (`scraper/feeds.py`)
- SQLite `scraper/articles.db` — **committed** (unlike itsalreadywritten's equivalent, which is rebuilt fresh each run) — this is the shared dedup store for both Issues and Field Notes
- `tweepy==4.14.0` — OAuth 1.0a, both v2 (`Client.create_tweet`) and v1.1 (`API.media_upload`, and in `set_avatar.py`, `update_profile_image`) used side by side
- Pillow — thumbnail cards, shared style module across this blog + itsalreadywhen + itsalreadywritten (dark green terminal theme, accent `rgb(29,158,117)`, for this blog specifically)

## Commands
No local dev loop — cloud-only, no persistent local clone.
```bash
gh workflow run daily-scrape.yml
gh workflow run daily-field-note.yml
gh workflow run weekly-issue.yml
gh workflow run weekly-rtfm.yml
gh workflow run deploy.yml
gh workflow run tweet-on-publish.yml -f tweet_latest_issue=true   # manual test
gh workflow run set-avatar.yml   # one-shot, sets X profile image
```

## Code Style
- No em dashes, no AI-authorship disclosure — stated directly in the Claude prompts inside `digest.py`/`field_note.py`/`rtfm.py` ("Do not use em dashes anywhere," "Do not mention that you used AI to write this").
- `resources.py`'s `validate_sources()` enforces in **code** that any model-declared `SOURCES:` URL is dropped unless it's a member of the real input article-URL set — a hard guard against hallucinated citations, not just a prompt instruction.
- `note_quality.py` deliberately avoids an LLM judge for the same cross-project reason documented in the sister blogs' code: "an LLM judge over-flages elsewhere in this project" — regex/word-count heuristics instead.

## Testing
- No test suite — validate via `workflow_dispatch` and read the actual published post.
- Field Note quality is gated by `note_quality.assess()` (deterministic substance floor); a failing note is regenerated once "stricter," then skipped if still failing — never published thin.

## Repository Etiquette
- `README.md` is comprehensive and was cross-checked against the actual workflow/script contents during this review — treat it as accurate.
- Content licensing split: code MIT, published post content CC BY-NC 4.0 (`LICENSE-CONTENT.md`).

## Architecture Notes
- `scraper.py` — pulls RSS into `articles.db`, dedupes by `sha256(url)[:16]`, tracks `used_in_digest`/`used_in_fieldnote` flags separately so the two generators don't compete for the same articles
- `digest.py` / `field_note.py` / `rtfm.py` — the three generators; `rtfm.py` contains its own redundant `git_push()` helper via `subprocess` that is NOT what actually runs in CI (the workflow's own shell step does the real commit/push) — don't assume that helper is live
- `resources.py` — deterministic Etherscan/Rekt/SlowMist link builder + keyword-overlap "Related" section (recency-only ranking was a past design mistake, since fixed)
- `x_thumbnail.py` — shared Pillow thumbnail generator across all three "It's Already *" blogs
- `set_avatar.py` — one-shot X profile-image setter; deliberately continues past a `verify_credentials()` failure to let the real error surface from `update_profile_image` itself (debug-friendly by design, not a bug)
- `scraper/articles.db` — committed SQLite, the single dedup/state store for Issues + Field Notes
- `scraper/issue_number.txt` — plain incrementing counter (currently `5`, matches 5 published issues)
- `scraper/rtfm_topics.yml` — 15 topics, 4 used (matching the 4 published RTFM posts), 11 remaining

## Boundaries — What NOT To Do
- **Cloud-only, no exceptions** — no persistent local clone of this repo exists or should exist.
- **RTFM must never be sourced from the article database or current news** — explicitly evergreen/framework-grounded.
- **Never let the LLM invent a source/resource URL** — always route through `resources.py`'s `validate_sources()` or the deterministic Etherscan/Rekt/SlowMist builders.
- **The X integration had a real, documented rollout failure — understand it before touching credentials.** All 6 failed "Tweet on publish" runs and both failed "Set Avatar" runs are clustered on repo-creation day (2026-07-05): first a `403 Forbidden`, then later the same day a `402 Payment Required` *after* `READ-AUTH OK` — i.e. valid read-only credentials that lacked write/paid-tier access to actually post. Every run since has succeeded. `tweet_on_publish.py` now prints an explicit credential-shape check and logs read-auth success/failure separately from post-attempt failure specifically because of this incident — don't remove that diagnostic, and if X posting ever silently stops working again, check read-auth vs. write-auth in the logs before assuming the token itself is invalid.
- **`deploy.yml` deliberately ignores `scraper/**` path changes** so DB/state-only commits don't trigger a site rebuild — don't remove this without understanding why.

## Workflow Preferences
- One fix at a time; this pipeline auto-commits and auto-tweets on every scheduled run.
- Validate content-generation changes via manual `workflow_dispatch` and read the actual post before trusting it.
- If touching the X posting path, re-check the 2026-07-05 incident pattern above (read-auth vs. write-auth) rather than assuming a new failure is the same root cause.

## Environment / Secrets
- `GH_PAT` — used for checkout in the three content-generating workflows so the resulting push fans out to `deploy.yml`/`tweet-on-publish.yml` (a default-`GITHUB_TOKEN` push would not)
- `ANTHROPIC_API_KEY` — Claude API calls for all three generators
- `X_API_KEY` / `X_API_SECRET` — X OAuth 1.0a consumer key/secret (used in both `tweet-on-publish.yml` and `set-avatar.yml`)
- `X_ACCESS_TOKEN` / `X_ACCESS_TOKEN_SECRET` — X OAuth 1.0a user access token/secret (same two workflows)
