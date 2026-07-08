---
layout: rtfm
title: "Token Approvals and the Infinite Allowance"
date: 2026-07-08
summary: "Infinite token approvals are the quiet mechanism behind most drained wallets, and understanding EIP-20's allowance model is the difference between an inconvenience and a total loss."
framework: "EIP-20 (approve / allowance)"
framework_url: "https://eips.ethereum.org/EIPS/eip-20"
---

Your seed phrase is probably fine. That is the part nobody wants to hear, because it means the thing that emptied a wallet was not some sophisticated key extraction or a compromised hardware device. It was a signature the owner produced voluntarily, months earlier, and forgot about. Token approvals are the most boring attack surface in the entire ecosystem, which is exactly why they remain the most productive one.

## The Standard

EIP-20, the fungible token standard that everything on Ethereum and its clones descends from, does not let contracts touch your balance directly. A token is just a ledger inside a contract: a mapping of addresses to numbers. When you hold `1000 USDC`, there is no coin in your wallet. There is an entry in the USDC contract that says your address is owed `1000`, and your private key is the only thing that can authorize moving that entry.

The problem the standard had to solve is that most useful things (swapping, lending, providing liquidity, staking) require a *different* contract to move your tokens on your behalf. You cannot hand a DEX router your private key. So EIP-20 defines a delegation primitive built from two functions.

`approve(spender, amount)` is you, the token owner, telling the token contract: "this `spender` address is permitted to move up to `amount` of my tokens." The contract records this in an `allowance` mapping, keyed by owner and spender.

`transferFrom(from, to, amount)` is the spender later saying: "move `amount` of tokens from this owner to this destination." The contract checks the recorded allowance, and if there is enough, it moves the tokens and decrements the allowance.

That is the whole mechanism. `allowance(owner, spender)` is a public view function so anyone can read how much any spender is authorized to pull from any owner. There is no expiry. There is no per-transaction confirmation. Once the allowance is set, the spender can call `transferFrom` at any point in the future, as many times as it likes, up to the approved amount, with no further input from you. The standard was designed this way on purpose. It is a standing authorization, not a one-time permission slip.

## Where It Breaks Down

The rot is in a single number: `amount`.

Setting an exact allowance for every interaction is annoying. If you want to swap `500 DAI`, you would `approve` the router for `500 DAI`, then swap. Next week, when you want to swap another `500`, the allowance is spent and you have to approve again. Each approval is its own transaction with its own gas cost and its own wallet popup. So the industry converged, years ago, on a shortcut: approve `2^256 - 1`. The maximum value a `uint256` can hold. Infinite allowance.

Now the router never has to be re-approved. The UX is smooth. You swap once and never see the approval prompt again. This became the default behavior baked into front ends, into router integrations, into the "Approve" button you click without reading. Most people have granted unlimited allowances to dozens of contracts and have no memory of doing so.

Here is the failure mode, and it has nothing to do with your keys.

An infinite allowance is a permanent, standing right for a contract to drain a specific token from your wallet. Its safety is entirely contingent on that contract remaining honest and remaining uncompromised, *forever*. The contract you approved might be a genuine protocol today. But consider what "the contract" actually is:

- **Upgradeable proxies.** A huge fraction of DeFi contracts sit behind a proxy pattern (transparent proxy, UUPS, diamond). The address you approved is the proxy. The logic can be swapped by whoever controls the admin key. You approved an address, not a behavior. If the implementation behind that address changes, or the upgrade key is compromised, your standing allowance now points at code you never reviewed.

- **Phishing approvals.** The classic drain. A malicious site presents a transaction that looks like a claim, a mint, or a connect step. What you are actually signing is `approve(attacker, 2^256-1)` on a token you hold. Nothing leaves your wallet in that transaction, so nothing looks wrong. The gas is trivial. Days later, the attacker calls `transferFrom` and your balance is gone. Your seed never left the hardware wallet. You signed the theft yourself and confirmed it on the device screen.

- **Permit and Permit2.** EIP-2612 `permit` lets you approve via an off-chain signature instead of an on-chain transaction, gasless from the token owner's perspective. Permit2 generalizes this. The security tradeoff is that a signature request looks even more innocuous than a transaction, and wallets historically rendered these as opaque hex or unhelpful typed-data blobs. A signed `permit` is a bearer authorization: whoever holds it can submit it. Phishing a signature is often easier than phishing a transaction because users have been trained that "signing is free and safe."

- **The `approve` race condition.** The original EIP-20 has a known flaw: changing a nonzero allowance to a new nonzero value creates a window where a watching spender can front-run and spend both the old and new allowances. This is why the convention is to set allowance to zero first, then to the new value. Many integrations still get this wrong.

- **Compromised front ends.** The contract can be flawless and the approval legitimate, but the website serving the interface can be hijacked (DNS, a poisoned dependency, a malicious script injection). The front end silently swaps the approval target. You think you are approving the protocol. You are approving an attacker's address.

In every one of these, the seed phrase is irrelevant. The exploit rides on an authorization the owner granted and never revoked.

## Doing It Right

**For holders:**

Treat every approval as a liability you are carrying until you cancel it. Audit them. Wallet-scanner tools and approval dashboards (the category exists across every major chain) let you enumerate every outstanding `allowance` your address has granted and revoke the ones you no longer need. Do this on a schedule, not after something goes wrong.

Prefer exact approvals over infinite ones. Modern wallets increasingly let you edit the approval amount at signing time. Approve what the transaction needs. The extra gas of occasional re-approval is cheap insurance against a standing unlimited grant.

Read what you sign. If a wallet shows you `approve` with an amount of `115792089237316195423570985008687907853269984665640564039457584007913129639935`, that is `2^256 - 1`. That is infinite. Treat any signature request on a page you did not fully trust as hostile, especially `permit` and Permit2 typed-data prompts, which do not cost gas and therefore feel harmless.

Segregate. Keep long-term holdings in an address that never interacts with contracts, and use a separate "hot" address for DeFi. An approval on your hot wallet cannot touch tokens it does not hold. A drained hot wallet is an inconvenience. A drained cold vault is a life event.

**For builders:**

Stop defaulting to infinite approvals in your front end. Request the exact amount. If your UX genuinely needs standing allowances, make that a deliberate, visible choice, not the silent default behind an "Approve" button.

Support and encourage revocation. If your protocol issues approvals, give users a first-class path to see and cancel them.

Render signatures honestly. If you build wallets, decode `approve`, `permit`, and Permit2 payloads into human language: which spender, which token, how much, and flag infinite amounts loudly. Opaque hex is complicity.

Use minimal, time-bounded authorizations where the primitive allows it. Permit2 supports expirations. Use them.

## The Bottom Line

The approval mechanism is not broken. It does exactly what EIP-20 says it does, which is grant a standing, expiry-free right to move your tokens to whoever you point it at. The failure is entirely social and habitual: an ecosystem that trained an entire generation of users to click "Approve" without reading, to sign gasless messages without thinking, and to leave unlimited allowances open for years. The drain does not need your keys because you already signed the permission. You will keep granting infinite approvals, and you will keep meaning to revoke them, and most of you will get around to it right after the transfer clears.

*It was already priced in the moment you clicked Approve.*