---
layout: field_note
title: "Field Note — October 13, 2026"
date: 2026-10-13
summary: "Ledger confirms an LTE spy chip in CryptoBilis-sold hardware wallets reads your seed off the screen during setup, roughly $86M suspected drained, and a THEO bridge exploit on Base cratered the token 92%."
---

## Today's Field Note
Ledger has now confirmed the CryptoBilis drain mechanism: a hidden LTE-enabled implant soldered inside the device reads your 24-word recovery phrase straight off the screen during setup, then transmits it over the mobile network. The Secure Element is untouched, so Genuine Check passes clean. Suspected losses run around $86M, and the fallout is spreading beyond CryptoBilis, with MediaMarkt pulling Ledger stock, Karpeles reporting a tampered airport-bought Ledger Flex, and Trezor and OneKey cutting ties with the reseller. Separately, Autheo's THEO fell 92% on Base after a suspected bridge exploit involving a 19 million-token mint and immediate sell-off. This is a supply-chain and setup-trust problem, not a firmware bug, which means your existing precautions may not cover it.

## Today's Move
- If you own a Ledger bought from any reseller (CryptoBilis, Metapod, MediaMarkt, airport kiosks, marketplaces), treat the seed as compromised: generate a new wallet on a device bought direct from Ledger and move funds now.
- Do not rely on Genuine Check alone. It validates the Secure Element, not added implant hardware.
- Weigh the Ledger Flex and other models bought secondhand or at retail with physical suspicion; inspect for tampering or retire them.
- Avoid THEO entirely: do not buy, sell, or bridge it on Base until Autheo publishes a post-mortem on the 19M mint.
- Watch the THEO bridge contract and the minter address for where proceeds move, and blacklist those addresses in any integrations.

## Resources

- https://decrypt.co/380826/ledger-finds-lte-implant-that-stole-recovery-phrases-in-suspected-86m-drain
- https://thedefiant.io/news/security/karpel-s-says-airport-bought-ledger-flex-contained-spy-implant
- https://thedefiant.io/news/hacks/autheo-s-theo-plunges-92-after-suspected-bridge-exploit-on-base
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Address Poisoning and Clipboard Malware](/itsalreadypriced/rtfm/2026/09/16/address-poisoning-and-clipboard-malware/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*