---
layout: field_note
title: "Field Note — August 18, 2026"
date: 2026-08-18
summary: "BitBox and SafePal both cough up hardware wallet trouble on the same day, one firmware, one data leak."
---

## Today's Field Note
Two hardware wallet vendors bled on the same day, and neither leak is theoretical. BitBox patched "severe" firmware flaws (fix shipped in version 9.26.5) that it says could put funds at risk, though it reports no known exploitation yet. SafePal separately disclosed that an authorization flaw in an order-tracking plug-in exposed names, emails, phone numbers, shipping addresses, and purchase details for roughly 39,798 customers, notified individually on August 16 from security@safepal.com. Firmware bugs threaten your keys, but the SafePal leak is the more durable problem: a list of confirmed hardware wallet owners with home addresses is exactly the targeting data that fuels physical coercion and tailored phishing. Assume that list is already circulating.

## Today's Move
- If you run a BitBox02, update to firmware 9.26.5 today, and verify the version on-device rather than trusting the app prompt.
- SafePal owners: treat any "order," "shipping," or "security update" email as hostile, especially ones matching your real address. Confirm the security@safepal.com notice only via the official site, never via links.
- Given the address leak, review your physical operational security: reduce single-device seed exposure and consider a passphrase (25th word) that never touched the vendor.
- Watch for SIM-swap and voice-phishing attempts tied to the leaked phone numbers. Move exchange and email 2FA off SMS if you have not.
- Builders shipping order-tracking or support plug-ins: audit authorization on every object-level endpoint now. This was an IDOR-class failure, not exotic.

## Resources

- https://thehackernews.com/2026/08/safepal-hardware-wallet-maker-says-flaw.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [The Week Your Trezor Order Became a Home Address](/itsalreadypriced/2026/08/16/issue-007/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*