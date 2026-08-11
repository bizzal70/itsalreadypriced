---
layout: field_note
title: "Field Note — August 11, 2026"
date: 2026-08-11
summary: "A Ravencoin block flaw, a drained BTCPay server, and a possibly insolvent BitMart converge on the same lesson: your funds are only as safe as the code and custodians holding them."
---

## Today's Field Note
Three separate reminders that "self-sovereign" has caveats. Ravencoin is weighing a rollback of roughly four days of transactions after a critical block flaw, meaning confirmations you treated as final may not be. BTCPay Server is offering a $190,000 bounty after an exploit drained bitcoin payment servers, so any merchant running self-hosted BTCPay should assume compromise until proven otherwise. And on the custodial side, OpenGradient's CEO alleges BitMart is insolvent and cannot process his market maker's withdrawals, with the exchange's founder denying misappropriation. Trading stops Aug 26 and withdrawal requests are due 05:00 UTC that day, which is the kind of timeline that tends to precede a gate slamming shut.

## Today's Move
- If you run self-hosted BTCPay Server, take it offline, rotate hot wallet keys, and move funds to a fresh wallet before patching. Assume your server was reachable.
- Treat any RVN deposits or settlements from the last four days as unconfirmed. Do not release goods or credit against them until the rollback question is resolved.
- If you hold anything on BitMart, submit a withdrawal request now rather than waiting for the Aug 26 deadline, and do not add new funds.
- Audit which merchant infrastructure exposes hot keys to the internet, and separate signing from any public-facing service.
- Watch onchain for the BTCPay drainer address and flag it in your monitoring before it filters through mixers.

## Resources

- https://www.coindesk.com/tech/2026/08/11/ravencoin-could-roll-back-four-days-of-transactions-after-critical-block-flaw
- https://www.coindesk.com/markets/2026/08/11/btcpay-offers-usd190-000-bounty-after-bitcoin-payment-servers-drained-in-exploit
- https://www.reddit.com/r/CryptoCurrency/comments/1vlgjet/opengradient_ceo_says_his_market_maker_cant/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Issue #002 — Week of July 12, 2026](/itsalreadypriced/2026/07/12/issue-002/)
- [The Week Bitcoin's Own Infrastructure Started Draining Itself](/itsalreadypriced/2026/08/09/issue-006/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*