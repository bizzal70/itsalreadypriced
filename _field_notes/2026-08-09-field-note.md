---
layout: field_note
title: "Field Note — August 09, 2026"
date: 2026-08-09
summary: "Attackers are draining BTCPay Server Lightning nodes via remote access, and the Coldcard exploit is still pulling institutional money into ETFs."
---

## Today's Field Note
BTCPay Server has restricted remote Lightning access after attackers drained funds from live nodes, with Foundation and Citadel21 among those reporting losses. The total stolen and the number of affected operators are still unknown, which is the part that should worry you: if you self-host a BTCPay instance with an internet-facing Lightning node, you are inside the blast radius until proven otherwise. This lands the same week ETFs booked over $1B in inflows on the back of the Coldcard exploit narrative, a reminder that the money keeps flowing in while the plumbing keeps leaking. Meanwhile a volunteer red team says AI scans of 150 Bitcoin repos have surfaced more than a dozen vulnerabilities, so expect more of these disclosures, not fewer.

## Today's Move
- If you run BTCPay Server, disable remote Lightning access now and update to the patched release before re-enabling anything internet-facing.
- Audit your Lightning node for unexpected channel closes or force-closes and rotate any exposed macaroons, LND admin credentials, and RPC access.
- Move hot Lightning balances down to operational minimums until you have confirmed your instance is clean; treat any node reachable from the open internet as suspect.
- Coldcard holders: verify firmware provenance and confirm you are not running any version tied to the recent exploit before signing.
- Run a full permission audit while you are at it: revoke stale token approvals, kill old WalletConnect sessions, and disable unused exchange API keys.

## Resources

- https://decrypt.co/375169/bitcoin-red-team-ai-finding-critical-vulnerabilities
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [A 2021 PRNG Bug Drained $89M From Coldcard Wallets in 41 Minutes](/itsalreadypriced/2026/08/02/issue-005/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*