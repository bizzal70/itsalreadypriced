---
layout: field_note
title: "Field Note — September 22, 2026"
date: 2026-09-22
summary: "A Coldcard exploit is still live, white hats scrambled 52 BTC into a recovery trust, and a stealthy npm package is targeting builders' machines."
---

## Today's Field Note
The Coldcard hardware wallet exploit remains an open wound. White hats moved roughly 52 BTC (about 40% of what was drained in the second wave) into a Wyoming recovery trust for victims, which tells you the attackers are still actively sweeping funds and this is not resolved. Separately, Checkmarx flagged a malicious npm package, "indexed-btree," that typosquats the legitimate "sorted-btree" and hides its loader inside runtime code rather than lifecycle scripts, a deliberate move to slip past the scanners everyone bolted on after the last supply-chain waves. Both hit the same soft spot: developers and holders trusting tooling they never audit. If you run a Coldcard or pull npm dependencies without pinning, today is the day to act, not to read.

## Today's Move
- If you hold a Coldcard, treat any wallet initialized or restored on affected firmware as compromised. Generate a new seed on a verified device and migrate funds now, do not wait for a formal statement.
- Audit your npm tree for "indexed-btree" (`npm ls indexed-btree`) and purge it. Confirm you meant to install "sorted-btree" and pin the exact version.
- Assume any build machine that pulled "indexed-btree" is dirty. Rotate credentials, npm tokens, and any keys stored in that environment.
- Watch the Coldcard drainer and the white-hat recovery trust addresses (via the Cointelegraph and CoinDesk reports) to confirm your funds are not among the moved coins.
- Enforce lockfile integrity and disable postinstall scripts by default in CI, since attackers have now moved malicious logic into runtime to dodge lifecycle-script controls.

## Resources

- https://www.coindesk.com/markets/2026/09/22/whitehats-move-52-bitcoin-from-the-coldcard-hack-to-a-recovery-trust
- https://thehackernews.com/2026/09/malicious-npm-package-indexed-btree-hid.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Issue #002 — Week of July 12, 2026](/itsalreadypriced/2026/07/12/issue-002/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Coldcard Ships Firmware After $114M Bitcoin Theft](/itsalreadypriced/2026/08/23/issue-008/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*