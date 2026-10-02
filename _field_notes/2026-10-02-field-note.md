---
layout: field_note
title: "Field Note — October 02, 2026"
date: 2026-10-02
summary: "Core Lightning nodes under active attack, FortiMail zero-day exploited in the wild, and a NEAR Intents drainer gets a 48-hour clock."
---

## Today's Field Note
Two patch-now items landed today. Core Lightning (CLN) is warning that attackers are actively targeting nodes running version 26.06.7 or earlier, which means Lightning routing node operators with real channel balances are the live target, not a theoretical one. Separately, Fortinet disclosed CVE-2026-104286, a CVSS 9.8 FortiMail flaw already exploited as a zero-day for unauthenticated arbitrary file writes and remote code execution, now in CISA's KEV catalog. On the DeFi side, NEAR Intents was drained for roughly $3.8M (via a third-party component, not NEAR core), and GM Alex Shevchenko says they have identified the attacker and set a 48-hour return window, which usually resolves into a bounty-or-nothing negotiation. None of these are price noise. They are operational fires.

## Today's Move
- If you run a Core Lightning node, upgrade off 26.06.7 or earlier immediately, then audit channel state and peer connections for anything odd.
- Patch any FortiMail appliance against CVE-2026-104286 now and check logs for unexpected file writes or new processes, assume compromise if exposed and unpatched.
- Move hot funds off Lightning routing nodes you cannot patch today, keep only working liquidity online.
- If you used NEAR Intents recently, revoke token approvals tied to the affected adapter and watch the three return addresses Shevchenko posted for resolution.
- Treat the Aave "third-party adapter" drain ($305K from two Safe multisigs) as the same lesson: audit every external adapter and integration your multisig has approved.

## Resources

- https://cointelegraph.com/news/core-lightning-urges-upgrade-amid-reports-attackers-targeting-unpatched-nodes?utm_source=rss_feed&utm_medium=rss_tag_hacks&utm_campaign=rss_partner_inbound
- https://www.bleepingcomputer.com/news/security/fortinet-warns-of-critical-fortimail-flaw-exploited-in-zero-day-attacks/
- https://cointelegraph.com/news/near-intents-says-its-identified-the-hacker-gives-48-hour-ultimatum?utm_source=rss_feed&utm_medium=rss_tag_hacks&utm_campaign=rss_partner_inbound
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)
- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*