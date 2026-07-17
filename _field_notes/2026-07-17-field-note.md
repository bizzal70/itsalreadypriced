---
layout: field_note
title: "Field Note — July 17, 2026"
date: 2026-07-17
summary: "A macOS Telegram-session stealer targets crypto wallets while ClickFix ACR Stealer harvests browser tokens, both trading on human clicks rather than broken cryptography."
---

## Today's Field Note
SlowMist has flagged macOS malware that hijacks Telegram sessions, decrypts local wallet files, and serves fake apps to phish recovery phrases. In parallel, The Hacker News documents ACR Stealer using ClickFix lures (paste-this-command-into-Run) to walk off with saved browser passwords, live session tokens, and OneDrive/SharePoint files. Neither breaks a cipher. Both rely on you executing something or trusting a session that is already stolen, which is exactly how the largest losses on record actually happen. If your keys, seed, or signing session live on the same machine you browse and Telegram on, treat that machine as hostile.

## Today's Move
- Move any real balance to a hardware wallet or an air-gapped signer today. Stop keeping seed phrases in plaintext, Notes, or synced cloud folders that ACR Stealer scrapes.
- Kill and reauthenticate all Telegram sessions (Settings, Devices, Terminate All Other Sessions), then enable a Telegram cloud password.
- Never paste a command into Run, Terminal, or a "verification" box because a site or "support" told you to. That is the entire ClickFix delivery chain.
- On macOS, audit installed apps for fake wallet or Telegram clones, and only reinstall wallets from official signed sources.
- Rotate browser-stored passwords and revoke live login tokens for any exchange or email that shares the infected device.

## Resources

- https://cointelegraph.com/news/macos-malware-crypto-investors-slowmist?utm_source=rss_feed&utm_medium=rss_tag_hacks&utm_campaign=rss_partner_inbound
- https://thehackernews.com/2026/07/acr-stealer-uses-clickfix-lures-to.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Field Note — July 16, 2026](/itsalreadypriced/field-notes/2026/07/16/field-note/)
- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Field Note — July 15, 2026](/itsalreadypriced/field-notes/2026/07/15/field-note/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*