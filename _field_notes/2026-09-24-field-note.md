---
layout: field_note
title: "Field Note — September 24, 2026"
date: 2026-09-24
summary: "Nothing on-chain today rises above phishing sentencing and market noise, but a WordPress RCE under mass exploitation and a placeholder-domain ClickFix trap are the real operational threats to crypto builders."
---

## Today's Field Note
No fresh protocol exploit or confirmed on-chain theft crossed the wire today. The signal is upstream, in the infrastructure crypto teams actually run on. Attackers are exploiting WordPress CVE-2026-87902 (CVSS 9.2, unauthenticated RCE) within hours of disclosure, which matters because half of crypto projects run their marketing sites, docs, and blogs on WordPress, and a compromised docs page is a direct route to swapping in a malicious contract address or drainer. Separately, the placeholder domain "third-party.com" (long used in dev docs and code examples) is now serving a fake Cloudflare verification page pushing ClickFix PowerShell payloads, so any dev who copy-pastes example code or clicks through a "verification" prompt is one step from a compromised machine holding keys. The Ronald Spektor sentencing (12 years for the $15.9M Coinbase social-engineering job) is a reminder that support-desk impersonation still empties accounts, not smart-contract bugs.

## Today's Move
- Patch any WordPress instance to the fixed release for CVE-2026-87902 today, and audit page templates and contract addresses on your docs/blog for tampering.
- Block or sinkhole "third-party.com" at your DNS resolver, and tell your team no Cloudflare page ever asks you to paste PowerShell.
- Kill copy-paste-to-terminal habits on dev machines that touch keys or deployment; move signing to hardware or an air-gapped box.
- Treat any unsolicited "Coinbase support" contact as hostile; Coinbase does not call about your account. Verify via the app, never a caller's link.
- Rotate credentials on any WordPress admin or CI system that was exposed while unpatched.

## Resources

- https://thehackernews.com/2026/09/attackers-exploit-wordpress-cve-2026.html
- https://www.bleepingcomputer.com/news/security/placeholder-domain-used-in-dev-docs-now-serves-clickfix-attacks/
- https://www.coindesk.com/business/2026/09/24/brooklyn-man-sent-to-prison-for-12-years-for-stealing-usd16m-in-a-coinbase-phishing-scheme
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Address Poisoning and Clipboard Malware](/itsalreadypriced/rtfm/2026/09/16/address-poisoning-and-clipboard-malware/)
- [Upgradeable Contracts and the Admin Key Problem](/itsalreadypriced/rtfm/2026/08/12/upgradeable-contracts-and-the-admin-key-problem/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*