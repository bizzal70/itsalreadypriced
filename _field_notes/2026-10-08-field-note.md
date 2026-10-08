---
layout: field_note
title: "Field Note — October 08, 2026"
date: 2026-10-08
summary: "Malicious Firefox wallet extensions and a compromised tensorlake npm package are actively stealing keys and secrets, while the 'bunker mode' panic is mostly noise."
---

## Today's Field Note
Two live credential-theft campaigns matter today, and neither is theoretical. Researchers flagged 16 malicious Firefox extensions posing as Rabby and OKX wallet portals that intercept recovery phrases and private keys during import flows and exfiltrate them. Separately, the npm package "tensorlake" was compromised at version 0.5.144 as part of the ChainDrop / Shai-Hulud worm, shipping obfuscated malware that harvests credentials, establishes persistence, and runs remote code (if you build on it, your CI secrets are already assumed gone). Meanwhile Justin Drake's "bunker mode" call, now echoed by Buterin, is a real long-term cryptography question dressed up as a today emergency. Ledger's CTO is right that a rushed mass migration to fresh addresses will drain more wallets through user error than any AI will.

## Today's Move
- Audit your Firefox extensions now. Remove anything impersonating Rabby or OKX, and never type a seed phrase into a browser extension import flow.
- If "tensorlake" is anywhere in your dependency tree, pin away from 0.5.144, purge node_modules and lockfiles, and rotate every credential and token reachable from your build pipeline.
- Rotate CI/CD secrets, npm tokens, and cloud keys on the assumption Shai-Hulud already exfiltrated them, then check for unexpected persistence and outbound calls.
- Ignore the "bunker mode" urgency. Do not blindly sweep funds to new addresses today. Verify any migration guidance against primary sources first.
- Revoke stale token approvals on hot wallets while you are already in cleanup mode.

## Resources

- https://thehackernews.com/2026/10/16-malicious-firefox-extensions-pose-as.html
- https://thehackernews.com/2026/10/tensorlake-npm-package-compromised-to.html
- https://thedefiant.io/news/security/justin-drake-urges-bunker-mode-migration-to-fresh-crypto-addresses
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Address Poisoning and Clipboard Malware](/itsalreadypriced/rtfm/2026/09/16/address-poisoning-and-clipboard-malware/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*