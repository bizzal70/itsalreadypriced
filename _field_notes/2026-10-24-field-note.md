---
layout: field_note
title: "Field Note — October 24, 2026"
date: 2026-10-24
summary: "Initia halts its L1 and rollups after a mint exploit drains ~$2.6M, dragging AUSD and a bridge adapter into the blast radius."
---

## Today's Field Note
Initia suspended its layer-1 and all rollups after an attacker minted unauthorized tokens and cashed out an estimated $2.6M, with onchain records showing stablecoin swaps and a later transfer of 1,135.5 ETH to Ethereum. Agora confirmed the fallout reached AUSD: roughly 1.4 million AUSD left a bridge adapter and was swapped for ETH, though Agora says it has no contracts deployed on Initia, pointing instead at a third-party product. Agora has since frozen the linked AUSD account. This is the familiar pattern, a mint bug plus a bridge adapter nobody was watching, and the chain being halted means your assets on Initia are frozen whether you like it or not. Separately, Succinct patched an SP1 bug (native Rust verification, versions 6.0.0 to 6.8.0) that could let invalid proofs pass; onchain Groth16 and Plonk via Solidity verifiers were unaffected.

## Today's Move
- If you hold positions or LP on Initia or its rollups, assume funds are locked until the team restarts; do not pay for "unlock" or "recovery" services.
- Audit any bridge adapters or third-party products touching AUSD on Initia and revoke approvals to contracts in that path now.
- If you integrate Succinct SP1, upgrade off versions 6.0.0 through 6.8.0 immediately, especially anything relying on native Rust verification rather than Solidity Groth16/Plonk.
- Watch the attacker's Ethereum destination for the 1,135.5 ETH and swapped AUSD proceeds, and flag counterparties interacting with it.
- Hold off on new deposits or bridging into Initia until a post-mortem and confirmed clean restart.

## Resources

- https://thedefiant.io/news/hacks/initia-halts-l1-and-rollups-after-reported-mint-exploit
- https://thedefiant.io/news/hacks/agora-says-initia-exploit-hit-third-party-product-using-ausd
- https://thedefiant.io/news/hacks/agora-freezes-ausd-account-linked-to-initia-exploit
- https://thedefiant.io/news/security/succinct-patches-sp1-bug-that-could-let-invalid-proofs-pass
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [A Hardware Implant in a Ledger Cost Users $86M](/itsalreadypriced/2026/10/11/issue-015/)
- [Bitget Loses $388M to Spoofed Transfers, Not Stolen Keys](/itsalreadypriced/2026/09/27/issue-013/)
- [An OpenAI Model Drained a Stranger's Wallet to Pay Its Own Gas](/itsalreadypriced/2026/10/18/issue-016/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*