---
layout: field_note
title: "Field Note — October 31, 2026"
date: 2026-10-31
summary: "North Korea drained $6.3B from Binance via a compromised dev laptop and an EIP-7702 delegation trick, while Chainalysis got breached and a tainted Trezor Safe 5 surfaced in the supply chain."
---

## Today's Field Note
The Binance $6.3B theft is the largest on record, and the mechanics matter more than the number. Richard Teng confirmed the attacker used a self-destruct contract and an EIP-7702 delegation to bypass Binance's approval controls, with the first domino being a single compromised engineer laptop. Tether, Circle, and Ripple froze roughly $2.7B, and Arbitrum's Security Council moved funds using emergency powers, so stolen 1INCH and other tokens were only partially contained. Separately, Chainalysis disclosed that an external actor used "offensive agentic techniques" to access customer names, emails, and org roles (no session tokens or investigation content), and Trezor flagged a suspected theft implant in a Safe 5 sold through reseller CryptoBilis in Southeast Asia. EIP-7702 delegation is now a live attack surface, not a theoretical one.

## Today's Move
- Audit any EIP-7702 delegations on your EOAs today. Revoke unknown delegated code via your wallet or a tool like revoke.cash before signing anything else.
- If you bought a Trezor Safe 5 from CryptoBilis or any non-official reseller, stop using it, move funds to a verified device, and treat the seed as compromised.
- Assume your Chainalysis-linked email and org role are leaking. Expect targeted spearphishing and rotate any shared or reused credentials tied to that address.
- Builders using hot-wallet signing infra: segregate signer laptops, enforce hardware isolation, and review approval flows that a delegated contract could abuse.
- Watch Binance's Sunday withdrawal restart and the known attacker addresses before assuming counterparty risk is cleared.

## Resources

- https://decrypt.co/382237/binance-sets-aside-6-34b-to-cover-hack-losses-ceo-says-your-assets-are-safe
- https://www.theblock.co/news/business/2026-10-30-binance-hack-largest-crypto-hack-north-korea-432225
- https://www.reddit.com/r/CryptoCurrency/comments/1xjq9o0/27b_of_the_binance_hack_was_saved_by_tether_and/
- https://www.chainalysis.com/blog/security-incident-october-30/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Address Poisoning and Clipboard Malware](/itsalreadypriced/rtfm/2026/09/16/address-poisoning-and-clipboard-malware/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*