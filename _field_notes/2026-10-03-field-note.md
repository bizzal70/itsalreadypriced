---
layout: field_note
title: "Field Note — October 03, 2026"
date: 2026-10-03
summary: "Arbitrum hits the emergency brake on Stylus, Blast schedules its own funeral, and NK is still winning."
---

## Today's Field Note
Arbitrum pushed an emergency security action pausing new Stylus contract activations, with a new BoLD guard that can delay unconfirmed withdrawals if contradictory proofs get accepted. That is a validity-proof concern on the chain's newer WASM execution path, and when a team pauses activations rather than issuing a routine patch, you treat it as live until proven otherwise. Separately, Blast is winding down its L2 with roughly $63.5 million still sitting in the canonical bridge and a hard withdraw date of Oct. 26, after which only contract-based withdrawals remain. And Chainalysis tied the $387M Bitget theft to North Korea, pushing DPRK-linked thefts past $1B for 2026, with stolen XRP already moving through THORChain. Nothing here is theoretical.

## Today's Move
- If you deployed or planned to deploy Stylus (WASM) contracts on Arbitrum, hold new activations and read the official advisory before touching production.
- If you have bridge withdrawals in flight on Arbitrum, assume possible BoLD-related delay and do not rely on fast finality for anything time-sensitive.
- If you hold any assets on Blast or in its canonical bridge, withdraw to Ethereum mainnet through the normal interface before Oct. 26. Do not wait for the contract-only phase.
- Flag THORChain swap paths and known DPRK laundering addresses if you run compliance or custody. Assume stolen Bitget XRP is being cycled now.
- Builders on Arbitrum: audit any contradictory-proof assumptions in your withdrawal logic before re-enabling anything.

## Resources

- https://thedefiant.io/news/security/arbitrum-pauses-new-stylus-activations-in-emergency-security-action
- https://thedefiant.io/news/blockchains/blast-to-shut-down-layer-2-citing-unsustainable-costs
- https://thedefiant.io/news/hacks/chainalysis-links-387-million-bitget-hack-to-north-korea
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Bitget Loses $388M to Spoofed Transfers, Not Stolen Keys](/itsalreadypriced/2026/09/27/issue-013/)
- [On-Chain Forensics and Following Stolen Funds](/itsalreadypriced/rtfm/2026/09/23/on-chain-forensics-and-following-stolen-funds/)
- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*