---
layout: field_note
title: "Field Note — September 26, 2026"
date: 2026-09-26
summary: "Bitget bleeds $387.5M to a suspected Lazarus operation, and legacy Magic Eden approvals become an active drain vector."
---

## Today's Field Note
Bitget lost $387.5 million after an attacker faked internal transfer requests to drain hot and warm wallets, with XRP and ETH dominating outflows and the CEO pointing at North Korea. Circle and Tether froze a wallet ("Bitget Exploiter 8") but caught only about $318,000 in USDC and USDT before the attacker swapped into unfreezable ETH, and $83M in stolen XRP has already moved beyond Ripple's reach. The lesson repeats: freeze functions are theater once funds hit native assets and the clock has run. Separately, a flaw in Limit Break's Payment Processor V2 exposed old Magic Eden Ethereum listings; whitehats (0xQuit) rescued 23,155 NFTs worth over $5.7M, but holders still carry live approvals to the vulnerable contracts. Withdrawals remain paused on Bitget.

## Today's Move
- If you hold funds on Bitget, assume withdrawals stay paused; do not chase deposits or believe "resuming shortly" until on-chain proof.
- Revoke NFT and token approvals to Limit Break's Payment Processor V2 and legacy Magic Eden contracts now (use revoke.cash or Etherscan token approval tool).
- If you listed Ethereum NFTs on Magic Eden previously, cancel those old listings and confirm no lingering operator approvals remain.
- Watch the "Bitget Exploiter 8" cluster and flag any downstream mixer or bridge hops; do not accept inbound transfers from tainted addresses.
- Builders on centralized platforms: audit internal-transfer authorization paths, the exact vector used here, and require multi-party signing for warm wallet movements.

## Resources

- https://decrypt.co/379350/bitget-hack-387m-what-happened-why-north-korea-suspect
- https://decrypt.co/379365/circle-tether-freeze-stablecoins-bitget-hack
- https://www.coindesk.com/markets/2026/09/26/bitget-hacker-moves-usd83-million-in-stolen-xrp-that-ripple-cannot-freeze
- https://decrypt.co/379342/magic-eden-old-ethereum-nft-listings-exposed-exploit
- https://thedefiant.io/news/hacks/legacy-magic-eden-approvals-exploited-as-white-hats-rescue-nfts
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Field Note — September 25, 2026](/itsalreadypriced/field-notes/2026/09/25/field-note/)
- [On-Chain Forensics and Following Stolen Funds](/itsalreadypriced/rtfm/2026/09/23/on-chain-forensics-and-following-stolen-funds/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*