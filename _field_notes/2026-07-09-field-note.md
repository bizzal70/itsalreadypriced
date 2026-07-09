---
layout: field_note
title: "Field Note — July 09, 2026"
date: 2026-07-09
summary: "A $999,999 USDT approval-phishing drain and a Hong Kong regulatory mandate both point at the same weak spot: signature hygiene."
---

## Today's Field Note
Same story, new victim. An Ethereum wallet signed a malicious ERC-20 approval on a phishing site and got drained of exactly 999,999 USDT in three multicall transactions (per Scam Sniffer). No smart contract was hacked, no key was stolen, the owner simply authorized a spender and moved on. Meanwhile Hong Kong's SFC has ordered platforms to roll out phishing-resistant login within 12 months, which tells you regulators now treat this class of loss as structural, not user error. Approvals are the attack surface that never sleeps, and multicall lets a drainer empty you in one confirmation.

## Today's Move
- Open revoke.cash (or Etherscan's token approval checker) and revoke every open USDT and USDC approval you are not actively using today.
- Kill infinite (unlimited) allowances specifically. Set exact-amount approvals per transaction going forward.
- Before signing anything, read the actual method: reject unexpected `approve`, `permit`, and `increaseAllowance` prompts from sites you did not initiate.
- Move core holdings to a hardware wallet or a fresh address that has never touched a dapp, and treat your hot wallet as burnable.
- If you use a Hong Kong venue, expect new login hardening within the year and enable hardware 2FA now rather than waiting for the mandate.

## Resources

- https://www.reddit.com/r/CryptoCurrency/comments/1urnh1n/a_brutal_lesson_in_crypto_crypto_user_lost_nearly/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)
