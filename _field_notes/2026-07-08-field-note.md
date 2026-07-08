---
layout: field_note
title: "Field Note — July 08, 2026"
date: 2026-07-08
summary: "A signed-commit forgery in GitHub's 'Verified' badge and a batch of actively exploited max-severity flaws (ColdFusion, Langflow, UniFi) are the real hazards today; the market noise is just oil."
---

## Today's Field Note
The board-moving item for builders is quiet: new research shows a signed Git commit's hash is not unique, so anyone can mint a second commit with identical files, author, and date that still carries a valid signature and GitHub's "Verified" stamp. For anyone shipping smart contracts or wallet software, "Verified" now means less than you assumed, and supply-chain review that trusts that badge is doing nothing. Meanwhile CISA added four actively exploited flaws to KEV, including CVE-2026-48282 (Adobe ColdFusion, CVSS 10.0) and the Langflow auth bypass, with a Friday federal patch deadline, plus a max-severity UniFi OS command injection from Ubiquiti. The BTC drop to $62k on the Iran ceasefire collapse and Strategy's 3,588 BTC sale are just weather. Patch the machines that hold your keys and pipelines.

## Today's Move
- Stop trusting GitHub's "Verified" badge as proof of integrity; pin and verify dependencies by commit hash plus known-good key fingerprints, not the green check.
- Patch Adobe ColdFusion now (CVE-2026-48282, CVSS 10.0) if any internal tooling or dashboards run it; assume active exploitation.
- Update Langflow immediately if you run AI-agent infra behind it; the auth bypass is on CISA's KEV and being exploited.
- Apply Ubiquiti's UniFi OS updates for the seven critical flaws, including the max-severity command injection, on any gateway near sensitive infra.
- Ignore the Strategy sale and oil-driven BTC dip for operational decisions; no key rotation needed on price alone.

## Resources

- https://thehackernews.com/2026/07/github-verified-commits-can-be.html
- https://thehackernews.com/2026/07/cisa-adds-4-actively-exploited-adobe.html
- https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-prioritize-patching-langflow-auth-bypass-flaw/
- https://www.bleepingcomputer.com/news/security/ubiquiti-warns-of-new-max-severity-unifi-os-vulnerability/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)
