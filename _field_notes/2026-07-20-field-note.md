---
layout: field_note
title: "Field Note — July 20, 2026"
date: 2026-07-20
summary: "Allbridge halts after a $1.65M flash loan exploit, and Zilliqa freezes ZIL exchange-wide over a compromised partner cold wallet."
---

## Today's Field Note
Two bridge-and-custody failures today, both the boring kind that keep happening. Allbridge Core paused its cross-chain protocol after an attacker used a flash loan and rapid swaps to manipulate the pool's stablecoin exchange rate, draining $1.65M and bridging it from Solana to Ethereum (per PeckShield and CertiK). Separately, Zilliqa asked exchanges to pause ZIL deposits and withdrawals after an exchange partner's cold wallet was compromised, amount still undisclosed. Neither is novel: the Allbridge vector is the same price-manipulation-via-flash-loan class we have watched for years, and "cold wallet" is doing a lot of work in the Zilliqa statement. If your funds touched either, act before the postmortem lands.

## Today's Move
- If you have liquidity in Allbridge Core pools, do not wait for the unpause. Track the drainer's Ethereum address once security firms publish it and confirm your position is not in the affected pool.
- Revoke any active token approvals granted to Allbridge Core contracts across Solana and Ethereum now.
- Move ZIL off exchanges to self-custody, or if it is already trapped by the freeze, stop new deposits until Zilliqa names the compromised partner and the stolen amount.
- Builders using flash-loan-priced stablecoin pools: audit your exchange-rate oracle for single-block manipulation and add a spot-vs-TWAP sanity check before it is your postmortem.
- Watch Zilliqa and its exchange partners' official channels for the loss figure. Undisclosed amounts usually mean bigger than convenient.

## Resources

- https://www.coindesk.com/business/2026/07/20/cross-chain-protocol-allbridge-halts-after-usd1-65-million-flash-loan-exploit
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Field Note — July 19, 2026](/itsalreadypriced/field-notes/2026/07/19/field-note/)
- [Field Note — July 18, 2026](/itsalreadypriced/field-notes/2026/07/18/field-note/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*