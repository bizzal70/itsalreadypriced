---
layout: field_note
title: "Field Note — September 04, 2026"
date: 2026-09-04
summary: "Trezor's shipping vendor breach widens by 67,000 US customers while a Chrome V8 zero-day is under active exploitation, both feeding straight into wallet-draining workflows."
---

## Today's Field Note
Two operational threats landed together today, and they compound. Trezor confirmed that the ShipMonk breach exposed another 67,000 US customers, with records from 2019 to 2021 (names, emails, phones, shipping addresses, order numbers), well past the 90-day retention its partner supposedly honored. That is a ready-made target list for hardware-wallet phishing and fake "device compromised, migrate your seed" lures. Separately, Google patched an actively exploited V8 type confusion zero-day (CVE-2026-85046) in Chrome, the same browser most people use to sign transactions. A malicious page plus an outdated Chrome is enough to hijack a session while you approve, so both of these hit the same soft spot: the human at the keyboard confirming a signature.

## Today's Move
- Update Chrome now to 152.0.7977.82 or later, then fully restart the browser to load the V8 patch. Do the same on any machine you use to sign.
- If you ever bought from Trezor, treat every email, SMS, or call referencing your order or device as hostile. Trezor will never ask for your seed, and no legitimate "migration" needs it.
- Enable and verify the passphrase (hidden wallet) feature on Trezor, so a leaked address list plus social engineering alone cannot reach your real funds.
- Sign transactions in a clean, dedicated browser profile with minimal extensions, and verify the destination address on the device screen, not the browser.
- Watch for spoofed sender domains mimicking trezor.io and shipmonk; confirm any support contact only through trezor.io typed by hand.

## Resources

- https://www.theblock.co/news/business/2026-09-04-trezor-says-shipmonk-breach-affected-another-67000-customers-413540
- https://thehackernews.com/2026/09/google-releases-chrome-update-to-patch.html
- https://www.bleepingcomputer.com/news/security/google-warns-of-new-chrome-zero-day-flaw-exploited-in-attacks/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*