---
layout: field_note
title: "Field Note — August 21, 2026"
date: 2026-08-21
summary: "MANTRA halts its chain after a Cosmos EVM exploit, and Coldcard tells users their existing seeds may already be compromised."
---

## Today's Field Note
Two hardware-and-protocol stories outrank the macro noise today. MANTRA Chain froze the entire network and all transactions after an incident in its Cosmos EVM module, with exchanges pausing OM deposits and withdrawals while the token dropped 18% to a record low. Separately, Coinkite shipped Coldcard firmware that hardens seed generation, but the important part is the warning: seeds produced under the old flaw remain unsafe, so a patch alone does not save you. This lands the same week a reported $114 million bitcoin theft is circulating in Coldcard coverage, which is the context you should read the seed advisory in. Weak randomness in seed generation is not a bug you patch and forget, it is a reason to move funds.

## Today's Move
- If you hold OM or use MANTRA Chain, stop transacting now and do not trust bridge or DEX balances until the team publishes a post-mortem and confirmed root cause.
- Coldcard users: update firmware, then generate a brand new seed on the patched device and sweep funds from any wallet created under the old seed generation, treating old addresses as burned.
- Do not reuse or "verify" the old seed as safe. Move the coins, do not rationalize.
- If you sit in MANTRA-adjacent liquidity pools or lending markets on other chains, pull collateral exposure to OM while the chain is halted and price discovery is broken.
- Watch exchange notices (deposits/withdrawals for OM remain suspended) as your signal for when, or whether, the network is actually back.

## Resources

- https://www.coindesk.com/tech/2026/08/21/mantra-token-plunges-18-to-record-low-as-blockchain-halts-after-exploit
- https://www.theblock.co/news/defi/2026-08-21-mantra-freezes-network-412416
- https://cointelegraph.com/news/coldcard-upgrade-strengthen-seed-phrase-generation?utm_source=rss_feed&utm_medium=rss_tag_hacks&utm_campaign=rss_partner_inbound
- https://www.coindesk.com/tech/2026/08/21/coldcard-ships-firmware-after-usd114-million-bitcoin-theft-says-ai-helped-catch-more-bugs
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [A 2021 PRNG Bug Drained $89M From Coldcard Wallets in 41 Minutes](/itsalreadypriced/2026/08/02/issue-005/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*