---
layout: field_note
title: "Field Note — November 16, 2026"
date: 2026-11-16
summary: "Lighter and Kava bleed while Luxor shows AI-driven attacks can redirect your hashrate in a weekend."
---

## Today's Field Note
Three separate security events, one theme: compromise through the soft edges. Kava is rushing a seven-day governance vote to wind down its HARD lending module after a 53.9M KAVA theft, with depositors still waiting to hear how open positions get settled. Lighter halted all withdrawals and suspended pool creation over an "apparent compromise of a single external party," and both Upbit and Bithumb froze LIT deposits and withdrawals while the probe runs. Meanwhile Luxor's Commander mining platform was hijacked over the weekend in what the CEO calls an AI-enabled attack that redirected client hashrate to an attacker before being patched within two hours. None of these are protocol-math failures. They are operational and third-party failures, which is where most money actually leaves.

## Today's Move
- If you have deposits in Kava's HARD lend module, pull what you can now and watch the governance vote closely; do not assume orderly unwind.
- Treat any funds on Lighter as frozen. Stop new deposits and pool creation there until the external-party compromise is fully scoped.
- If you hold LIT, do not route it through Upbit or Bithumb right now; transfers are halted even though trading continues.
- Luxor Commander users: rotate API keys and pool credentials, reconfirm your payout addresses on-chain, and verify hashrate is pointed where you expect.
- Audit third-party integrations across your own stack this week, that external connector is the attack surface, not the contract.

## Resources

- https://thedefiant.io/news/hacks/kava-speeds-hard-lend-shutdown-after-53-9m-kava-theft
- https://thedefiant.io/news/security/lighter-halts-all-withdrawals-over-security-incident
- https://thedefiant.io/news/security/upbit-and-bithumb-halt-lit-transfers-amid-lighter-probe
- https://www.theblock.co/news/business/2026-11-15-luxor-attack-client-hashrate-440810
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [On-Chain Forensics and Following Stolen Funds](/itsalreadypriced/rtfm/2026/09/23/on-chain-forensics-and-following-stolen-funds/)
- [Smart Contract Security Best Practices for Builders](/itsalreadypriced/rtfm/2026/10/14/smart-contract-security-best-practices-for-builders/)
- [Governance Attacks and Flash-Loan Voting](/itsalreadypriced/rtfm/2026/10/07/governance-attacks-and-flash-loan-voting/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*