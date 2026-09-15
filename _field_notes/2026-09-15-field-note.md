---
layout: field_note
title: "Field Note — September 15, 2026"
date: 2026-09-15
summary: "Cisco email gateway zero-day and a critical VMware vCenter RCE are both under active exploitation, while CoinEx announces an orderly shutdown with withdrawals open until December."
---

## Today's Field Note
Two infrastructure holes are being actively worked right now. Cisco confirmed CVE-2026-76461, a CVSS 9.8 flaw in Secure Email Gateway (AsyncOS) that lets an unauthenticated remote attacker execute commands as root via crafted email parsing, and it is already exploited in the wild. Separately, CISA reports ransomware crews have joined the crowd hitting the critical VMware vCenter RCE that was patched back in July, so anyone who deferred that patch is now on the clock. On the exchange side, CoinEx is winding down after nine years, claiming 100 percent reserves with withdrawals open only until December 22, 2026. "Orderly cessation" is a phrase that ages badly, so treat the deadline as the real one.

## Today's Move
- Patch Cisco Secure Email Gateway (AsyncOS) for CVE-2026-76461 today, and review mail logs for anomalous parsing errors or unexpected root-level processes.
- Apply the July VMware vCenter RCE patch immediately if still outstanding, and isolate any vCenter reachable from untrusted networks given the ransomware pivot.
- Withdraw all funds from CoinEx now rather than near the December 22 deadline. Do not wait for the queue.
- Segment dev infrastructure: the Vite mass-scanning campaign is siphoning AWS and Azure credentials from exposed dev servers, so pull any internet-facing dev instances behind a VPN.
- If you hold BAL, read the Balancer wind-down proposal and plan for treasury distribution mechanics before voting closes.

## Resources

- https://thehackernews.com/2026/09/cisco-secure-email-gateway-flaw.html
- https://www.bleepingcomputer.com/news/security/cisa-critical-vmware-vcenter-rce-flaw-now-exploited-by-ransomware-gangs/
- https://www.coindesk.com/business/2026/09/15/hong-kong-crypto-exchange-coinex-to-cease-operations-after-9-years-in-business
- https://thehackernews.com/2026/09/mass-scanning-campaign-exploits-vite.html
- https://www.theblock.co/news/defi/2026-09-15-balancer-proposes-winding-down-414782
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Exchange Custody, Counterparty Risk, and Proof of Reserves](/itsalreadypriced/rtfm/2026/09/09/exchange-custody-counterparty-risk-and-proof-of-reserves/)
- [Coldcard Ships Firmware After $114M Bitcoin Theft](/itsalreadypriced/2026/08/23/issue-008/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*