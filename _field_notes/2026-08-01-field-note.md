---
layout: field_note
title: "Field Note — August 01, 2026"
date: 2026-08-01
summary: "Coldcard drain hits $70M via a supply-chain style exploit that never touched the devices, plus Metronome's $15.7M oracle-lag shortfall and the Adform clipboard-swap campaign."
---

## Today's Field Note
Galaxy Research now puts the Coldcard loss at 1,082.65 BTC (~$70M) across 1,196 addresses, drained in a 41-minute window. The devices were never physically touched, which means this was a supply-chain or firmware/software vector, not a hands-on theft, and cold storage users who assumed air-gap equals safety are the ones exposed. Separately, MetronomeDAO disclosed a $15.7M shortfall (6,367 msETH and 4.57M msUSD unbacked) from Chainlink oracle lag in its swap module, an "unbacked float" that accreted quietly over years. And Adform's ad-serving JavaScript was poisoned on July 27 to rewrite copied BTC addresses in browsers, so anyone who copy-pasted a wallet address that day may have sent to an attacker.

## Today's Move
- If you run Coldcard, move funds to a freshly generated seed on a device you trust, and verify receive addresses on-device before any transfer.
- Do not trust any address you copied from a browser on July 27; re-derive and re-verify every payment address, especially BTC.
- Metronome (msETH/msUSD) holders: treat the peg as impaired, exit or hedge exposure now rather than waiting on the $34M defensive backstop to hold.
- Rebuild the habit of on-device address confirmation for every send; clipboard swaps only work when you skip that step.
- Watch the 1,196 tagged Coldcard drain addresses via Galaxy's list before assuming your funds are unaffected.

## Resources

- https://www.coindesk.com/tech/2026/08/01/how-bitcoin-cold-wallets-lost-usd70-million-in-an-attack-that-never-touched-the-devices
- https://thedefiant.io/news/defi/metronome-discloses-usd15-7-million-synth-shortfall-blames-oracle-lag-in-swap-module
- https://thehackernews.com/2026/08/hackers-poison-adform-script-to-swap.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*