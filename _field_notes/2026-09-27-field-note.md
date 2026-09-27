---
layout: field_note
title: "Field Note — September 27, 2026"
date: 2026-09-27
summary: "Two Citrix NetScaler zero-days are under active exploitation with no patch, and a compromised GitHub Actions supply-chain payload is still live."
---

## Today's Field Note
watchTowr disclosed two unpatched RCE zero-days in Citrix NetScaler ADC and NetScaler Gateway on September 26, already exploited in the wild, with no Citrix confirmation or fix. NetScaler sits in front of plenty of exchange, custody, and fund back-office infrastructure, so a pre-auth RCE here is a direct path to internal networks and, eventually, keys and treasury ops. Separately, two third-party GitHub Actions caught in the Mini Shai-Hulud campaign were re-enabled by their maintainer and left pointing at malicious code for over a week, meaning any CI pipeline that pinned to a tag (not a commit SHA) may have run the payload. Meanwhile ShinyHunters is bypassing WAF rules for Oracle PeopleSoft CVE-2026-35273 with simple URL-encoding, so any "mitigated but unpatched" server is back in scope. This is a supply-chain and edge-appliance week, not a market week. Treat your build system and your perimeter as compromised until proven otherwise.

## Today's Move
- If you run NetScaler ADC or Gateway, take it offline or restrict to VPN now (as some admins already have), since there is no patch. Watch for it.
- Audit every GitHub Actions workflow: replace any `uses:` tag reference with a full pinned commit SHA, and rotate any secret exposed to CI in the last two weeks.
- Rotate deploy keys, npm/PyPI tokens, and cloud credentials that lived in your Actions environment during the Mini Shai-Hulud window.
- If you have Oracle PeopleSoft exposed, apply the actual CVE-2026-35273 patch. WAF-only mitigation is now bypassed via URL-encoding.
- Cold-wallet operators: assume any signing machine reachable from the corporate network is downstream of these edges, and verify offline signing paths still hold.

## Resources

- https://thehackernews.com/2026/09/warning-two-unpatched-citrix-netscaler.html
- https://www.bleepingcomputer.com/news/security/github-actions-re-enabled-with-mini-shai-hulud-payload-still-active/
- https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Issue #002 — Week of July 12, 2026](/itsalreadypriced/2026/07/12/issue-002/)
- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*