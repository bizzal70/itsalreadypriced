---
layout: field_note
title: "Field Note — October 28, 2026"
date: 2026-10-28
summary: "A Zilliqa bridge exploit, an Avalanche tranche vault drain, and a Bithumb internal breach define the day's real losses."
---

## Today's Field Note
Three separate hits today, none of them theoretical. Zilliqa pulled its X-Bridge in both directions and the CEO stepped down amid a security probe, with PlunderSwap reporting losses across four token pools. On Avalanche, a Tranche vault was drained of 1.01 million USDC via a flash loan that minted inflated tranche shares then redeemed the real collateral (Blockaid confirms the identified contract is empty). Separately, Bithumb (South Korea's second-largest exchange) says attackers reached an internal employee mobile system and leaked personal data, part of a cluster of Korean financial breaches this week. Bridges and leveraged vault math remain the soft targets, and exchange insider systems are the new perimeter.

## Today's Move
- Exit any Zilliqa X-Bridge positions and PlunderSwap pools now; the bridge is halted, do not try to force transactions through.
- If you hold Tranche protocol positions on Avalanche, withdraw from unaffected vaults and revoke approvals to the Tranche contracts until a post-mortem lands.
- Treat the Bithumb leak as a phishing vector: assume your email and phone are exposed, rotate exchange passwords, and move off SMS 2FA to an authenticator or hardware key.
- Watch the Tranche attacker address for USDC movement and bridging to Ethereum; flag it to your bridge and mixer monitors.
- Separately, patch Tailscale to 1.104.4 if you run Tailscale SSH on any infra touching keys or signers.

## Resources

- https://thedefiant.io/news/security/zilliqa-ceo-steps-down-as-board-takes-oversight-amid-security-probe
- https://thedefiant.io/news/hacks/tranche-vault-on-avalanche-drained-of-1-01-million-usdc
- https://thehackernews.com/2026/10/tailscale-patches-ssh-flaws-that-could.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [On-Chain Forensics and Following Stolen Funds](/itsalreadypriced/rtfm/2026/09/23/on-chain-forensics-and-following-stolen-funds/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*