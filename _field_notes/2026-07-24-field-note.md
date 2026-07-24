---
layout: field_note
title: "Field Note â€” July 24, 2026"
date: 2026-07-24
summary: "Odos is winding down with a hard July 30 withdrawal deadline, and a fresh batch of exploitable flaws (Redis RCE PoCs, NodeBB, ChatGPT AgentForger) landed the same day."
---

## Today's Field Note
Odos Protocol, the DEX aggregator, announced a shutdown with a one week window: withdraw by July 30 or wager that a decommissioned frontend and unmaintained contracts stay reachable and safe. No reason given, which is its own reason. Separately, the infrastructure floor gave way underneath everyone: Redis shipped seven security releases on July 23 after researchers published authenticated RCE proof-of-concepts against stock 6.2.22, 7.4.9, 8.6.4, and 8.8.0 (all four chains require RESTORE, some need EVAL), and NodeBB patched eight high-severity flaws in versions before 4.14.0 with exploit code already public. If your stack caches sessions or price data in Redis, or runs a NodeBB forum, this is your Thursday.

## Today's Move
- Withdraw all funds from Odos before July 30. Do not trust the UI to persist. Interact with contracts directly if the frontend goes dark, and revoke any lingering token approvals to Odos router contracts.
- Patch Redis now to 6.2.23, 7.2.15, or 7.4.10 (and the 8.x fixes). If you cannot patch today, restrict RESTORE, EVAL, and XGROUP via ACLs and lock Redis off the public internet.
- Upgrade NodeBB to 4.14.2 immediately. Exploit code is public and the simplest chain is a settings change, so assume opportunistic scanning has already started.
- If you run OpenAI Workspace Agents, confirm you are past the June 8 AgentForger fix and audit for any agents deployed via phishing links.
- Run a quick revoke.cash pass on wallets that touched Odos or any winding-down aggregator this cycle.

## Resources

- https://thehackernews.com/2026/07/kimi-k3-agents-found-redis-zero-days.html
- https://thehackernews.com/2026/07/nodebb-patches-eight-ai-found-flaws.html
- https://thehackernews.com/2026/07/chatgpt-agentforger-flaw-could-deploy.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Issue #002 — Week of July 12, 2026](/itsalreadypriced/2026/07/12/issue-002/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*