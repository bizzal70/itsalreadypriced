---
layout: field_note
title: "Field Note — November 21, 2026"
date: 2026-11-21
summary: "Chainflip halts swaps over a suspected $4.86M vault drain, Fluidkey bleeds $1.58M via a logging flaw, and a wrapped Monero token collapses 99.8% in a $13.5M exploit."
---

## Today's Field Note
Three live wounds today. Chainflip flagged roughly $4.86M in Ethereum vault outflows and killed deposits, withdrawals, and quotes while it investigates, so the protocol itself is dark. Fluidkey confirmed a logging-tool flaw let an attacker trigger transfers whenever users opened the app, Bitquery tracing at least $1.58M, and the detail that matters is that private keys never left devices, meaning your custody model did not save you. Separately, a wrapped Monero token cratered 99.8% in a suspected $13.5M breach, operator promising reimbursement, which is the oldest line in the book. None of these are market noise, they are drains in progress.

## Today's Move
- If you hold funds in Chainflip, do nothing hasty but do not attempt swaps. Wait for an official post-mortem before re-engaging, and watch the flagged Ethereum vault outflow address.
- If you used Fluidkey, revoke all approvals tied to that app immediately and move assets to a clean wallet. Opening the app was the trigger, so stop opening it.
- Exit any wrapped Monero (XMR wrapper) positions now. Do not wait on the operator's reimbursement promise, which is unsecured and non-binding.
- Builders using logging or telemetry tooling: audit what your client-side logging can trigger. Fluidkey proves an observability layer can become a transfer vector.
- Track the Binance-hack laundering (Elliptic reports $149M in BTC pushed through coinjoins since Nov. 17) if you run exchange or compliance flows.

## Resources

- https://thedefiant.io/news/security/chainflip-halts-swaps-over-potential-vault-exploit
- https://thedefiant.io/news/hacks/bitquery-traces-at-least-1-58-million-in-fluidkey-hack
- https://www.theblock.co/news/markets/2026-11-20-binance-hack-laundering-ramps-up-149-million-bitcoin-mixed-coinjoins-elliptic-444758
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [A French Bank Lost $133M Through Its Own Vendor's Account](/itsalreadypriced/2026/11/08/issue-019/)
- [Address Poisoning and Clipboard Malware](/itsalreadypriced/rtfm/2026/09/16/address-poisoning-and-clipboard-malware/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*