---
layout: field_note
title: "Field Note â€” July 25, 2026"
date: 2026-07-25
summary: "A North Korean phishing kit fingerprints your wallet before it drops malware, while Fastjson 1.x eats unauthenticated RCE with no patch in sight."
---

## Today's Field Note
Two operational threats worth your attention today. BlueNoroff (the DPRK crew) is running an active ClickFix-style phishing kit that impersonates Zoom and Microsoft Teams via typosquatted domains, and notably profiles browser wallet extensions before deciding whether to deliver malware. Translation: they qualify targets by what they can steal, so anyone joining a "recruiter" or "investor" call over a slightly-wrong Zoom link is being scoped in real time. Separately, CVE-2026-16723 is an unauthenticated RCE in Fastjson 1.x (Alibaba's Java JSON library), CVSS 9.0, actively exploited per ThreatBook and Imperva, with no patch available. If your backend, bridge relayer, or exchange infra runs Spring Boot with Fastjson 1.x, a single crafted JSON request runs code as your Java process.

## Today's Move
- Never join a video call from a link sent by a new contact. Type zoom.us or teams.microsoft.com manually, and reject any "update this client" prompt outright.
- Move active trading funds off browser-extension wallets onto a hardware signer today. BlueNoroff is specifically enumerating wallet extensions before payload delivery.
- Inventory every Java service for Fastjson 1.x. Since no patch exists, migrate to Fastjson2 in safeMode or rip it out for a maintained parser (Jackson, Gson).
- Block outbound egress from Spring Boot hosts to untrusted destinations to break the RCE fetch stage until you can remediate.
- Watch for typosquatted Zoom/Teams domains in your org DNS logs and null-route them.

## Resources

- https://thehackernews.com/2026/07/bluenoroff-zoom-phishing-kit-profiles.html
- https://thehackernews.com/2026/07/fastjson-1x-rce-vulnerability-targeted.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Issue #002 — Week of July 12, 2026](/itsalreadypriced/2026/07/12/issue-002/)
- [Signature Requests and Blind Signing](/itsalreadypriced/rtfm/2026/07/22/signature-requests-and-blind-signing/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*