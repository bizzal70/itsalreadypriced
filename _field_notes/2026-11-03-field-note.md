---
layout: field_note
title: "Field Note — November 03, 2026"
date: 2026-11-03
summary: "Two live wallet-draining campaigns, BTCPay Server and a WordPress payment plugin, plus a $133M EU theft that tangles Kraken."
---

## Today's Field Note
Two self-hosted bitcoin stacks are bleeding right now. BTCPay Server confirmed Bitcoin and Litecoin stolen from hot wallets on instances running 2.4.1 (released July 23, 2026) or earlier, so anyone running their own BTCPay node is exposed today. Separately, attackers are hitting an unpatched max-severity flaw (CVE-2026-81648, CVSS 10.0) in the CryptoPayment Gateway WordPress plugin, allowing unauthenticated file deletion and wallet credential extraction. Meanwhile ZachXBT surfaced a suspected $133M-plus EU theft, with Kraken restricting accounts and Crypto.com blocking tied funds while both insist their own systems were untouched. None of this is noise. These are keys walking out the door.

## Today's Move
- If you run BTCPay Server, update off 2.4.1 immediately, then treat any hot wallet on that instance as compromised and sweep remaining funds to a fresh key.
- Audit WordPress sites for the CryptoPayment Gateway plugin. There is no patch for CVE-2026-81648, so disable or remove it and rotate any wallet credentials it touched.
- Move anything above operational float off exchange hot wallets into self-custody given the Kraken and Crypto.com freeze activity around the $133M EU case.
- Watch ZachXBT's feed for the EU theft wallet addresses and pre-emptively screen incoming deposits if you operate a desk.
- Pull hot wallet keys off any internet-facing server you do not actively monitor. The pattern this week is self-hosted infrastructure, not smart contracts.

## Resources

- https://thehackernews.com/2026/11/hackers-exploit-btcpay-server-flaw-to.html
- https://thehackernews.com/2026/11/attackers-target-unpatched.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [The Week Bitcoin's Own Infrastructure Started Draining Itself](/itsalreadypriced/2026/08/09/issue-006/)
- [Field Note — November 02, 2026](/itsalreadypriced/field-notes/2026/11/02/field-note/)
- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*