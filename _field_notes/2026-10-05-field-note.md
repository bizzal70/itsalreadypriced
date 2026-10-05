---
layout: field_note
title: "Field Note — October 05, 2026"
date: 2026-10-05
summary: "Treasury exposes a $2M Hamas crypto fundraising network, and a Citrix NetScaler zero-day is under active exploitation."
---

## Today's Field Note
Two items clear the noise today, and neither is price action. Treasury's OFAC unwound a crypto-denominated Hamas fundraising network moving roughly $2 million, another reminder that stablecoin and on-chain rails remain traceable and that interacting with freshly sanctioned addresses is a compliance landmine. Separately, Citrix patched CVE-2026-88779, a NetScaler ADC and Gateway memory overflow already exploited as a zero-day in targeted attacks, with researchers still probing whether it extends from denial-of-service to remote code execution. If your exchange, custody desk, or node infrastructure sits behind NetScaler for SAML auth, that is your perimeter and it is being hit now.

## Today's Move
- Patch NetScaler ADC and Gateway immediately for CVE-2026-88779, then kill active sessions and rotate SAML signing credentials, since DoS may not be the ceiling here.
- Audit any wallet or treasury flow against the latest OFAC SDN additions from the Hamas network action before you move funds.
- If you run institutional custody behind Citrix, pull auth logs for anomalous SAML sessions over the past week and assume compromise until proven otherwise.
- Screen counterparty and deposit addresses with an updated sanctions list, not a cached one from last month.
- Do not touch tagged addresses to "test" them. On-chain interaction with sanctioned wallets is itself the exposure.

## Resources

- https://www.coindesk.com/policy/2026/10/05/treasury-crackdown-exposes-crypto-s-role-in-usd2-million-hamas-fundraising-network
- https://www.bleepingcomputer.com/news/security/citrix-patches-netscaler-saml-zero-day-exploited-in-attacks/
- https://thehackernews.com/2026/10/new-netscaler-zero-day-exploited-in.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [A 2021 PRNG Bug Drained $89M From Coldcard Wallets in 41 Minutes](/itsalreadypriced/2026/08/02/issue-005/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Issue #002 — Week of July 12, 2026](/itsalreadypriced/2026/07/12/issue-002/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*