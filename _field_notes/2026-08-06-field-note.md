---
layout: field_note
title: "Field Note — August 06, 2026"
date: 2026-08-06
summary: "A twelve-year-old weak RNG in CryptoJS drained $5.7M from five wallet apps, while the Coldcard thieves start washing 64 BTC and 200 ETH through mixers."
---

## Today's Field Note
Coinspect traced the Ill Bloom wallet drains to `CryptoJS.lib.WordArray.random()`, a function shipped weak entropy for twelve years and used by five wallet apps to generate recovery phrases. Measured theft across two sweeps since late May is at least $5.7M, and the flaw is deterministic: if your seed came from an affected app, your keys were guessable from the start, hardware or not. Separately, the crew behind the Coldcard exploit has begun laundering 64 BTC and 200 ETH through mixers, though most stolen funds remain traceable in attacker wallets. Two different lessons, same root: the entropy source and the supply chain are the attack surface, not the vault.

## Today's Move
- If you generated a seed in any CryptoJS-based wallet app (check Coinspect's list of the five affected), assume it is compromised. Generate a fresh seed on an audited offline device and sweep funds to it today.
- Do not "verify" or re-import the old seed anywhere. Treat those addresses as burned and never reuse them.
- Coldcard users: confirm your firmware version against the disclosed exploit, and move funds if you are on an affected build. Do not trust "no funds at risk" statements until you have personally verified.
- Watch the Coldcard attacker wallets and mixer deposit addresses via a block explorer if you suspect exposure, and flag any inbound dust from them.
- Builders: audit your dependency tree for CryptoJS and any use of its RNG for key material. Swap to a CSPRNG (WebCrypto `getRandomValues`) and force-rotate affected users.

## Resources

- https://thehackernews.com/2026/08/cryptojs-weak-rng-behind-57-million-in.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [A 2021 PRNG Bug Drained $89M From Coldcard Wallets in 41 Minutes](/itsalreadypriced/2026/08/02/issue-005/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*