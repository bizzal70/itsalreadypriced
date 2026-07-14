---
layout: field_note
title: "Field Note — July 14, 2026"
date: 2026-07-14
summary: "Humanity Protocol loses $36M to social engineering as researchers show 85 wallet extensions leak your addresses."
---

## Today's Field Note
Humanity Protocol confirmed a $36M loss, and the founder's own framing is the tell: attackers are moving off smart contract bugs and onto the humans holding the keys. That lines up with the KU Leuven study of 85 browser wallet extensions, which found the wallets themselves leak enough (through how they talk to sites and RPC endpoints) to link your separate addresses and follow you across the web. The pattern this week is not clever bytecode, it is operational sloppiness and metadata bleed. If your threat model still assumes the contract is the weak point, update it. The people and the browser are the attack surface now.

## Today's Move
- Treat any Humanity Protocol (ONT ID adjacent) integration or approval as suspect until the team publishes a post-mortem naming the compromised keys or signers; revoke what you can via Revoke.cash.
- Audit your browser wallet extensions against the KU Leuven findings; separate high-value addresses into a dedicated browser profile or a hardware-only setup that never touches dApp sites.
- Assume RPC endpoints see your address linkage. Route sensitive wallets through your own node or a privacy-respecting RPC rather than the wallet default.
- For teams: harden the human layer. Enforce multi-party signing on treasury movements, and drill your staff on social engineering, since that is where the $36M went.
- Watch for a Humanity Protocol drained-funds address on Arkham or the usual chain trackers and blacklist it in your monitoring.

## Resources

- https://cointelegraph.com/news/humanity-protocol-operational-security-36m-hack?utm_source=rss_feed&utm_medium=rss_tag_hacks&utm_campaign=rss_partner_inbound
- https://thehackernews.com/2026/07/study-of-85-crypto-wallet-extensions.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*