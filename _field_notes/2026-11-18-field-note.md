---
layout: field_note
title: "Field Note — November 18, 2026"
date: 2026-11-18
summary: "Compromised Ledger hardware wallets from Virgin Megastore Dubai drain $604K, while a poisoned Microsoft agent-framework PyPI package steals cloud credentials on every Python start."
---

## Today's Field Note
Two supply-chain failures, same lesson: the breach happens before you ever sign anything. Two Ledger owners report a combined $604,000 gone from devices bought at an authorized retailer, Virgin Megastore in Dubai, with a research registry confirming a physical implant in at least one unit from photos. Separately, attackers pushed malicious versions 1.26.1 and 1.26.2 of Microsoft's agent-framework to PyPI (published 33 minutes apart on Nov 17), running a credential stealer on every Python start before Wiz and OX Security caught them. If you bought hardware through a reseller shelf or pulled that package into an agent, your keys and cloud secrets are already assumed exposed. Hardware trust and dependency trust both broke at the boundary, not at the keystroke.

## Today's Move
- If you hold a Ledger bought retail (especially Virgin Megastore Dubai or similar shelf stock), stop using it, generate a fresh seed on a device you provisioned from sealed factory state, and move funds to a new address.
- Audit your build logs for agent-framework 1.26.1 or 1.26.2, remove them, and pin to a known-good prior release.
- Rotate every cloud credential, API key, and token reachable from any host that ran those PyPI versions. Assume exfiltration, not suspicion.
- Heed LUKSO's warning separately: if your Universal Profile was hit, remove the attacker key and malicious recovery controller. Revoking permissions alone is not enough.
- Ignore unsolicited "support" from Etherscan, Ledger, or any explorer. They are not DMing you about access, and they never need your seed.

## Resources

- https://thehackernews.com/2026/11/attackers-compromise-microsofts-agent.html
- https://thedefiant.io/news/security/lukso-urges-key-removal-after-universal-profile-attack
- https://thedefiant.io/news/security/etherscan-warns-users-after-support-access-attempts
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Address Poisoning and Clipboard Malware](/itsalreadypriced/rtfm/2026/09/16/address-poisoning-and-clipboard-malware/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*