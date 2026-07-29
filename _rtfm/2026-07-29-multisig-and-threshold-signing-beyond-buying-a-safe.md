---
layout: rtfm
title: "Multisig and Threshold Signing, Beyond Buying a Safe"
date: 2026-07-29
summary: "Buying a Safe multisig does nothing if one person controls the threshold; real security comes from independent signers, hardware diversity, and rehearsed recovery, not from the contract itself."
framework: "Safe (Gnosis Safe) Smart Account"
framework_url: "https://docs.safe.global/"
---

Everybody knows a multisig is safer than a single key. Everybody says so. And then everybody deploys a 2-of-3 Safe where all three keys live on the same laptop, in the same MetaMask profile, backed up to the same iCloud account, and signed from the same chair. Congratulations: you have paid gas to deploy a smart contract whose only function is to make you feel responsible.

## The Standard

A Safe (formerly Gnosis Safe) Smart Account is not a wallet in the EOA sense. It is a smart contract account that holds assets and executes transactions only when it receives enough valid signatures to satisfy a configured threshold. The core parameters are the owner set (a list of signer addresses) and the threshold M, where M-of-N owners must sign before a transaction executes.

Mechanically, each Safe transaction is hashed according to EIP-712 typed structured data, producing a unique digest that binds the destination, value, calldata, operation type, and the Safe's internal nonce. Owners sign that digest. The contract's `execTransaction` function collects those signatures, verifies each one against the owner set (supporting ECDSA signatures from EOAs, EIP-1271 contract signatures, and pre-approved hashes via `approveHash`), and only proceeds when the count of valid, distinct owner signatures reaches the threshold.

That is the entire security model, and it is a good one. The threshold means no single key compromise drains the treasury. The nonce means transactions cannot be replayed. The modular architecture (modules, guards, fallback handlers) means you can extend behavior without touching the core. Safe gives you the primitive. What it does not give you, and cannot give you, is the thing that actually matters: independence between the entities holding those N keys.

The standard requires M valid signatures. It says nothing about who signs, on what device, from what location, under what authority. The contract counts signatures. It does not count humans. That distinction is where every failure lives.

## Where It Breaks Down

The most common failure is the one in the opening: threshold theater. A 3-of-5 where all five keys are derived from the same seed phrase is a 1-of-1 wearing a costume. If those five addresses came out of the same BIP-39 mnemonic through BIP-32 derivation, then whoever holds the mnemonic holds all five. The Safe contract sees five distinct owner addresses and is perfectly satisfied. An attacker who phishes one seed backup satisfies the threshold instantly. You did not build a multisig. You built a single point of failure with a more expensive deployment cost and a false sense of security that will stop you from taking real precautions.

The second failure is correlated infrastructure. The keys are genuinely separate, held by separate people, but every signer uses the same wallet software, the same browser extension, connects through the same WalletConnect session to the same interface, and reviews transactions on the same class of hot device with no independent verification. A malicious or compromised frontend can present one payload to the screen while the wallet signs another. If every signer is looking at the same lying interface, the threshold provides no protection, because all N humans are being deceived by the same lie simultaneously. Blind signing on hardware wallets that display an opaque hash instead of decoded EIP-712 fields turns your signers into rubber stamps. They are approving a digest they cannot read.

The third failure is the delegatecall problem. Safe supports two operation types: `CALL` and `DELEGATECALL`. A transaction executed as a delegatecall runs arbitrary code in the context of the Safe itself, with access to its storage. A delegatecall to a malicious contract can rewrite the owner set, change the threshold, or install a module that bypasses signing entirely. Signers who approve delegatecall transactions without understanding what the target contract does are handing over the account. The signature was valid. The threshold was met. The Safe is now owned by someone else.

The fourth failure is modules and guards misunderstood as features rather than attack surface. A module is code with permission to execute transactions without meeting the threshold at all. Install a sketchy module and you have added a signer that never sleeps and never says no. Guards run on every transaction and can be used defensively, but a poorly written guard can brick the Safe (a guard that reverts on all transactions locks the account permanently, because you need to execute a transaction to remove the guard, and the guard reverts it).

The fifth failure is the one nobody rehearses: signer loss. A 2-of-3 sounds resilient until you realize what it actually tolerates. It survives the loss of exactly one key. Lose two (a dead laptop and a forgotten passphrase, or one person leaving the company while another loses their Ledger) and the treasury is frozen forever. There is no recovery. The contract does not care about your circumstances. People conflate "multisig" with "backup" and set thresholds that leave zero margin.

The sixth failure is address and chain confusion. The same Safe address can exist on multiple chains, but the owner set and threshold are per-deployment. People assume a Safe deployed on one chain is configured identically on another. It may not be. Sending assets to "the same" Safe address on a chain where it was never deployed, or was deployed with different owners, is a slow-motion loss.

## Doing It Right

Start with independence as the design goal, not signature count. N keys held by one person is not a multisig. Enforce that every owner key is generated on a separate device, from a separate entropy source, and controlled by a separate person or role with genuinely separate compromise conditions. If two keys share a threat (same building, same admin, same seed, same cloud backup), treat them as one key when you reason about your threshold.

Diversify signer hardware. Do not standardize your entire signer set on one hardware wallet vendor or one firmware version. A vendor-specific supply chain issue or firmware bug should not be able to compromise your threshold in one move. Mix hardware types. Require that signers verify the decoded EIP-712 transaction on the device screen, not a bare hash. If your hardware cannot decode Safe transactions, use tooling that lets signers independently compute and compare the transaction hash out of band before approving.

Ban blind delegatecall as policy. Install a transaction guard that restricts operations to `CALL` unless a delegatecall target is on an explicit allowlist. Treat any transaction that modifies the owner set, threshold, modules, guard, or fallback handler as a high-ceremony event requiring out-of-band confirmation on a separate channel by every signer.

Size the threshold for both attack and loss. A 3-of-5 tolerates two independent compromises and two independent losses at the same margin, which is why it is the sane default for anything holding real value. A 2-of-3 is the absolute floor and only acceptable when key custody is genuinely disciplined. Distribute geographically. Keep at least one signer in cold storage that never touches a hot interface.

Rehearse recovery before you need it. Actually execute an owner-swap on a testnet deployment. Actually simulate losing a signer and adding a replacement. Document the exact `swapOwner` and `changeThreshold` calldata. Use transaction simulation tooling (Tenderly-class simulators, Safe's own simulation) on every non-trivial transaction so signers see state changes, not intentions. Verify the chain ID and deployment address every single time.

## The Bottom Line

The Safe contract will do exactly what it promises: it will count to M and execute. It will never tell you that your M signers are one person in a trench coat, that they all sign blind from the same poisoned frontend, or that the delegatecall they just approved rewrote the owner set. The primitive is sound. The people deploying it are the vulnerability, and they always have been. A multisig is a distribution of trust, and if you have not actually distributed anything, you have distributed nothing but the illusion.

*You didn't build a multisig, you built a group chat that spends money.*

## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Signature Requests and Blind Signing](/itsalreadypriced/rtfm/2026/07/22/signature-requests-and-blind-signing/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)
