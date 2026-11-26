---
layout: field_note
title: "Field Note — November 26, 2026"
date: 2026-11-26
summary: "A BGP hijack quietly rerouted 1,000+ bitcoin miners to a thief's pool, while RISC Zero patched a proof-forgery flaw and Zcash scrambles to drain a $300M legacy pool."
---

## Today's Field Note
Three separate reminders today that the attack surface is infrastructure, not just contracts. Someone faked internet routes (a BGP hijack) and silently redirected the hashpower of over 1,000 bitcoin miners into their own pool for roughly a second at a time, skimming work without touching a single private key. Separately, RISC Zero shipped a Nov. 10 patch for a critical proof-forgery flaw that let forged ZK proofs pass verification, and anyone relying on their Groth16 or set-proof verification onchain needs to upgrade and regenerate. And Zcash devs are urging holders to move roughly $300M (about 376,530 ZEC) out of the legacy Sapling shielded pool over fears that advancing math and AI could weaken its cryptography before a planned deposit cutoff. None of these are price stories. All three are "patch now or inherit the risk" stories.

## Today's Move
- Miners: verify your pool's stratum endpoints and connection, pin pool IPs or use stratum over TLS, and watch for unexplained short drops in accepted shares that signal BGP rerouting.
- Builders on RISC Zero: upgrade to the post Nov. 10 release immediately, regenerate proofs, and apply the separate onchain fixes for Groth16 verification versus set proofs against cached roots.
- ZEC holders: migrate funds out of the Sapling pool into Orchard before the proposed deposit cutoff, do not wait for the deadline.
- 1Password and Zodia Custody users: assume your name and email leaked, expect targeted phishing, and treat any "verify your account" message as hostile.
- Everyone: rotate credentials exposed to SYS01 infostealer campaigns delivered via Meta ads, and audit any browser profiles enrolled in unexpected enterprise management.

## Resources

- https://www.coindesk.com/markets/2026/11/26/hackers-hijacked-1-000-plus-bitcoin-mines-in-one-second-by-faking-internet-routes
- https://thedefiant.io/news/security/risc-zero-patch-fixes-critical-proof-forgery-flaw
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)
- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)
- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*