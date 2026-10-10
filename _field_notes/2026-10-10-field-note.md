---
layout: field_note
title: "Field Note — October 10, 2026"
date: 2026-10-10
summary: "Compromised Ledger devices from reseller CryptoBilis drained $72M to $86M, with funds now laundering through USDD and Tornado Cash."
---

## Today's Field Note
The CryptoBilis story is the only thing that matters today, and it is the oldest trick in the book executed at scale. Ledger confirmed that devices sold through the Southeast Asian reseller CryptoBilis appear compromised, with researchers estimating $72M to $86M stolen across the cluster. The mechanism is pre-initialized seed phrases: the reseller controls the keys before you ever plug the thing in, so your "self-custody" was custodial from the first block. The laundering is already well underway, with 464 ETH routed to Tornado Cash and 2M USDT converted through USDD's stability module to dodge Tether's freeze controls (Bitquery pegs frozen funds at only $10M of the cluster). A hardware wallet from anyone but the manufacturer is just a trojan with a nice box.

## Today's Move
- If you bought a Ledger from CryptoBilis or any third-party reseller (Amazon, eBay, Telegram), assume the seed is known and move all funds now to a device purchased directly from Ledger with a seed you generate yourself.
- Never use a pre-filled recovery sheet. A device shipping with a written seed phrase is compromised by definition, full stop.
- On your new device, confirm you generate the seed on-device during setup, with no cards, QR codes, or "activation" steps from a seller.
- Watch the laundering path: the source wallet still holds roughly 700 ETH, and funds are flowing through USDD to evade Tether freezes. Flag counterparties touching USDD's stability module.
- For existing legit hardware wallets, verify firmware authenticity via Ledger Live and revoke stale token approvals on any address that ever lived on a resold device.

## Resources

- https://thedefiant.io/news/hacks/wallet-linked-to-cryptobilis-thefts-routes-464-eth-to-tornado-cash
- https://thedefiant.io/news/hacks/ledger-theft-funds-shift-into-usdd-beyond-tether-s-freeze-controls
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*