---
layout: field_note
title: "Field Note — August 31, 2026"
date: 2026-08-31
summary: "Cronos halted its entire chain after a $75M Tectonic exploit, while More Markets bled $9.3M through an Ankr LST and E-mode borrow trick."
---

## Today's Field Note
Two lending exploits, one playbook: manipulate an illiquid or mispriced collateral asset, then overborrow against it. On Cronos, an attacker inflated the TONIC token price and drained roughly $75M from Tectonic, a Mango Markets rerun that forced validators to halt the entire chain (about $6M reached Ethereum before the freeze, the rest is stranded on a network not producing blocks). Separately, Blockaid reports an attacker used an Ankr liquid staking token plus E-mode to overborrow and drain about $9.3M in WFLOW from a More Markets lending reserve. The Cronos halt matters most: a chain-wide stop means your funds there are frozen regardless of what you hold, and a restart with $6M already exfiltrated is not a clean recovery. Illiquid collateral and aggressive E-mode remain the soft underbelly of every lending market.

## Today's Move
- Assume any Cronos-based positions are inaccessible until validators confirm block production resumes; do not send new funds to Cronos addresses or bridges today.
- Exit or reduce exposure to any lending market that accepts illiquid, thin-liquidity collateral like TONIC, especially in high-leverage E-mode categories.
- If you supplied to More Markets on Flow, pull remaining liquidity and revoke approvals to its contracts now.
- Audit E-mode borrow positions across all lending protocols; oracle-manipulable collateral pairs are the current attack surface.
- Watch the attacker's Ethereum address for the ~$6M bridged from Cronos and flag it to exchanges if you run compliance tooling.

## Resources

- https://decrypt.co/376913/crypto-coms-cronos-halts-entire-blockchain-after-75m-tectonic-exploit
- https://www.theblock.co/news/defi/2026-08-30-crypto-com-linked-cronos-network-halts-after-tectonic-exploit-estimated-at-75-million-413069
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*