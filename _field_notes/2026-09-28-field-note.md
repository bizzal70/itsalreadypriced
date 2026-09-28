---
layout: field_note
title: "Field Note — September 28, 2026"
date: 2026-09-28
summary: "Fake GIWA bridge drains 766 ETH, a Robinhood Chain rug nets $18.4M, and Zano rolled back a month of chain history after a Gateway Address exploit."
---

## Today's Field Note
Three separate onchain thefts landed in the same day, and none of them required a fancy zero-day. DYORSWAP bridged to a "GIWA Layer 2" that does not exist yet (Dunamu's Upbit-backed GIWA mainnet has not launched), losing 766 ETH (~$2M) to a spoofed network and now offering partial reimbursement. On Robinhood Chain, an analyst tied $18.4M in memecoin extractions to a single operator who exempted insider wallets from Pons V2's anti-sniping tax and let them buy up supply before dumping. And Zano restarted its chain at the block before Hard Fork 6, unwinding a month of history because its new Gateway Addresses feature was exploitable. The pattern is old: unverified infrastructure, privileged carve-outs, and a fresh consensus feature shipped without enough eyes.

## Today's Move
- If you touched DYORSWAP or any "GIWA" bridge, stop. GIWA mainnet is not live. Revoke approvals on the fake contract and do not chase the 40% reimbursement with more transactions.
- Verify chain IDs and official RPC endpoints from the project's own domain before bridging anywhere. A network that "does not exist yet" cannot be bridged to.
- Avoid Robinhood Chain Pons V2 launches until the tax-exemption mechanism is audited. Check onchain whether deployer wallets are exempt from anti-sniping fees before buying.
- If you hold or ran a Zano node, confirm you are on the post-rollback chain (pre Hard Fork 6 height) and treat any Gateway Address balances as suspect until the fix ships.
- Watch the Bitget hacker flow through THORChain (THORChain refused to blacklist, $6M already moved to BTC) if you clear funds via THOR pools.

## Resources

- https://www.theblock.co/news/defi/2026-09-27-onchain-analyst-links-18-4-million-in-robinhood-chain-memecoin-extractions-to-single-rug-pull-operation-416960
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)
- [Reading a Token Contract Before You Buy the Rug](/itsalreadypriced/rtfm/2026/08/26/reading-a-token-contract-before-you-buy-the-rug/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*