---
layout: field_note
title: "Field Note — July 29, 2026"
date: 2026-07-29
summary: "Two live software supply-chain compromises plus an Apple-listed fake wallet that drained $1.8M, all pointing at the same failure mode: trusting the store."
---

## Today's Field Note
Three items worth your attention, all the same lesson. Two npm packages in the @joyfill namespace (@joyfill/layouts@0.1.2-2773.beta.0 and @joyfill/components@4.0.0-rc24-2773-beta.4) were compromised to run a DEV#POPPER-family RAT at import time, meaning a build step is enough to own your machine. Separately, Gitea shipped a fix for CVE-2026-60004 (CVSS 9.8), where anyone with plain repo write access can plant a Git hook and get shell as the service account; anything below 1.27.1 is exposed. And a lawsuit alleges Apple ranked a fake Sparrow Wallet app inside its own curated crypto collections, where it drained $1.8M in BTC, a reminder that "featured in the store" is not a security guarantee on any platform.

## Today's Move
- Pin and audit @joyfill dependencies now; if you pulled the beta builds above, treat the build host as compromised, rotate any keys or tokens it touched, and rebuild clean.
- Upgrade self-hosted Gitea to 1.27.1 immediately, and review repo write access plus recent Git hook changes for anything you did not create.
- Verify wallet software by signature and project domain, never by App Store or Play Store ranking; download Sparrow only from sparrowwallet.com and check the PGP sig.
- For any signer machine tied to funds, assume store-ranked apps can be impostors and keep signing keys on hardware, offline.
- Watch your CI logs for unexpected outbound connections at install or import time, not just at runtime.

## Resources

- https://thehackernews.com/2026/07/two-compromised-joyfill-npm-packages.html
- https://thehackernews.com/2026/07/new-gitea-rce-lets-repository-writers.html
- https://decrypt.co/374628/apple-sued-after-fake-iphone-wallet-app-drained-1-8m-in-bitcoin
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Issue #002 — Week of July 12, 2026](/itsalreadypriced/2026/07/12/issue-002/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*