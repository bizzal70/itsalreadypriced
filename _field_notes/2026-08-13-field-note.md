---
layout: field_note
title: "Field Note — August 13, 2026"
date: 2026-08-13
summary: "Harmony ONE cracks 40% on an alleged 4B-token mint, Trezor buyer data leaks via a shipping partner, and a SharePoint auth bypass is now under active exploitation."
---

## Today's Field Note
Harmony's ONE fell roughly 40% after an attacker allegedly minted 4 billion tokens, the kind of supply blowout that usually means a compromised bridge or mint key rather than a market wobble. Separately, Trezor confirmed a shipping supplier breach exposing customer names, physical addresses, phone numbers, and emails. Devices and backups are untouched, but that dataset is a phishing and physical-coercion kit handed straight to attackers who now know who holds hardware wallets and where they live. And CVE-2026-55040, the SharePoint auth bypass patched in July, is being actively exploited after a public PoC dropped, which matters for any org running on-prem SharePoint near key infrastructure. None of these are price-action noise. All three are live.

## Today's Move
- If you hold or LP ONE, exit exposure now and treat any Harmony bridge or wrapped-ONE position as suspect until the mint source is confirmed.
- Trezor buyers: assume your name, address, and email are compromised. Distrust any "Trezor" email, SMS, or physical mail asking you to verify, upgrade, or re-seed. Never enter a seed anywhere, ever.
- Consider a duress PIN and moving high-value holdings off any address linkable to your shipping identity given the physical-address leak.
- Patch on-prem SharePoint against CVE-2026-55040 today and audit auth logs for the known bypass pattern if you run it near treasury or signing infra.
- Watch Harmony's known deployer and bridge addresses for the minted 4B tokens hitting DEXs or CEX deposit wallets before dumping fully lands.

## Resources

- https://www.reddit.com/r/CryptoCurrency/comments/1vmykoo/harmonys_one_falls_40_after_attacker_allegedly/
- https://decrypt.co/375556/trezor-customer-data-exposed-in-shipping-partner-breach
- https://www.reddit.com/r/CryptoCurrency/comments/1vnabtf/trezor_data_breach/
- https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Upgradeable Contracts and the Admin Key Problem](/itsalreadypriced/rtfm/2026/08/12/upgradeable-contracts-and-the-admin-key-problem/)
- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*