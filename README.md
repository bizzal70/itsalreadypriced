# It's Already Priced.

*Crypto security and markets for people who already know how this ends.*

A fully automated, self-publishing crypto security publication. It scrapes, writes, publishes, and posts to X — no manual steps required. Security-led, markets-aware.

**Live site:** https://bizzal70.github.io/itsalreadypriced  
**X:** [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice)

Sister site to [It's Already When.](https://github.com/bizzal70/itsalreadywhen) (cyber) and [It's Already Written.](https://github.com/bizzal70/itsalreadywritten) (TTRPG).

---

## Three sections, three cadences

| Section | Cadence | What it is |
|---|---|---|
| **Issues** | Weekly, Sunday 10am MT | Long-form digest: exploits, hacks, market events, on-chain analysis, the week's verdict |
| **Field Notes** | Daily | Short entries on one exploit, on-chain event, or security habit from the last 24 hours |
| **RTFM** | Weekly, Wednesday | Evergreen technical deep dives: key management, wallet security, DeFi mechanics |

Each section has its own index page and RSS feed.

---

## How it works

```
Daily scrape              Daily Field Note          Sunday 10 AM MT          Wednesday
─────────────             ────────────────          ───────────────          ─────────
10 RSS feeds              Last 24h articles          Week's articles          Next unused topic
      │                         │                         │                         │
      ▼                         ▼                         ▼                         ▼
  scraper.py              field_note.py              digest.py                  rtfm.py
      │                         │                         │                         │
      ▼                         ▼                         ▼                         ▼
 articles.db              _field_notes/ post          _posts/ issue            _rtfm/ post
                                │                         │                         │
                                └─────────────────────────┴─────────────────────────┘
                                                          │
                                                          ▼
                                              deploy.yml → GitHub Pages
                                                          │
                                                          ▼
                                          X card thumbnail generated (Pillow)
                                          dollar figures extracted from summary
                                                          │
                                                          ▼
                                                  Tweet posted to X
```

Everything runs on GitHub Actions. No local machine, server, or cron required.

---

## Workflows

| Workflow | Schedule | What it does |
|---|---|---|
| `daily-scrape.yml` | Daily | Pulls 10 RSS feeds; deduplicates; caches to `articles.db` |
| `daily-field-note.yml` | Daily | Generates Field Note from last 24h articles; pushes; triggers tweet |
| `weekly-issue.yml` | Sunday 10am MT | Catches up missed articles; generates Issue with Claude; pushes; tweets with card |
| `weekly-rtfm.yml` | Wednesday | Picks next RTFM topic; generates article; pushes; tweets |
| `tweet-on-publish.yml` | On push to `_posts/`, `_field_notes/`, `_rtfm/` | Waits for page live (200 OK), then posts tweet with generated thumbnail card |
| `deploy.yml` | On every push to `main` | Builds + deploys Jekyll site to GitHub Pages |
| `set-avatar.yml` | Manual | Updates X account avatar |

All scheduled workflows support `workflow_dispatch` for manual runs.

---

## RSS sources

10 feeds across security, crypto news, DeFi, and community signal:

| Feed | Category |
|---|---|
| Cointelegraph Hacks | Incident (primary security spine) |
| The Hacker News | Security |
| Bleeping Computer | Security |
| Chainalysis Blog | Research |
| The Block | News |
| CoinDesk | News |
| Cointelegraph | News |
| Decrypt | News |
| The Defiant | DeFi |
| r/CryptoCurrency | Community signal |

---

## Scraper components

| File | Purpose |
|---|---|
| `scraper/feeds.py` | RSS source list (10 feeds, categorized) |
| `scraper/scraper.py` | Pulls feeds, deduplicates by URL hash, caches to `articles.db` |
| `scraper/digest.py` | Generates weekly Issue from this week's articles via Claude API |
| `scraper/field_note.py` | Generates daily Field Note from last 24h articles |
| `scraper/rtfm.py` | Picks next unused topic from `rtfm_topics.yml`; generates evergreen RTFM article |
| `scraper/resources.py` | Builds deterministic block-explorer and incident-tracker links from token/tx IDs — never LLM-generated URLs |
| `scraper/x_thumbnail.py` | Generates 1200×675 X card image (Pillow): dark terminal-green theme, dollar figures from summary extracted and shown in right column |
| `scraper/tweet_on_publish.py` | Posts tweet with thumbnail when new post is detected; waits for page live first |

---

## Content rules

- **No em dashes** — a deliberate choice to avoid an obvious AI-writing tell
- **No AI disclosure** in post copy
- **Source links are deterministic** — `resources.py` builds block-explorer URLs from token/tx IDs directly; never hallucinated
- **RTFM is not news-driven** — grounded in official protocol docs and audit reports, not scraped articles
- **Token pages resolve to CoinGecko** — `coingecko.com/en/coins/{id}`, stable and verifiable

---

## Required secrets

Settings → Secrets and variables → Actions:

| Secret | Purpose |
|---|---|
| `GH_PAT` | Personal access token with repo write access (used for committing posts) |
| `ANTHROPIC_API_KEY` | Claude API for content generation |
| `X_API_KEY` / `X_API_SECRET` | X app consumer keys (OAuth 1.0a) |
| `X_ACCESS_TOKEN` / `X_ACCESS_TOKEN_SECRET` | X user access tokens |

---

## Site structure

```
_posts/           Weekly Issues
_field_notes/     Daily Field Notes (Jekyll collection)
_rtfm/            Evergreen RTFM articles (Jekyll collection)
_layouts/         Jekyll templates
assets/           CSS, theme (trading-terminal green/gold)
scraper/          All automation scripts
.github/workflows/ GitHub Actions workflows
```

Issue numbers tracked in `scraper/issue_number.txt`, incremented on each Issue run.
