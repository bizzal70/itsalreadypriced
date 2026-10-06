---
layout: field_note
title: "Field Note — October 06, 2026"
date: 2026-10-06
summary: "ZachXBT fronted $349,700 to infiltrate a Chinese laundering network moving Lazarus funds, and two self-hosted tooling flaws (Atlassian, LibreOffice) give attackers quiet code and file access."
---

## Today's Field Note
ZachXBT disclosed he posed as a client and personally fronted $349,700 to infiltrate a Chinese network that laundered over $1B for Lazarus, including proceeds from the $1.5B Bybit hack, intelligence that helped freeze funds. The takeaway is not the drama, it is the plumbing: Lazarus still runs through Chinese OTC and laundering desks, and your counterparties on P2P and OTC may be sitting downstream of tainted flow. Separately, Atlassian disclosed CVE-2026-21589 (CVSS 9.3) on October 5, letting unauthenticated attackers read known files across eight self-hosted Data Center products, and researchers showed LibreOffice and OpenOffice can run attacker code on file-open when Java is enabled. If you self-host Confluence, Jira, or Bitbucket, or open spreadsheets from strangers, you are the attack surface today.

## Today's Move
- Patch all self-hosted Atlassian Data Center products (Confluence, Jira, Bitbucket) against CVE-2026-21589 now, and rotate any secrets stored in web app root paths.
- Disable Java support in LibreOffice and OpenOffice (Tools, Options, Advanced) and treat unsolicited .ods/.xlsx files as hostile.
- If you run OTC or P2P desks, screen incoming addresses against the Bybit hack cluster and ZachXBT's published tags before settling.
- Re-check that signing keys and treasury multisigs are not reachable from any machine that opens untrusted documents.
- Watch for frozen-fund followups on the Lazarus laundering network and avoid counterparties routing through flagged Chinese OTC desks.

## Resources

- https://www.theblock.co/news/defi/2026-10-06-zachxbt-infiltrated-chinese-launderers-lazarus-hack-417767
- https://thehackernews.com/2026/10/critical-atlassian-flaw-lets.html
- https://thehackernews.com/2026/10/libreoffice-and-openoffice-flaws-let.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Issue #002 — Week of July 12, 2026](/itsalreadypriced/2026/07/12/issue-002/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Bitget Loses $388M to Spoofed Transfers, Not Stolen Keys](/itsalreadypriced/2026/09/27/issue-013/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*