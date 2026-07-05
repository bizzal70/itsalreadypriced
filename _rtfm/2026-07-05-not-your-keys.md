---
layout: rtfm
title: "Not your keys: what custody actually means"
summary: "A working model of who can move your coins, and the three failure modes that empty wallets."
date: 2026-07-05
framework: "EIP-20 Token Standard"
framework_url: "https://eips.ethereum.org/EIPS/eip-20"
---

"Not your keys, not your coins" is repeated so often it has stopped meaning anything. Here is the version that survives contact with an incident report.

## Who Can Move The Coins

Control of an asset on-chain reduces to one question: who holds the private key that authorizes a transfer. Everything else is a wrapper around that fact.

- **Self-custody.** You hold the key. You are the whole security model, which means you are also the whole failure model.
- **Exchange custody.** The exchange holds the key. Your balance is a database row that represents a claim against their reserves. You are trusting their operational security and their solvency.
- **Smart-contract custody.** A contract holds the funds and moves them according to code. You are trusting the code, the people who can upgrade it, and whatever keys govern it.

None of these is safe by default. Each is a different question about who you trust and what breaks first.

## The Three Failure Modes

Across incident reports, wallet losses cluster into three shapes.

### 1. Key compromise

The key leaks. Malware scrapes it, a phishing page harvests the seed phrase, or a signer reuses a device that was already owned. Once the key is out, the chain does exactly what it is designed to do and honors the transfer.

Defense is boring and effective: hardware wallets keep the key off the internet, and multisig means one compromised key is not enough to move funds.

### 2. Approval abuse

You never lose the key. You lose a permission. As covered in today's Field Note, a live token allowance lets a contract spend what you already authorized. This is how funds leave wallets whose owners swear they never signed anything.

Defense: minimal allowances, routine revocation, and reading what you sign.

### 3. Protocol failure

The key and the approvals are fine. The contract itself is the problem: a logic bug, an oracle that can be pushed, or an upgrade key in the wrong hands. Your funds were only ever as safe as the weakest line of code holding them.

Defense here is mostly selection. Prefer audited, battle-tested contracts, understand who controls upgrades, and size positions to survive the contract failing entirely.

## The Working Model

Before you hold value anywhere, answer three questions. Who holds the key. What one failure empties this. And whether you could survive that failure. If you cannot answer all three, you are not self-custodying. You are gambling with extra steps.

## Sources

- Token transfer semantics: [EIP-20 Token Standard](https://eips.ethereum.org/EIPS/eip-20)
- Approval mechanics: [EIP-20 `approve` / `allowance`](https://eips.ethereum.org/EIPS/eip-20)
- Historical incident data by loss size: [Rekt News leaderboard](https://rekt.news/leaderboard/)
