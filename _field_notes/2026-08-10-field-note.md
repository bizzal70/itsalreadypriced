---
layout: field_note
title: "Field Note — August 10, 2026"
date: 2026-08-10
summary: "Coinsbuy loses $8M in a coordinated two-chain hit, and a malicious 'Solidity Pro' VS Code extension is draining dev wallets and keys."
---

## Today's Field Note
Two items with real teeth today. Crypto payment processor Coinsbuy lost roughly $8 million in a coordinated attack spanning two blockchains, the sort of simultaneous cross-chain drain that points at a compromised hot-wallet signing setup rather than a single contract bug. Separately, researchers flagged a malicious VS Code extension named "Solidity Pro" (published as helper-beeps.solidity-pro and web3devtoolsx.solidity-pro) that ships a browser-wallet and credential stealer straight onto builder machines. That second one matters more than the dollar figure suggests: if it is on your dev box, your keys, API tokens, and browser wallet are already gone. This is Lazarus-adjacent tradecraft (see Kimsuky's AI-themed phishing) aimed squarely at the people who write the contracts.

## Today's Move
- Uninstall any "Solidity Pro" VS Code extension (helper-beeps.solidity-pro, web3devtoolsx.solidity-pro) now, then treat that machine as compromised.
- On any dev box that ran it: rotate all API keys, exchange keys, and seed phrases, and move funds from any hot wallet touched on that machine to fresh keys.
- If you held funds on Coinsbuy, withdraw what remains and stop routing payments through it until they publish a full post-mortem.
- Audit VS Code and browser extensions across your team, pin to known-good publishers, and block install of unvetted marketplace extensions.
- Assume any "urgent" crypto-themed document or investment PDF is Kimsuky-style bait: open nothing in a signing environment.

## Resources

- https://www.coindesk.com/business/2026/08/10/crypto-exchange-coinsbuy-loses-usd8-million-in-coordinated-two-blockchain-attack
- https://thehackernews.com/2026/08/solidity-pro-vs-code-extensions-steal.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Issue #002 — Week of July 12, 2026](/itsalreadypriced/2026/07/12/issue-002/)
- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*