---
layout: field_note
title: "Field Note — August 17, 2026"
date: 2026-08-17
summary: "SafePal wallet breach exposes 39,798 customers to physical and phishing risk while Harmony floats another chain rollback after the ONE exploit."
---

## Today's Field Note
SafePal, a hardware wallet vendor, exposed names, physical addresses, and phone numbers for 39,798 customers through a flaw in an order-tracking plug-in, and a threat actor is already selling the data. This lands the same week as a separate Trezor-adjacent leak, so hardware wallet buyers are now a marked cohort for phishing and, worse, wrench attacks. The exposure is doxxing, not key compromise, but for anyone whose real name is now tied to a Bitcoin hardware purchase, the threat model just shifted from digital to physical. Separately, Harmony is proposing to roll back 109,000 transactions to undo the ONE exploit, a reminder that "immutable" chains reorg when the treasury is at stake, with Ravencoin fighting the same fight.

## Today's Move
- If you bought from SafePal, assume your name, address, and phone are in criminal hands. Treat every unsolicited call, text, or "support" email as hostile and verify nothing over inbound contact.
- Enable strong non-SMS 2FA everywhere and never confirm a wallet firmware update or seed "verification" prompt that arrives via message. SafePal will not ask.
- If your delivery address is now public and holdings are meaningful, consider operational changes: move funds to a fresh seed on hardware bought anonymously, and do not store size at your home address.
- Harmony holders and bridge users: watch the rollback governance decision before transacting, since selective restoration risks inconsistent chain state. Do not treat recent ONE transactions as final.
- Builders shipping order-tracking or third-party plug-ins: audit what customer PII those integrations expose. This breach came through a bolt-on, not the core product.

## Resources

- https://www.bleepingcomputer.com/news/security/safepal-data-breach-impacts-39-798-customers-stolen-info-for-sale/
- https://decrypt.co/375743/safepal-bitcoin-wallet-data-breach
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)
- [The Week Your Trezor Order Became a Home Address](/itsalreadypriced/2026/08/16/issue-007/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*