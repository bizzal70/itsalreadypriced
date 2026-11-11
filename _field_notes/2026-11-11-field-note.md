---
layout: field_note
title: "Field Note — November 11, 2026"
date: 2026-11-11
summary: "Across domain hijack, LNbits wallet thefts, and Initia's second exploit in three weeks all land the same day, a reminder that infrastructure is the soft target."
---

## Today's Field Note
Three infrastructure failures hit in one window, none of them clever cryptography. Across Protocol lost control of its official domain via a social engineering attack on registrar Namecheap, redirecting users to a phishing site that drained wallets of anyone who signed. LNbits shipped an emergency patch after reported Bitcoin wallet thefts, warning that older installs are exposed and that upgrading alone is not enough (credentials must be rotated). And Initia confirmed its second exploit in three weeks, $3.27M moved via compromised cloud credentials, with about $2.16M frozen on the halted chain. The common thread is boring: DNS, stale deployments, and leaked cloud keys, not zero-days.

## Today's Move
- If you touched the Across website or signed anything cross-chain in the last 48 hours, revoke approvals (revoke.cash or Etherscan token approvals) immediately and move funds to a fresh address.
- Bookmark Across's contract addresses directly and stop trusting the domain for now; verify any URL against their official GitHub or X before interacting.
- LNbits operators: upgrade to the patched release now, then rotate all wallet credentials and admin keys, and treat pre-patch balances as potentially compromised.
- Initia users: keep funds off the halted network until a post-mortem lands, and watch the attacker address flagged in the disclosure for movement of the unfrozen ~$1.1M.
- Builders: audit where your cloud credentials and registrar accounts live, enable registrar lock and MFA, and assume social engineering of your registrar is in scope.

## Resources

- https://www.theblock.co/news/defi/2026-11-11-crosschain-protocol-across-restores-systems-after-domain-hijack-437843
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Address Poisoning and Clipboard Malware](/itsalreadypriced/rtfm/2026/09/16/address-poisoning-and-clipboard-malware/)
- [Upgradeable Contracts and the Admin Key Problem](/itsalreadypriced/rtfm/2026/08/12/upgradeable-contracts-and-the-admin-key-problem/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*