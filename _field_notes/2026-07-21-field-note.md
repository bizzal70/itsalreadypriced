---
layout: field_note
title: "Field Note — July 21, 2026"
date: 2026-07-21
summary: "A hijacked npm package, live PAN-OS and ServiceNow exploitation, and WordPress wp2shell mean the machines your keys live on are the actual attack surface today."
---

## Today's Field Note
The signal today is not a protocol drain, it is the plumbing under your keys. A widely used npm package was hijacked this month and shipped an infostealer that sweeps browser sessions, password vaults, software wallets, seed phrases, and AI coding tool configs from whatever machine runs it. Meanwhile Qilin is actively exploiting the critical PAN-OS GlobalProtect auth bypass, ServiceNow's AI Platform sandbox escape (CVE-2026-6875, CVSS 9.5) is under in-the-wild exploitation for unauthenticated RCE, and WordPress wp2shell (CVE-2026-63030 plus CVE-2026-60137) is being mass-scanned into full site compromise. None of this cares about your Ledger. All of it cares about the laptop you signed with last, the CI pipeline that pulls dependencies, and the VPN in front of your infra.

## Today's Move
- Audit your npm dependency tree today for the hijacked package, pin exact versions, and rebuild from a clean lockfile. Assume any seed phrase or software wallet on a build or daily-driver machine is already burned, and rotate it.
- Move signing to an offline device. If you signed a real transaction from a browser-connected hot wallet this week, migrate funds to freshly generated hardware keys.
- If you run PAN-OS GlobalProtect, patch the auth bypass now and hunt for Qilin indicators, do not just deploy and walk away.
- Patch ServiceNow AI Platform for CVE-2026-6875 immediately, it is unauthenticated RCE under active exploitation.
- If you host anything on WordPress, patch CVE-2026-63030 and CVE-2026-60137 (wp2shell) and check for web shells, exploitation was live by Saturday morning UTC.

## Resources

- https://www.reddit.com/r/CryptoCurrency/comments/1v2bwp9/a_reminder_from_this_months_npm_supplychain_hit/
- https://www.bleepingcomputer.com/news/security/critical-globalprotect-vpn-bug-now-exploited-in-ransomware-attacks/
- https://thehackernews.com/2026/07/critical-servicenow-ai-platform-flaw.html
- https://thehackernews.com/2026/07/wordpress-wp2shell-exploitation-grows.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Field Note — July 20, 2026](/itsalreadypriced/field-notes/2026/07/20/field-note/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Field Note — July 19, 2026](/itsalreadypriced/field-notes/2026/07/19/field-note/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*