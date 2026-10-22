---
layout: field_note
title: "Field Note — October 22, 2026"
date: 2026-10-22
summary: "Railway secrets breach already costing crypto devs real money, while LiteLLM's poisoned release and three max-severity RCE bugs round out a brutal day for the supply chain."
---

## Today's Field Note
Railway, the PaaS many crypto teams use to host bots and backends, disclosed that an intruder accessed customer environment variables, in some cases the decrypted contents. This is not theoretical: a developer has already linked a $370,000 theft to the exposure, and Enterprise builds were restored before other plans could even redeploy with fresh credentials. Separately, LiteLLM's release pipeline was compromised on October 21 to push version 1.107.0 with a credential stealer and backdoor to both PyPI and Docker Hub, meaning anyone who pulled it handed over whatever secrets that host held. If your stack touches either, assume every key in that environment is burned.

## Today's Move
- If you deploy on Railway, rotate every secret stored there now: RPC keys, exchange API keys, hot wallet private keys, database creds, webhook signers. Do not just redeploy, regenerate.
- Sweep any hot wallet whose key sat in a Railway env var to a freshly generated address.
- Pin and audit LiteLLM: if you pulled 1.107.0 from PyPI or Docker Hub on or after Oct 21, treat the host as compromised, rotate its tokens, and roll back to a known-good version.
- Patch Node.js today (22.x, 24.x, 26.x) for the Brotli decoder RCE, and update GitLab for the max-severity RegEx compiler flaw.
- Revoke and reissue any GitHub tokens that passed through LiteLLM gateway logs, which is the suspected leak vector.

## Resources

- https://thedefiant.io/news/security/developer-links-370-000-theft-to-railway-secrets-exposure
- https://thehackernews.com/2026/10/railway-says-intruder-may-have-accessed.html
- https://thehackernews.com/2026/10/litellm-suspects-github-token-leak-in.html
- https://thehackernews.com/2026/10/nodejs-brotli-decoder-bug-could-allow.html
- https://www.bleepingcomputer.com/news/security/gitlab-warns-of-new-max-severity-code-execution-vulnerability/
- Incident trackers (reference standard): [Rekt leaderboard](https://rekt.news/leaderboard/) · [SlowMist Hacked](https://hacked.slowmist.io/)


## Related

- [Cold Storage and Operational Security for Custody](/itsalreadypriced/rtfm/2026/09/02/cold-storage-and-operational-security-for-custody/)
- [North Korea Slips Into Consensys While macOS Malware Reads Your Telegram](/itsalreadypriced/2026/07/19/issue-003/)
- [Seed Phrases and Where Keys Actually Leak](/itsalreadypriced/rtfm/2026/07/15/seed-phrases-and-where-keys-actually-leak/)

More: [Issues](/itsalreadypriced/) · [Field Notes](/itsalreadypriced/field-notes/) · [RTFM](/itsalreadypriced/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@ItsAlreadyPrice](https://x.com/ItsAlreadyPrice) or subscribe via RSS.*