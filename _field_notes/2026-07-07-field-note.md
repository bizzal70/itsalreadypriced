---
layout: field_note
title: "Field Note — July 07, 2026"
date: 2026-07-07
summary: "A governance attacker turned $4.4M into $21.2M by buying enough BONK to pass a malicious treasury proposal, while a trader ate a $2M same-block backrun on a route they never checked."
---

## Today's Field Note
The BONK governance treasury got drained for roughly $21.2M by an attacker who spent about $4.4M acquiring voting weight to push through a malicious proposal, netting around $16.8M. This is the standard governance-capture play: if quorum is cheap relative to what the treasury holds, someone will eventually do the math. Separately, a trader lost $2M to a same-block backrun extraction after signing a transaction without reading the route, a reminder that MEV bots do not care about your conviction. Neither of these needed a zero-day. Both needed you to not check the thing in front of you.

## Today's Move
- If you hold BONK or LP against it, watch the treasury and governance contracts for further malicious proposals and pending execution, and pull exposure until the token holders re-secure quorum.
- For any DAO you hold governance tokens in, check the ratio of treasury value to the cost of passing a proposal. If capture is cheaper than the prize, treat it as compromised.
- Before signing any swap, actually read the transaction route and simulate it (Tenderly, Rabby, or your wallet's preview). Same-block backruns hit large orders on thin routes hardest.
- Split large trades and use tight slippage plus private/MEV-protected RPC (Flashbots Protect, MEV Blocker) rather than trusting the default mempool.
- Patch BeyondTrust Remote Support and PRA now (CVE-2026-40138, auth bypass, CVSS 9.2) if any custody or ops infra sits behind it.

## Resources

- https://www.coindesk.com/markets/2026/07/07/bonk-faces-usd20-million-treasury-drain-after-attacker-spends-usd4-million-to-pass-malicious-proposal
- https://thehackernews.com/2026/07/beyondtrust-patches-critical-auth.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)
