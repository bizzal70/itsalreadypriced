---
layout: rtfm
title: "MEV, Front-Running, and Sandwich Attacks"
date: 2026-09-30
summary: "Your pending transaction sits in a public mempool announcing exactly what you intend to do, and specialized bots parse, simulate, and profit from that intent before your trade ever confirms."
framework: "Flashbots MEV Documentation"
framework_url: "https://docs.flashbots.net/"
---

You already know the mempool is public. Everyone knows the mempool is public. And yet people continue to broadcast six-figure swaps with default slippage settings through a public RPC endpoint, then act surprised when the fill comes back worse than the quote. The problem was never a lack of information. The problem is that "public" is an abstraction people nod along to without internalizing that it means a global audience of automated adversaries who read your transaction, model its consequences, and reorder the block around it faster than your wallet finishes animating the confirmation modal.

## The Standard

Start with the mechanics, because most of the confusion downstream comes from skipping them.

When you sign a transaction on a public Ethereum RPC, it does not go straight into a block. It enters the mempool, the set of pending, valid, unconfirmed transactions that propagate peer to peer across the network. Anyone running a node can watch this set in real time. Your transaction contains, in the clear, the destination contract, the calldata (which function you are calling and with what arguments), the value, and the gas price you are willing to pay. That is not metadata. That is a fully specified statement of intent, cryptographically signed by you, waiting to be executed.

MEV, or Maximal Extractable Value, is the term of art (formalized in the research the Flashbots documentation builds on) for the value that can be extracted by whoever gets to decide the order, inclusion, and exclusion of transactions within a block. The party building the block does not have to include transactions in the order they arrived, in gas-price order, or in any fair order at all. They can insert their own transactions, drop yours, or wrap yours between two of their own. The Flashbots framing here is worth stating plainly: block space is an auction, ordering is a commodity, and the searchers bidding on that ordering are strictly better resourced than you are.

The three canonical extraction patterns follow directly:

- **Front-running.** A searcher sees your pending transaction, copies your intent, and submits an equivalent transaction with a higher priority fee so it lands before yours. Classic on any action where being first has value.
- **Back-running.** The searcher wants to be immediately after your transaction, typically to capture an arbitrage or liquidation your action created. Less predatory, often just efficient, but still ordering extracted from your activity.
- **Sandwich attacks.** The combination. The bot front-runs your swap with a buy that pushes the price against you, lets your transaction execute at the worse price, then back-runs with a sell. Your slippage tolerance is the bot's profit margin, extracted by design.

The standard, such as it is, is not "trust the mempool to be fair." The standard is that ordering is adversarial by construction, and any system you build or trade on that assumes otherwise is mispriced.

## Where It Breaks Down

The failures are boringly consistent, which is what makes them worth naming.

**Default slippage on AMM swaps.** Constant-product AMMs (the `x * y = k` family) move price as a function of trade size relative to pool depth. Your slippage tolerance defines the worst execution you will accept. A sandwich bot solves a simple optimization: given your trade and your slippage setting, what is the largest front-run buy that still leaves your transaction executable within tolerance? Set slippage to 1 percent on a thin pool and you have handed the bot a precise, self-authorized budget to extract. Wallets that ship a fat default (or auto-slippage that quietly widens on volatile pairs) are quietly funding this.

**Public RPC endpoints as the default transport.** The RPC URL baked into most wallets forwards your signed transaction into the public mempool the instant you hit confirm. There is a window, sometimes seconds, sometimes longer during congestion, where your transaction is visible and pending. That window is the entire game. Users who never change their RPC are broadcasting on the public band and wondering why the bots always seem to know.

**Naive on-chain design patterns.** Builders reproduce the same footguns. Oracles read from a single spot price on an AMM, so an attacker manipulates the pool within the same block to move the reported price. Liquidation and reward functions that pay the caller create a race that gets front-run to the point where honest participants never win. NFT mints and token launches with predictable, high-value function calls are front-run trivially because the intent is legible and the payoff is large. `approve` followed by a separate `transferFrom` in the same flow can be reordered against. Any function whose profitability depends on being called first, and which broadcasts that profitability in its calldata, is a standing invitation.

**Commit-reveal that does not commit.** Protocols that intend to hide intent sometimes implement a commit phase that leaks the answer anyway: a commit hash with a guessable preimage, or a reveal window short enough that the commit and reveal land in the same block a builder can observe and reorder. The pattern is right, the implementation defeats it.

**Assuming private order flow is private.** Sending through a "protected" RPC or a private relay reduces public mempool exposure, but it does not eliminate MEV. The block builder still sees your bundle. The trust assumption moves from the entire network to the specific builders and relays in your path. People treat private transport as a force field. It is a narrower attack surface, not a closed one.

## Doing It Right

None of this is exotic. It is discipline applied to defaults.

**As a holder or trader:**

- **Tighten slippage deliberately, per trade.** Do not accept the wallet default. For deep pools a fraction of a percent is plenty. If a trade genuinely requires wide slippage to execute, that is information: the pool is thin and you are the liquidity event the bots are waiting for. Size down or split the order.
- **Route through private transaction submission.** Use an RPC or relay that forwards to block builders without exposing you to the public mempool first. This is the single highest-leverage change for a normal user, and it costs you nothing but a settings change. Understand the trust model you are adopting, but adopt it.
- **Prefer venues and aggregators with MEV-aware routing.** Some aggregators submit through protected channels, use RFQ or intent-based fills where a solver commits to a price off-chain, or return part of the extracted value to you. Intent-based architectures in particular invert the problem: you specify the outcome you want, and a filler competes to deliver it, rather than you broadcasting the exact path.
- **Do not do large, price-sensitive swaps during congestion.** Wide pending windows and volatile pricing are exactly when the math favors the bot.

**As a builder:**

- **Never use spot AMM price as an oracle.** Use time-weighted average prices, or purpose-built oracle networks, so a single-block manipulation cannot move your reference price.
- **Design so that ordering does not matter.** Batch auctions that clear at a uniform price remove the value of being first. Where you cannot batch, use proper commit-reveal with reveal windows spanning multiple blocks and preimages that are actually hard to guess.
- **Assume every parameter in calldata is public and adversarial.** If profitability is legible from the function call, someone will front-run it. Move the sensitive value off-chain until execution, or auction the right to execute.
- **Consider capturing MEV for your users rather than leaking it.** Back-running arbitrage and liquidation revenue can be redistributed rather than surrendered to searchers.

## The Bottom Line

The uncomfortable truth is that the mempool worked exactly as designed, and so did the bots. There is no bug here, no exploit to patch, just a permissionless system doing permissionless things to a transaction you signed with your own key and announced to the world. You cannot make ordering fair. You can only stop pretending it is, tighten your slippage, change your RPC, and accept that in an auction for block space you are the retail bidder and everyone else showed up with a supercomputer and a script. The bots read your intent faster than you do. They always will. The only variable you control is how much you tell them.

*Broadcast accordingly.*

## Related

- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)
- [Reading a Token Contract Before You Buy the Rug](/itsalreadypriced/rtfm/2026/08/26/reading-a-token-contract-before-you-buy-the-rug/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)
