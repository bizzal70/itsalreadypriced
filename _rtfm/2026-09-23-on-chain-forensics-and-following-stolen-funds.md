---
layout: rtfm
title: "On-Chain Forensics and Following Stolen Funds"
date: 2026-09-23
summary: "The public ledger makes stealing crypto trivial and keeping it nearly impossible, which is why on-chain forensics turns every theft into a slow-motion chase across an immutable record that never forgets."
framework: "Etherscan and Public Block Explorers"
framework_url: "https://etherscan.io/"
---

Everyone knows the blockchain is public. Everyone says it like a marketing slogan, "transparent, immutable, trustless," and then acts as though the transparency stops working the moment their own funds move. The uncomfortable truth is that stealing crypto is the easy part. A leaked key, a malicious approval, a signature phished out of a distracted user, and the assets are gone in one transaction. The hard part, the part attackers spend most of their time and cleverness on, is convincing the world that money which is on a ledger that never forgets somehow now belongs to them.

## The Standard

There is no EIP for forensics. The "standard" here is the ledger itself, and the tooling built to read it.

A public block explorer (Etherscan being the canonical example for EVM chains) is nothing more than an indexed, human-readable view of state that is already fully public. Every account, every transaction, every internal call produced by the EVM, every event emitted via `LOG` opcodes, every token transfer described by the `Transfer` events in ERC-20 (EIP-20) and ERC-721 (EIP-721): all of it is there, permanently, addressable by hash.

What the explorer actually gives you, and what forensics depends on, is a small set of primitives. First, the transaction graph: `from`, `to`, `value`, and the call tree of internal transactions that a plain transaction receipt hides but that trace-based indexing exposes. Second, the token ledger reconstructed from event logs, so you can follow an ERC-20 balance moving even though the token contract, not the EOA, is what "holds" it. Third, address labeling: the tags explorers and analytics firms attach to known exchange deposit addresses, bridges, mixer contracts, and sanctioned entities. Fourth, the mempool, the pre-confirmation view where intent becomes visible before it becomes final.

The standard, put plainly, is this: on an account-based chain, funds do not disappear. They move to another address, and that address is visible, and every subsequent move from it is visible, forever, to anyone with a browser. The chain of custody is not something investigators have to reconstruct from witnesses. It is the substrate.

## Where It Breaks Down

It breaks down for defenders first, which is the part nobody likes to admit.

The most common failure is treating an address as an identity. A hexadecimal address is a public key hash, not a person. Attackers generate them for free, in unlimited quantity, and the naive investigator loses the trail the instant funds fan out across a hundred fresh EOAs. The graph does not lie, but it also does not simplify itself. Following it requires clustering heuristics (common-input ownership, peel chains, gas-funding relationships where one address pays the gas that activates the next), and most people never get past reading a single transaction.

Then there is the confusion between value and tokens. A `value` field of zero on a transaction does not mean nothing happened. ERC-20 transfers move no ether. Someone watching only the native-value column will completely miss a nine-figure token drain because the actual movement lives in `Transfer` event logs, not in the transaction's `value`. Similarly, internal transactions (the `CALL`, `DELEGATECALL`, and `CREATE` operations the EVM performs inside a contract execution) are invisible on a plain receipt. Funds routed through a contract, a multicall, or a proxy will not appear on the sender's normal transaction list at all. If you are not reading traces, you are reading a redacted document.

For attackers, the breakdown is the mirror image, and it is why laundering is the genuinely hard problem. The ledger is a permanent, timestamped confession. The moment stolen funds touch a centralized exchange deposit address (which is KYC'd and labeled), the pseudonymity collapses. So attackers reach for obfuscation, and every technique leaves its own signature:

- **Mixers and privacy pools.** These break the direct link between deposit and withdrawal, but the deposits and withdrawals themselves are on-chain, the anonymity set is finite and measurable, and timing analysis plus amount-matching frequently narrows it. Contracts of this class are also aggressively labeled and, in many jurisdictions, sanctioned, so anything downstream inherits taint.
- **Cross-chain bridges.** Moving assets to another chain feels like escaping the explorer. It is not. Bridge contracts emit lock and mint events on both sides. Bridge-hopping produces a legible sequence of `deposit` on chain A and `withdraw` on chain B, and analytics tooling that indexes multiple chains stitches it back together.
- **DEX swaps and chain-splitting.** Swapping the stolen token for something else changes the asset but not the provenance. The swap is a transaction with a `to` of a well-known router, decodable down to the exact pool.
- **Chain-hopping to non-EVM chains and back.** More friction, more time, but time is exactly what the immutable record has infinitely more of than the thief does.

The deepest breakdown is behavioral. Approvals are the quiet catastrophe. A user who signs an unbounded `approve` (the classic `type(uint256).max` allowance) to a contract they will interact with once has handed a standing withdrawal right to that contract's controller. `Permit` (EIP-2612) and `Permit2` push this further, moving the approval into an off-chain signature that the user often does not even recognize as a transaction. The theft, when it comes, is a perfectly valid `transferFrom`. On the explorer it looks like consent, because mechanically it was.

## Doing It Right

For holders, the discipline is dull and therefore ignored.

Read the transaction you are actually signing. A wallet that shows you a decoded action ("approve unlimited USDC to 0xrouter") is doing you a favor. Set finite allowances scoped to the amount you intend to spend, and revoke standing approvals you no longer need. Allowance-management tooling exists precisely for this, and checking your approval surface should be a routine, not a post-mortem.

Treat address labels as leads, not verdicts. Etherscan's tags are useful and frequently correct, but they are curated, not authoritative. A contract can be verified and still malicious. Verified source only means the bytecode matches submitted source, not that the source is safe. Read the code, or read someone competent's audit of it, before granting it power over your funds.

If you are ever on the receiving end of a theft, speed and reading skill matter. Trace the funds through internal transactions, not just the top-level list. Follow the token via `Transfer` logs. Identify the first choke point, which is almost always a centralized exchange deposit address or a labeled bridge, because that is where off-chain legal process can freeze what the chain cannot. The window between theft and cash-out is your entire opportunity, and it exists only because the thief cannot spend the money as fast as they can steal it.

For builders, design as though your users will be phished, because they will be.

Prefer `Permit2` with expiring, scoped allowances over unbounded approvals. Emit rich, specific events; a contract that under-emits is a contract that hides its own state from the very forensics that might later save its users. Do not build "helpful" batching that obscures what moves where. Publish and verify your source, but understand verification is table stakes, not a security claim. And if you run anything custodial or bridge-like, assume you are a labeled choke point and build the monitoring and freeze capability that role implies.

## The Bottom Line

The ledger is the best witness in the history of financial crime, and almost nobody calls it to the stand until after the money is gone. Theft on a public chain is not the end of a story, it is the beginning of a chase across a record that outlives everyone involved. Attackers know this, which is why they spend their real effort on laundering, and defenders forget it, which is why they keep signing the approvals that make the theft a formality. The transparency was never optional. You are just choosing not to read it.

*Verify the trace, not the vibe. The chain already remembers what you'd rather forget.*

## Related

- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)
- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)
