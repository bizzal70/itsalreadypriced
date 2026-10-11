---
layout: field_note
title: "Field Note — October 11, 2026"
date: 2026-10-11
summary: "Ledger confirms a hardware implant in a reseller device with losses past $86M, while Coldcard's X account spat out a seed-phrase phishing link."
---

## Today's Field Note
Two hardware-wallet stories landed on the same day, and together they are the real signal. Ledger confirmed an "unauthorized hardware implant" in a device sold through Southeast Asian reseller CryptoBilis, with losses that may exceed $86M, and CryptoBilis has now paused all hardware wallet sales pending investigation. Separately, Coldcard's official X account posted a phishing link to a fake "migration" site built to harvest recovery phrases, and the company says it found no matching login record (meaning the compromise vector is still unexplained). The common thread is that your threat model cannot stop at "I bought a cold wallet." Supply chain tampering and hijacked official channels both bypass the device entirely and go straight for the seed.

## Today's Move
- If you bought a Ledger (or any hardware wallet) via CryptoBilis or any Southeast Asian reseller, treat it as compromised: generate a fresh seed on a known-good device and move funds to new addresses today.
- Ignore any "migration" or "update" link from the Coldcard X account or elsewhere. Coldcard does not need your recovery phrase, ever.
- Never type a 12/24-word seed into any website, full stop. Legitimate migrations happen on-device.
- Verify firmware and reseller provenance directly at coldcard.com and ledger.com, not via links in social posts.
- If you hold meaningful size on a device of uncertain provenance, assume the seed is known and rotate to a newly initialized wallet from a sealed, direct-from-manufacturer unit.

## Resources

- https://cointelegraph.com/news/ledger-confirms-unauthorized-hardware-implant-losses-may-exceed-86m?utm_source=rss_feed&utm_medium=rss_tag_hacks&utm_campaign=rss_partner_inbound
- https://thedefiant.io/news/hacks/ledger-says-affected-user-s-device-contained-hardware-implant
- https://thedefiant.io/news/security/coldcard-warns-of-phishing-post-on-its-official-x-account
- https://cointelegraph.com/news/coldcard-says-its-investigating-how-phishing-link-appeared-on-its-x-account?utm_source=rss_feed&utm_medium=rss_tag_hacks&utm_campaign=rss_partner_inbound
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*