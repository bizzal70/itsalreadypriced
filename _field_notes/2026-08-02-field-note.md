---
layout: field_note
title: "Field Note — August 02, 2026"
date: 2026-08-02
summary: "A 2021 Coldcard firmware bug crippled seed entropy, and someone spent it, sweeping ~1,082 BTC (~$70M, now near $89M) from 4,500 addresses in minutes."
---

## Today's Field Note
On July 30 an attacker drained 1,196 Coldcard-generated Bitcoin addresses in 41 minutes, taking 1,082.65 BTC (~$70.2M at the time), a toll Galaxy Research and CoinDesk now put near $89M across roughly 4,500 addresses. The root cause is not user error: a March 2021 firmware integration error on Coldcard MK3 routed seed generation to a deterministic software PRNG, meaning affected seeds were guessable from the start. This is a supply-chain and RNG failure, the worst kind, because your funds could be gone before you ever notice. The attack is still active, and the panic is visible onchain as 39,600 BTC moved in sub-1 BTC transactions, the biggest such spike since FTX. Separately, Rails shipped a fix for a critical Active Storage flaw with arbitrary file read and RCE potential, which matters if your exchange or wallet backend runs Rails.

## Today's Move
- If you ever generated a seed on a Coldcard MK3 (especially post March 2021), treat it as compromised. Generate a fresh seed on a known-good source (dice, Sparrow, Electrum) and sweep funds to it now.
- Do not simply "reuse" the MK3 with the old seed. Load a newly generated seed onto it instead, or move to a different device.
- Spread holdings across multiple wallets and seeds rather than one device, per CZ's (broken-clock-correct) point.
- Builders: patch Rails Active Storage immediately if you run it in production, and audit for arbitrary file read exposure.
- Watch the attacker's consolidation addresses via Galaxy/Lookonchain feeds before assuming your untouched funds are safe.

## Resources

- https://thehackernews.com/2026/08/coldcard-hardware-wallet-flaw-linked-to.html
- https://www.coindesk.com/tech/2026/08/02/bitcoin-cold-wallet-attack-spreads-to-4-500-addresses-as-losses-near-usd89-million
- https://decrypt.co/374810/cz-warns-bitcoin-holders-70-million-coldcard-wallet-exploit
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*