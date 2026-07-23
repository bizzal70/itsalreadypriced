---
layout: field_note
title: "Field Note — July 23, 2026"
date: 2026-07-23
summary: "Two bridge exploits drained $35M across Bitcoin and Ethereum, with Verus hit through the same flaw class it ignored in May."
---

## Today's Field Note
Two custody bridges bled roughly $35M within hours of each other. The Verus-Ethereum bridge lost $7.54M to the same vulnerability class Blockaid flagged after a May exploit, meaning the team shipped a patch that did not close the door. Separately, Arbitrum perp DEX AFX Trade lost $24M through its custody bridge (not the chain itself), moved fast to Ethereum, and is now begging the attacker to keep 30% and return the rest. The pattern is the usual one: bridges are single points of custody, and "we fixed it" rarely survives a second look. If your capital sits behind a bridge or a perp DEX that self-custodies deposits, you are the collateral.

## Today's Move
- Pull funds out of AFX Trade now. A protocol negotiating a 30% bounty is not a protocol that has secured user assets.
- If you hold or bridge through Verus-Ethereum, exit and revoke any bridge contract approvals until an independent post-mortem confirms the vulnerability class is actually closed, not repatched.
- Audit approvals across all bridge and perp DEX contracts (revoke.cash or Etherscan token approvals) and cut anything unlimited.
- Watch the AFX attacker's Ethereum consolidation address for movement to mixers or CEX deposit wallets before you assume any recovery.
- Treat any protocol re-exploited on a known flaw class as untrusted infrastructure regardless of the fix announcement.

## Resources

- https://decrypt.co/374133/arbitrum-perp-dex-afx-trade-drained-of-24m-offers-hacker-30-to-return-it
- https://www.coindesk.com/tech/2026/07/23/bitcoin-ethereum-linked-protocols-lose-usd35-million-in-multiple-attacks-hours-apart
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Signature Requests and Blind Signing](/itsalreadypriced/rtfm/2026/07/22/signature-requests-and-blind-signing/)
- [Field Note — July 22, 2026](/itsalreadypriced/field-notes/2026/07/22/field-note/)
- [Field Note — July 21, 2026](/itsalreadypriced/field-notes/2026/07/21/field-note/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*