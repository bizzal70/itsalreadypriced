---
layout: field_note
title: "Field Note — November 17, 2026"
date: 2026-11-17
summary: "A supply-chain attack via Optimizely poisoned 178 major sites including Ledger and HSBC with wallet-swapping JavaScript, while the Binance hacker moved $137M in ETH."
---

## Today's Field Note
A malicious script served through website testing platform Optimizely (and reportedly Kissmetrics) hit at least 178 organizations, including Ledger, HSBC, BBC, Zoom, and CNN. The payload scans pages and your clipboard, validates checksums, and silently swaps crypto addresses across ETH/EVM, BTC, TRON, TON, Solana, Litecoin, BCH, and Doge, while skimming card data. This is address-replacement at the content-delivery layer, so a correct-looking copied address on a trusted site can still be the attacker's. Separately, the Binance exploiter moved nearly 75,000 ETH (about $137M) across eight transfers to seven addresses after two weeks of silence, worth watching for laundering routing. On the exchange side, Aster and Lighter both bled from leaked API keys ($4.56M alleged, ~$5M returned respectively), a reminder that API wallet hygiene is the current soft spot.

## Today's Move
- Verify every withdrawal address out-of-band today. Check the full string, not just the first and last characters, and confirm via a second channel for anything large.
- Treat clipboard paste as hostile. Hardware-wallet users: confirm the address on the device screen, not the browser, since the swap happens client-side on trusted sites like Ledger's own.
- Audit and rotate exchange/DEX API keys now (Aster, Lighter, and any perp venue). Delete unused API wallets and restrict IP allowlists and withdrawal permissions.
- Patch and update iOS devices immediately. The same campaign drops an iPhone exploit loader (DarkSword), per 1inch, so move funds to a fresh wallet on a clean device if you suspect compromise.
- Tag the Binance hacker's seven receiving addresses and watch for mixer or bridge deposits if you run monitoring.

## Resources

- https://decrypt.co/383414/optimizely-hack-hijacked-ledger-bbc-and-176-other-sites-to-swap-crypto-wallet-addresses
- https://www.coindesk.com/tech/2026/11/17/hackers-planted-crypto-stealing-code-on-178-organizations-sites-including-hsbc-bbc-and-ledger
- https://www.reddit.com/r/CryptoCurrency/comments/1xye9iw/poisoned_scripts_on_major_sites_ledger_bbc_zoom/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Address Poisoning and Clipboard Malware](/itsalreadypriced/rtfm/2026/09/16/address-poisoning-and-clipboard-malware/)
- [A French Bank Lost $133M Through Its Own Vendor's Account](/itsalreadypriced/2026/11/08/issue-019/)
- [On-Chain Forensics and Following Stolen Funds](/itsalreadypriced/rtfm/2026/09/23/on-chain-forensics-and-following-stolen-funds/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*