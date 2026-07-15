---
layout: field_note
title: "Field Note — July 15, 2026"
date: 2026-07-15
summary: "Two live zero-days at SonicWall and a Cursor RCE that runs code the moment you open a repo, plus a poisoned @asyncapi npm chain."
---

## Today's Field Note
Three supply-chain and edge holes worth your morning. SonicWall confirms active exploitation of two SMA 1000 zero-days, CVE-2026-15409 (SSRF, CVSS 10.0) and a second flaw chaining to arbitrary command execution, which is exactly the kind of remote-unauth foothold that precedes treasury drains at desks running VPN appliances. Separately, Cursor on Windows will execute a git.exe sitting in a cloned repo's root with no prompt, meaning a malicious repo runs as you, with your SSH keys and cloud tokens, and keeps re-running for as long as the project is open. And four @asyncapi npm packages (generator@3.3.1, generator-helpers@1.1.1, generator-components@0.7.1, specs 6.11.2) were caught shipping a multi-stage botnet loader. Any builder who touches these this week is one clone or install away from a signer machine that is no longer yours.

## Today's Move
- Patch SonicWall SMA 1000 appliances now and pull them off the public internet until confirmed clean; review logs for SSRF and command-exec indicators.
- Pin @asyncapi away from generator@3.3.1, generator-helpers@1.1.1, generator-components@0.7.1, and specs 6.11.2 / 6.11.2-alpha.1; audit lockfiles and rebuild from a known-good state.
- Do not open untrusted repos in Cursor on Windows; disable auto-execution, and treat any recent clone as suspect until the git.exe behavior is confirmed patched.
- If any signing or deploy machine touched the above, rotate SSH keys, cloud tokens, and any hot wallet keys it held.
- Avoid Switcher.finance, reported non-delivery of swapped funds with a bot-farm promo network behind it.

## Resources

- https://thehackernews.com/2026/07/two-sonicwall-sma-1000-zero-days.html
- https://thehackernews.com/2026/07/cursor-flaw-lets-malicious-cloned.html
- https://thehackernews.com/2026/07/compromised-asyncapi-npm-packages.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*