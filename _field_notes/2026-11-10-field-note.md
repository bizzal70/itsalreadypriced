---
layout: field_note
title: "Field Note — November 10, 2026"
date: 2026-11-10
summary: "An iOS sandbox escape threatens locally stored wallet keys, and Initia halted its L1 after a $605K rollup-key compromise."
---

## Today's Field Note
Two keys to watch today, both literal. First, the worse_query iOS sandbox escape (published Sunday on GitHub by a researcher going by forcequit) lets a malicious app read other apps' files on iPhones running iOS 26.x and 27.2. SlowMist and Binance both flag the obvious consequence: any wallet storing seed phrases or private keys in local plaintext is exposed, and Apple's latest updates do not list a fix. Separately, Initia halted its L1 after roughly $605,000 in USDC was moved out via fabricated cross-chain transfers, with the team's preliminary read pointing at compromised rollup infrastructure keys (an operator-side breach, not a contract bug). Different layers, same lesson: the secret was reachable by someone who should not have reached it.

## Today's Move
- On iPhone, delete any sideloaded or manually signed IPAs immediately, and update iOS plus all wallet apps to official versions. Assume this does not fully close the hole.
- If you hold meaningful funds in a mobile hot wallet on iOS 26.x or 27.2, move them now to a hardware wallet or a fresh wallet generated on a clean device, and reset active sessions.
- Treat any seed phrase that ever lived in plaintext on an affected iPhone as potentially compromised. Rotate it.
- Initia users: do not interact with bridges or cross-chain transfers while the chain is halted. Wait for a post-mortem and explicit all-clear before resuming.
- Watch the Initia team's channels for the specific drained address and compromised keyset so you can confirm your own positions were not routed through it.

## Resources

- https://thehackernews.com/2026/11/binance-warns-of-ios-sandbox-escape.html
- https://thedefiant.io/news/security/slowmist-flags-ios-sandbox-escape-risk-to-wallet-data
- https://thedefiant.io/news/hacks/initia-halts-l1-after-605-000-usdc-outflow-team-says
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Address Poisoning and Clipboard Malware](/itsalreadypriced/rtfm/2026/09/16/address-poisoning-and-clipboard-malware/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*