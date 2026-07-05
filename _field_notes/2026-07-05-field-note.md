---
layout: field_note
title: "Approvals are the attack surface you forgot you signed"
summary: "Most wallet drains don't crack your key. They cash a permission you granted months ago."
date: 2026-07-05
---

<span class="chain-badge">ON-CHAIN</span>

Here is the pattern behind a large share of wallet drains: the attacker never touches your seed phrase. They do not need it. Months ago you approved a token spend to interact with some contract, granted an unlimited allowance because the UI defaulted to it, and moved on. That allowance is still live. When the contract turns malicious, or was malicious all along, it simply spends what you already let it spend.

Approvals do not expire. They sit on-chain until you revoke them. A wallet you consider dormant can be emptied through a permission you forgot you gave.

**The habit:** audit your allowances on a schedule, not after something goes wrong. Revoke anything you are not actively using, and never grant unlimited when a fixed amount will do.

## Sources

- Check and revoke token approvals: [Etherscan Token Approval Checker](https://etherscan.io/tokenapprovalchecker) (and the equivalent explorer for each chain you use)
- Standard being exploited: [EIP-20 `approve` / `transferFrom`](https://eips.ethereum.org/EIPS/eip-20)
