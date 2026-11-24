---
layout: field_note
title: "Field Note — November 24, 2026"
date: 2026-11-24
summary: "Chainflip loses $12.6M to suspected key theft and halts services, while an Ansem-linked wallet gets drained of $2.15M in USDC."
---

## Today's Field Note
Chainflip's cross-chain vaults got hit for roughly $12.6 million, and the team's own first report points at suspected validator key theft, not a contract bug. Validly signed transfers moved funds outside the protocol, which is the signature of compromised signing keys rather than an exploit you can patch. Services are paused while they sort out which keys are dirty, so anything bridged through Chainflip is frozen or in limbo right now. Separately, Lookonchain flagged a drain of 2.15 million USDC from an Ansem-linked wallet, with 1.55 million routed to Arbitrum via Relay, another reminder that EOAs and hot wallets remain the softest target this cycle. Key compromise, not clever math, is doing the damage this week.

## Today's Move
- If you have assets mid-bridge on Chainflip or liquidity in its vaults, assume them frozen and do not attempt new swaps until the team confirms which validator keys are compromised.
- Watch the Arbitrum receiving address tied to the Ansem drain (1.55M USDC via Relay) and avoid any token flowing from it.
- Rotate signing keys and hardware for any protocol or treasury where a single key set controls vault movement, and move to multisig or MPC if you have not.
- Audit your hot wallet approvals today at revoke.cash and pull anything you do not actively use, since this week's losses are credential and key theft, not DeFi logic bugs.
- If you run validators or signers, assume phishing and infostealer malware are the delivery vector and reimage any machine with wallet or signing access.

## Resources

- https://thedefiant.io/news/hacks/chainflip-suspects-key-theft-in-12-6-million-vault-hack
- https://thedefiant.io/news/hacks/lookonchain-flags-suspected-hack-of-ansem-linked-wallet
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*