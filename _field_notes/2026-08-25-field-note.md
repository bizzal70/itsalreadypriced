---
layout: field_note
title: "Field Note — August 25, 2026"
date: 2026-08-25
summary: "Galaxy pegs Coldcard hack at 1,789 BTC, and a max-severity Oracle WebLogic bug is under active exploitation."
---

## Today's Field Note
Galaxy Research tallied the Coldcard hardware wallet compromise at 1,789 BTC across 221 victim reports, with more than half losing over 1 BTC each and 87% of the stolen coins still unmoved. Unmoved does not mean safe, it means the thief is patient or laundering slowly, so the on-chain clock is running for anyone still on a compromised seed. Separately, CISA added Oracle WebLogic and HTTP Server flaw CVE-2026-21962 (CVSS 10.0) to its Known Exploited Vulnerabilities catalog: unauthenticated network access to critical data, already being exploited in the wild. If any of your infra, custody backend, or exchange integrations touch WebLogic, you are exposed today, not eventually.

## Today's Move
- If you hold a Coldcard from the affected batches, treat the seed as burned: generate a fresh seed on a verified device and sweep funds to a new address now.
- Cross-check your Coldcard firmware version and provenance against Galaxy's report before trusting any existing balance.
- Patch or take offline any Oracle WebLogic or Oracle HTTP Server instance for CVE-2026-21962 immediately, then hunt logs for unauthenticated HTTP access to sensitive endpoints.
- Builders: audit whether any custody, KYC, or settlement service in your stack runs WebLogic, and rotate any secrets that box could have exposed.
- Watch the flagged Coldcard thief clusters for the 87% that has not yet moved, and set alerts on your own historical deposit addresses.

## Resources

- https://cointelegraph.com/news/coldcard-hack-galaxy-btc-lost-87-unmoved?utm_source=rss_feed&utm_medium=rss_tag_hacks&utm_campaign=rss_partner_inbound
- https://thehackernews.com/2026/08/actively-exploited-oracle-weblogic-flaw.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [A 2021 PRNG Bug Drained $89M From Coldcard Wallets in 41 Minutes](/itsalreadypriced/2026/08/02/issue-005/)
- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*