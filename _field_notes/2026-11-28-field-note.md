---
layout: field_note
title: "Field Note — November 28, 2026"
date: 2026-11-28
summary: "Solana validators get an urgent Agave upgrade, Chainflip stays paused after a vault theft, and a pCloud Pass breach bypassed 2FA."
---

## Today's Field Note
Three operational items today, none of them price noise. Anza is telling Solana mainnet operators to upgrade to Agave v4.4.2 immediately (Jito-Solana and Harmonic have matching builds); clusters are running normally, which is the window you want for patching, not the aftermath. Chainflip remains paused after its November vault theft and is routing new trades through SwapKit while it tallies losses and drafts a payout plan, so treat the native protocol as offline. Separately, pCloud Pass confirmed a breach where unknown devices connected to accounts even with 2FA enabled, a bad failure mode for a password manager that may be guarding your seed phrases and exchange logins. The AI-breaks-Bitcoin paper (Ledger, Blockstream) is theoretical with no practical 256-bit shortcut; ignore the headlines.

## Today's Move
- Solana validators: upgrade to Agave v4.4.2 now (or the matching Jito-Solana / Harmonic builds). Do it while clusters are healthy, not during an incident.
- Stop routing through Chainflip's native protocol while it stays paused. Any pending swaps should be considered stuck until the payout plan is published.
- If you use pCloud Pass, rotate every credential stored in it, revoke unknown device sessions, and reset 2FA. Move any seed phrases or exchange secrets out of it entirely.
- Chiliz Chain holders: bridge USDC off via ChainPort (Arbitrum, BNB Chain, or Avalanche) before Dec. 1, after which withdrawals are not guaranteed.
- SafePal buyers from the August breach window: ignore any firmware-update emails or letters. Verify firmware only through the official app.

## Resources

- https://thedefiant.io/news/blockchains/anza-urges-immediate-agave-upgrade-on-solana-mainnet
- https://thedefiant.io/news/hacks/chainflip-tallies-hack-losses-payout-plan-still-pending
- https://www.bleepingcomputer.com/news/security/pcloud-confirms-password-manager-hack-after-suspicious-login-alerts/
- https://thedefiant.io/news/infrastructure/chiliz-urges-holders-to-bridge-usdc-off-its-chain-before-chainport-shutdown
- https://thedefiant.io/news/security/safepal-extends-august-breach-disclosure-to-older-orders
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)
- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*