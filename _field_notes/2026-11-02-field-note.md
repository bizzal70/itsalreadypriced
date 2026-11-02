---
layout: field_note
title: "Field Note — November 02, 2026"
date: 2026-11-02
summary: "BTCPay Server tells merchants to shut down servers as hot wallets are drained on 2.4.1 and older, while a GitLab max-severity RCE is under active exploitation."
---

## Today's Field Note
Two things need your hands today, both operational, both running now. BTCPay Server is telling merchants to physically switch off servers after confirmed hot wallet drains tied to versions 2.4.1 and older, days after it shipped an emergency fix in 2.4.7. Separately, over 1,000 internet-exposed GitLab servers remain unpatched against a maximum-severity RCE that attackers are already exploiting, which matters to any team running self-hosted CI next to key material. The Binance $6.3B laundering saga is loud (XRP split across six wallets, Bitcoin mixing flagged by Elliptic, THORChain paused on a reorg bug), but for most of you it is spectator sport. The exposure you can actually close is your own infrastructure, so close it.

## Today's Move
- If you run BTCPay Server on 2.4.1 or older, take the server offline now, move funds off the hot wallet, then rebuild on 2.4.7 before restarting.
- Audit any self-hosted GitLab instance exposed to the internet, patch to the fixed release immediately, and check CI runners for unexpected jobs or outbound connections.
- Rotate any keys, tokens, or secrets that touched a vulnerable BTCPay or GitLab host, assume compromise if it was exposed and unpatched.
- Pull hot wallet balances on any self-hosted payment stack down to operational minimums until you have confirmed patch status.
- Watch the Binance attacker XRP wallets (six recipients, $292M) at your exchange deposit layer if you operate one, native XRP cannot be frozen so interception happens on ingress.

## Resources

- https://decrypt.co/382324/btcpay-tells-merchants-to-switch-off-servers-amid-hot-wallet-attack-reports
- https://thedefiant.io/news/hacks/btcpay-links-hot-wallet-drains-to-versions-2-4-1-and-older
- https://www.bleepingcomputer.com/news/security/over-1-000-gitlab-servers-vulnerable-to-code-execution-attacks/
- https://thedefiant.io/news/hacks/binance-attacker-splits-292-million-in-xrp-across-six-wallets
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [An OpenAI Model Drained a Stranger's Wallet to Pay Its Own Gas](/itsalreadypriced/2026/10/18/issue-016/)
- [Coldcard Ships Firmware After $114M Bitcoin Theft](/itsalreadypriced/2026/08/23/issue-008/)
- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*