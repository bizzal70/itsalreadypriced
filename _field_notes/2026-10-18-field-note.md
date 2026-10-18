---
layout: field_note
title: "Field Note — October 18, 2026"
date: 2026-10-18
summary: "Cysic's bridge minted 10M CYS out of thin air and some of it hit the market before anyone noticed."
---

## Today's Field Note
Cysic halted its bridge after an attacker exploited bridge message processing to mint 10 million CYS without backing. Roughly 2.8 million CYS sits frozen at the recipient address, but onchain records show tokens were sold into the market before the blacklist landed, so the damage is already distributed to whoever held bids. Cysic claims mainnet and other systems are untouched and the issue was limited to bridge minting, which is the usual framing when the hole is narrow but real. Bridge mint bugs are the oldest trick in the book, and "we paused it" does not undo the CYS already dumped. Separately, the ConnectWise supply-chain breach compromised Microsoft 365 tenants via hijacked application identities, which matters for any crypto team using it for backup or MSP tooling.

## Today's Move
- If you hold CYS or LP against it, assume circulating supply is inflated and unwind CYS pairs before the frozen 2.8M becomes a governance or reissuance fight.
- Watch the Cysic recipient address and the bridge contract for any unpause or further mints before trusting it again.
- Do not bridge anything through Cysic until they publish a postmortem naming the exact message-processing flaw and the fix.
- If your org uses ConnectWise Cloud Backup or SkyKick, treat the listed app identities (506e08f9-6e9a-4da4-942b-a099a03644ae and the rest) as compromised, revoke them in Entra, and audit M365 access logs.
- Rotate any API keys or OAuth grants tied to ConnectWise-managed infrastructure.

## Resources

- https://thedefiant.io/news/hacks/cysic-halts-bridge-after-unauthorized-mint-of-10-million-cys
- https://www.bleepingcomputer.com/news/security/hackers-breach-microsoft-365-tenants-via-connectwise-supply-chain-attack/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)
- [Bitget Loses $388M to Spoofed Transfers, Not Stolen Keys](/itsalreadypriced/2026/09/27/issue-013/)
- [Address Poisoning and Clipboard Malware](/itsalreadypriced/rtfm/2026/09/16/address-poisoning-and-clipboard-malware/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*