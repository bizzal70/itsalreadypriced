---
layout: field_note
title: "Field Note — September 18, 2026"
date: 2026-09-18
summary: "DPRK-linked npm stealers and a hijacked IOG YouTube channel are the day's live threats, both aimed at builder machines and Cardano holders."
---

## Today's Field Note
Two supply-chain and social-engineering campaigns are live and worth your attention today. OpenSourceMalware flagged 13 npm packages carrying WeaselBiscuit, a JavaScript stealer that harvests Chrome extension storage (read: browser wallet vaults) and shares functional overlap with DPRK's BeaverTail and the Contagious Interview campaign. Separately, a second npm strain called PhantomRaven surfaced, likely LLM-authored, same registry, same goal. Meanwhile Input Output Group told users to stay off its own YouTube channel after it was hijacked to livestream an AI-manipulated Charles Hoskinson "double your wealth" giveaway. None of this is exotic. It is the usual DPRK and scam-adjacent plumbing, and it works because people paste before they check.

## Today's Move
- Audit recent npm installs against the flagged WeaselBiscuit and PhantomRaven packages (check the OpenSourceMalware writeup for names) and purge from any machine holding keys.
- Assume browser extension wallet storage is compromised if you touched suspect packages: move funds to a fresh hardware wallet and rotate seeds, do not just re-import.
- Never run "test tasks" or repos from unsolicited recruiters. That is the Contagious Interview playbook, and it targets builders specifically.
- Treat every YouTube "giveaway" livestream, including from official-looking channels like IOG's, as a hijack until proven otherwise. No legitimate project doubles your ZEC, ADA, or anything else.
- Pin your dev environment dependencies and enable install-time scanning before your next build, not after.

## Resources

- https://thehackernews.com/2026/09/weaselbiscuit-stealer-spreads-via-13.html
- https://thehackernews.com/2026/09/claimed-bug-bounty-hunter-likely-used.html
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)
- [Multisig and Threshold Signing, Beyond Buying a Safe](/itsalreadypriced/rtfm/2026/07/29/multisig-and-threshold-signing-beyond-buying-a-safe/)
- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*