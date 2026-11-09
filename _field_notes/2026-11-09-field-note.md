---
layout: field_note
title: "Field Note — November 09, 2026"
date: 2026-11-09
summary: "A Web3Auth flaw drained Keplr social-login wallets, LNbits told every operator to pull the plug, and Coinify quietly suspended trading after a hot wallet breach."
---

## Today's Field Note
Three custody failures landed at once, all pointing at the same lesson: your keys are only as safe as the infrastructure holding them. A flaw at Web3Auth let an attacker reach Keplr wallets created via Google or Apple sign-in, and Web3Auth then used the attacker's own route to drain other at-risk wallets "for safety," meaning if you used social login you may have been swept either way. LNbits told all operators to shut down their Lightning servers amid active attacks, after at least one lost roughly 0.023 BTC (2,285,545 sats) to a withdrawal exploit, with fixes still pending. And Coinify disclosed a Sunday breach affecting hot wallet withdrawals, suspending trading and payments while it reviews. None of these are market noise. They are live infrastructure compromises.

## Today's Move
- If your Keplr wallet was created via Google or Apple (Web3Auth) social login, treat it as compromised: generate a fresh seed-phrase wallet and move any residual funds now.
- Shut down your LNbits server until the project ships its pending fixes, and audit recent withdrawal logs for unauthorized new-account activity.
- Stop initiating Coinify orders and payments; confirm pending settlements before assuming they cleared, and don't trust the "no funds affected" line until a full post-mortem lands.
- Audit every wallet tied to a social-login or MFA-as-a-service provider and migrate critical balances to self-custodied seed phrases or hardware.
- Watch for drainer follow-on: cracked "TradingView Premium" malware (flagged by SlowMist) is actively harvesting wallet data on Windows, so avoid pirated trading tools.

## Resources

- https://thehackernews.com/2026/11/web3auth-flaw-exploited-to-steal-keplr.html
- https://thehackernews.com/2026/11/lnbits-urges-all-operators-to-shut-down.html
- https://www.reddit.com/r/CryptoCurrency/comments/1xrofbl/coinify_breached/
- https://thedefiant.io/news/security/slowmist-flags-cracked-tradingview-premium-as-wallet-data-malware
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*