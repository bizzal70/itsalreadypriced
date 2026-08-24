---
layout: field_note
title: "Field Note — August 24, 2026"
date: 2026-08-24
summary: "Term Finance bled $8.5M when an attacker bought governance power and drained the Meta Vaults, a reminder that on-chain votes are an attack surface."
---

## Today's Field Note
Ethereum lending protocol Term Finance lost an estimated $8.5 million after an attacker acquired enough voting power to push through a malicious governance action and drain nearly all ETH deposits from its Meta Vaults. Term has permanently closed the Meta Vaults in response. This is a governance capture, not a smart contract bug in the classic sense, which is why it slid past the usual audit defenses. If your protocol lets token holders or vault depositors vote, and voting power is cheaply purchasable, you already own this exploit surface. Separately, keep an eye on the BNB Chain hard fork scheduled for August 25th, which is a live operational event for anyone running infrastructure or bridges.

## Today's Move
- If you have deposits in Term Finance Meta Vaults, confirm exit status and revoke any lingering token approvals to Term contracts via Etherscan or Revoke.cash.
- Audit governance parameters on any protocol you hold or build: check timelock delays, quorum thresholds, and whether voting power can be flash-bought or borrowed.
- Builders: add execution delays and multisig veto on governance proposals that touch vault funds, and monitor for sudden voting-power accumulation.
- Prepare for the BNB Chain hard fork on August 25th. Update nodes, pause bridge automation during the transition, and verify RPC endpoints post-fork.
- Watch Wintermute's ~$190M Hyperliquid short book (0xecb63caa47c7c4e77f60f1ce858cf28dc2b82b00) if you are running leverage into a stretched rally.

## Resources

- https://www.coindesk.com/markets/2026/08/24/ethereum-lending-app-term-finance-loses-usd8-5-million-after-attacker-buys-voting-power
- https://www.reddit.com/r/CryptoCurrency/comments/1vwvrw7/bnb_chain_to_undergo_hard_fork_on_august_25th/
- On-chain address: https://etherscan.io/address/0xecb63caa47c7c4e77f60f1ce858cf28dc2b82b00
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Upgradeable Contracts and the Admin Key Problem](/itsalreadypriced/rtfm/2026/08/12/upgradeable-contracts-and-the-admin-key-problem/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*