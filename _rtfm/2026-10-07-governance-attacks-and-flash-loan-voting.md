---
layout: rtfm
title: "Governance Attacks and Flash-Loan Voting"
date: 2026-10-07
summary: "Governance tokens that gate voting power on a single snapshot block are perfectly happy to count borrowed votes as real votes, and flash loans make that borrowing free."
framework: "Compound and OpenZeppelin Governor"
framework_url: "https://docs.openzeppelin.com/contracts/governance"
---

Everyone who has ever deployed a Governor contract knows that voting power should be hard to acquire and hard to fake. Everyone also ships a system where voting power is a number in a mapping, measured at a single block, that anyone with enough capital can rent for the duration of one transaction. These two facts have coexisted for years, politely, because the people who understand the problem are usually not the people signing off on the launch checklist, and because "nobody has drained us yet" is an answer that satisfies right up until it does not.

## The Standard

The reference design here is Compound's `GovernorAlpha`/`GovernorBravo` lineage and the generalized `Governor` in OpenZeppelin Contracts, built on `ERC20Votes` (formerly `Comp`/`ERC20VotesComp`). The mechanism is straightforward and, read carefully, tells you exactly where the knife goes in.

Voting power is not your current balance. It is your *delegated* balance, tracked through checkpoints. When tokens move or delegation changes, `ERC20Votes` writes a checkpoint: a `(blockNumber, votes)` pair via `_writeCheckpoint`. When a proposal is created, the Governor records a `proposalSnapshot` (in Bravo, `startBlock`). When you call `castVote`, the contract does not read your balance now. It reads `getPastVotes(account, proposalSnapshot)`, which binary-searches your checkpoint history for the number of votes you controlled *at that snapshot block*.

This is EIP-5805 territory now (`clock()` and `CLOCK_MODE`, standardizing checkpointed voting with either block numbers or timestamps), with `getVotes` and `getPastVotes` as the canonical surface. The snapshot exists for a good reason: it prevents vote-buying *after* a proposal's terms are known relative to the moment deliberation begins, and it makes the electorate deterministic. OpenZeppelin's `GovernorVotes` extension wires `getPastVotes` into `_getVotes`, and `GovernorVotesQuorumFraction` computes quorum against `getPastTotalSupply` at the same snapshot. Compound's `proposalThreshold` gates who can even submit a proposal, measured the same way.

The entire security model rests on one assumption: that the snapshot block is far enough in the past, relative to the moment an attacker must commit capital, that renting voting power across that gap is uneconomical. Break that assumption and the standard does exactly what it was designed to do, for the wrong person.

## Where It Breaks Down

The failure is not a bug in `ERC20Votes`. It is a configuration and composability failure, and it has a specific shape.

**Zero or tiny voting delay.** In OpenZeppelin's `Governor`, `votingDelay()` is the gap between `propose()` and `proposalSnapshot`. If `votingDelay` is zero, the snapshot block is the proposal block. An attacker can then, in a single transaction: flash-borrow a large quantity of the governance token, self-delegate (or delegate to a controlled address), call `propose`, and because the snapshot is taken at the current block, the borrowed votes are already checkpointed and counted. The naive assumption is that `castVote` happens later, so borrowing cannot persist. It does not need to. The checkpoint at the snapshot block is immutable. Repay the loan in the same transaction and the votes *at that past block* remain on the books forever.

**The one-block self-delegate.** `ERC20Votes` only grants voting power to accounts that have delegated. A lot of people assume this is friction that stops flash attacks. It is not. `delegate(self)` is one call, and after it, incoming transfers immediately move voting weight via `_moveVotingPower` inside `_update`/`_afterTokenTransfer`. Borrow, delegate, receive, snapshot, vote, transfer back, repay. All atomic.

**Executable proposals with no timelock, or a timelock the attacker controls.** Even with a nonzero voting delay, the deeper rot is what the proposal *does*. If the DAO executes directly from `Governor` without a `TimelockController`, a passed malicious proposal self-executes the moment quorum and threshold are met. The classic payload is a proposal that transfers the treasury, or `upgradeTo` on a proxy the Governor admins, or granting the attacker a role. The flash loan funds the vote; the proposal funds the attacker. Where a timelock *does* exist, people misconfigure it: the Governor is not the sole proposer, or `CANCELLER_ROLE` is held by an address the attacker can obtain, or the `minDelay` is measured in minutes.

**Vote-weight tokens that are also lending collateral.** This is the composability trap. If the governance token is listed on a money market with deep liquidity, the flash loan need not even be a dedicated flash-loan primitive. Single-block borrow-against-collateral, or an atomic position opened and closed inside one transaction, supplies the capital. The token's utility as collateral is directly in tension with its utility as a vote. Protocols routinely want both and reconcile neither.

**Snapshot on current block in forked governors.** Teams fork a Governor, "simplify" it, and in doing so read `getVotes(account)` (current) instead of `getPastVotes(account, snapshot)` somewhere in a custom path, or set the snapshot to `block.number` in `propose`. Any current-block read is a flashloan oracle waiting to be queried.

**Low `proposalThreshold` combined with low quorum.** Even honest-looking parameters compose into an attack surface. If the threshold to propose is small and quorum is a low fraction of a thin, mostly-undelegated supply, the *effective* electorate is tiny. Flash-renting a majority of the *actively delegated* supply is far cheaper than renting a majority of total supply, because most holders never delegate. People benchmark quorum against total supply and feel safe. The attacker benchmarks against participating supply.

## Doing It Right

For builders deploying or auditing a Governor:

- **Set a nonzero `votingDelay`, measured in blocks or time that spans multiple blocks.** This is the single highest-leverage control. A snapshot one block in the past still falls inside a single flash transaction's atomic scope only if the proposal and snapshot share a block. With a real delay, the attacker must hold the position from `propose` through the snapshot block, which breaks atomicity and reintroduces the cost of actually owning the stake. Treat `votingDelay == 0` as a deployment-blocking finding.

- **Always route execution through `TimelockController` with a `minDelay` long enough for humans to react.** The timelock does not stop a bad vote. It buys time to cancel, exit, or fork before a malicious proposal executes. Ensure the Governor is the only `PROPOSER_ROLE`, that `CANCELLER_ROLE` sits with a trusted guardian or the same Governor, and that nobody retains `TIMELOCK_ADMIN_ROLE` after setup (renounce it).

- **Verify every voting read is `getPastVotes` at `proposalSnapshot`.** Audit custom Governor forks specifically for any `getVotes` (current) call in the propose/vote/quorum path. There should be none.

- **Benchmark quorum against delegated, participating supply, not total supply.** Use `GovernorVotesQuorumFraction` deliberately and model the worst case where only actively-delegated tokens matter. If participation is thin, raise quorum or incentivize delegation.

- **Reconsider listing the governance token as flash-loanable collateral**, or design the token so voting power and transferable liquidity diverge (vote-escrow / locked models, where voting weight requires a time-lock the holder cannot flash through). A token you cannot borrow for one block cannot be flash-voted.

For holders: delegate your tokens. Undelegated supply is dead weight that shrinks the effective electorate and makes the whole system cheaper to capture. Watch `votingDelay`, `votingPeriod`, and timelock `minDelay` as first-class risk parameters before you hold a governance token at all. If a DAO executes without a timelock, treat its treasury as already spent by whoever has the most capital for one block.

## The Bottom Line

The snapshot mechanism is not broken. It works exactly as specified, which is the problem, because "whoever controls the most delegated votes at block N wins" is a perfectly good description of both legitimate governance and a flash-loan heist. Borrowed voting power is real voting power for exactly one block, and one block is the entire duration of the attack. The fixes are known, cheap, and sitting in the same library you deployed from. They will keep getting skipped, because a nonzero voting delay feels like friction and a timelock feels like

## Related

- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Upgradeable Contracts and the Admin Key Problem](/itsalreadypriced/rtfm/2026/08/12/upgradeable-contracts-and-the-admin-key-problem/)
- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)
