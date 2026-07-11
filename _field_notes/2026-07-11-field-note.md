---
layout: field_note
title: "Field Note — July 11, 2026"
date: 2026-07-11
summary: "Injective Labs' npm SDK was backdoored to steal wallet keys, Bonzo Lend lost $9M to a Supra oracle exploit on Hedera, and a Solana whale lost 181K SOL."
---

## Today's Field Note
Supply chain first: unknown actors compromised the Injective Labs GitHub and pushed @injectivelabs/sdk-ts@1.20.21 to npm with fake telemetry that exfiltrates wallet private keys and seed phrases. If your build touches that package, treat any key it saw as burned. Meanwhile Bonzo Lend on Hedera dropped $9M when an attacker inflated SAUCE collateral through a flaw in Supra's on-chain oracle verifier, another reminder that your lending market is only as honest as its price feed. And a long-time Solana holder lost 181K SOL (about $14.2M), later bridged to ETH per zachxbt, the kind of single-key catastrophe that no protocol audit saves you from.

## Today's Move
- Audit your lockfiles for @injectivelabs/sdk-ts@1.20.21. Pin to a known-good version, purge caches, and rebuild clean.
- If any wallet key or seed touched a machine that installed that package, rotate to a fresh seed now and move funds.
- If you're an LP or borrower on Bonzo Lend or anything consuming Supra oracles, exit or reduce exposure until the verifier fix is confirmed.
- Move long-term SOL/ETH holdings to hardware or multisig custody. Single hot keys are the 181K SOL story.
- Watch the drainer's ETH consolidation address flagged by zachxbt and set alerts on your own approvals.

## Resources

- https://thehackernews.com/2026/07/injective-labs-github-compromise-pushes.html
- https://cointelegraph.com/news/bonzo-lend-9m-oracle-exploit-hedera?utm_source=rss_feed&utm_medium=rss_tag_hacks&utm_campaign=rss_partner_inbound
- https://www.reddit.com/r/CryptoCurrency/comments/1uti7ci/biggest_hack_from_an_individual_in_crypto_history/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)
