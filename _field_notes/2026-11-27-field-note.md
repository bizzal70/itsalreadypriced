---
layout: field_note
title: "Field Note — November 27, 2026"
date: 2026-11-27
summary: "Atoshi bridge drained of 201M ATOS on Ethereum while Fluid preemptively pauses DEX swaps on a security finding."
---

## Today's Field Note
The Atoshi bridge on Ethereum was drained of 201 million ATOS, and the attacker promptly dumped into two Uniswap pools, collapsing ATOS roughly 94% in an hour while netting only about $60,300 from a KyberSwap trade. That gap between tokens stolen and value extracted is the usual tell: a thin-liquidity token where the "theft" is nominal and the realized take is small, but anyone still holding ATOS or LPing those pools ate the move. Separately, Fluid paused DEX swaps after a "Mythos 5.2" security review with no restart date, though borrowers can still repay and users can still withdraw. One is a post-mortem, the other is a live precaution, and both point the same direction today: get out of anything bridge-dependent or under active review before someone decides for you.

## Today's Move
- If you hold ATOS or provide liquidity in the affected Uniswap ATOS pools, exit now and stop treating the quoted price as real.
- Revoke any token approvals granted to the Atoshi bridge contract on Ethereum via Revoke.cash or Etherscan.
- If you have funds in Fluid, withdraw or repay while those paths remain open rather than waiting for the swap pause to lift.
- Watch the Atoshi drainer wallet and the KyberSwap/Uniswap routing for follow-on dumps or cross-chain movement.
- Treat any "redeploy" or "migration" messaging from Atoshi as hostile until an independent post-mortem lands.

## Resources

- https://thedefiant.io/news/hacks/atoshi-bridge-drained-of-201-million-atos-on-ethereum
- https://thedefiant.io/news/security/fluid-pauses-dex-swaps-after-mythos-5-2-security-review
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [On-Chain Forensics and Following Stolen Funds](/itsalreadypriced/rtfm/2026/09/23/on-chain-forensics-and-following-stolen-funds/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*