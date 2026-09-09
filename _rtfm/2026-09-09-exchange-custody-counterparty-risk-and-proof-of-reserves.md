---
layout: rtfm
title: "Exchange Custody, Counterparty Risk, and Proof of Reserves"
date: 2026-09-09
summary: "'Not your keys, not your coins' is a balance-sheet claim about an exchange's solvency you have no way to verify, and even Proof of Reserves only closes half the gap."
framework: "Chainlink Proof of Reserve"
framework_url: "https://chain.link/proof-of-reserve"
---

You already know the slogan. "Not your keys, not your coins." You have seen it on stickers, in bios, in the replies under every custodial exchange's uptime announcement. And yet the aggregate balance sitting on centralized venues never meaningfully shrinks, because the slogan is treated as a moral position rather than what it actually is: an unverifiable claim about someone else's balance sheet. When you deposit, you are not holding an asset. You are holding a liability that a third party has promised to honor, and you have no primitive with which to check whether they can.

## The Standard

Proof of Reserves (PoR) is the attempt to make that liability checkable. The cleanest framework to reason about it is Chainlink Proof of Reserve, so let us use it as the reference implementation and describe what it actually requires.

A PoR system has two halves, and both must hold for the proof to mean anything.

The first half is **proof of reserves**: demonstrating that an entity controls assets on-chain (or attesting to off-chain assets) equal to some published number. On-chain, this is straightforward in principle. An address either holds tokens or it does not, and anyone can read balances directly from state. Chainlink PoR productizes this by running a decentralized oracle network that reads reserve balances (across the chains and addresses a custodian designates, or via an attesting auditor for off-chain assets like fiat or tokenized treasuries) and writes an aggregated reserve figure on-chain to a `AggregatorV3Interface`-style feed. A consuming contract can then read that feed the same way it reads a price feed, and gate its own behavior on it. A wrapped-asset minter, for example, can refuse to mint if reserves fall below circulating supply.

The second half is **proof of liabilities**: demonstrating the total of what the entity owes to its users. This is the hard half, and it is where the whole exercise lives or dies. The canonical technique is a Merkle-sum tree. Each user's balance becomes a leaf, internal nodes carry the sum of their children, and the root commits to the total liability. The exchange publishes the root. Each user receives a Merkle proof letting them verify that their specific balance is included in the tree that produced that root, without revealing anyone else's balance.

Solvency, then, is a single inequality: **reserves >= liabilities**, where reserves come from something like Chainlink PoR and liabilities come from a Merkle-sum root that users can individually audit. That is the standard. Not "trust our attestation letter." A verifiable number on both sides of the ledger and an inequality anyone can check.

## Where It Breaks Down

In practice almost every "proof of reserves" you will encounter proves only the first half, and the first half in isolation proves nothing about solvency.

**Reserves without liabilities is theater.** An address holding a billion dollars tells you nothing if you do not know whether the exchange owes its users nine hundred million or nine billion. A screenshot of a big wallet, or even a live Chainlink reserve feed, satisfies the reserves side while saying nothing about the denominator. Most published "proofs of reserve" stop exactly here, because the reserves side is easy and flattering and the liabilities side is hard and revealing.

**Borrowed reserves and snapshot gaming.** Reserve attestations are point-in-time. An entity can borrow assets, move them into the attested addresses for the block the oracle reads, and return them after. Without proof that the entity has exclusive and unencumbered control (rather than merely transient custody), a reserve figure is a photograph, not a bank statement. Chainlink PoR can update on a schedule or deviation threshold, which narrows the window, but no oracle can tell you an asset is not simultaneously pledged as collateral somewhere off-chain.

**The negative-balance omission in Merkle-sum trees.** The Merkle-sum construction has a known attack surface: if the exchange is allowed to insert a leaf or internal node with a negative value, it can reduce the published total liability below the real total while still giving each honest user a valid inclusion proof. A correct implementation must constrain every node to be non-negative and must commit to that constraint, otherwise the liabilities root understates what is owed and the solvency inequality is quietly satisfied by arithmetic fraud. Users verifying their own leaf will see nothing wrong.

**Address control is not proven.** Publishing a list of addresses and their balances is trivial. Proving you control the private keys is a separate act. Absent a signed message from each address (or a spend), the "reserves" could belong to anyone: another exchange, a market maker, an address scraped off a block explorer.

**Off-chain and cross-chain reserves reintroduce trust.** Tokenized RWAs, fiat in a bank, assets on chains without native oracle coverage: all of these require an attesting party. Chainlink PoR can surface an auditor's number on-chain, but it cannot make that auditor honest. The oracle faithfully reports whatever it is told. Garbage in, cryptographically-signed garbage out.

**The rehypothecation gap.** Even a perfect reserves >= liabilities snapshot says nothing about what happens between snapshots, nor about lending against user assets, internal-transfer obligations, or liabilities denominated in assets the exchange does not actually hold. Solvency at block N is not solvency at block N+1.

**Consuming the feed without reading it.** On the builder side, integrating a PoR feed and then never checking `updatedAt` for staleness, never bounding the answer, or hardcoding a fallback that ignores the feed under load is functionally equivalent to not having it. The feed is a circuit breaker only if you actually let it break the circuit.

## Doing It Right

If you hold assets:

- **Treat every custodial balance as an unsecured loan to a counterparty**, priced accordingly. Diversify across custodians the way you would across debt issuers. Assume any single one can go to zero.
- **Demand both halves.** A reserves attestation with no liabilities proof is not proof of solvency. When an exchange publishes a Merkle-sum root, actually run the verifier against your own account. Your inclusion proof is the only part of their attestation you can personally trust, and it is worthless if you never check it.
- **Prefer venues that prove address control** via signed messages, and that publish reserve feeds you can read directly on-chain rather than PDFs.
- **Withdraw the balance you are not actively trading.** Self-custody is the only construction where the reserves-equal-liabilities question collapses, because you are both parties.

If you build:

- **Implement liabilities, not just reserves.** Use a Merkle-sum tree with enforced non-negative nodes at every level. Publish the root every settlement period and give every user a working, documented verifier. If you cannot let users audit their own leaf, you have not built proof of anything.
- **Gate minting and issuance on a PoR feed.** For any wrapped or tokenized asset, read a Chainlink Proof of Reserve feed in the mint path and revert when circulating supply would exceed reserves. This turns solvency into an invariant the contract enforces rather than a promise the operator makes.
- **Handle the feed defensively.** Check `updatedAt` against a maximum staleness bound, sanity-bound the returned answer, and fail closed (halt issuance) rather than open when the feed is stale or reverts. A reserve feed that is trusted blindly is a new single point of failure, not a safeguard.
- **Minimize off-chain attestation surface.** Every reserve component that requires a human attester is a component you cannot cryptographically verify. Keep reserves on-chain and readable wherever the asset design allows.

## The Bottom Line

Proof of Reserves does not make an exchange trustworthy. At best it converts an act of blind faith into a checkable inequality that most users will never check and most exchanges will never fully publish. The slogan was never a slogan. It is the recognition that the only balance sheet you can audit is the one whose private keys you hold. Everything else is a promise, denominated in someone else's solvency, verifiable only in the moment it stops being honored.

*Verify the tree, or admit you are just hoping.*

## Related

- [Oracle Manipulation and Price Feed Integrity](/itsalreadypriced/rtfm/2026/08/19/oracle-manipulation-and-price-feed-integrity/)
- [Bridge Risk and Why Cross-Chain Is the Weakest Link](/itsalreadypriced/rtfm/2026/08/05/bridge-risk-and-why-cross-chain-is-the-weakest-link/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)
