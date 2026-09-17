---
layout: field_note
title: "Field Note — September 17, 2026"
date: 2026-09-17
summary: "Revolut breach turns on-chain wealth into a targeting list, while DPRK and Iran industrialize blockchain as malware infrastructure."
---

## Today's Field Note
Two claimants are shaking Revolut over a customer data breach, one demanding $3M in Monero, another 10,000 BTC, and the tell is how they picked marks: scanning chains for Revolut-linked accounts holding significant crypto. Revolut says it has had no direct contact, which is not the same as saying nothing leaked. Meanwhile Chainalysis and Cointelegraph document a 5.2x (420%) YoY surge in blockchain-assisted attacks, with DPRK using Tron, Aptos, and BNB Chain to host malware instructions and suspected Iran actors embedding commands in Bitcoin transactions. The pattern is the same in both stories: your on-chain footprint is now the reconnaissance layer, and the malware C2 sits on chains you cannot seize. If your identity is linkable to a public balance, you are already on someone's list.

## Today's Move
- Break the link between your legal identity (Revolut, any KYC'd exchange) and any address holding meaningful balance. Move funds through a fresh wallet if your Revolut-associated addresses are exposed.
- Assume the Revolut dataset is in circulation regardless of ransom outcome. Rotate passwords, kill SMS 2FA in favor of hardware keys, and lock down email recovery today.
- Move size to cold storage. Anything scannable and hot is bait for the exact targeting method the attackers described.
- Builders: audit any contract or agent that reads calldata or memo fields as instructions. The DPRK and Iran playbook uses Tron, Aptos, BNB, and Bitcoin transactions as dead drops.
- Watch for spoofed Revolut "breach response" emails and support DMs. The follow-on phishing wave is more likely to drain you than the original leak.

## Resources

- https://decrypt.co/378472/revolut-hackers-demand-3m-monero-ransom-threaten-to-sell-customer-data-report
- https://www.chainalysis.com/blog/etherhiding-blockchain-dead-drops/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [The Week Your Trezor Order Became a Home Address](/itsalreadypriced/2026/08/16/issue-007/)
- [The $7M Custody Gap That Killed a Tether-Backed Exchange](/itsalreadypriced/2026/09/06/issue-010/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*