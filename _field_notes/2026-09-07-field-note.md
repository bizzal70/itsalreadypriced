---
layout: field_note
title: "Field Note — September 07, 2026"
date: 2026-09-07
summary: "Liquid Network paused after a $320M 'white hat' withdrawal via an Elements bug, while the Coldcard third-wave thief starts laundering 1,779 BTC."
---

## Today's Field Note
Blockstream's Liquid sidechain is paused after actors withdrew roughly 4,000 BTC (about $320M) by exploiting a vulnerability in Elements, the software that underpins the network. They are signing PGP messages inside Bitcoin transactions and claiming white-hat intent, promising to return most of it once the bug is patched, which is a negotiation, not a rescue. Treat the "good guys" framing as leverage until coins actually move back. Separately, the Coldcard third-wave attacker has begun draining 293 self-built vaults, moving $7.7M so far (45% of the wave-three haul), emptying largest first, with Galaxy tracing 1,779 BTC from 190 victims. Two reminders in one day that the seed and the sidechain are both attack surface.

## Today's Move
- If you hold L-BTC or run anything on Liquid, stop peg-ins and treat the two-way peg as frozen until Blockstream ships and confirms the Elements patch across functionaries.
- Node and functionary operators: pull the patched Elements build the moment it drops, do not wait for the attacker's "return."
- Coldcard users who bought hardware in the affected supply-chain window: assume the seed is compromised, generate a fresh wallet on verified firmware, and move funds now rather than trusting the largest-first drain order to skip you.
- Watch the Coldcard exploiter's cluster (Galaxy's 8,600-plus flagged addresses) and set alerts on your own deposit addresses for unexpected outflows.
- Ignore the Zcash and Fomo/Pump.fun noise today. The signal is key hygiene and Liquid downtime.

## Resources

- https://www.theblock.co/news/defi/2026-09-07-liquid-network-attacker-says-they-will-return-most-of-4000-btc-after-bug-fix-413673
- https://decrypt.co/377528/purported-white-hat-hackers-withdraw-320m-in-bitcoin-from-liquid
- https://www.theblock.co/news/defi/2026-09-07-coldcard-exploiter-moves-wave-3-413661
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Coldcard Ships Firmware After $114M Bitcoin Theft](/itsalreadypriced/2026/08/23/issue-008/)
- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*