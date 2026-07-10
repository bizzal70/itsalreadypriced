---
layout: field_note
title: "Field Note — July 10, 2026"
date: 2026-07-10
summary: "Two live wallet-drain stories today: the Coinspect 'Ill Bloom' weak-entropy seed flaw, actively swept, and a Ledger-disclosed laser attack on Tangem cards."
---

## Today's Field Note
Coinspect disclosed "Ill Bloom," a flaw where certain wallet software generated recovery phrases with weak randomness, letting an attacker reconstruct the seed and sweep everything it controls. They confirmed at least one coordinated sweep, with reported losses around $3.1 million, so this is active, not theoretical. Separately, Ledger researchers detailed a laser fault-injection attack that resets Tangem card passwords by bypassing a recovery-state check in firmware. Tangem calls the everyday risk "virtually non-existent," which is true right up until someone has your card and a lab bench. The common thread: your seed is only as good as the entropy that made it and the hardware that holds it.

## Today's Move
- If you hold funds in any wallet whose seed you did not generate with verified hardware entropy (especially browser or app-based wallets), generate a fresh seed on a trusted device and move funds today.
- Check whether your wallet software appears in Coinspect's "Ill Bloom" disclosure and treat any affected seed as burned, not rotatable.
- Prioritize migrating any wallet created from software with a history of weak or unaudited RNG, regardless of balance.
- Tangem holders: treat physical possession of the card as the whole threat model. Do not leave cards with anyone, and move meaningful balances to a seed-based cold setup you control.
- After migrating, revoke stale token approvals on the old addresses so a swept key cannot drain via existing allowances.

## Resources

- https://thehackernews.com/2026/07/attackers-exploit-ill-bloom.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)
