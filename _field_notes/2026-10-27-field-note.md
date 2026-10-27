---
layout: field_note
title: "Field Note — October 27, 2026"
date: 2026-10-27
summary: "Keystone's device verification key is in attacker hands, SlowMist found address-swapping malware in Udesk scripts, and a Bloom trading bot bled $953K across 48 wallets."
---

## Today's Field Note
Three supply-chain and infrastructure failures, none of them requiring your seed phrase to hurt you. Keystone had its website breached and the attacker walked off with the key hardware wallets use to prove they are genuine, so the company is destroying 18,835 devices because counterfeits can now pass the online authenticity check. Separately, SlowMist found data-stealing and address-swapping code embedded in Udesk customer-service scripts, the kind that silently rewrites both the displayed and copied deposit address at the moment you paste. And Bloom's trading bot lost $953K across 48 wallets in minutes, with Bloom insisting no private keys were compromised, which tells you the signing was happening somewhere you did not control. The pattern is consistent: the attack surface is the tooling, not the chain.

## Today's Move
- If you bought a Keystone wallet recently, do not trust the online genuine-check alone. Verify provenance through the reseller and treat any device whose packaging looks off as suspect until Keystone publishes serials in scope.
- Stop trusting copy-paste for any deposit address. Manually verify the first and last 6 characters on-chain before sending, especially on sites running third-party support widgets (Udesk payload swaps displayed and copied addresses).
- If you use Bloom or any Telegram trading bot, withdraw funds to a wallet you alone sign for and revoke its trading permissions until Bloom publishes a root cause, not just a reimbursement promise.
- Audit any dApp or exchange frontend you use for embedded Udesk scripts, and builders should pull third-party customer-support JS from your production bundle pending review.
- Watch the 48 drained Bloom wallets and the reimbursement follow-through before re-enabling anything.

## Resources

- https://thehackernews.com/2026/10/keystone-to-destroy-18835-hardware.html
- https://thedefiant.io/news/security/slowmist-finds-data-stealing-and-address-swapping-code-in-udesk-scripts
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Address Poisoning and Clipboard Malware](/itsalreadypriced/rtfm/2026/09/16/address-poisoning-and-clipboard-malware/)
- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)
- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*