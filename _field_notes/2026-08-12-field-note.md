---
layout: field_note
title: "Field Note — August 12, 2026"
date: 2026-08-12
summary: "Harmony's ONE minted into oblivion, Ravencoin faces a 51% reorg, and a small XRP bridge got fooled by fake deposits."
---

## Today's Field Note
Harmony confirmed an exploit that minted roughly 4 billion unauthorized ONE (about a quarter of supply), tanking the token ~37-40% and forcing the team to weigh a full rollback while working with exchanges to freeze funds. Note what a rollback means: it erases every legitimate transaction alongside the theft, so treat all recent ONE activity as provisional. Separately, Ravencoin (RVN) is under active consensus attack, with mining pools holding most of the hash rate building a competing chain that could trigger a three-day reorganization, which is textbook 51% territory. And a smaller XRP bridge lost $200,000 after its software accepted fake deposits as real, the usual reminder that bridge accounting logic is where value quietly leaks.

## Today's Move
- If you hold ONE, stop transacting now. Any deposit, swap, or bridge you make today may be reversed or orphaned by a rollback.
- Watch Harmony's official channels for the confirmed patch and rollback decision before moving funds on or off exchanges.
- For RVN: halt deposits and withdrawals, and do not treat any confirmations as final until the reorg risk clears (assume far deeper confirmation depth than usual, or just wait it out).
- Audit any bridge you operate or use for deposit-verification logic that trusts unconfirmed or spoofable events. The $200K XRP bridge failed exactly here.
- Delist or flag ONE and RVN in any automated system (bot, treasury, LP) that assumes finality; pause those strategies until chains stabilize.

## Resources

- https://decrypt.co/375390/harmonys-one-sinks-37-after-attacker-mints-4-billion-tokens
- https://www.theblock.co/news/defi/2026-08-12-harmony-confirms-exploit-one-token-411527
- https://www.coindesk.com/tech/2026/08/12/xrp-bridge-drained-for-usd200-000-after-software-mistook-fake-deposits-for-real-ones
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*