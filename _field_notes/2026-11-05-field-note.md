---
layout: field_note
title: "Field Note — November 05, 2026"
date: 2026-11-05
summary: "Binance pulls SignalPlus API access on a security scare, XRPL quietly patches a token-minting bug, and the Mercado Bitcoin hack ran for hours after 'contained.'"
---

## Today's Field Note
Three things worth your attention, none of them price action. Binance revoked SignalPlus API keys over a "potential security issue" at the options trading platform, and while Binance says its own systems and user funds are untouched, that is exactly the posture an exchange holds a week after losing $6.4 billion to North Korea. SignalPlus users were told to check positions and open orders directly on Binance and wait for a confirmed resolution before reconnecting, which means assume the keys are burned. Separately, XRP Ledger disclosed and fixed a bug that let approved token burners mint new tokens, the kind of supply-integrity flaw that is only boring until someone scripts it. And a fresh report shows the Mercado Bitcoin hack kept draining for hours after the exchange publicly called it contained, which is the lesson of the day about taking "resolved" at face value.

## Today's Move
- If you used SignalPlus, revoke and delete its Binance API keys now, then manually reconcile every open position and order inside Binance before trusting any dashboard.
- Generate fresh API keys with IP whitelists and trade-only (no withdrawal) permissions once SignalPlus confirms a full resolution, not before.
- XRPL node operators and issuers: upgrade to the patched rippled/validator build today and audit any authorized-burner permissions on your tokens.
- If you hold funds on Mercado Bitcoin, stay in view-only mode, do not rush withdrawals on the Nov. 9 reopening, and screenshot your balances now for the reimbursement claim.
- Audit all third-party trading tools and bots with exchange API access this week, killing any key that carries withdrawal rights.

## Resources

- https://thedefiant.io/news/security/binance-revokes-signalplus-api-keys-after-security-warning
- https://decrypt.co/382599/binance-cuts-off-signalplus-api-keys-over-potential-security-issue-at-trading-platform
- https://www.coindesk.com/markets/2026/11/05/xrp-ledger-closes-bug-that-let-approved-token-burners-create-new-tokens
- https://www.coindesk.com/business/2026/11/05/mercado-bitcoin-hack-continued-hours-after-exchange-said-attack-was-contained-report-finds
- https://thedefiant.io/news/hacks/mercado-bitcoin-plans-view-only-reopening-on-nov-9-after-hack
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [One Laptop, EIP-7702, and a $6.3B Hole at Binance](/itsalreadypriced/2026/11/01/issue-018/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*