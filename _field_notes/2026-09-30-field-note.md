---
layout: field_note
title: "Field Note — September 30, 2026"
date: 2026-09-30
summary: "Bitget's $387.5M breach traces to an August 31 zero-day in third-party security tooling, and the launderers are now feeding funds through Zcash's shielded pool."
---

## Today's Field Note
The Bitget theft is no longer a mystery. SlowMist and the exchange now agree the $387.5M loss came from a zero-day in third-party security products, with malicious activity live on the network since August 31, weeks before withdrawals started. That means the intrusion sat inside the trust boundary you cannot see: vendor tooling, not the exchange's own contracts. The attackers have since routed roughly $4M into Zcash's shielded pool, which is the standard tell that tracing is about to go cold and recovery odds are dropping. Separately, the same supply-chain logic is playing out everywhere today: a Citrix NetScaler pre-auth flaw (CVE-2026-88772, CVSS 9.5) is under active exploitation for root, and TeamViewer is begging customers to patch high-severity bugs. The perimeter is the vendor, and the vendor is bleeding.

## Today's Move
- If you hold funds on Bitget, treat continuity as uncertain: reduce balances to what you actively trade and pull the rest to self-custody today.
- Watch the Zcash shielded-pool inflows and any transparent addresses on the exit side; flag them with your compliance/monitoring stack before they mix further.
- Patch Citrix NetScaler ADC/Gateway for CVE-2026-88772 now if any part of your infra touches it, and assume pre-auth compromise if it was exposed and unpatched.
- Apply TeamViewer's high-severity fixes on every operator and treasury machine; remote-access tooling is a direct path to signing keys.
- Audit which third-party security and monitoring vendors sit inside your withdrawal or signing flow, and revoke any standing access they no longer need.

## Resources

- https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products/
- https://www.coindesk.com/markets/2026/09/30/bitget-hackers-move-usd4-million-into-zcash-s-private-pool-making-funds-harder-to-trace
- https://thehackernews.com/2026/09/citrix-netscaler-cve-2026-88772-exploit.html
- https://www.bleepingcomputer.com/news/security/teamviewer-urges-users-to-patch-severe-flaws-as-soon-as-possible/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Coldcard Ships Firmware After $114M Bitcoin Theft](/itsalreadypriced/2026/08/23/issue-008/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*