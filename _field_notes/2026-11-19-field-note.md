---
layout: field_note
title: "Field Note — November 19, 2026"
date: 2026-11-19
summary: "A sBOLD vault approval bug bleeds 3.43M BOLD, and a counterfeit Ledger campaign spreads to Germany and the UAE."
---

## Today's Field Note
Two supply-chain stories matter today, both old lessons in new packaging. K3 Capital's post-mortem pins the 3.43M BOLD drain on unused token-spending approvals left live in its sBOLD vault, the same stale-allowance pattern that keeps feeding drainers. Liquity's base protocol was untouched, so this is squarely a wrapper problem, not a BOLD problem. Separately, Ledger confirmed its counterfeit-device investigation has spread from Southeast Asia to Germany and the UAE, with new units showing the same physical tampering. If you bought hardware through any channel but the vendor direct, treat it as suspect, because a modified secure element does not care how careful your seed hygiene is.

## Today's Move
- Revoke any outstanding token approvals tied to K3's sBOLD vault contracts now, then audit remaining allowances across your addresses with revoke.cash or Etherscan's token approval tool.
- If you hold BOLD or sBOLD, exit or at minimum stop depositing into the affected vault until K3 ships a fixed contract and a public audit.
- Verify your Ledger was purchased direct from Ledger, not a marketplace reseller, and run a genuineness check before signing anything.
- If provenance is unclear, assume compromise: move funds to a freshly initialized device or clean signer, generating a new seed offline.
- Watch the Binance hacker wallets (another $248M in ETH moved today) if you run any address screening, and refresh your sanctioned-list filters against the 26,000-wallet living list.

## Resources

- https://thedefiant.io/news/security/k3-capital-says-sbold-vault-flaw-drained-3-43m-bold
- https://www.theblock.co/news/web3/2026-11-18-ledger-new-hardware-incidents-germany-uae-443530
- https://thedefiant.io/news/hacks/binance-hack-wallet-moves-another-248-million-in-eth
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Address Poisoning and Clipboard Malware](/itsalreadypriced/rtfm/2026/09/16/address-poisoning-and-clipboard-malware/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*