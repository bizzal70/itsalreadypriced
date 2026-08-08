---
layout: field_note
title: "Field Note — August 08, 2026"
date: 2026-08-08
summary: "BTCPay Server has a live, actively exploited flaw draining Lightning nodes, and a macOS ClickFix stealer is emptying crypto wallets."
---

## Today's Field Note
The BTCPay Server bug is the one to act on now. Operators are getting their Lightning nodes swept, with Foundation and Citadel21 both confirming drains in some cases hours before the public alert dropped. BTCPay says the flaw under active attack is not the one listed in the changelog, so treat this as a live zero-day and assume credential exposure. Version 2.4.2 is out. Separately, a Go-based macOS stealer delivered via ClickFix (fake "run this to fix it" prompts) is lifting wallet files, Keychain data, and browser passwords, and Microsoft flagged a parallel campaign using BNB Chain to host malicious payloads behind fake CAPTCHAs. Self-hosted infra and desktop hygiene are both the attack surface today.

## Today's Move
- Update every BTCPay Server instance to 2.4.2 immediately, or shut it down until you can. Do not wait for the changelog to match the exploit.
- Rotate all BTCPay credentials, API keys, and any hot wallet seeds touching a payment node. Assume they leaked.
- Move Lightning channel funds off exposed merchant nodes if you cannot patch within the hour.
- Never paste terminal commands from a website or "CAPTCHA verification" step. That is the ClickFix vector, and it targets macOS Keychain and wallet files directly.
- Treat any BNB Chain contract read triggered by a random site as hostile. Block the fake CAPTCHA scripts at the browser or DNS level.

## Resources

- https://thedefiant.io/news/hacks/btcpay-server-tells-operators-to-update-or-shut-down-over-actively-exploited-flaw
- https://decrypt.co/375159/bitcoin-payment-service-btcpay-critical-flaw-active-attack
- https://thehackernews.com/2026/08/clickfix-attacks-deliver-macos-stealer.html
- https://decrypt.co/375133/hackers-use-bnb-chain-spread-malware-fake-captchas
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*