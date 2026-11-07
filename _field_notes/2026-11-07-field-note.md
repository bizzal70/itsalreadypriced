---
layout: field_note
title: "Field Note — November 07, 2026"
date: 2026-11-07
summary: "Keplr pulls social login after unauthorized transactions, while Gnosis Pay admits its legacy card system leaked customer data and wallet info."
---

## Today's Field Note
Two wallet-adjacent incidents landed today, both targeting the soft parts. Keplr paused Google and Apple social login after reports of unauthorized transactions, which means the compromise sits in the custodial login path, not in seed-phrase or hardware accounts (those, per Keplr's initial read, are untouched). Separately, Gnosis Pay confirmed unauthorized access to the legacy system behind its branded debit cards on Nov. 3, exposing card details, personal data, and crypto wallet information. Funds are reportedly safe in both cases, but "safe funds" and "leaked wallet mapping plus PII" is exactly the starter kit for the next round of targeted phishing. If your identity is now tied to a known onchain address, treat yourself as a marked target.

## Today's Move
- If you use Keplr via Google or Apple login, stop sending funds to those accounts and migrate to a seed-phrase or hardware-backed account now.
- Keplr social-login users: move assets out of the social wallet to a fresh hardware wallet address, then abandon the old one.
- Gnosis Pay customers: assume your card data and wallet address are now linked in a leaked set, freeze or reissue the affected card, and watch that address for approval-spoofing.
- Revoke lingering token approvals on any wallet exposed in either incident (use Revoke.cash on the relevant chains).
- Expect tailored phishing emails referencing your real Gnosis Pay card or Keplr login. Verify any "security alert" out of band, never via the inbound link.

## Resources

- https://thedefiant.io/news/security/keplr-pauses-google-and-apple-login-after-unauthorized-transaction-reports
- https://thedefiant.io/news/security/gnosis-pay-confirms-breach-of-consumer-card-system
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*