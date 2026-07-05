---
layout: field_note
title: "Field Note — July 05, 2026"
date: 2026-07-05
summary: "A fake Maccy clipboard app ships PamStealer on macOS, and Moonbeam is forcing GLMR holders to bridge off Polkadot to Base by July 31."
---

## Today's Field Note
Two operational items today, both with hard deadlines or live risk. First, a new macOS infostealer called PamStealer is masquerading as Maccy, the open-source clipboard manager, and it lifts passwords and wallet material once installed. Clipboard managers are exactly the wrong thing to trust blindly, since that is where your seed phrases and addresses transit in plaintext. Second, Moonbeam is pivoting from Polkadot to Base and has told GLMR holders to bridge tokens off the Polkadot parachain before July 31 or risk being stranded. Neither is a headline exploit, but both are the kind of quiet thing that costs people money while they are watching the BTC candle instead.

## Today's Move
- Do not install Maccy from any source except the official GitHub or Homebrew. If you grabbed it recently from a search-ad link or third-party site, treat the machine as compromised.
- On any Mac that touched a suspect clipboard app, rotate exchange passwords, revoke sessions, and move funds from any hot wallet whose seed or keys were on that device.
- If you hold GLMR on the Polkadot parachain, bridge to Base before July 31 using Moonbeam's official bridge only. Verify the contract, do not trust DM'd links.
- Stop using clipboard managers to move seed phrases entirely. Type or use a hardware wallet's confirmation screen instead.
- Watch for copycat drainer sites riding the Moonbeam migration. Fake "bridge assistant" pages are the obvious next step.

## Resources

- https://decrypt.co/372743/fake-mac-clipboard-app-delivers-password-stealing-malware
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)
