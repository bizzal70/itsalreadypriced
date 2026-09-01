---
layout: field_note
title: "Field Note — September 01, 2026"
date: 2026-09-01
summary: "A $74M price-manipulation exploit on Cronos-based Tectonic halted a whole chain, while Lazarus-linked wallets openly launder $30M through Hyperliquid."
---

## Today's Field Note
Tectonic, the lending market on Cronos, got drained for roughly $74 million via a price-manipulation attack, and the response was to halt the entire chain and restart it. That is the tell worth noting: a single lending pool's oracle failure was severe enough that Cronos chose to stop block production rather than let the exploit propagate. Separately, wallets tied to the OFAC-sanctioned Lazarus Group have been pushing around $30 million through Hyperliquid, in the open, weeks after regulators floated onshoring the venue in the US. If you touch Cronos DeFi or hold funds on Hyperliquid, you are exposed to both an active exploit blast radius and a sanctions-adjacent counterparty, today.

## Today's Move
- Exit or pause any positions on Tectonic and other Cronos lending markets until a full post-mortem and reimbursement plan is published, not just a chain restart.
- Revoke token approvals granted to Tectonic contracts using a revoke tool on Cronos before assuming the restart made you safe.
- Treat any Cronos oracle-dependent protocol (borrow/lend, leveraged vaults) as suspect until each confirms its price feeds were not the same manipulation vector.
- If you hold on Hyperliquid, understand that Lazarus flows through the venue raise real sanctions and delisting risk, and consider reducing balances held there directly.
- Watch the flagged Lazarus-linked addresses and Hyperliquid's response; a sudden freeze or bridge restriction could trap withdrawals.

## Resources

- https://www.bleepingcomputer.com/news/security/cronos-blockchain-restarts-after-74-million-tectonic-exploit/
- https://www.coindesk.com/business/2026/08/31/north-korean-hackers-are-moving-tens-of-millions-on-hyperliquid-as-trump-pushes-to-onshore-the-crypto-platform
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*