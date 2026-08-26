---
layout: field_note
title: "Field Note — August 26, 2026"
date: 2026-08-26
summary: "Active exploitation of a critical Gitea RCE (CVE-2026-60004) and a second unsafe-deserialization pair in Kaltura's mwEmbed threaten the self-hosted infrastructure crypto teams quietly run."
---

## Today's Field Note
CISA confirmed active exploitation of CVE-2026-60004, a 9.8 RCE in Gitea that lets anyone with ordinary write access to a repo run shell commands as the Gitea user, with reported attacks already dropping miner-like payloads. Plenty of crypto teams self-host Gitea for contracts, deploy scripts, and CI secrets, so a compromised instance is a straight line to your keys and pipeline, not just your source. Separately, CERT/CC disclosed two unpatched flaws in Kaltura's mwEmbed player (CVE-2026-19913 and CVE-2026-19912), both arbitrary file read plus RCE via the mwEmbedLoader.php endpoint, with no vendor fix yet. Neither is a flashy onchain drain, but self-hosted infra is where quiet drains begin. Patch the boring boxes before someone else audits them for you.

## Today's Move
- Patch every self-hosted Gitea instance to the fixed release immediately, then check logs for unexpected shell processes and outbound connections since disclosure.
- Rotate any deploy keys, CI/CD tokens, signing keys, and .env secrets that ever touched a Gitea or CI runner you cannot prove is clean.
- Restrict repo write access to a minimum and put Gitea behind a VPN or IP allowlist rather than the open internet.
- If you run Kaltura mwEmbed, take the mwEmbedLoader.php endpoint offline or block it at the WAF until a patch ships (CVE-2026-19913, CVE-2026-19912).
- Audit build servers and runners for miner-like processes and unauthorized cron jobs, then treat any compromised host as fully burned.

## Resources

- https://thehackernews.com/2026/08/critical-gitea-rce-actively-exploited.html
- https://www.bleepingcomputer.com/news/security/hackers-now-exploit-critical-gitea-flaw-in-code-injection-attacks/
- https://thehackernews.com/2026/08/unpatched-kaltura-mwembed-flaws-could.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [A 2021 PRNG Bug Drained $89M From Coldcard Wallets in 41 Minutes](/itsalreadypriced/2026/08/02/issue-005/)
- [Upgradeable Contracts and the Admin Key Problem](/itsalreadypriced/rtfm/2026/08/12/upgradeable-contracts-and-the-admin-key-problem/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*