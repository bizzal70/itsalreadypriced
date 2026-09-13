---
layout: field_note
title: "Field Note — September 13, 2026"
date: 2026-09-13
summary: "Revolut coughed up passports and full Bitcoin transaction histories to a fraudster spoofing a government email domain, and ZachXBT thinks HNW users were the target."
---

## Today's Field Note
Revolut confirmed it fulfilled a fraudulent data request sent from a legitimate government agency's own email domain, exposing passports, selfies, KYC records, and full Bitcoin transaction histories for a "limited" set of customers. Onchain investigator ZachXBT flags this as likely targeting of high-net-worth users, which is the part that matters. This is not a smart contract hack, it is a social engineering breach against the custodian's compliance desk, and the leaked data (linking real identities to onchain BTC history) is exactly the ammunition needed for wrench attacks, SIM swaps, and phishing. Separately, the Microsoft passkey phishing campaign (over a million scam emails, Aug 3 to 5) shows the same pattern: attackers abusing trusted infrastructure and identity flows, not code.

## Today's Move
- If you hold BTC with Revolut, assume your identity is now linked to your onchain addresses. Move funds to a fresh self-custody wallet and stop reusing any address Revolut has ever seen.
- Treat any inbound "Revolut security" or "government verification" contact as hostile. Do not click, call the number on the back of your card only.
- Rotate 2FA off SMS immediately (SIM swap risk is now concrete for exposed accounts) and set a carrier port-out PIN.
- If you use Microsoft cloud for a crypto team, audit passkey registrations and mail forwarding rules, and revoke any unrecognized authentication methods now.
- Builders and treasuries: reject any data or fund request based on sender domain alone, even a .gov one. Require out-of-band confirmation.

## Resources

- https://www.theblock.co/news/business/2026-09-12-revolut-says-customer-kyc-bitcoin-transaction-data-exposed-after-fake-request-from-govt-domain-414516
- https://decrypt.co/378114/revolut-passports-bitcoin-activity-data-breach
- https://thehackernews.com/2026/09/attackers-use-passkey-phishing-to.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [The Week Your Trezor Order Became a Home Address](/itsalreadypriced/2026/08/16/issue-007/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Signature Requests and Blind Signing](/itsalreadypriced/rtfm/2026/07/22/signature-requests-and-blind-signing/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*