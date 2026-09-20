---
layout: field_note
title: "Field Note — September 20, 2026"
date: 2026-09-20
summary: "A live iOS full-chain exploit is draining wallet keys from Safari, and North Korea's WaterPlum moved $10.7M in stolen crypto."
---

## Today's Field Note
SlowMist's 23pds is warning that attackers have operationalized a full-chain iOS exploit that runs from a malicious Safari page straight through WebKit/JSC memory corruption, a PAC bypass, sandbox escape, and kernel privilege escalation to root, ending in a clean sweep of device Keychains and local wallet app data. This is a zero-interaction path from "you clicked a link" to "your seed is gone," and it spans iOS 13 through 26.5, so most hot-wallet users on iPhone are in scope. Separately, a joint law enforcement advisory confirms North Korea's WaterPlum compromised at least 30,000 devices between December 2025 and July 2026 and funneled over $10.7M in stolen crypto home, a reminder that the endpoint, not the contract, is the soft target this cycle. Nothing here is theoretical. Both are being used right now.

## Today's Move
- Update every iPhone and iPad to the latest iOS today, before anything else. Anything on 13 through 26.5 unpatched is exposed.
- Treat any seed phrase that has ever touched an iPhone as potentially compromised. If a device may have hit a bad Safari page, migrate funds to a freshly generated wallet on hardware.
- Move meaningful balances off mobile hot wallets to a hardware signer (Ledger, Trezor) where keys never leave the device.
- Stop opening wallet-related links in Safari from DMs, airdrop pitches, or "support" contacts. Watering-hole and social engineering are the delivery vector here.
- Enable Lockdown Mode on iOS for any device holding real crypto value. It kills much of the WebKit attack surface this exploit relies on.

## Resources

- https://www.reddit.com/r/CryptoCurrency/comments/1wkua95/every_iphone_user_should_update_their_ios_to/
- https://www.bleepingcomputer.com/news/security/north-korean-waterplum-hackers-infected-30-000-devices-worldwide/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*