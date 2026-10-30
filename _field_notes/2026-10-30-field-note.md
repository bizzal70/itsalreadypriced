---
layout: field_note
title: "Field Note — October 30, 2026"
date: 2026-10-30
summary: "Binance lost $6.3B via a compromised DevOps laptop, withdrawals are paused, and the attacker is dumping low-liquidity tokens onchain."
---

## Today's Field Note
Binance, the largest exchange on earth, has been drained of roughly $6.3B, with Chainalysis and TRM attributing it to North Korea's TraderTraitor. The entry point was mundane: a compromised DevOps engineer's laptop, followed by what Richard Teng calls "additional points of breach," not a one-click fluke. EIP-7702 did not cause this but appears to have helped the attacker bypass withdrawal safeguards, and about $3.3B has already been swapped into assets that cannot be frozen. Withdrawals are paused (45-hour restart estimate), and the exploiter is actively dumping low-liquidity tokens like FUN (down 95%), RAD, and OGN into Uniswap pools. Separately, Trezor flagged a suspected hardware implant in Safe 5 units sold by reseller CryptoBilis, broadcasting recovery phrases over cellular.

## Today's Move
- If you bought a Trezor from CryptoBilis since March 2026, treat the seed as burned: move funds to a new device with a freshly generated recovery phrase today.
- Do not hold working balances on Binance while withdrawals are paused; wait for a clean restart and proof-of-reserves before re-depositing anything you cannot lose.
- Review and revoke any EIP-7702 delegations on your EOAs (check via revoke.cash or Etherscan's authorization list); the attacker leaned on this mechanism.
- Exit or pull liquidity from thin Uniswap pools in the exploiter's dump path (FUN, RAD, OGN) rather than providing exit liquidity for stolen bags.
- If you use Unit, Jupiter Lend, or Aave, note the freezes and delayed withdrawals; stage exits now rather than when caps tighten further.

## Resources

- https://www.bleepingcomputer.com/news/security/binance-links-63-billion-crypto-theft-to-compromised-devops-laptop/
- https://decrypt.co/382224/trm-and-chainalysis-tie-6-4b-binance-hack-to-north-koreas-tradertraitor
- https://thedefiant.io/news/markets/fun-plunges-95-in-uniswap-pool-as-binance-exploiter-sells
- https://thehackernews.com/2026/10/trezor-warns-of-suspected-hardware.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*