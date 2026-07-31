---
layout: field_note
title: "Field Note — July 31, 2026"
date: 2026-07-31
summary: "A weak-RNG flaw in Coldcard Mk3 firmware drained 594 BTC ($38M) from ~500 addresses in a 25-minute sweep, and the vendor confirms it."
---

## Today's Field Note
Coinkite has confirmed a seed-generation weakness in older Coldcard Mk3 firmware, and attackers used it to sweep 594 BTC (roughly $38M) out of about 500 addresses in a single 25-minute window. This is not a phishing story or a careless-user story. If the device generated your seed on vulnerable firmware, the entropy was predictable enough to reconstruct offline, which means the keys were arguably compromised the moment they were created. Coinkite believes an attacker likely fed old open-source firmware to an AI to surface the bug, which is the part worth sitting with: your public repo is now an attack surface someone can grind cheaply. Users who migrated off Coldcard to other wallets using the same seed are not safe either.

## Today's Move
- If you hold a Coldcard Mk3, assume the seed is burned. Generate a fresh wallet on current firmware using a strong, unique BIP-39 passphrase and move funds today, not this weekend.
- Do not reuse the old seed anywhere, including on a new device or any wallet you migrated to. The seed is the compromised asset, not the hardware.
- Fund the new wallet from a clean address and verify the receive address on-device before sending the full balance.
- Sweep in one motion to a single new address to minimize the window; watch for any unexpected outbound tx as a signal your seed is already known.
- Builders: treat every published firmware version as adversary-readable. Audit RNG and key-derivation paths in old releases, not just HEAD.

## Resources

- https://www.coindesk.com/tech/2026/07/31/major-bitcoin-wallet-flaw-drains-594-btc-in-25-minute-sweep
- https://decrypt.co/374766/38m-in-bitcoin-drained-by-coldcard-key-flaw-its-maker-thinks-ai-found
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*