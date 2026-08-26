---
layout: rtfm
title: "Reading a Token Contract Before You Buy the Rug"
date: 2026-08-26
summary: "The exit scam is usually written into the token contract in plain Solidity before you ever hit buy, and reading it takes less time than the loss takes to hurt."
framework: "OWASP Smart Contract Top 10"
framework_url: "https://owasp.org/www-project-smart-contract-top-10/"
---

The rug is not a surprise. It is a function. Somewhere in the bytecode you approved, there is almost always a line that lets someone mint supply, freeze your balance, or tax your exit to zero, and it was there before you bought, sitting in public storage, waiting for you to not read it. People will spend forty minutes comparing gas fees and zero seconds checking whether the contract owner can blacklist their wallet. The information asymmetry in a rug pull is not technical. It is behavioral.

## The Standard

The OWASP Smart Contract Top 10 is the closest thing this industry has to a shared checklist, and it exists precisely because these failures repeat. It is not a novel document. It restates, in a form auditors and builders can point at, the categories of defect that keep draining wallets: access control flaws, price oracle manipulation, logic errors, reentrancy, unchecked external calls, and so on. For the specific problem of buying a token that is engineered to trap you, three entries carry most of the weight.

The first is access control (the perennial top entry in one form or another). The standard says, in plain language, that privileged functions must be restricted to the correct roles, that those roles must be intentional, and that ownership must be either renounced or governed transparently. A `mint` function guarded by `onlyOwner` is not a bug. It is a documented capability. The standard does not tell you it is forbidden. It tells you that you, the reader, are supposed to know it exists and reason about who holds the key.

The second is logic errors, which OWASP uses as a catch-all for functions that do something other than what a naive user assumes. A transfer function that silently applies a 99 percent fee when a flag is set is not broken. It executes exactly as written. The defect is in your expectation, not the code.

The third is unchecked or dangerous external calls and upgradeability, because a proxy pattern (EIP-1967, transparent or UUPS) means the code you read today is not necessarily the code that runs tomorrow. The standard's guidance is blunt: know whether the contract is upgradeable, and know who can upgrade it. An immutable contract with a mint function is a known quantity. An upgradeable contract that looks clean today is a promise from a stranger.

The framework does not promise safety. It gives you a vocabulary for the ways you are about to be robbed.

## Where It Breaks Down

The failures are boring and consistent, which is what makes them survivable if you look.

**Mint functions with no cap.** The most common trap is an ERC-20 with an owner-callable `mint` that has no maximum supply check. The token page shows a fixed supply. The contract shows that supply is a suggestion. When the deployer decides to leave, they mint themselves several orders of magnitude more tokens and sell into whatever liquidity you provided. This is not hidden. It is a public function in the verified source. People miss it because they read the token's marketing supply number on an aggregator and never open the code.

**Ownership theater.** A deployer calls `renounceOwnership`, the explorer shows the owner as the zero address, and everyone relaxes. Meanwhile the contract has a second privileged role, `_authority` or `_taxWallet` or a plain unnamed address checked in a `require`, that was never renounced and never will be. OpenZeppelin's `Ownable` is one pattern. `AccessControl` with named roles is another. A hand-rolled `require(msg.sender == someHardcodedAddress)` is a third, and it does not show up as an "owner" anywhere convenient. Renouncing `Ownable` while retaining a custom admin is one of the oldest sleights in the deck.

**Blacklists and allowlists disguised as compliance.** A `_isBlacklisted` mapping, or an `_isExcludedFromFee` inverted into a de facto whitelist, lets the deployer prevent specific addresses from selling. The honeypot variant is elegant: anyone can buy, but the transfer function reverts for any address not on an allowlist that only ever contains the deployer. Your buy succeeds. Your sell reverts every time. On-chain, this looks like a token nobody can sell, which is exactly what it is.

**Mutable fees.** A `setFee` function with no upper bound. You buy at a 3 percent tax. Before you sell, the fee is set to 100 percent, or to 99 with a floor that swallows the rest to gas. The fee variable is a state variable, the setter is `onlyOwner`, and the ceiling that should be enforced in the setter is simply absent.

**Upgradeable proxies as a blank check.** The implementation contract you read on the explorer is clean. It is also not the contract users interact with. The proxy at EIP-1967 storage slots delegates to an implementation the admin can swap at will. A malicious upgrade replaces `transfer` with a honeypot after liquidity has accumulated. The tell is in the storage slots and the admin address, not in the pretty implementation code everyone reads.

**Wallet behavior finishes the job.** The reason none of this gets caught is the approval flow. Users click through `approve` for `type(uint256).max` because the wallet UI presents unlimited approval as the default convenience, and because reading a hex calldata blob in a signing prompt is not something the interface encourages. The contract's malice and the wallet's opacity meet exactly at the confirm button. Simulation is available. Most people confirm blind.

**Unverified source, or verified-but-unread.** Half the rugs ship unverified bytecode, and people buy anyway on the theory that the chart looks good. The other half verify the source, correctly assuming that verification itself functions as a trust signal and that almost nobody reads what was verified.

## Doing It Right

You do not need to be an auditor. You need a checklist and fifteen minutes.

**Open the verified source.** If it is not verified, that is your answer. If it is, read the token functions specifically: `transfer`, `transferFrom`, `_transfer`, and every function with an access modifier. You are looking for branches, fee math, and mappings that gate transfers.

**Grep for the capabilities, not the promises.** Search the source for `mint`, `blacklist`, `whitelist`, `setFee`, `setTax`, `pause`, `onlyOwner`, `setMax`, and `owner`. Every match is a capability someone holds over your position. For `mint`, confirm whether there is a hard cap enforced in the function body, not just declared as a constant that is never checked.

**Enumerate every privileged role.** Do not stop at `owner`. Look for `AccessControl` roles, hardcoded addresses in `require` statements, and secondary admin variables. Check whether ownership is actually renounced by reading the current owner from storage, and confirm no shadow admin survives.

**Check for a proxy.** Read EIP-1967 implementation and admin slots. If it is a proxy, the admin can change everything, and your analysis of the implementation has a shelf life of exactly one upgrade. Treat an upgradeable token with an EOA admin as a token controlled by one person's private key.

**Simulate the sell before the buy.** Use a transaction simulator or a honeypot-detection tool to execute a buy and a sell against the live contract state. If the sell reverts or returns dust, you have found the trap without funding it. Tooling categories exist for exactly this. Use them.

**Scope your approvals.** Never approve `type(uint256).max` to a contract you have owned for four minutes. Approve the amount you are spending. Revoke approvals you no longer use. This does not stop a mint or a blacklist, but it caps the blast radius of the ones you missed.

**For builders:** renounce completely or govern transparently through a timelock and multisig, cap your mint in the function body, put a hard ceiling in every fee setter, and if you must be upgradeable, put the proxy admin behind a timelock so users can exit before a malicious upgrade lands. Make the contract boring to read. Boring is the compliment.

## The Bottom Line

The rug was in the source the whole time. It was public, it was verified, and it was legible to anyone willing to spend less time than they later spent explaining the loss to their spouse. The tooling exists, the standard is written down, and none of it matters if the confirm button is faster than the checklist. You will read the contract next time. Everyone says that.

*It was priced in before you signed.*

## Related

- [Upgradeable Contracts and the Admin Key Problem](/itsalreadypriced/rtfm/2026/08/12/upgradeable-contracts-and-the-admin-key-problem/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)
