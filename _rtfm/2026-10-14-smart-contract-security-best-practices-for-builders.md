---
layout: rtfm
title: "Smart Contract Security Best Practices for Builders"
date: 2026-10-14
summary: "Reentrancy keeps draining protocols decades after it was solved, because checks-effects-interactions is unglamorous discipline that builders skip until the exploit writes their postmortem for them."
framework: "ConsenSys Smart Contract Best Practices"
framework_url: "https://consensys.github.io/smart-contract-best-practices/"
---

Reentrancy is not a zero-day. It is not an exotic cryptographic failure or a novel class of bug that nobody saw coming. It is a vulnerability pattern older than most of the people writing Solidity today, with a fix so well-documented it fits in a single hyphenated phrase: checks-effects-interactions. And yet protocols still get drained by it with depressing regularity, because the fix is boring, boredom does not ship, and "we'll audit it later" is the most expensive sentence in this industry.

## The Standard

The canonical reference here is the ConsenSys Smart Contract Best Practices guide, and its treatment of reentrancy is not ambiguous. The core prescription is the **checks-effects-interactions** pattern, and it describes the order in which a function should do its work:

1. **Checks.** Validate everything first. Require the caller has the balance, the inputs are sane, the state permits the action.
2. **Effects.** Update your own contract's state next. Decrement balances, flip flags, write storage. Do this *before* you talk to anyone else.
3. **Interactions.** Only now do you call out to external addresses: transfer ETH, call another contract, trigger a token hook.

The logic is mechanical. When your contract makes an external call, it surrenders control flow to the callee. If that callee is a malicious contract (or a benign one with a malicious hook), it can call back into your function before the first invocation finishes. If you have not yet updated your state, the reentrant call sees stale data. It sees a balance you were about to zero out but have not. So it withdraws again. And again. The call stack unwinds and your contract is empty.

Checks-effects-interactions defeats this by ensuring that by the time control leaves your contract, your internal accounting already reflects the action. The reentrant call hits a require that fails, or a balance that is already zero. There is nothing to drain.

The guide pairs this with two supporting controls. First, **reentrancy guards**: a mutex, typically implemented as a `nonReentrant` modifier (OpenZeppelin's `ReentrancyGuard` is the reference implementation), that sets a lock on entry and reverts any reentrant call while the lock is held. Second, a healthy distrust of external calls in general, with the guide explicitly warning that `call` forwards all gas and that any external interaction is a potential handoff of control. These are defense in depth. The pattern is the foundation. The guard is the seatbelt.

## Where It Breaks Down

If the fix is this well-known, the interesting question is why it keeps failing. The answer is that reentrancy in 2024-era codebases is rarely the textbook case. It mutates.

**Cross-function reentrancy.** Developers protect `withdraw()` with the pattern and consider the job done. But the attacker does not reenter `withdraw()`. They reenter a *different* function that reads the same state variable. Function A updates balances last, function B reads balances to compute a transfer. Reenter B from inside A's external call and B sees the stale balance. A `nonReentrant` modifier on A alone does nothing here unless B shares the same lock. People forget that the mutex must cover every function that touches the shared state, not just the obvious one.

**Read-only reentrancy.** This is the one that embarrasses otherwise careful teams. A `view` function cannot change state, so it feels safe. But if a lending protocol or AMM exposes a price or a share value through a view function, and that view reads state mid-update during an external call, an attacker can reenter and query the view while your contract is in an inconsistent intermediate state. The view returns a wrong price. A downstream protocol that trusts that oracle makes a decision on bad data. The vulnerable contract never loses funds directly. The *consumer* of its view function does. Reentrancy guards that only protect state-mutating functions leave this door wide open.

**The ERC-777 and ERC-721 hook problem.** The old mental model was "ERC-20 `transfer` does not call back, so a token transfer is a safe interaction." That model is dead. **ERC-777** introduced `tokensReceived` and `tokensToSend` hooks that hand control to the recipient on every transfer. **ERC-721** and **ERC-1155** have `onERC721Received` and `onERC1155Received` callbacks. **ERC-677** and various transfer-and-call schemes do the same. The moment you integrate a token with a receive hook, a function you believed had no external calls suddenly has one, invoked implicitly by what looks like a simple transfer. Builders who hardcoded the assumption that token transfers are inert get surprised by composability they never opted into.

**The `.call` migration that reintroduced the bug.** When `transfer` and `send` were effectively deprecated for forwarding ETH (because the fixed 2300 gas stipend broke against proxy wallets and gas repricing), the ecosystem moved to low-level `.call{value: ...}("")`. Correct for gas, but `.call` forwards *all* remaining gas, which is exactly enough for a recipient to run a full reentrant attack. Teams that migrated their send mechanism without revisiting their function ordering handed attackers the gas budget they previously lacked.

**Cross-contract and cross-protocol reentrancy.** In a world of composable protocols, the reentrant call does not have to come back to your contract at all. It can route through a third protocol that calls back into yours, or exploit the fact that two of your contracts share a state assumption that only holds when neither is mid-execution. Single-contract mutexes do not reason about this.

The through-line: every one of these is checks-effects-interactions violated somewhere, by someone who thought this particular call was safe. The pattern did not fail. The developer's model of where the external calls *were* failed.

## Doing It Right

Concrete, implementable, non-negotiable.

- **Treat checks-effects-interactions as a hard rule, not a preference.** Update all state before any external call, in every function, without exception. If you catch yourself writing an external call before a state write, stop and reorder. This costs nothing and prevents the entire textbook class.
- **Enumerate your external calls honestly.** Any ETH transfer via `.call`, any token transfer that might trigger a hook, any call to an address you do not fully control. Assume every token could be ERC-777. Assume every NFT transfer invokes a callback. If the token address is attacker-controllable, assume the callback is hostile.
- **Use a reentrancy guard, and share it across functions that share state.** OpenZeppelin's `nonReentrant` is cheap insurance, but a mutex on one function is theater if a sibling function reads the same variable. Group functions by shared state and lock them together.
- **Defend your view functions.** If external protocols will consume your prices, share values, or any derived state, your view functions must not return values read mid-update. Either apply read-only reentrancy protection (check the guard state in the view and revert if locked) or architect so that no external call ever happens while the state the view reads is inconsistent.
- **Run the tooling.** Static analyzers (Slither) flag reentrancy patterns and state-after-call ordering automatically. Symbolic execution and fuzzing (Echidna, Foundry invariant tests) can find cross-function cases a human misses. Property-based invariant tests that assert "total deposits always equals sum of balances" catch drains that unit tests sail past. None of this is optional for anything holding value.
- **Prefer the pull-payment pattern where you can.** Instead of pushing funds out mid-logic, let users withdraw their own balance in a separate, isolated transaction. This collapses the interaction surface to a single, guarded, state-first function.

## The Bottom Line

The thing about reentrancy is that nobody loses funds to it because they did not know better. They lose funds because knowing better and doing better are separated by the gap where discipline is supposed to live, and discipline does not generate a demo-day screenshot. Checks-effects-interactions has been the answer for the entire life of this ecosystem, and it will still be the answer long after whatever you are building is forgotten. The exploit is not clever. It never was. It just waits for the one function where you decided the external call looked harmless.

*It was already priced. The audit just hadn't been written yet.*

## Related

- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)
- [Upgradeable Contracts and the Admin Key Problem](/itsalreadypriced/rtfm/2026/08/12/upgradeable-contracts-and-the-admin-key-problem/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)
