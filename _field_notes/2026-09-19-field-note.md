---
layout: field_note
title: "Field Note — September 19, 2026"
date: 2026-09-19
summary: "A self-inflicted drainer campaign, a stablecoin depeg with a tranche wipeout, and a custody-provider breach dominate the day."
---

## Today's Field Note
Three things worth your attention. TRM traced 274.60 ETH across six operator addresses in a campaign where 224 victims followed fake AI trading-bot tutorials and deployed and funded their own drainer contracts between February and August, a reminder that the signature you sign matters more than the site you signed it on. Separately, Neutrl opened NUSD redemptions at 51 cents while Strata scheduled a 48-hour valuation update that writes the jrNUSD junior tranche to zero, with senior sNUSD holders settling at revised share values, a textbook tranche waterfall doing exactly what it says on the tin. And crypto tech provider Haruko confirmed a cyberattack affecting 15 clients with some funds lost, so if your desk touches Haruko infrastructure, treat keys and permissions as suspect until told otherwise.

## Today's Move
- If you ever deployed a "trading bot" from a GitHub or YouTube tutorial, inspect the contract you funded, withdraw remaining balances, and revoke any approvals it holds via Revoke.cash or Etherscan token approvals.
- Watch the six TRM-flagged operator addresses and block them in your treasury tooling if you run automated payouts.
- If you hold NUSD, decide now whether to take the 51 cent redemption or wait, and assume jrNUSD is a total loss before the 48-hour Strata valuation closes.
- If you are a Haruko client or custody through them, rotate API keys, force-reset withdrawal permissions, and reconcile balances against on-chain state today.
- Builders: stop trusting tutorial-supplied contract bytecode. Verify source, diff against known-good, and simulate before funding.

## Resources

- https://thedefiant.io/news/security/fake-ai-bot-tutorials-tricked-224-victims-into-deploying-their-own-drainers
- https://thedefiant.io/news/defi/neutrl-opens-nusd-redemptions-at-51-cents-as-strata-junior-tranche-faces-wipeout
- https://www.coindesk.com/business/2026/09/18/crypto-tech-provider-haruko-hit-by-cyberattack-affecting-15-clients-some-funds-lost
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Signature Requests and Blind Signing](/itsalreadypriced/rtfm/2026/07/22/signature-requests-and-blind-signing/)
- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*