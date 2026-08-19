---
layout: field_note
title: "Field Note — August 19, 2026"
date: 2026-08-19
summary: "MAYAChain halted after six chained bugs let a 23-message transaction drain the pools, and 200K Bits of Gold customers had their data leaked."
---

## Today's Field Note
MAYAChain (Maya Protocol) halted its network after an attacker chained six bugs into a single 23-message transaction, draining roughly $1.7M and 48.87M CACAO from pools, with pool value down about $11M and CACAO off nearly 89%. This is the same THORChain-derived architecture, so the six-bug chain matters beyond Maya: if you touch any THORChain fork or cross-chain swap layer, assume the class of flaw is portable until proven otherwise. Separately, Israeli exchange Bits of Gold disclosed a breach hitting 200K customers, which is a phishing and SIM-swap accelerant, not just a privacy footnote. Neither is a price story. Both are operational.

## Today's Move
- If you have liquidity or CACAO in Maya pools, do nothing on-chain until the halt lifts and a post-mortem confirms which pools were touched. Do not trust "resume" chatter without an official address list.
- Revoke any standing approvals to Maya or THORChain router contracts on the EVM chains you use (Etherscan, revoke.cash), then re-approve only when needed.
- If you are a builder on a THORChain-derived stack, freeze cross-chain message handling and audit for multi-message transaction chaining before your next deploy.
- Bits of Gold customers: assume name, email, and phone are exposed. Move exchange logins to app-based 2FA (not SMS), call your carrier to lock the SIM, and treat any "Bits of Gold support" contact as hostile.
- Watch the attacker's cash-out path across bridges over the next 48 hours before assuming funds are gone.

## Resources

- https://www.coindesk.com/markets/2026/08/19/maya-protocol-exploit-drains-bitcoin-and-other-assets-as-pool-value-drops-usd11-million
- https://www.reddit.com/r/CryptoCurrency/comments/1vshhrd/major_crypto_data_leak_affects_200k_customers_in/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*