---
layout: field_note
title: "Field Note — September 21, 2026"
date: 2026-09-21
summary: "A Fetch.ai/NuNet $2M exploit, a WaterPlum developer-malware campaign, and live npm supply-chain abuse all point at the same target this week: builders."
---

## Today's Field Note
Three separate items converge on developers as the soft underbelly. Fetch.ai and NuNet were drained for roughly $2 million by the same attacker, hitting two connected projects in one sweep. Meanwhile North Korea's WaterPlum group ran fake recruiter lures that infected at least 30,000 devices across 100+ countries and pulled $10.7M, the same playbook Jade Sleet is running against an Indian IT provider with FLATROOF and ROOFDECK backdoors. Layer on the live npm campaign around the 'indexed-btree' package, which hides its payload in runtime behavior to slip past install-script scanners, and the pattern is clear. The attack surface this week is your machine and your dependency tree, not your wallet UI.

## Today's Move
- If you touch Fetch.ai or NuNet contracts or LPs, exit and revoke approvals now via Etherscan/revoke.cash until the post-mortem lands.
- Audit any npm project for 'indexed-btree' and pin/lock dependencies. Runtime-based payloads defeat install-script blocking, so review actual package behavior, not just lifecycle hooks.
- Treat every unsolicited recruiter, coding test, or "run this repo" request as WaterPlum until proven otherwise. Run it in a disposable VM, never on a key-bearing machine.
- Move signing keys off any dev box that has cloned unknown repos or run a "job interview" project. Assume that box is compromised.
- Enable hardware-key 2FA on GitHub, npm, and exchange accounts, and rotate npm tokens if you publish packages.

## Resources

- https://www.reddit.com/r/CryptoCurrency/comments/1wlww2j/fetchai_and_nunet_exploited_for_2_million_by_same/
- https://cointelegraph.com/news/north-korean-fake-recruiters-infect-30k-devices-steal-107m-in-crypto?utm_source=rss_feed&utm_medium=rss_tag_hacks&utm_campaign=rss_partner_inbound
- https://www.bleepingcomputer.com/news/security/malicious-npm-packages-evade-install-script-defenses-at-runtime/
- https://thehackernews.com/2026/09/jade-sleet-linked-to-indian-it-provider.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [North Korea's WaterPlum Drains 30,000 Devices for $10.7M](/itsalreadypriced/2026/09/20/issue-012/)
- [Issue #002 — Week of July 12, 2026](/itsalreadypriced/2026/07/12/issue-002/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*