---
layout: field_note
title: "Field Note — July 18, 2026"
date: 2026-07-18
summary: "Two live supply-chain campaigns (ViteVenom npm, OtterCookie SVG fake-interview lures) are hunting crypto wallets on developer machines right now."
---

## Today's Field Note
The developer laptop remains the softest target in crypto, and two campaigns confirmed today lean on it. Checkmarx flagged seven malicious npm packages ("ViteVenom") targeting the Vite frontend ecosystem, using a four-tier blockchain-based C2 (Tron among them) to deliver a RAT. Separately, North Korean actors tied to Contagious Interview are hiding a four-stage OtterCookie payload (browser credential and wallet stealer, file stealer) inside SVG files served through fake coding tests and job postings. Same theme running under it: Consensys disclosed it unknowingly outsourced MetaMask developer work to a DPRK-linked operator through a "reputable" third party. The attack surface is your build pipeline and your hiring funnel, not your cold wallet.

## Today's Move
- Audit recent npm installs for the seven ViteVenom packages; pin and lockfile your Vite dependencies, and treat any new frontend-tooling package added this week as suspect until verified.
- Never run a "coding challenge" repo or take-home project on a machine that touches keys or seed phrases. Use a disposable VM with no wallet extensions installed.
- Move signing keys and seeds off any dev box entirely. Hardware wallet or a dedicated air-gapped signer, not a browser extension on the same laptop you build on.
- If you hire contractors, verify identity independently and assume "reputable third-party provider" introductions can be DPRK fronts, as Consensys just learned.
- Rotate any browser-stored credentials and revoke token grants on machines that ran unvetted npm or GitHub projects recently.

## Resources

- https://thehackernews.com/2026/07/seven-malicious-vite-npm-packages-use.html
- https://thehackernews.com/2026/07/north-korea-linked-hackers-hide.html
- https://cointelegraph.com/news/consensys-north-korean-hacker-software-developer?utm_source=rss_feed&utm_medium=rss_tag_hacks&utm_campaign=rss_partner_inbound
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Field Note — July 17, 2026](/itsalreadypriced/field-notes/2026/07/17/field-note/)
- [Field Note — July 16, 2026](/itsalreadypriced/field-notes/2026/07/16/field-note/)
- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*