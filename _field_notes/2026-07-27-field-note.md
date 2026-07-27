---
layout: field_note
title: "Field Note â€” July 27, 2026"
date: 2026-07-27
summary: "SparkKitty photo-scraping malware and a fresh n8n sandbox escape land the same day Triple-A eats an $11.8M treasury breach, while BitMart withdrawals stall on the way out the door."
---

## Today's Field Note
Three things worth your attention, none of them the Strategy cash-reserve theater. Check Point documented SparkKitty, mobile malware hidden in apps that scans your photo library for seed phrase screenshots, which is exactly why your recovery words should never have been photographed in the first place. n8n patched a high-severity expression sandbox escape (CVE follows the February CVE-2026-27577 fix) that lets an authenticated workflow editor run OS commands as the n8n process, affecting versions below 2.31.5 and 2.32.0 to 2.32.1. Meanwhile Triple-A confirmed an $11.8M treasury wallet breach (claiming client funds untouched), and BitMart's wind-down withdrawals are visibly slowing as attributed wallets drop to roughly $69M. When an exchange announces a shutdown and then adds "compliance checks" to withdrawals, that is your cue, not a coincidence.

## Today's Move
- If you self-host n8n, upgrade to 2.31.5 or 2.32.1 now, and audit who has workflow-editor access. That role is now effectively shell access.
- Purge any seed phrase or private key screenshots from your phone's photo library and cloud photo backups today. SparkKitty is looking for exactly those.
- Get funds off BitMart immediately if you have any left. Withdrawals are already stalling and wallet balances are draining toward $69M.
- Audit apps installed from outside official stores and sideloaded APKs, since that is SparkKitty's delivery path. Uninstall anything unvetted with photo permissions.
- Watch the Triple-A situation before assuming your integration is safe. If you route payments through them, rotate any shared API keys and confirm the breach scope independently.

## Resources

- https://thehackernews.com/2026/07/n8n-sandbox-escape-lets-workflow.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Issue #002 — Week of July 12, 2026](/itsalreadypriced/2026/07/12/issue-002/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*