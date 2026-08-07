---
layout: field_note
title: "Field Note — August 07, 2026"
date: 2026-08-07
summary: "The Coldcard exploit has moved from disclosure to on-chain reality, with 210,000 BTC fleeing old wallets and a French tax leak turning holder lists into physical threats."
---

## Today's Field Note
The Coldcard fallout is now visible on-chain: roughly 210,000 BTC has left old wallets as holders scramble to rotate off potentially weak seeds, and the exploit alone drove over $100M in losses that pushed July thefts to $247M. The root issue is entropy. If your seed came from the device's own RNG rather than something you generated yourself, treat it as suspect. Separately, a French tax official stole and sold the country's crypto owner registry, and criminals are now showing up at doors with zip ties, a reminder that OPSEC failures upstream become wrench attacks downstream. Two different failure modes, same lesson: the key and the fact that you hold one are both attack surfaces.

## Today's Move
- If you hold funds on any Coldcard with a device-generated seed, generate a fresh 24-word seed using external entropy (dice, coin flips) offline, then sweep funds to the new wallet today.
- Verify the 24th checksum word offline on an air-gapped machine or SeedSigner, never on a connected device.
- Assume any registry-style list (KYC, tax, exchange) containing your name and holdings may be public; scrub address-to-identity links and reduce on-chain footprint tied to your real identity.
- Harden physical OPSEC: no bragging about holdings, split custody, and consider a decoy wallet for coercion scenarios.
- Watch the flows: monitor the clusters draining old Coldcard wallets to distinguish legitimate self-sweeps from attacker consolidation before trusting any "safe" migration advice.

## Resources

- https://www.coindesk.com/markets/2026/08/07/coldcard-fallout-shows-up-onchain-as-210-000-bitcoin-leaves-old-wallets
- https://cointelegraph.com/news/coldcard-exploit-july-second-worst-month-2026?utm_source=rss_feed&utm_medium=rss_tag_hacks&utm_campaign=rss_partner_inbound
- https://www.reddit.com/r/CryptoCurrency/comments/1vhrkqx/with_the_whole_coldcard_fiasco_you_should/
- https://www.reddit.com/r/CryptoCurrency/comments/1vhqhca/a_tax_official_in_france_stole_a_list_of_everyone/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [A 2021 PRNG Bug Drained $89M From Coldcard Wallets in 41 Minutes](/itsalreadypriced/2026/08/02/issue-005/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*