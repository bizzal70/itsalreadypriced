---
layout: field_note
title: "Field Note — October 20, 2026"
date: 2026-10-20
summary: "Live software supply-chain and wallet-key risks (OVHcloud CLI backdoor, Qubic seed recovery), plus a reminder that the Drift thief is still moving $295M of DPRK loot."
---

## Today's Field Note
Two concrete builder-side exposures landed today. Attackers used a hijacked contributor GitHub account to swap five OVHcloud CLI release archives with a secret-stealer, live for up to 94 minutes (12:47 to 14:21 UTC on Oct 19); anything built or run from those releases should be treated as compromised, including any keys or cloud credentials sitting on disk. Separately, SlowMist showed Qubic wallet seeds could be reconstructed from six network samples, and the 4.26.4 patch only fixes new account seeds while leaving header generation unchanged, so old Qubic wallets stay exposed. Meanwhile the Drift exploiter, tied by Mandiant to a North Korean group after April's ~$295M hack, pushed another $54.8M to $61M in ETH through Tornado Cash and still sits on roughly $194M, confirming the laundering is active, not dormant. None of this is price noise. It is key hygiene.

## Today's Move
- If you installed or CI-pulled OVHcloud CLI on/after Oct 19, rebuild the machine, rotate every cloud credential, API token, and SSH key that touched it, and verify release hashes before reinstalling.
- Audit GitHub Actions and build pipelines that auto-fetch "latest" release archives; pin to verified checksums, not tags.
- Move funds out of any Qubic wallet created before the 4.26.4 patch to a freshly generated seed, and do not trust the patch for legacy accounts.
- Flag the Drift exploiter clusters (five Etherscan-labeled wallets holding ~84,164 ETH) in your monitoring and screening to avoid touching tainted post-Tornado flows.

## Resources

- https://www.bleepingcomputer.com/news/security/ovhcloud-cli-releases-backdoored-on-github-to-steal-developer-secrets/
- https://thehackernews.com/2026/10/hackers-hijack-five-ovhcloud-cli.html
- https://thedefiant.io/news/security/slowmist-says-qubic-wallet-keys-could-be-recovered-from-six-network-samples
- https://thedefiant.io/news/hacks/drift-linked-wallet-sends-54-8-million-in-eth-to-tornado-cash
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)
- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*