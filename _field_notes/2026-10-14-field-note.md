---
layout: field_note
title: "Field Note — October 14, 2026"
date: 2026-10-14
summary: "Ledger halts Asian resales over device tampering while a curl client-side RCE and an Ivanti zero-day hit the tooling builders actually run."
---

## Today's Field Note
Ledger has asked resellers across Southeast Asia and Hong Kong to pull devices off shelves while investigators trace where hardware implants are entering the supply chain, even through authorized sellers. That is the quiet part of the threat model made loud: the box can be compromised before you ever touch it, and a tampered secure element defeats every careful seed phrase habit you have. Separately, the curl project shipped 8.23.0 on October 14 fixing an HTTP/2 upload flaw that lets a malicious server corrupt client memory and, in the right build, run code on the uploading machine, which matters because curl is buried in half the deploy scripts and nodes you operate. And CISA flagged an actively exploited Ivanti Connect Secure auth bypass (CVE-2026-104935) with honeypots logging 105 exploit attempts since October 1. None of these are market noise. They are the plumbing under your keys and infra.

## Today's Move
- If you bought a Ledger from an Asian reseller recently, do not initialize it with real funds. Verify genuineness via Ledger Live attestation, and treat any pre-set or pre-filled seed as a theft trap.
- Upgrade curl to 8.23.0 everywhere, including CI runners, Docker base images, signing scripts, and any node tooling that pipes uploads over HTTP/2.
- Patch Ivanti Connect Secure immediately if you run it for ops or team VPN access, then review logs for compromise since October 1.
- For high-value cold storage, generate and verify seeds on a device you can attest, or move to a multisig so a single tampered unit cannot drain you.
- Watch Ledger's official channels for the tampering disclosure before trusting any new hardware purchase this week.

## Resources

- https://thehackernews.com/2026/10/curl-patches-http2-upload-flaw-after.html
- https://www.bleepingcomputer.com/news/security/cisa-warns-admins-to-immediately-fix-ivanti-flaw-exploited-as-zero-day/
- https://thehackernews.com/2026/10/cisa-urges-immediate-ivanti-connect.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Upgradeable Contracts and the Admin Key Problem](/itsalreadypriced/rtfm/2026/08/12/upgradeable-contracts-and-the-admin-key-problem/)
- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*