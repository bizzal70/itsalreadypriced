---
layout: field_note
title: "Field Note — August 22, 2026"
date: 2026-08-22
summary: "A $3M BounceBit exploit kills a chain, MANTRA freezes after a Cosmos EVM fault, and Coldcard patches a $130M-class seed flaw."
---

## Today's Field Note
Three infrastructure failures landed at once while everyone watched the squeeze. BounceBit is sunsetting its own blockchain and migrating to BNB Chain after an attacker moved roughly 286.5 million BB across nine wallets before block production was halted, a ~$3M loss and an admission the chain is not salvageable. MANTRA's RWA Layer 1 has been frozen since Thursday, blaming its Cosmos EVM module; the team says two wallets it controls were touched and no user funds taken, but it will not say whether anything left those wallets, which is its own kind of answer. Separately, Coinkite shipped new Coldcard firmware after a three-week review tied to a $130M Bitcoin exploit, now forcing user-supplied entropy at seed generation. If you hold BB, LP on MANTRA, or generated a Coldcard seed on old firmware, today is not a market-watching day.

## Today's Move
- If you hold BB, do not bridge or trade until BounceBit publishes the exact migration contract and snapshot terms for BNB Chain. Assume any unofficial "migration" link is a drainer.
- MANTRA (OM) holders and LPs: withdraw nothing during the halt, watch the two team-controlled wallets on-chain for outflows, and treat any "unfreeze claim" site as hostile.
- Coldcard users: update to the latest Coinkite firmware today and verify the signed binary hash before flashing.
- If you generated a Coldcard seed on pre-patch firmware and hold meaningful size, generate a fresh seed with user-supplied entropy and sweep funds to it.
- Revoke stale approvals on any BounceBit or MANTRA-connected dApps via Revoke.cash before liquidity gets stranded or exploited further.

## Resources

- https://www.theblock.co/news/ecosystems/2026-08-21-bouncebit-sunset-blockchain-migrate-bnb-chain-after-3-million-exploit-412485
- https://thedefiant.io/news/blockchains/mantra-halts-chain-blames-cosmos-evm-module
- https://decrypt.co/376270/coldcard-new-security-after-bitcoin-exploit
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)
- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [A 2021 PRNG Bug Drained $89M From Coldcard Wallets in 41 Minutes](/itsalreadypriced/2026/08/02/issue-005/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*