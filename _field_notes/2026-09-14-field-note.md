---
layout: field_note
title: "Field Note — September 14, 2026"
date: 2026-09-14
summary: "Symbiosis bridge exploit mints 46.1B syBTC from thin air, and Revolut's breach hands attackers passports and selfies now being leaked daily."
---

## Today's Field Note
The Symbiosis cross-chain bridge was exploited to mint roughly 46.1 billion syBTC out of nothing, per Blockaid, though the attacker only extracted about $336,000 and Symbiosis has clawed back 15 BTC. The firm is now offering a 20% bounty after the hacker declined the same terms as a white hat, which tells you negotiations are stalling. Separately, Revolut disclosed a breach where a threat actor impersonating a government agency pried loose customer financial data, passports, and selfies, and is now threatening daily leaks until paid. The infinite-mint pattern on syBTC is the operational lesson here: any wrapped-BTC representation is only as sound as the mint authority behind it. If you hold syBTC or route through Symbiosis, treat that peg as suspect until a full postmortem lands.

## Today's Move
- If you hold syBTC or have LP exposure to Symbiosis pools, exit or reduce today and stop routing bridge transactions through it until a postmortem confirms the mint bug is patched.
- Revoke any open token approvals granted to Symbiosis bridge contracts via Revoke.cash or Etherscan token approvals.
- If you are a Revolut customer, assume your KYC docs (passport, selfie) are compromised: freeze credit where possible, and treat any inbound "Revolut" or "government agency" contact as a phishing attempt.
- Rotate passwords and enable non-SMS 2FA on your Revolut and any linked exchange accounts.
- Watch the Symbiosis exploiter address and syBTC mint activity for further movement before assuming funds are contained.

## Resources

- https://www.theblock.co/news/defi/2026-09-13-symbiosis-says-it-recovered-15-btc-after-bitcoin-bridge-exploit-offers-attacker-20-bounty-414568
- https://www.bleepingcomputer.com/news/security/revolut-discloses-data-breach-exposing-financial-info-passports/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Upgradeable Contracts and the Admin Key Problem](/itsalreadypriced/rtfm/2026/08/12/upgradeable-contracts-and-the-admin-key-problem/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*