---
layout: field_note
title: "Field Note — October 17, 2026"
date: 2026-10-17
summary: "A $3.8M NEAR Intents exploit, Ledger supply-chain implants from two more resellers, and an active npm shellcode loader are the day's real threats."
---

## Today's Field Note
Three supply-and-protocol risks worth your attention. NEAR Intents published a postmortem tying a $3.8M exploit to a deposit notification bug (users made whole, notifications removed, a second critical bug already reported, so treat it as still-settling). Mark Karpelès reports Ledger hardware implants found in devices from two more resellers, and Ledger's own authenticity check cannot detect the added hardware, which turns "buy from a reseller" into a seed-exposure event. Separately, the MALFEX npm package "imgdecode" (979 downloads, still live at writing) hides a Windows shellcode loader in a native addon, the kind of thing that ends up in a build pipeline and then in your signing machine. None of these are hypothetical.

## Today's Move
- If you deposited into NEAR Intents, confirm your balance against the postmortem, withdraw to a wallet you control, and do not re-deposit until the second reported bug is resolved.
- Only use Ledger devices bought direct from Ledger. For any device from a reseller or marketplace, assume physical compromise, move funds to a freshly initialized seed, and retire the old one.
- Audit your npm dependencies for "imgdecode" and anything from publisher "malfexteste8"; purge it, rotate any credentials or signing keys touched by affected build hosts.
- Builders: pin dependencies and run native addon builds in isolated, disposable environments, not on your signing or deploy machine.
- Ignore and never interact with unsolicited airdropped tokens; receiving is harmless, interacting is the trap.

## Resources

- https://thedefiant.io/news/security/near-intents-postmortem-links-3-8-million-exploit-to-deposit-bug
- https://thedefiant.io/news/security/karpel-s-reports-ledger-implants-in-devices-from-two-more-resellers
- https://thehackernews.com/2026/10/malfex-npm-package-imgdecode-hides.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)
- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Address Poisoning and Clipboard Malware](/itsalreadypriced/rtfm/2026/09/16/address-poisoning-and-clipboard-malware/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*