---
layout: field_note
title: "Field Note — September 09, 2026"
date: 2026-09-09
summary: "A self-hosted Lightning wallet flaw and an active Chrome zero-day are the only things worth your attention today."
---

## Today's Field Note
Alby disclosed a critical flaw in Alby Hub, its self-hosted Lightning wallet, affecting versions v1.7.0 through the current release. If you exposed your Hub to the internet, an attacker could take over the wallet and drain the bitcoin sitting in it. Separately, Google shipped a patch for CVE-2026-87491, an actively exploited out-of-bounds write in Chrome's V8 engine, the seventh Chrome zero-day patched this year and the browser most of you sign transactions from. Neither is a headline theft yet, but both put keys and signing surfaces directly in reach, which is the part that matters before it becomes a headline.

## Today's Move
- If you run Alby Hub on versions v1.7.0 or later, update immediately and pull it off any public-facing endpoint (bind it behind a VPN or Tor, not open ports).
- Assume an internet-exposed Hub is already compromised: move funds to a fresh wallet with new keys once patched.
- Restart Chrome on every machine to force the V8 patch, then confirm the build post-update. Do not sign transactions in an unpatched browser.
- Prefer a hardware wallet for signing today so a browser-level compromise cannot lift keys directly.
- Watch the CoinPal treasury wallet 0x22c8b4ce699db4fc9409eE6FC7A4ff4fBA7AEaD8 if you routed a payment through their gateway and never got credited.

## Resources

- https://thehackernews.com/2026/09/alby-hub-critical-flaw-could-let.html
- https://thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html
- https://www.bleepingcomputer.com/news/security/google-patches-seventh-chrome-zero-day-exploited-in-attacks-this-year/
- On-chain address: https://etherscan.io/address/0x22c8b4ce699db4fc9409eE6FC7A4ff4fBA7AEaD8
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*