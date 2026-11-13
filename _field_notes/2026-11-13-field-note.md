---
layout: field_note
title: "Field Note — November 13, 2026"
date: 2026-11-13
summary: "Unocoin freezes while attackers signed outside BitGo, Check Point patches an actively exploited root zero-day, and a second actor hits unpatched gateways with the TSGA backdoor."
---

Looking at the highest-signal operational items.


## Today's Field Note
Unocoin has halted deposits and withdrawals after transfers were signed outside BitGo's platform while its account was frozen, likely abusing a wallet recovery feature. Separately, Check Point shipped emergency hotfixes for a high-severity flaw that attackers have been exploiting since late October to grab root and persist on gateways, and a distinct actor is chaining the PHP2Shell flaws plus a new Gaia OS privilege-escalation bug to deploy a backdoor called TSGA and wipe ESXi files, with activity starting October 30 against Israeli organizations. These are not price-chart problems. The wallet-recovery angle at Unocoin is the one to watch, because recovery and co-signing features are exactly where custody assumptions quietly break. If you run Check Point gateways or route institutional flow through custodians, today is a patch-and-verify day.

## Today's Move
- Do not deposit to or withdraw from Unocoin until they publish a post-mortem and confirm the recovery vector is closed.
- If you run Check Point Security Gateways, apply the emergency hotfixes now and audit for root persistence and TSGA artifacts, especially boxes exposed since October 30.
- Check ESXi hosts behind Check Point gateways for wiped or missing files and restore from known-good backups if touched.
- Audit any custody setup that relies on wallet recovery or out-of-band signing (BitGo included), and disable recovery features you are not actively using.
- Watch the DOJ action on the North Korea Binance hack ($1.2B targeted, $2.7B frozen) and confirm none of your counterparty addresses overlap with the flagged clusters.

## Resources

- https://cointelegraph.com/news/unocoin-withdrawals-halted-bitgo-wallet-transfer-probe?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- https://www.bleepingcomputer.com/news/security/check-point-patches-zero-day-that-lets-hackers-get-root-access/
- https://thehackernews.com/2026/11/hackers-exploit-php2shell-flaws-in.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [A French Bank Lost $133M Through Its Own Vendor's Account](/itsalreadypriced/2026/11/08/issue-019/)
- [Exchange Custody, Counterparty Risk, and Proof of Reserves](/itsalreadypriced/rtfm/2026/09/09/exchange-custody-counterparty-risk-and-proof-of-reserves/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*