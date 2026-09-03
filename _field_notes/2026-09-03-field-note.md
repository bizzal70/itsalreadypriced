---
layout: field_note
title: "Field Note — September 03, 2026"
date: 2026-09-03
summary: "Coldcard thief launders BTC through THORChain while Lazarus runs $30M through Hyperliquid, and Shai-Hulud's npm worm now scans 469 credential paths."
---

## Today's Field Note
Three threads worth your attention, all operational. The third-wave Coldcard exploiter is moving stolen Bitcoin, roughly 10% so far, through THORChain into a fresh Ethereum address, the usual cross-chain wash that frustrates freezes. Separately, Lazarus-tagged addresses pushed about $30M through Hyperliquid, a reminder that perps venues are now laundering rails as much as trading ones. And the Shai-Hulud npm worm has expanded to scan 469 credential locations (up from 189), sweeping CI/CD, cloud config, and AI tool secrets across developer environments. None of this is price noise. It is theft in motion and supply-chain rot, and both hit builders directly.

## Today's Move
- If you build on npm, audit your dependency tree today for Shai-Hulud compromise, rotate any npm, cloud, and CI/CD tokens, and enforce least-privilege on CI runners. Assume anything in a scanned path is burned.
- Rotate credentials stored in .env files, AWS/GCP config, and AI tool configs (Claude, etc.); the worm now reads these explicitly.
- Coldcard holders on affected firmware: move funds to a clean device now, do not wait for tracing to resolve.
- Watch the flagged Lazarus addresses on Hyperliquid and blacklist them in your compliance tooling if you run a venue or desk.
- Add the new Coldcard-thief Ethereum address to your watchlists and any inbound-deposit screening.

## Resources

- https://www.reddit.com/r/CryptoCurrency/comments/1w5wffl/lazarus_group_addresses_move_30m_through/
- https://thehackernews.com/2026/09/shai-huluds-reach-just-grew-to-469.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [A 2021 PRNG Bug Drained $89M From Coldcard Wallets in 41 Minutes](/itsalreadypriced/2026/08/02/issue-005/)
- [Coldcard Ships Firmware After $114M Bitcoin Theft](/itsalreadypriced/2026/08/23/issue-008/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*