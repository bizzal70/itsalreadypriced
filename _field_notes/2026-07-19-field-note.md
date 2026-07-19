---
layout: field_note
title: "Field Note — July 19, 2026"
date: 2026-07-19
summary: "Two live RCE flaws with public exploits and a stealer surge mean the threat this week is your machine, not your chart."
---

## Today's Field Note


## Today's Field Note
The board-moving stuff today is boring infrastructure, which is exactly the stuff that empties wallets. 7-Zip 26.02 patches a remote code execution flaw triggered by opening a crafted archive, and WordPress Core's "wp2shell" RCE now has public exploits in the wild. At the same time Microsoft is flagging a surge in ACR Stealer, which lifts browser-stored passwords, session tokens, and documents, the exact loot that precedes a "how did they drain my hot wallet" post. None of these are crypto-branded, and that is the point. Signature theft and quantum FUD can wait years, but a malicious .7z or a compromised WordPress admin panel drains you today. Separately, a fake exchange has taken $240K+ from hundreds of victims, the usual reminder that the drainer does not need a zero-day when a fake front-end works.

## Today's Move
- Update 7-Zip to 26.02 now on every machine that touches a seed phrase or signs transactions, and do not open unsolicited archives.
- If you run WordPress (project site, docs, mint page), patch Core against the wp2shell RCE today before the public exploits find you.
- Assume browser-stored credentials are burnable: move exchange logins to hardware-backed or non-SMS 2FA, and clear session tokens on any machine you cannot vouch for.
- Sign transactions from a hardware wallet only, keeping the signing device on a machine that never opens random downloads.
- Verify exchange and DEX URLs by bookmark, not search results, given the $240K fake-exchange drain still collecting victims.

## Resources

- https://www.bleepingcomputer.com/news/security/update-now-7-zip-fixes-rce-flaw-exploitable-with-malicious-archives/
- https://www.bleepingcomputer.com/news/security/wordpress-core-wp2shell-rce-flaws-get-public-exploits-patch-now/
- https://www.bleepingcomputer.com/news/security/microsoft-warns-of-surge-in-acr-stealer-attacks-on-customers/
- https://www.reddit.com/r/CryptoCurrency/comments/1v0gvt1/a_fake_crypto_exchange_has_drained_240k_from/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Field Note — July 18, 2026](/itsalreadypriced/field-notes/2026/07/18/field-note/)
- [Field Note — July 17, 2026](/itsalreadypriced/field-notes/2026/07/17/field-note/)
- [Field Note — July 16, 2026](/itsalreadypriced/field-notes/2026/07/16/field-note/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*