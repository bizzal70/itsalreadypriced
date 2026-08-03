---
layout: field_note
title: "Field Note — August 03, 2026"
date: 2026-08-03
summary: "Coldcard hardware wallet drains near $114M and enter a suspected fourth sweep, five days in."
---

## Today's Field Note
The Coldcard exploit is now five days old and losses are approaching $114 million, with Galaxy Research flagging a probable fourth sweep and 462 new suspected victims. This is a five-year-old flaw, per Kraken's security chief, which means the affected seeds have likely been vulnerable the entire time you owned the device. The tell in the data is a spike in sub-1 BTC transfers, last seen after FTX collapsed, meaning small holders are moving coins in a hurry. Self-custody was supposed to remove counterparty risk, not hand you a silent single point of failure baked into firmware. If you hold a Coldcard, treat every key it ever generated as compromised until proven otherwise.

## Today's Move
- If you use a Coldcard, generate a fresh seed on a different, audited device (Trezor, Ledger, or a verified airgapped setup) and sweep all funds to the new addresses today.
- Do not reuse any seed phrase or passphrase that ever touched a Coldcard, even on new hardware.
- Watch the drainer consolidation addresses being tracked by Galaxy Research and Arkham before you move, so you are not broadcasting into a live sweeping bot.
- Move in a single well-fee'd transaction rather than dribbling sub-1 BTC amounts that mark you as a panicked target.
- If you cannot migrate immediately, move to a temporary exchange custody address as a stopgap, then to fresh cold storage once you have clean hardware.

## Resources

- https://decrypt.co/374820/coldcard-losses-near-114m-as-small-bitcoin-transfers-spike
- https://www.coindesk.com/tech/2026/08/03/coldcard-wallet-losses-may-near-usd114-million-as-possible-fourth-sweep-emerges
- https://www.reddit.com/r/CryptoCurrency/comments/1ve3zw8/coldcards_5year_flaw_reveals_hardware_wallet/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [A 2021 PRNG Bug Drained $89M From Coldcard Wallets in 41 Minutes](/itsalreadypriced/2026/08/02/issue-005/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*