---
layout: field_note
title: "Field Note — October 26, 2026"
date: 2026-10-26
summary: "A hardware wallet key theft, an Ethereum signing advisory, and a Bitcoin wallet bug all demand hands-on-keys action today."
---

## Today's Field Note
Keystone is bricking 18,835 wallets after a device-authentication key was stolen, meaning units shipped and received after Oct. 20 can pass the normal online verification check and still be counterfeit. The attacker holds the key that signs "this is a genuine Keystone," so your usual authenticity test is now worthless. Separately, Consensys has warned Ethereum operators about eMudhra signing risks: default setups are fine, but certain Web3Signer deployments with vulnerable Java trust stores need immediate access-control changes. And CoinDesk reports a Bitcoin wallet bug where rogue Electrum-style servers could steal funds when users tried to fee-bump (RBF/CPFP) a payment. None of these are theoretical. All three are live today.

## Today's Move
- If you bought a Keystone received after Oct. 20, stop using it, run Keystone's additional authenticity checks (not just the online verify), and move funds to a known-good device before signing anything.
- Ethereum node and validator operators: audit your Web3Signer config today, check Java trust stores for eMudhra exposure, and lock down access controls per the Consensys advisory even if you think you are on defaults.
- Bitcoin users: hold off on fee-bumping stuck transactions through untrusted servers, update your wallet to the patched release, and prefer your own node or a trusted Electrum server.
- Watch the X100 exploiter: 420.8 ETH already went to Tornado Cash with roughly 1,602 ETH still sitting in four holding wallets. Blacklist those addresses if you run a protocol or front end.
- Blast bridge users: $40 million is still stranded with the withdrawal deadline hit. Follow the contract-level exit guide, budget for the one-day wait, and claim USDB as DAI separately.

## Resources

- https://thedefiant.io/news/security/keystone-to-destroy-18-835-wallets-after-device-authentication-key-theft
- https://thedefiant.io/news/security/consensys-warns-ethereum-operators-of-emudhra-signing-risks
- https://www.coindesk.com/tech/2026/10/26/bitcoin-wallet-bug-let-rogue-servers-steal-funds-when-users-tried-to-speed-up-payments
- https://thedefiant.io/news/hacks/x100-exploiter-sends-420-8-eth-to-tornado-cash
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [The Week AI Agents Learned to Sign Away Your Whole Balance](/itsalreadypriced/2026/10/25/issue-017/)
- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)
- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*