---
layout: field_note
title: "Field Note — November 22, 2026"
date: 2026-11-22
summary: "Two live bridge mint exploits (Chainflip, Cyber) and a signer compromise, both with exchanges already freezing transfers."
---

## Today's Field Note
Two bridges bleeding at once. Chainflip confirmed a $12M drain (122.86 BTC plus Ethereum outflows) from what looks like an automated attack on a compromised signing key, dropped FLIP ~30%, and is now begging the attacker to keep 10% as a "white-hat" fig leaf with a Nov. 23 deadline. Separately, Cyber reported unexpected CYBER minting on Solana followed by tokens draining out of its Ethereum lockbox, prompting Upbit and Bithumb to freeze CYBER deposits and withdrawals entirely. Different protocols, same old story: mint authority and signing keys are the soft underbelly of every cross-chain design, and once the key goes, the bounty email is all you have left. If you touch either bridge, you are already downstream of the mint.

## Today's Move
- Stop using the Cyber bridge now. Do not deposit or withdraw CYBER until Cyber confirms the Ethereum lockbox and Solana mint authority are secured.
- Pull liquidity and open positions from Chainflip vaults and revoke any lingering token approvals to Chainflip contracts.
- If you hold CYBER on an exchange other than Upbit or Bithumb, assume supply is inflating and treat on-chain balances as unreliable until a post-mortem lands.
- Watch the Chainflip attacker address through the Nov. 23 bounty deadline. A non-return means laundering begins, likely via Tornado Cash as seen in the Cysic bridge case.
- Builders running cross-chain mint authority: audit your signer setup today, enforce multisig or MPC on mint and lockbox keys, and rate-limit mint functions.

## Resources

- https://thedefiant.io/news/hacks/chainflip-offers-10-bounty-for-return-of-stolen-funds
- https://thedefiant.io/news/hacks/cyber-warns-against-bridge-use-after-unexpected-minting
- https://www.theblock.co/news/defi/2026-11-21-cyber-investigating-suspected-1-million-bridge-exploit-as-upbit-bithumb-freeze-transfers-444810
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*