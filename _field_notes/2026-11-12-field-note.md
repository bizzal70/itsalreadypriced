---
layout: field_note
title: "Field Note — November 12, 2026"
date: 2026-11-12
summary: "Chainstack breach forces node credential rotation, Bitcoin Core discloses a Tor peer-trust bug, and a GitHub supply chain attack bleeds CI secrets from 1,800+ repos."
---

## Today's Field Note
Three infrastructure items matter today, none of them price action. Chainstack confirmed a breach and is treating all node credentials as exposed, telling customers to rotate credentials and change passwords (services stayed online, but assume your RPC endpoints and keys are compromised). Bitcoin Core disclosed a bug that made thousands of nodes trust any stranger connecting over Tor, weakening the peer-selection assumptions those nodes relied on. Separately, an attacker used 4,837 hijacked GitHub accounts to plant a CI secret stealer in at least 1,806 repositories, harvesting cloud credentials and any secrets reachable from build workflows. If you run blockchain infra, depend on a third-party RPC, or ship code through CI, you were in blast radius this week.

## Today's Move
- If you use Chainstack, rotate all node credentials and change account passwords now. Reissue any API keys or RPC endpoints and update dependent apps.
- Audit CI secrets across your GitHub org: rotate cloud keys, deploy tokens, and signing keys reachable from workflows, and check Actions logs for unexpected runs since Tuesday.
- Enforce phishing-resistant 2FA on GitHub accounts with write access and review recently granted OAuth apps and PATs.
- Update Bitcoin Core to the patched release if you run a node, and confirm you are not accepting unauthenticated inbound Tor peers.
- Treat any app pointing at third-party RPC as untrusted until its provider confirms clean: avoid signing high-value transactions through those endpoints today.

## Resources

- https://thedefiant.io/news/security/chainstack-urges-credential-rotation-after-data-breach
- https://www.theblock.co/news/ecosystems/2026-11-12-chainstack-security-breach-438509
- https://www.coindesk.com/tech/2026/11/12/bitcoin-core-reveals-bug-that-made-thousands-of-nodes-trust-any-stranger-on-tor
- https://thehackernews.com/2026/11/4837-hijacked-github-accounts-ran-ci.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [A French Bank Lost $133M Through Its Own Vendor's Account](/itsalreadypriced/2026/11/08/issue-019/)
- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*