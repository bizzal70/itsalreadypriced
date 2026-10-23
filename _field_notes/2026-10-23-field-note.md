---
layout: field_note
title: "Field Note — October 23, 2026"
date: 2026-10-23
summary: "Fake Rabby and OKX wallet extensions on Firefox harvested seed phrases, Swell paused swETH redemptions over a NAV problem, and an x402 SDK flaw let malicious APIs drain AI agent balances."
---

## Today's Field Note
Three unrelated custody problems landed at once. Socket found 16 counterfeit Rabby and OKX wallet extensions on Firefox, unpublished by Mozilla around Oct. 5, but removal does nothing for anyone who already typed a recovery phrase into one. Swell paused swETH and rswETH deposits and withdrawals citing a NAV correction, with on-chain controls now blocking withdrawal requests and ETH claims, which means your liquid staking position is frozen until they reprice. Separately, V12 disclosed an x402 SDK flaw (fixed by the Aug. 18 release) where the default client set no spending limit, letting a malicious API prompt an agent to sign away its full token balance. None of these are market events. All three bite the same way: something you trusted to hold or move funds was not what it claimed.

## Today's Move
- If you installed any Rabby or OKX wallet extension on Firefox recently, assume the seed is burned. Generate a fresh wallet from the official source, move funds, and never reuse that phrase.
- Verify your real Rabby or OKX extension against the official publisher and store listing, not search results.
- If you hold swETH or rswETH, stop expecting withdrawals to clear. Do not panic-swap into illiquid secondary pools at a discount while Swell reprices NAV.
- If you run agents on x402 SDKs, update past the Aug. 18 release that added spending limits, and set an explicit per-call cap. Do not leave auto-signing unbounded.
- Audit token approvals on any address touched by those extensions via Revoke.cash and pull anything open.

## Resources

- https://thedefiant.io/news/security/socket-finds-16-fake-rabby-and-okx-wallet-extensions-on-firefox
- https://thedefiant.io/news/hacks/swell-pauses-sweth-and-rsweth-deposits-and-withdrawals
- https://thehackernews.com/2026/10/critical-x402-sdk-flaw-could-let.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Address Poisoning and Clipboard Malware](/itsalreadypriced/rtfm/2026/09/16/address-poisoning-and-clipboard-malware/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*