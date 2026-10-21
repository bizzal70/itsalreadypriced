---
layout: field_note
title: "Field Note — October 21, 2026"
date: 2026-10-21
summary: "The Drift exploiter is laundering through Tornado Cash in size, and there is a PHP RCE patch landing today that anyone running a node or backend should treat as urgent."
---

## Today's Field Note
Wallets tied to April's $295M Drift exploit have pushed $109M in ETH through Tornado Cash over two days, including another $46M on Wednesday, with roughly $138M in ETH still sitting in attacker-controlled addresses. That is not a rumor or a reorg risk, it is active laundering of stolen funds, which means tainted ETH is entering circulation now. Separately, PHP shipped an out-of-cycle fix at 14:00 UTC for two critical RCE flaws (CVSS 9.2) dubbed PHP2Shell, and the widely shared workaround was disowned by the firm that suggested it. If you run any PHP-facing infrastructure (RPC proxies, dashboards, webhook endpoints, exchange or wallet backends), the only real mitigation is the patch.

## Today's Move
- Patch PHP today. Pull the official out-of-cycle release and update every PHP-facing service (node proxies, admin panels, webhook receivers). Do not rely on the config-only workaround, the vendor retracted it.
- Flag Drift exploiter addresses in your compliance and treasury screening. Expect freshly mixed ETH from Tornado Cash exits and tag inbound deposits accordingly.
- If you operate an exchange or custodian, review ETH deposits for post-mixer provenance over the coming days rather than assuming clean history.
- Audit UpdraftPlus/UpdraftCentral installs on any WordPress property you own. TeamUpdraft's connection keys were compromised and used to backdoor sites, so rotate keys and check for unexpected admin users.
- If you run SSH over Tor, assume October 1 to 5 password logins were intercepted via hijacked exit relays. Rotate those credentials and move to key-based auth.

## Resources

- https://cointelegraph.com/news/drift-exploiter-moves-109m-eth-tornado-cash-2-days?utm_source=rss_feed&utm_medium=rss_tag_hacks&utm_campaign=rss_partner_inbound
- https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html
- https://thehackernews.com/2026/10/php2shell-what-actually-protects-you.html
- https://thehackernews.com/2026/10/attackers-abuse-updraftcentral-keys-to.html
- https://thehackernews.com/2026/10/attackers-hijacked-over-300-tor-exit.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Exchange Custody, Counterparty Risk, and Proof of Reserves](/itsalreadypriced/rtfm/2026/09/09/exchange-custody-counterparty-risk-and-proof-of-reserves/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Field Note — October 20, 2026](/itsalreadypriced/field-notes/2026/10/20/field-note/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*