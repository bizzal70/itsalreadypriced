---
layout: rtfm
title: "Signature Requests and Blind Signing"
date: 2026-07-22
summary: "A first-principles look at why blind-signing EIP-712 messages, especially token permits, remains the fastest way to lose a wallet, and how to actually read what you sign."
framework: "EIP-712 (Typed Structured Data Signing)"
framework_url: "https://eips.ethereum.org/EIPS/eip-712"
---

Every wallet you have ever used has a button that says "Sign." Almost nobody who clicks it can tell you what they just authorized, and the industry has spent years building tooling that makes this ignorance feel safe. It is not safe. The single most efficient way to empty a wallet in production today is not a smart contract exploit or a bridge failure, it is a human being clicking "Sign" on a structured message they did not read and could not have read if they tried.

## The Standard

EIP-712 is the specification for signing typed structured data. It exists because the older approach, `eth_sign` and `personal_sign` over an opaque hash or arbitrary byte string, was unreadable by design. When you signed a raw 32-byte hash, you were signing entropy. You had no way to know whether that hash committed you to a harmless login challenge or to a transfer of your entire balance.

EIP-712 tried to fix the human-facing half of the problem. It defines a canonical way to encode a structured message so that a wallet can display it as fields instead of a hash. The message has a `types` definition, a `domain` separator, and the actual `message` payload. The domain separator is the important part most people ignore: it binds a signature to a specific `name`, `version`, `chainId`, and `verifyingContract`. In principle this means a signature intended for one contract on one chain cannot be replayed against another.

The encoding is deterministic. You hash the type definition to get a `typeHash`, you hash the struct data according to that type, you concatenate the domain separator, and you produce the digest that gets signed. `keccak256("\x19\x01" || domainSeparator || hashStruct(message))`. That prefix is not decoration. It exists specifically so that an EIP-712 digest can never collide with a regular transaction or a `personal_sign` payload. The standard did its job. It gave wallets everything they need to show you a legible, scoped, human-readable description of what you are about to authorize.

The problem is that legibility is optional, and almost everyone opts out.

## Where It Breaks Down

Start with the mechanism that does most of the damage: EIP-2612 `permit`. This is an EIP-712 typed signature that authorizes a token spend without an on-chain approval transaction. The signed struct contains an `owner`, a `spender`, a `value`, a `nonce`, and a `deadline`. When you sign it, you produce a signature that anyone holding it can submit to the token contract to grant `spender` an allowance of `value`. No gas from you. No second confirmation. The signature is the authorization.

Now consider what a drainer does. It presents a dApp that needs you to "verify your wallet" or "approve to continue." What you are actually signing is a `permit` with `spender` set to the attacker's contract, `value` set to `type(uint256).max`, and a `deadline` far in the future. You click Sign. Nothing happens in your wallet. No transaction appears. There is no pending confirmation, no gas estimate, no red warning, because from your wallet's perspective you did not transact, you merely signed a message. The attacker then submits your signature and the follow-up `transferFrom` in a single bundle, often through a batch contract, and your balance is gone in one block.

The related pattern is `Permit2`, the router-based approval system many aggregators use. Permit2 signatures are also EIP-712, and they encode a `PermitTransferFrom` or `PermitBatch` with a spender, amounts, and a `sigDeadline`. A single Permit2 signature can authorize transfers of multiple tokens at once. This is convenient for legitimate routers and catastrophic when the router address in the message is hostile. The signed data will faithfully contain the malicious spender. It is right there in the struct. Nobody reads it.

Here is why nobody reads it, and this is where the wallets share the blame. A large fraction of dApps do not sign proper EIP-712 typed data. They fall back to `eth_sign` or feed raw bytes, and the wallet renders the infamous full-width warning that users have been trained to click through. Worse, many wallets that do receive valid EIP-712 payloads still render the message as a wall of raw fields: hex-encoded addresses, a `value` printed as `115792089237316195423570985008687907853269984665640564039457584007913129639935`, a `deadline` as a Unix timestamp. Technically legible. Practically meaningless to a human at click speed. The domain separator, the one field that would tell you which contract this signature binds to, is usually collapsed or hidden entirely.

Then there is the deeper failure, which is that the signing surface and the transacting surface look different to users and identical to attackers. People have internalized that a transaction costs gas and shows a confirmation, so they treat transactions with suspicion. A signature is "free" and "just a message," so they treat it as harmless. This mental model is exactly backwards for permits. An off-chain signature can be more dangerous than a transaction because it produces no on-chain footprint until the attacker chooses to use it, which may be days later, from an address you never interacted with.

Contract-side, builders make it worse by requesting broad, long-lived permits when they need narrow, short-lived ones. Requesting `type(uint256).max` as the permit value because it saves a future signature is normalizing infinite approvals as the default UX. A `deadline` set to `type(uint256).max` turns a one-time authorization into a permanent standing order. Every one of these is a decision to trade the user's safety for one fewer click.

## Doing It Right

For holders, the rules are unglamorous and they work.

Treat every signature request as a transaction. The absence of a gas fee is not evidence of safety, it is the opposite. If a site asks you to sign something to "connect" or "verify," it does not need that. Connection is `eth_requestAccounts` and costs no signature. A signature request during login is either SIWE (EIP-4361, which is human-readable plain text and says exactly what it is) or it is something you should refuse.

Read the domain and the spender. On any typed-data prompt, find `verifyingContract` in the domain and the `spender` in the message. If either is an address you do not recognize and cannot map to the protocol you think you are using, stop. This is the single highest-value habit available to you.

Use a wallet or extension that decodes and simulates. The tooling category you want performs transaction and message simulation, showing you the net asset changes a signature would enable, not just the raw fields. A simulator that says "this signature can move all of your USDC to 0xUnknown" is worth more than any amount of self-discipline.

Revoke standing allowances periodically. Use an allowance dashboard to review and zero out approvals and Permit2 authorizations you no longer need. An infinite allowance you granted a year ago is a loaded weapon left on the counter.

For builders, the guidance is equally direct.

Sign real EIP-712 typed data, never `personal_sign` over encoded structs. If your wallet integration shows a raw-bytes warning, you have already failed the user. Populate `domain` fully and correctly, including `chainId` and `verifyingContract`, so replay protection actually holds.

Scope your requests. Request the exact `value` you need, not `uint256` max. Set a `deadline` measured in minutes, not centuries. If your product cannot function without infinite, perpetual approvals, redesign the product, do not offload the risk onto users who cannot read the request.

Name your types honestly. The `typeHash` is derived from the type string, and wallets display field names to users. A struct field called `spender` communicates intent. A field called `data` communicates nothing.

## The Bottom Line

EIP-712 gave us everything we needed to make signing legible, and we responded by building interfaces that hide the one field that matters behind a button people have been conditioned to reflexively press. The standard is not broken. The habit is. You will keep hearing that self-custody means being your own bank, and the part nobody says out loud is that it also means being your own signing officer, the one who is supposed to read the document before stamping it. Most people will not. The drainers are counting on exactly that, and they are rarely disappointed.

*Read the message. It is the only part of the transaction that was ever actually yours to control.*

## Related

- [Field Note — July 22, 2026](/itsalreadypriced/field-notes/2026/07/22/field-note/)
- [Field Note — July 21, 2026](/itsalreadypriced/field-notes/2026/07/21/field-note/)
- [Field Note — July 20, 2026](/itsalreadypriced/field-notes/2026/07/20/field-note/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)
