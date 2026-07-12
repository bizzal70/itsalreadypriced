---
layout: field_note
title: "Field Note — July 12, 2026"
date: 2026-07-12
summary: "A $9M oracle exploit gutted Hedera's Bonzo Lend while a poisoned jscrambler npm release quietly shipped an infostealer to every install."
---

## Today's Field Note
Two supply-chain problems worth your attention today. First, Bonzo Lend on Hedera lost about $9M after its Supra oracle verifier accepted a manipulated price update, and a second wallet borrowed another ~$1M before claiming white-hat intentions. TVL cratered 77%, which tells you the depositors already understood what happened. Second, and more broadly dangerous, jscrambler npm 8.14.0 shipped on July 11 with a preinstall hook that drops a native Rust infostealer for Windows, macOS, and Linux. Socket caught it six minutes in, but six minutes is enough time for CI pipelines and dev machines to run it, and infostealers go straight for wallet files, browser sessions, and SSH keys.

## Today's Move
- Audit your lockfiles now: pin jscrambler below 8.14.0, purge caches, and rebuild any image that pulled it on or after July 11.
- If a dev machine or CI runner installed 8.14.0, treat it as compromised: rotate every key, seed, and session token that touched it, from a clean device.
- If you hold funds in Bonzo Lend on Hedera, exit remaining positions and revoke approvals to the protocol's contracts.
- Anyone building on Supra oracle feeds should recheck price-update verification logic and add sanity bounds before trusting a single source.
- Watch the two attacker wallets from the Bonzo incident for the promised white-hat return before assuming any recovery.

## Resources

- https://www.coindesk.com/web3/2026/07/11/lending-protocol-bonzo-loses-77-of-value-locked-as-usd9-million-oracle-exploit-rattles-hedera
- https://thehackernews.com/2026/07/compromised-jscrambler-8140-npm-release.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)
