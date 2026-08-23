---
layout: field_note
title: "Field Note — August 23, 2026"
date: 2026-08-23
summary: "The Sandbox bridge got hit, minting unbacked SAND on Base and BSC while Korean exchanges slammed the doors."
---

## Today's Field Note
The Sandbox confirms a bridge exploit that minted unbacked SAND tokens on Base and BNB Chain, and it has halted bridging on both while claiming Ethereum was unaffected. Upbit and Bithumb froze SAND transfers under South Korea's user-protection law, with Upbit suspending deposits and withdrawals on Ethereum too, which tells you the counterparties are not taking the "contained" framing at face value. Unbacked mints mean any SAND you buy or LP against right now could be freshly conjured supply chasing real liquidity out the door. Separately, Microsoft patched a CVSS 10.0 Entra ID flaw allowing remote code execution (claimed unexploited, patched pre-disclosure), relevant to any custodian or exchange running on Azure identity. Bridges remain the single worst attack surface in this market, and this is the same story with a new logo.

## Today's Move
- Do not add or provide SAND liquidity on Base or BNB Chain today. Pull any SAND from AMM pools (Uniswap, PancakeSwap) until The Sandbox publishes the exact minted amount and burns or reconciles it.
- Revoke bridge and router approvals for SAND on Base and BSC via revoke.cash. Assume the bridge contract is compromised until proven otherwise.
- If you hold SAND on Upbit or Bithumb, do not expect to move it. Plan around the freeze rather than fighting it.
- Builders and custodians on Azure: confirm the Entra ID patch (the CVSS 10.0 actor-token flaw) is applied, then audit for any cross-tenant token issuance in logs regardless of Microsoft's "no evidence" line.
- Watch The Sandbox official channels for the mint address and quantity. Until that number is public, treat all SAND price action as noise on top of unknown phantom supply.

## Resources

- https://thedefiant.io/news/hacks/the-sandbox-says-it-contained-bridge-exploit-that-minted-unbacked-sand-on-base-and-bsc
- https://www.coindesk.com/web3/2026/08/22/web3-gaming-network-sandbox-stops-base-and-bnb-chain-bridging-after-exploit
- https://decrypt.co/376287/microsoft-perfect-10-exploit-hackers-run-code
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*