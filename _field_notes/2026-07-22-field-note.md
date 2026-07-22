---
layout: field_note
title: "Field Note — July 22, 2026"
date: 2026-07-22
summary: "Zilliqa's Ledger app leaked private keys onchain since 2019, and a Wanchain bridge breach hit Cardano's Midnight token."
---

## Today's Field Note
The Zilliqa Ledger app has been leaking signer private keys through onchain signature data since 2019, a nonce-reuse class flaw that lets anyone reconstruct keys from public chain history. Zilliqa halted native transactions in response, but the exposure is retroactive: any address that signed with the vulnerable app is already compromised, and the attacker needs nothing but a block explorer. Separately, a Wanchain bridge breach drove Cardano's Midnight token to an all-time low, with Hoskinson calling for a ZK overhaul, and SecondFi is winding down after a $2.6M ADA theft tied to a wallet flaw. The pattern this week is not novel exploits, it is old signing bugs and bridge trust that were quietly load-bearing until they weren't.

## Today's Move
- If you ever signed a Zilliqa transaction from a Ledger, treat those keys as burned. Generate a fresh seed on a patched setup and move ZIL and any co-located assets now.
- Do not sign anything with the Zilliqa Ledger app until an audited fix ships and is confirmed by the team, not just announced.
- Audit any address that touched Wanchain's cross-chain bridge for Cardano or Midnight assets, and pull liquidity out of the affected routes.
- SecondFi users: stop waiting on the promised recovery tools (they are not coming) and export what you can before wind-down completes.
- Broadly, review any hardware wallet app that predates 2020 for deterministic-nonce and signature-reuse advisories before trusting it with fresh funds.

## Resources

- https://www.coindesk.com/business/2026/07/22/midnight-token-rebounds-after-wanchain-bridge-hack-hoskinson-calls-for-industry-overhaul
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Field Note — July 21, 2026](/itsalreadypriced/field-notes/2026/07/21/field-note/)
- [Field Note — July 20, 2026](/itsalreadypriced/field-notes/2026/07/20/field-note/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*