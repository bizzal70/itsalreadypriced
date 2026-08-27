---
layout: field_note
title: "Field Note — August 27, 2026"
date: 2026-08-27
summary: "Moonwell bled $8.7M to a MAMO oracle manipulation on Base, and Lightning node operators face an emergency patch cycle after AI-found bugs."
---

## Today's Field Note
Two things worth your attention, both about price feeds and code that trusts the wrong input. Moonwell's Base lending market lost roughly $8.7 million (per CertiK and PeckShield) when an attacker manipulated the collateral price of MAMO, the same low-liquidity oracle pattern that has drained lenders for years now hitting a Base bluechip. Separately, the Lightning Network devs issued an emergency warning after several AI-generated vulnerability reports turned out to be accurate, with fixes still being prepared. Neither is theoretical: one is a confirmed drain, the other is a live window before patches ship. Thin-collateral markets and unpatched nodes are exactly where the next hour hurts.

## Today's Move
- If you have supplied or borrowed on Moonwell (Base), exit or reduce exposure now and revoke approvals to affected market contracts until the postmortem lands.
- Treat any market listing MAMO or similar low-liquidity collateral as compromised; do not deposit into it.
- Lightning node operators (LND, Core Lightning, Eclair): watch the project channels and apply patches the moment they publish. Consider closing channels you cannot actively monitor.
- Watch the Moonwell exploiter address and monitor bridges out of Base for the stolen funds.
- If you run any DeFi lending market, audit your oracle sources today for assets with shallow liquidity and add sanity bounds or TWAP checks.

## Resources

- https://www.theblock.co/news/defi/2026-08-27-moonwell-investigates-base-lending-market-issue-412913
- https://www.reddit.com/r/CryptoCurrency/comments/1vzts4k/moonwell_suffered_a_loss_of_87_million_in_an/
- https://decrypt.co/376714/ai-critical-flaw-bitcoin-lightning-warning
- https://www.coindesk.com/tech/2026/08/27/ai-bug-reports-trigger-emergency-warning-for-bitcoin-lightning-node-operators
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)
- [Coldcard Ships Firmware After $114M Bitcoin Theft](/itsalreadypriced/2026/08/23/issue-008/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*