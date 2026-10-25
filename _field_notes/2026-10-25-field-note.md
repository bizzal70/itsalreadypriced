---
layout: field_note
title: "Field Note — October 25, 2026"
date: 2026-10-25
summary: "The X100 governance takeover drained ~$4.85M and is laundering through ETH while Electrum patches a wallet flaw that already cost one user funds."
---

## Today's Field Note
The X100 exploit on Ethereum is not a smash and grab, it is a governance takeover. The attacker seized control, converted treasury tokens and liquidity positions into roughly 4.85 million USDT (Blockaid flagged it as ongoing), pulled another 549,916 X from a Uniswap pool, and has already split proceeds into four 400-ETH wallets and swapped about 4.75 million USDT into ether. That is textbook laundering structure, not panic. Separately, Electrum patched a flaw where a malicious server substitutes a fake payment and tricks you into signing it while bumping the fee, and at least one user already lost money. And Keystone's website was breached, exposing customer shipping addresses and order details (not seeds, but enough for targeted phishing and physical wrench attacks).

## Today's Move
- If you hold or LP any X100 governance or token positions, exit now and revoke all approvals tied to the protocol contracts via Revoke.cash. The attack is reported ongoing.
- Watch the four ~400-ETH distribution wallets and the USDT-to-ETH swapper flagged by The Defiant and Blockaid, and flag any inbound from them.
- Update Electrum immediately to the patched build. Until then, pin to a trusted server and verify output address and fee on your hardware screen before signing, never on the host.
- Keystone customers: assume your shipping address and order history are now in attacker hands. Expect fake "security" calls and phishing referencing your real order. Verify recovery phrase is still yours alone (it was not exposed), and ignore any unsolicited "upgrade" outreach.
- For any new X100-style governance protocol, check whether a single compromised proposal can drain the treasury before you deposit.

## Resources

- https://thedefiant.io/news/hacks/x100-exploit-nets-4-85-million-usdt-after-governance-takeover
- https://thedefiant.io/news/hacks/x100-exploit-proceeds-split-into-four-400-eth-wallets
- https://thedefiant.io/news/hacks/third-x100-exploit-transaction-pulls-550-000-x-from-uniswap-pool
- https://thedefiant.io/news/security/electrum-patches-wallet-flaw-exploited-through-malicious-servers
- https://thedefiant.io/news/security/keystone-website-breach-exposes-customer-addresses-and-order-details
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Address Poisoning and Clipboard Malware](/itsalreadypriced/rtfm/2026/09/16/address-poisoning-and-clipboard-malware/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*