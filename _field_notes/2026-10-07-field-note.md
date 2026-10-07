---
layout: field_note
title: "Field Note — October 07, 2026"
date: 2026-10-07
summary: "Cardano hands token issuers freeze-and-seize powers, and a Tether freeze lawsuit shows what that looks like in practice."
---

## Today's Field Note
Two items that rhyme. Cardano shipped a feature letting token issuers freeze, seize, and restrict assets at the ledger level, the kind of programmable control that makes "self-custody" conditional on an issuer's goodwill. On cue, Conduit sued Tether over $2.8M in USDt frozen in a Conduit wallet, allegedly without explanation, tied to a 2024 Brazilian probe. This is the standing reality of issuer-controlled assets: whatever you hold in a centralized stablecoin or a freezable token can be locked by the party that minted it, no court order required at the moment of freezing. If your treasury or protocol relies on these assets, counterparty risk is not theoretical, it is a function clause in the contract.

## Today's Move
- Audit which of your holdings are freezable: USDT, USDC, and any Cardano native tokens with issuer admin keys. Map exposure by wallet.
- For operational treasuries, split balances across multiple stablecoin issuers so a single freeze does not halt payroll or settlement.
- Read the actual token contract before integrating any Cardano asset. Check for freeze, seize, and restrict permissions and who holds those keys.
- If you route funds through flagged jurisdictions (Brazil, in Conduit's case), assume issuer compliance teams can act preemptively and keep a non-frozen reserve.
- Hold a decentralized collateral option (native BTC, ETH) for critical reserves you cannot afford to have locked.

## Resources

- https://www.coindesk.com/tech/2026/10/07/cardano-gives-token-issuers-power-to-freeze-seize-and-restrict-assets
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Exchange Custody, Counterparty Risk, and Proof of Reserves](/itsalreadypriced/rtfm/2026/09/09/exchange-custody-counterparty-risk-and-proof-of-reserves/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Reading a Token Contract Before You Buy the Rug](/itsalreadypriced/rtfm/2026/08/26/reading-a-token-contract-before-you-buy-the-rug/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*