---
layout: field_note
title: "Field Note — September 12, 2026"
date: 2026-09-12
summary: "Blockstream refuses ransom on the Liquid exploit, GitLab ships a CVSS 10 file-read bug already being probed, and JFrog Artifactory flaws are being chained for backdoors."
---

## Today's Field Note
Blockstream confirmed it will not pay the extortionist behind the Liquid Network exploit, with roughly 598.5 BTC (about 47 million dollars) still outstanding after 3,400 BTC came back. Peg-outs remain disabled while the negotiation plays out in public via OP_RETURN, so anyone holding L-BTC or running Liquid-adjacent infrastructure is exposed to a frozen bridge, not a clean recovery. Separately, two infrastructure bugs matter more for builders than any price tick: GitLab's CVE-2026-85706 (CVSS 10.0 path traversal in the commits API, unauthenticated arbitrary file read) is already seeing in-the-wild probes within hours, and JFrog Artifactory flaws are being chained to bypass auth and drop a Rust backdoor on self-hosted servers. If your CI/CD or artifact registry touches keys, this is a supply-chain problem, not an IT ticket.

## Today's Move
- If you hold L-BTC, assume peg-outs stay disabled and do not treat Liquid as a live exit path. Watch the OP_RETURN thread for status, not the ransom drama.
- Patch GitLab now for CVE-2026-85706. If you cannot patch today, restrict the commits API and check logs for path-traversal reads of config and secrets files.
- Patch self-hosted JFrog Artifactory and audit for the Rust backdoor. Rotate any deploy keys, signing keys, or registry tokens that lived on those servers.
- Assume any secrets exposed via GitLab or Artifactory are burned. Rotate CI/CD credentials and re-sign affected artifacts before you trust another build.
- Builders using Claude Artifacts or shared AI chat links: treat them as untrusted download vectors given the active weaponization campaigns.

## Resources

- https://thedefiant.io/news/security/blockstream-rejects-ransom-demand-after-liquid-bitcoin-exploit
- https://decrypt.co/377959/blockstream-refuses-ransom-for-return-of-47m-in-bitcoin-from-liquid-hack-it-is-theft
- https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Coldcard Ships Firmware After $114M Bitcoin Theft](/itsalreadypriced/2026/08/23/issue-008/)
- [A 2021 PRNG Bug Drained $89M From Coldcard Wallets in 41 Minutes](/itsalreadypriced/2026/08/02/issue-005/)
- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*