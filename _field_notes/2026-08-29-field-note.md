---
layout: field_note
title: "Field Note — August 29, 2026"
date: 2026-08-29
summary: "A known-vulnerable Cosmos EVM module got exploited across six chains, and an outdated Rain contract cost Solana neobank users half a million dollars."
---

## Today's Field Note
Two supply-chain style failures landed today. Cosmos Labs confirmed the critical balance-handling flaw in the shared Cosmos EVM module (GHSA-7g4w-cg88-2cq2, affecting versions < 0.6.2) was exploited to drain six chains between August 20 and 25, and it shipped without a CVE, CVSS, or weakness class, meaning downstream chains were left guessing about their own exposure while attackers were already moving. Separately, Rain disclosed that an attacker used an outdated version of its Solana card contract to drain roughly $500,859 from 1,685 Avici users. Both are the same lesson: unpatched or forked code you thought was retired is still live and still holding balances. Rain and Avici say users will be made whole, which is worth watching but not banking on.

## Today's Move
- If you run a Cosmos EVM chain or module, upgrade past 0.6.2 immediately and audit balance-handling state against GHSA-7g4w-cg88-2cq2, do not wait for a CVE that may never come.
- Avici and Rain users: revoke any lingering approvals to old Rain card contract addresses on Solana, then verify you are interacting only with the current contract version.
- Assume any forked or "deprecated" contract you deployed is still exploitable, inventory what is still on-chain and holding funds today.
- Watch the six affected Cosmos chains for follow-on movement and pause bridge activity in and out until each posts a concrete patched-version confirmation.
- Track Rain's and The Sandbox's reimbursement wallets before treating "users made whole" as done.

## Resources

- https://thehackernews.com/2026/08/cosmos-evm-flaw-exploited-after-cosmos.html
- https://thedefiant.io/news/hacks/attacker-drains-more-than-usd1-million-from-avici-users-in-live-solana-neobank-attack
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Coldcard Ships Firmware After $114M Bitcoin Theft](/itsalreadypriced/2026/08/23/issue-008/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*