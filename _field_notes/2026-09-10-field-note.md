---
layout: field_note
title: "Field Note — September 10, 2026"
date: 2026-09-10
summary: "Trezor's email vendor got popped and is now spraying 'STM32 Entropy Vulnerability' phishing from Trezor's real domain, while OFAC sanctions the Xinbi laundering marketplace."
---

## Today's Field Note
Trezor confirmed a breach at its third-party email provider, and attackers are using the legitimate Trezor domain to send fake "Critical Security Alert: STM32 Entropy Vulnerability" emails aimed at coaxing recovery phrases out of users. This is the third backend incident for Trezor in roughly two months (ShipMonk shipping data last month, now email), and BitBox says the same shared newsletter provider hit multiple Bitcoin firms. The hardware and firmware have not failed. The vendors around them keep doing so, which means the attack surface is your inbox, not your device. Separately, the US sanctioned the Xinbi marketplace and restrained $52M in crypto, with DOJ pursuing 47 more wallets, so laundering-adjacent counterparties are worth a fresh look.

## Today's Move
- Treat any email citing an "STM32 Entropy Vulnerability" or urgent recovery-phrase action as phishing, even if it comes from a genuine Trezor or BitBox address. Do not click.
- Never enter your seed phrase anywhere except directly on the device. No legitimate alert will ever ask for it via email or web.
- Assume your email and shipping details tied to hardware wallet purchases are now in circulation. Watch for tailored spear-phishing referencing your real order.
- Verify firmware and any advisories only through the official Trezor Suite app or the vendor's site typed manually, not through email links.
- If you interact with OFAC-sensitive flows, screen counterparties against the newly sanctioned Xinbi wallets before moving funds.

## Resources

- https://www.bleepingcomputer.com/news/security/trezor-warns-users-of-email-provider-breach-phishing-attacks/
- https://www.theblock.co/news/defi/2026-09-09-trezor-phishing-emails-414086
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [The Week Your Trezor Order Became a Home Address](/itsalreadypriced/2026/08/16/issue-007/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*