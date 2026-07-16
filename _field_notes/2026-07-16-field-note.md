---
layout: field_note
title: "Field Note — July 16, 2026"
date: 2026-07-16
summary: "Ostium's oracle signer key got stolen and drained up to $18M, the second oracle/keeper exploit in a week after SummerFi."
---

## Today's Field Note
Ostium lost between $11.86M and $18M USDC (roughly 28% of a $63M vault) after an attacker obtained the private key that signs its price oracle reports, then pushed fake future-dated prices through the PriceUpKeep contract (Gelato-triggered) across about 20 open/close loops. The audits, the code, none of it mattered, because the failure was in oracle infrastructure, not the contract. This follows SummerFi's roughly $6M oracle/keeper exploit last week, and SummerFi is now winding down its UI after seven years. Blockaid flagged Ostium publicly, Ostium paused trading, and positions and user funds are currently frozen. Signer key compromise is the emerging attack surface: off-chain keys that on-chain contracts blindly trust.

## Today's Move
- If you hold positions or LP in Ostium, assume funds are frozen and stop adding. Watch official channels for the post-mortem and any reimbursement terms before acting.
- Audit any protocol you're in for single-signer oracle or keeper dependencies (Gelato-triggered upkeeps, off-chain price feeds). Concentrated signer risk is the theme, not smart contract bugs.
- Exit or reduce exposure to perps/vaults relying on a single oracle signer without on-chain price sanity checks or multi-source validation.
- Builders: add staleness and deviation bounds on oracle inputs, reject future-dated timestamps, and move signing behind multisig or threshold schemes now.
- Note the pattern (SummerFi last week, Ostium now) and treat keeper/oracle infra as your primary threat model this cycle.

## Resources

- https://www.reddit.com/r/CryptoCurrency/comments/1uxxw7c/ostiums_18m_exploit_was_a_stolen_oracle_key/
- https://thedefiant.io/news/defi/summerfi-to-wind-down-after-seven-years-citing-exploit
- https://decrypt.co/373636/morning-minute-base-hands-its-app-over-to-cobie
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*