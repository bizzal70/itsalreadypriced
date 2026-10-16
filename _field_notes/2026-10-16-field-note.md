---
layout: field_note
title: "Field Note — October 16, 2026"
date: 2026-10-16
summary: "Two live chain exploits (Pirate Chain, Osmosis bOSMO) mint tokens out of thin air while holders are told to sit still."
---

## Today's Field Note
Two separate supply bugs landed today, and both involve attackers conjuring tokens rather than draining wallets. Pirate Chain (ARRR) confirms an exploit minted 39.8 million ARRR out of nothing; the chain is still up, but devs are asking users not to move funds while they chase recovery, which usually means the fix involves a rollback or coordinated halt you do not want to be caught trading against. On Osmosis, a bOSMO bug has left the wrapped token with almost no backing and the contract still permits cheap minting, putting any pool holding bOSMO at direct risk. The compensation plan has a snapshot cutoff, so bOSMO bought after that point gets nothing. When issuance itself is broken, LP exposure is the trap, not your keys.

## Today's Move
- If you hold bOSMO or provide liquidity in any bOSMO pair on Osmosis, exit the pool now; backing is gone and minting is still open.
- Note the bOSMO compensation snapshot already passed. Do not buy bOSMO expecting to be made whole.
- Stop moving ARRR until Pirate Chain devs confirm the recovery path; assume a halt or reorg is on the table.
- If you run an exchange or bridge listing ARRR or bOSMO, pause deposits until supply is reconciled.
- Audit any pool or treasury that routes through wrapped or synthetic assets for similar unbounded-mint logic.

## Resources

- https://thedefiant.io/news/hacks/pirate-chain-says-exploit-created-39-8-million-arrr
- https://thedefiant.io/news/security/bosmo-bug-leaves-little-backing-prompts-holder-compensation-plan
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [On-Chain Forensics and Following Stolen Funds](/itsalreadypriced/rtfm/2026/09/23/on-chain-forensics-and-following-stolen-funds/)
- [Exchange Custody, Counterparty Risk, and Proof of Reserves](/itsalreadypriced/rtfm/2026/09/09/exchange-custody-counterparty-risk-and-proof-of-reserves/)
- [Governance Attacks and Flash-Loan Voting](/itsalreadypriced/rtfm/2026/10/07/governance-attacks-and-flash-loan-voting/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*