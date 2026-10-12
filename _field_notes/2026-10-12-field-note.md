---
layout: field_note
title: "Field Note — October 12, 2026"
date: 2026-10-12
summary: "Ledger's CryptoBilis supply-chain implant spreads to the EU, an XRP overflow bug nearly minted 18 trillion coins, and a maxed-out GitLab RCE lands."
---

## Today's Field Note
The CryptoBilis story is no longer a Southeast Asia footnote. Bitquery now traces up to $93.2 million drained across six chains, with only $10 million frozen, and a user reports a hardware implant in a Ledger bought from a mainstream European retailer. The implant leaves the secure chip intact, so Ledger's own Genuine Check cannot flag it, which means "it passed verification" tells you nothing. Separately, the XRP Ledger shipped an emergency patch for a decade-old overflow bug that could have minted roughly 18 trillion spendable XRP in a single transaction, and GitLab disclosed a CVSS 10.0 RCE in its CI/CD regex compiler that lets remote attackers run code on your instance. Two of these are supply-chain and build-pipeline problems, which are exactly the vectors drainers prefer.

## Today's Move
- If you bought a Ledger from CryptoBilis or any reseller (now including EU retail), treat the device as compromised: move funds to a wallet generated on a known-clean device and abandon the old seed.
- Do not rely on Ledger Genuine Check as proof of safety for implant-class tampering. Only trust devices bought directly from Ledger, factory-sealed.
- Patch GitLab now against the CI/CD Regular Expression Compiler RCE, and audit runner logs for unexpected code execution since the disclosure.
- Confirm your XRPL node or validator is on the patched rippled build covering the 18 trillion XRP overflow fix before processing further payments.
- Watch the frozen CryptoBilis-linked wallets and the remaining ~$83M in motion across the six chains before signing anything touching counterparties in that flow.

## Resources

- https://thedefiant.io/news/hacks/bitquery-says-10-million-frozen-in-cryptobilis-linked-wallet-drains
- https://thedefiant.io/news/security/ledger-user-reports-hardware-implant-in-wallet-bought-in-europe
- https://www.bleepingcomputer.com/news/security/gitlab-warns-of-max-severity-rce-flaw-in-regex-compiler-engine/
- https://www.theblock.co/news/ecosystems/2026-10-11-xrp-ledger-patches-decade-old-bug-that-could-have-minted-trillions-of-xrp-418230
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [A Hardware Implant in a Ledger Cost Users $86M](/itsalreadypriced/2026/10/11/issue-015/)
- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Coldcard Ships Firmware After $114M Bitcoin Theft](/itsalreadypriced/2026/08/23/issue-008/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*