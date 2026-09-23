---
layout: field_note
title: "Field Note — September 23, 2026"
date: 2026-09-23
summary: "North Korea's WaterPlum crew drains $11M via fake job interviews, a malicious App Store app steals $580K, and Zcash's NU7 upgrade threatens to strand legacy Sprout funds."
---

## Today's Field Note
Three things worth your attention, none of them the price ticker. A seven-agency advisory ties Pyongyang's WaterPlum crew and the fake remote-IT-worker scheme to $11M drained across roughly 7,000 wallets, the usual pattern of fake interview flows and trojanized "coding assessments" fed to job-seeking developers. Separately, SlowMist attributes a $580K theft to FomoPeek, a malicious iOS app that slipped past Apple review and used kernel exploits to escape the sandbox and read data from other apps, which means an App Store presence is no longer a trust signal. And on the protocol side, Zcash's proposed NU7 upgrade in November would disable v4 transactions, leaving any ZEC still parked in the legacy Sprout shielded pool permanently unspendable. All three reward acting before the deadline, not after.

## Today's Move
- If you took a "job interview" coding task recently, treat that machine as compromised: rotate keys from a clean device, revoke token approvals, move funds to a fresh wallet.
- Audit installed iOS apps for FomoPeek or anything sideloaded-adjacent; delete it, and assume any seed typed on that device is burned.
- If you hold ZEC in the legacy Sprout pool, migrate it out before the November NU7 activation or accept the funds may be frozen forever.
- Builders: stop treating App Store or job-platform vetting as endpoint trust. Sandbox anything unknown, verify signatures out-of-band.
- Watch the WaterPlum advisory's named indicators and add flagged addresses to your monitoring.

## Resources

- https://decrypt.co/379032/north-koreas-fake-job-interviews-drained-11m-from-7000-crypto-wallets
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)
- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*