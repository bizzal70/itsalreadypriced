---
layout: field_note
title: "Field Note — November 14, 2026"
date: 2026-11-14
summary: "Pennysia got drained across four addresses and swaps were cut before anyone said a word, while DOJ moves on $1.2B tied to a Binance hack."
---

## Today's Field Note
Pennysia suffered an onchain exploit that SlowMist flagged publicly, but records show swaps were already disabled before the warning, meaning the team knew before you did. Four addresses were drained, and the team is now telling users to revoke approvals, which is the usual order of operations: get hit, then ask everyone to clean up after the fact. Separately, the DOJ is moving to seize $1.2 billion tied to a Binance hack and disrupting a North Korean deepfake scheme, a reminder that laundered proceeds have a long tail and that the people on the other side of these drains are increasingly state-backed. Neither is a reason to panic, but both are reasons to check what you still have signed.

## Today's Move
- Revoke all Pennysia contract approvals now (use Revoke.cash or etherscan token approvals), especially for any address that interacted with their swap contracts.
- Assume the four drained addresses are compromised and stop any pending interactions with Pennysia pools until a verified post-mortem lands.
- If you use Cursor, check machines and rotate credentials after the tampered Claude Code extension incident (up to 5,000 users potentially hit).
- Audit your full approval list across chains while you are at it, not just Pennysia; dormant unlimited approvals are the standard drain vector.
- Watch DOJ filings on the $1.2B Binance seizure if you hold on exchanges, since frozen or clawed-back flows can touch counterparties downstream.

## Resources

- https://thedefiant.io/news/hacks/pennysia-users-urged-to-revoke-approvals-after-exploit
- https://www.theblock.co/newsletters/the-daily/2026-11-14-meta-prediction-market-app-doj-binance-hack-more-crypto-news-440304
- https://thedefiant.io/frontier/security/cursor-links-extension-attack-to-exposed-credentials
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [On-Chain Forensics and Following Stolen Funds](/itsalreadypriced/rtfm/2026/09/23/on-chain-forensics-and-following-stolen-funds/)
- [Reading a Token Contract Before You Buy the Rug](/itsalreadypriced/rtfm/2026/08/26/reading-a-token-contract-before-you-buy-the-rug/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*