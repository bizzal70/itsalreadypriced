---
layout: rtfm
title: "Seed Phrases and Where Keys Actually Leak"
date: 2026-07-15
summary: "Nobody brute-forces a BIP-39 seed phrase; they photograph it, sync it to the cloud, or paste it into a machine that was already compromised, and this article explains exactly where the leaks happen and how to stop them."
framework: "BIP-39 (Mnemonic Code)"
framework_url: "https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki"
---

Nobody has ever brute-forced your seed phrase. Let that sink in before you buy another metal plate. The entropy math has been settled for a decade, and it is not the weak link. The weak link is you, photographing twelve words on a kitchen table because typing them into a password manager felt paranoid and a screenshot felt convenient. The attacker did not beat the cryptography. The attacker read your camera roll.

## The Standard

BIP-39 defines how a random number becomes a set of human-readable words, and how those words become the seed that feeds a hierarchical deterministic wallet (BIP-32) through a derivation path (BIP-44 and friends). The mechanism is deliberately simple. You start with entropy: 128 bits for a twelve-word phrase, 256 bits for twenty-four. You append a checksum derived from the SHA-256 hash of that entropy (four bits for the twelve-word case, eight for the twenty-four). You slice the combined bits into eleven-bit chunks, and each chunk indexes into a fixed wordlist of exactly 2048 words. That is the whole trick.

The security claim is a claim about entropy, and only about entropy. A twelve-word phrase encodes 128 bits of it. To guess a 128-bit secret by brute force you would need to search a space of 2^128 possibilities, which is the same order of magnitude protecting the AES keys that run the internet. No one is doing that. No one will do that. The number is not large in some hand-wavy sense; it is large in the sense that all the computers that will ever exist could run until the heat death of the sun and not scratch it.

BIP-39 also specifies an optional passphrase, sometimes called the "25th word." This is not part of the mnemonic. It is a separate string mixed into the PBKDF2 key derivation (2048 iterations of HMAC-SHA512, salted with the literal string "mnemonic" concatenated with your passphrase). Change the passphrase and you get an entirely different seed, and therefore an entirely different wallet, from the same words. Remember that. It matters later.

So the standard does exactly one job well: it turns strong randomness into something a human can write down. The word "write" is where the trouble starts. BIP-39 says nothing about where you write it, how you store it, or what machine generated the entropy in the first place. Those are precisely the parts that get people killed, financially speaking.

## Where It Breaks Down

The seed leaks at the boundary between the cryptographic object and the human handling it. Every real-world compromise I have seen lives in one of a few categories, and none of them involve mathematics.

**The phrase becomes a photograph.** You generate the wallet, and the screen shows you twelve words with a countdown-timer sense of urgency. You take a picture. That picture goes to your camera roll, which syncs to iCloud or Google Photos by default, which means your seed phrase now exists as plaintext (well, as pixels containing plaintext) on a server owned by a company that is a permanent target and that will hand data to anyone with the right subpoena or the right breach. Cloud photo backups are also increasingly run through OCR and machine-vision indexing so you can search "receipt" or "dog." That same indexing turns your words into searchable text sitting in a database you do not control.

**The phrase becomes a synced note.** People paste seed phrases into Notes, into a Google Doc, into a password manager, into a Telegram "saved messages" chat to themselves. The password manager is the least-bad of these and still bad, because it collapses your entire portfolio's security into a single credential that is phished daily. The synced note is worse: it rides your account's session tokens across every device you have ever logged in on, including the old laptop you sold.

**The phrase gets typed into a compromised machine.** This is the quiet killer. Clipboard-hijacking malware watches for anything that looks like a BIP-39 mnemonic or an address and either exfiltrates it or swaps it. Infostealers (the commodity malware category that scrapes browser storage, wallet extension vaults, and clipboard history) do not need to break anything. They wait for you to paste. A "wallet recovery" or "validate your wallet" web form is the same attack wearing a suit. The moment the words touch a networked, general-purpose computer, entropy stops being your protection.

**The generation itself was poisoned.** BIP-39's entropy claim assumes the entropy was actually random. A fake hardware wallet with a pre-loaded seed, a compromised random number generator, a "wallet generator" website that seeds its PRNG from something predictable, or a supply-chain-tampered device all produce phrases that look perfectly valid (the checksum passes) and are known to the attacker in advance. The funds are drained the instant they arrive. There was no leak because the key was never secret.

**The passphrase gets misunderstood.** The 25th-word passphrase is powerful precisely because it is not stored with the words. People then store it with the words, defeating the entire point, or they forget it and permanently lose access, or they treat it as a password with 30 bits of guessable entropy and assume it protects a phrase an attacker already has. A weak passphrase on a leaked seed is brute-forceable, because now the attacker is only searching your passphrase space, not the 128-bit seed space.

**Import sprawl.** A hardware wallet only protects the seed if the seed never leaves it. The moment you import those same words into a hot software wallet "just to check a balance" or to use a dapp, you have copied a cold key into a hot environment, and every guarantee the hardware gave you is void for that seed forever.

## Doing It Right

Assume the phrase will eventually be exposed to whatever you store it near. Design backward from that.

**Never let the words touch a camera, a network, or a general-purpose OS after generation.** Generate on a hardware device that displays the words on its own screen. Transcribe by hand. If you must verify, verify on the device, not by typing back into software.

**Store the transcription offline and redundantly.** Paper is fine for a lot of threat models and burns in a house fire; steel plates solve fire and water but not theft or discovery. Two or three geographically separated copies beats one "perfect" copy. The failure mode for most people is loss, not theft, so redundancy is not optional.

**Use the passphrase correctly or not at all.** If you use a BIP-39 passphrase, treat it as an independent secret with real entropy, memorized or stored separately from the words, never in the same location. Understand that losing it loses everything. This is a plausible-deniability and second-factor tool, not a magic wand.

**Consider Shamir-style splitting (SLIP-39) or multisig for meaningful amounts.** Multisig (a 2-of-3 across independent devices and locations) removes the single point of failure entirely. A leaked single share does nothing. This is the correct answer for anything you would be sick to lose, and it is underused because it is slightly annoying to set up once.

**Verify the device and the entropy.** Buy hardware from the manufacturer directly. Check that the device generates a fresh seed in front of you rather than shipping one. Never, ever accept a pre-filled phrase from anyone or anything.

**Keep cold keys cold.** If a seed has been imported into a hot wallet, treat it as hot forever. For serious storage, the phrase is generated, written down, and used only on the airgapped or hardware device. It never gets typed into a browser.

## The Bottom Line

The cryptography did its job. It always does. The 128 bits held. What failed was the two feet of air between the screen and the phone camera, the checkbox for cloud sync you never unchecked, the machine you assumed was clean. Nobody is coming for your entropy. They are coming for your convenience, and you keep leaving it out on the counter.

*Write it down. Don't take a picture of it. This is not hard, which is exactly why you won't do it.*