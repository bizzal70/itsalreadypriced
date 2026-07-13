---
layout: field_note
title: "Field Note — July 13, 2026"
date: 2026-07-13
summary: "CISA flags two 10.0-severity Joomla zero-days under active exploitation while three Microsoft 365 phishing kits surface, a bad week for anyone with credentials worth stealing."
---

## Today's Field Note
Two things worth your attention today, neither of them a chart. CISA added CVE-2026-48939 (iCagenda) and a companion Balbooa Forms flaw to its Known Exploited Vulnerabilities catalog, both rated 10.0 and both being exploited in the wild against Joomla sites. Separately, the Microsoft 365 attack surface is lighting up: a new PhaaS called Forg365 ($400/month over Telegram) is running device-code phishing and adversary-in-the-middle session theft, and a misconfigured operator server let Lexfo lift the toolkits behind three more Evilginx M365 campaigns. If your treasury ops, multisig coordination, or team comms live behind a Microsoft 365 tenant, that is the door being kicked at. Session-token theft walks straight past your password and often past basic MFA.

## Today's Move
- Patch or take offline any Joomla instance running iCagenda or Balbooa Forms today. These are 10.0 CVEs already being hit, not theoretical.
- Move every M365 account tied to funds or infra to phishing-resistant MFA (FIDO2 hardware keys or passkeys). Device-code and AitM attacks defeat SMS and TOTP.
- In Entra ID, disable device code flow where you do not explicitly need it, and set Conditional Access to require compliant devices.
- Revoke active M365 sessions for privileged accounts and force reauth. Evilginx and Forg365 steal live session tokens, so a password reset alone does not evict them.
- Audit mailbox rules and OAuth app grants on treasury and admin accounts for post-compromise persistence (auto-forwarding, hidden inbox rules).

## Resources

- https://thehackernews.com/2026/07/icagenda-and-balbooa-forms-joomla-flaws.html
- https://thehackernews.com/2026/07/forg365-phaas-targets-microsoft-365.html
- https://thehackernews.com/2026/07/misconfigured-server-reveals-three.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)
