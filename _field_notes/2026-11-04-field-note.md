---
layout: field_note
title: "Field Note — November 04, 2026"
date: 2026-11-04
summary: "North Korean launderers are running Binance's stolen SOL through THORChain again, and ZachXBT says a French bank quietly ate a $133M theft."
---

## Today's Field Note
Two laundering stories converge today. The Binance attackers behind the record $6.3B theft have moved 81% of the stolen Solana and resumed routing funds through THORChain after the protocol turned swaps back on, which is exactly why RUNE popped 10% (volume is the business model here, no matter the source). Separately, ZachXBT named French bank Crédit Mutuel Arkéa as the suspected victim of a $133M exploit he says is being actively covered up, with over $30M already laundered during the silence. Note he is confident this one is not Lazarus, so you have at least two serious crews working cross-chain rails simultaneously. The through-line: non-KYC cross-chain swap venues remain the preferred cash-out, and disclosure delays are buying attackers laundering windows measured in weeks.

## Today's Move
- If you run a THORChain-adjacent service or LP, screen incoming SOL and cross-chain flows against the published Binance exploit addresses before accepting them.
- Builders handling user uploads on Rails: patch to 8.1.4.1 or 8.0.5.2 now (the ImageMagick Active Storage flaw is unauthenticated arbitrary file write).
- Patch WordPress Core for CVE-2026-119977 (CISA confirmed active exploitation during upgrades) if any front-end or docs site touches your ops.
- Treat any counterparty who went quiet about a "temporary" outage as a potential breach in progress; Crédit Mutuel Arkéa is the template.
- Watch ZachXBT's feed for the Arkéa attacker clusters and pre-emptively flag those addresses in your compliance tooling.

## Resources

- https://www.coindesk.com/markets/2026/11/04/thorchain-s-rune-jumps-10-as-north-korean-hackers-resume-laundering-binance-loot
- https://decrypt.co/382486/zachxbt-names-french-bank-credit-mutuel-arkea-as-alleged-victim-of-133m-crypto-theft
- https://thehackernews.com/2026/11/critical-rails-flaw-lets-attackers.html
- https://thehackernews.com/2026/11/cisa-confirms-hackers-exploiting.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [One Laptop, EIP-7702, and a $6.3B Hole at Binance](/itsalreadypriced/2026/11/01/issue-018/)
- [Bitget Loses $388M to Spoofed Transfers, Not Stolen Keys](/itsalreadypriced/2026/09/27/issue-013/)
- [A 2021 PRNG Bug Drained $89M From Coldcard Wallets in 41 Minutes](/itsalreadypriced/2026/08/02/issue-005/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*