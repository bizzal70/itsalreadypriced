---
layout: field_note
title: "Field Note — July 26, 2026"
date: 2026-07-26
summary: "Two Ethereum bridges bled $31.7M in hours while a browser-built malware campaign impersonates Solana and TradingView to drain retail traders."
---

## Today's Field Note
Two Ethereum bridges lost a combined $31.7M within hours of each other, with a third protocol halting staking as a precaution. The pattern (rapid sequential drains) usually means either a shared dependency or copycats piling onto a freshly disclosed class of bug, so treat any bridge you touch as suspect until postmortems land. Separately, the SourTrade malvertising campaign (flagged by Confiant, corroborated by Bleeping Computer) is impersonating Solana, TradingView, and Luno with fake pages that assemble malware in browser memory using the legitimate Bun runtime, sidestepping single-file detection. Meanwhile Triple-A, a payments processor, confirmed a $9.7M wallet drain. This is a day to move funds out of anything with a bridge in the path and to stop clicking "fixes."

## Today's Move
- Pull liquidity and pending transfers from any Ethereum bridge until the two $31.7M drains are named and postmortemed. Do not assume yours is clean.
- Revoke approvals granted to bridge contracts and any dApp you touched in the last week via Revoke.cash or Etherscan token approvals.
- Do not follow any "fix this error" instructions from Steam forums, search ads, or fake TradingView/Solana/Luno pages. SourTrade builds the payload in your browser, so URL blocklists will not save you.
- If you interacted with Triple-A payment flows, rotate the receiving keys and watch for unexpected outbound transactions.
- Move signing to a hardware wallet and stop pasting seed phrases into anything, given the browser-memory malware in circulation.

## Resources

- https://www.reddit.com/r/CryptoCurrency/comments/1v6940c/two_ethereum_bridges_lose_317m_within_hours_as/
- https://thehackernews.com/2026/07/malvertising-sends-malware-in-pieces.html
- https://www.bleepingcomputer.com/news/security/malicious-sites-use-javascript-to-build-malware-in-browser-memory/
- https://www.reddit.com/r/CryptoCurrency/comments/1v6aplc/crypto_payments_firm_triplea_hit_by_97_million/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Issue #002 — Week of July 12, 2026](/itsalreadypriced/2026/07/12/issue-002/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*