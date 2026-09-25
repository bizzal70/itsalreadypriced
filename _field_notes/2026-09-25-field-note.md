---
layout: field_note
title: "Field Note — September 25, 2026"
date: 2026-09-25
summary: "Bitget bled $351.6M from hot wallets to a suspected DPRK crew, and an old Limit Break contract is being drained of NFTs live on Ethereum."
---

## Today's Field Note
Two live losses today, one old, one fresh. Bitget confirmed $351.6M pulled from hot and warm wallets at 18:31 UTC on Sept 24, withdrawals suspended, CEO Gracy Chen blaming spoofed transfers (not key compromise) with IPs matching DPRK VPN patterns; the firm points to a $464M User Protection Fund to make users whole. Separately, an attacker began draining NFTs via Limit Break's Payment Processor V2, the settlement contract Magic Eden used on its Ethereum marketplace through October 2024, exploiting a bug that lets anyone claim NFTs still approved to it for 0 ETH. Whitehat 0xQuit front-ran the thief and moved roughly 23,155 NFTs (~$5.7M) to protective custody, returnable once owners revoke. If you traded NFTs on Magic Eden's Ethereum marketplace in 2024 and never cleaned up, you are exposed right now.

## Today's Move
- Revoke any NFT approvals to Limit Break's Payment Processor V2 (Ethereum) today via revoke.cash or Etherscan token approvals, especially if you used Magic Eden's ETH marketplace in 2024.
- Do not treat 0xQuit's rescue as safety: your approval is still live until you revoke, so revoke before requesting your NFTs back.
- If you hold funds on Bitget, assume withdrawals stay frozen; move only what you can once they reopen, and do not chase "recovery" DMs.
- Watch the Bitget attacker consolidation addresses and the User Protection Fund payout mechanics before deciding whether to trust the "funds safe" line.
- Builders: audit any legacy settlement or payment contracts you deprecated but never revoked from at the user level; forgotten approvals are the attack surface.

## Resources

- https://thehackernews.com/2026/09/bitget-says-suspected-north-korean.html
- https://www.coindesk.com/markets/2026/09/25/bitget-s-usd351-million-hack-happened-via-spoofed-transfers-not-private-keys-ceo-gray-chen-says
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)
- [On-Chain Forensics and Following Stolen Funds](/itsalreadypriced/rtfm/2026/09/23/on-chain-forensics-and-following-stolen-funds/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*