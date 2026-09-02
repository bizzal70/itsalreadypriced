---
layout: rtfm
title: "Cold Storage and Operational Security for Custody"
date: 2026-09-02
summary: "Self-custody isn't a hardware wallet in a drawer, it's a key management program with a full lifecycle, and NIST SP 800-57 has been telling us how to run one for years."
framework: "NIST SP 800-57 (Key Management)"
framework_url: "https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final"
---

You bought a hardware wallet. You wrote twelve words on a card. You put the card somewhere you think is safe, and you told yourself you were done. You were not done. You had not started. Custody is not an object you acquire, it is a program you operate, and the difference between those two ideas is the difference between the people who still have their coins in ten years and the people who write threads about how they used to.

## The Standard

NIST Special Publication 800-57 is the reference document for key management, and it has been for a very long time. It predates most of the assets you hold and it will outlive most of the wallets you use. It is not blockchain-specific, which is exactly why it is useful: it describes key management as a discipline independent of what the keys happen to unlock.

The central idea in SP 800-57 is the key lifecycle. A key is not a static secret. It moves through phases: generation, distribution, storage, use, backup and recovery, and eventually destruction or revocation. Each phase has its own threat model and its own controls. The document is emphatic that security is a property of the entire lifecycle, not of any single stage. A perfectly generated key that is backed up carelessly is a compromised key. A perfectly stored key with no recovery plan is a lost key, which for your purposes is the same as a stolen one.

SP 800-57 also insists on a few principles that translate directly to self-custody. Cryptoperiods: keys should not live forever, and the longer a key is exposed to use, the more its risk accumulates. Separation of duties: no single person or single failure should be able to compromise or destroy a key. Key protection commensurate with the value protected: your controls should scale with what is at stake. And documentation: a key management program that exists only in one person's head is not a program, it is a single point of failure with a pulse.

Notice what is absent from all of this. There is no mention of a specific device, no brand, no drawer. The framework treats hardware as an implementation detail of the storage and use phases. That is the whole point.

## Where It Breaks Down

The failures are almost never in the cryptography. They are in the lifecycle stages people never think of as security decisions.

**Generation.** Seed phrases generated on a compromised or non-airgapped machine are compromised at birth. Browser-based generators, screenshots of the words, cloud-synced notes apps, a photo of the card that quietly uploads to a backup service you forgot you enabled. The BIP-39 mnemonic is only as strong as the entropy behind it and the isolation of the environment that produced it. People obsess over the storage of the seed while paying zero attention to the moment it existed in plaintext on a general-purpose computer.

**Storage and backup.** The single card in the single location is the canonical mistake. It fails to fire, meaning it burns or floods or gets thrown out by someone who thought it was junk mail. The overcorrection is worse: people photograph the phrase, split it into an email draft and a text file, or type it into a password manager whose vault lives in a cloud you do not control. Naive Shamir-style splitting done by hand, where the "shares" are just the phrase cut into thirds, is not secret sharing at all. Two of three thirds dramatically reduces the search space for the remainder. This is a math error dressed up as prudence.

**Use.** This is where the smart contract era makes everything worse. The private key is never exposed, and yet the funds leave. Blind signing of opaque calldata is the modern equivalent of signing a blank check. A user approves a transaction they cannot read, and the hardware wallet dutifully signs it because the device authenticates the key, not the intent. ERC-20 `approve` grants a spender an allowance, and unlimited approvals (the `type(uint256).max` pattern that dapps request for convenience) mean a single malicious or later-compromised contract can drain a token balance at any future time. `permit` and `permit2` move that approval into an offchain signature, which means a phishing signature request, not a transaction, can authorize a transfer. `setApprovalForAll` on an NFT collection hands over the entire collection in one click. None of this touches your seed phrase. Your key management was flawless and you still lost everything, because the use phase had no controls on it.

**Recovery.** Untested backups are Schrödinger's backups. The passphrase (the BIP-39 "25th word") that people add for plausible deniability is the same passphrase they forget, turning a recoverable wallet into a permanently locked one. Recovery plans that depend on a person remembering a scheme they invented once, under no time pressure, and will next execute under maximum stress, are not plans.

**Destruction and succession.** Almost nobody thinks about the end of the lifecycle. Old wallets from abandoned setups still hold dust and, worse, still hold live approvals. And the inheritance problem is total: a self-custodied key with no succession mechanism guarantees that your assets die with you or, more likely, get found by whoever cleans out your things.

## Doing It Right

Treat each lifecycle stage as a distinct control, and write it down.

**Generation.** Generate seeds on a dedicated airgapped device or a hardware wallet with a true hardware RNG, never on a networked general-purpose machine. If you want to verify entropy, do it in an environment that will be wiped. The plaintext phrase should exist in exactly one context, in your hands, and then never again in digital form.

**Storage and backup.** Use metal backups, not paper, because your threat model includes fire and water whether you acknowledge it or not. Use geographic distribution so a single physical event cannot destroy every copy. If you split the secret, use a real scheme: SLIP-39 (Shamir's Secret Sharing done correctly) with a proper threshold, not a mnemonic cut into pieces with scissors. Choose your threshold deliberately: a 2-of-3 tolerates one lost share and one compromised share is not enough to steal.

**Use.** This is where most of your gains are now. Adopt a tiered architecture: a hot wallet with trivial balances for interacting with the noise of the ecosystem, and a cold vault that never signs a transaction it did not initiate. For meaningful value, use a smart contract wallet or multisig (Safe being the reference implementation) so that a single key compromise is not a single point of failure. This is separation of duties from the standard, expressed onchain. Stop granting unlimited approvals; set finite allowances and revoke them periodically with a revocation tool. Refuse to blind-sign. Use wallets and setups that support transaction simulation and clear-signing (EIP-712 typed data that shows you what you are actually authorizing) and treat any request you cannot read as hostile.

**Rotation and cryptoperiods.** Keys are not permanent. If you suspect exposure, or on a schedule for high-value holdings, move funds to a freshly generated key. Migrate deliberately, verify receipt, then abandon the old key. A smart contract wallet makes signer rotation possible without moving assets at all, which is one of its quieter advantages.

**Recovery and succession.** Test your recovery. Actually do it: restore to a spare device from your backups before you trust them with anything. Document the scheme for a competent person who is not you, in a form that survives your absence. Social recovery wallets and multisig arrangements with a lawyer or trusted parties turn inheritance from an impossibility into a procedure.

## The Bottom Line

The uncomfortable truth is that the cryptography was never the hard part. The hard part is running a boring operational program, forever, with no deadline and no reward for doing it right, where the only feedback you ever get is catastrophic and final. NIST wrote the manual decades ago. You will not read it. You will buy another hardware wallet, put it in a drawer, and call it custody, and it will work perfectly right up until the one moment it needed to.

*Not your process, not your coins.*

## Related

- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Token Approvals and the Infinite Allowance](/itsalreadypriced/rtfm/2026/07/08/token-approvals-and-the-infinite-allowance/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)
