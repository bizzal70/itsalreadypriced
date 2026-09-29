---
layout: field_note
title: "Field Note — September 29, 2026"
date: 2026-09-29
summary: "A drainer-fund story, an MCP OAuth flaw, and a HSM impersonation attack are the only things worth your attention today."
---

## Today's Field Note
NEAR Intents says it blocked roughly $50M in swaps tied to the Bitget hackers, actively filtering stolen funds while THORChain holds its line that it does not censor transactions. That is the real fault line: "permissionless" cross-chain routing now comes with discretionary blocklists that vary by protocol, so where you route matters. Separately, the official MCP Python SDK shipped a flaw (fixed in 1.30.0) where a malicious MCP server could harvest OAuth client secrets, authorization codes, and PKCE proofs by pointing the client at an attacker-controlled token endpoint. If you are wiring AI agents into wallets or exchange APIs, that is a direct credential-theft path. And a UC San Diego team impersonated a hardware security module without extracting its key, a reminder that "the key never leaves the HSM" is not the whole threat model.

## Today's Move
- Bump the MCP Python SDK to 1.30.0 or later today, and audit any agent that talks to an MCP server for leaked OAuth client secrets or exchange API keys. Rotate anything that touched an untrusted server.
- If you hold funds tied to Bitget-linked addresses or route large swaps, assume NEAR Intents will freeze the flow. Do not treat any single cross-chain router as guaranteed-permissionless.
- Review HSM-backed signing assumptions. Add transaction-level authorization checks rather than trusting HSM key isolation alone.
- Watch the Bitget hacker addresses and any THORChain routes they pivot to now that NEAR Intents is filtering.
- Patch Apple devices for CVE-2026-86950 (CoreGraphics zero-day) if you sign or hold keys on iOS or macOS.

## Resources

- https://cointelegraph.com/news/near-intents-says-it-blocked-50m-tied-to-bitget-hackers?utm_source=rss_feed&utm_medium=rss_tag_hacks&utm_campaign=rss_partner_inbound
- https://thehackernews.com/2026/09/official-mcp-python-sdk-flaw-can-let.html
- https://decrypt.co/379505/rsa-attack-without-stealing-key-what-it-means-crypto
- https://thehackernews.com/2026/09/apple-patches-coregraphics-flaw.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*