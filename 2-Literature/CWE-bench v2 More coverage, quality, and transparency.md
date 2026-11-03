---
title: "CWE-bench v2: More coverage, quality, and transparency"
source: "https://huggingface.co/blog/cwe-bench"
author: "Hugging Face Blog"
published: "2026-11-03"
created: 2026-11-04
description: "Our goal is to be exhaustive. A defender has to anticipate the ways an attacker could get in, and get it right every single time. These 100 tasks cover 91 different CWEs, spanning a wide range of vulnerability classes. A model that does well here has to understand the multiple weakness surfaces that a potential attacker can exploit. Recognising a familiar pattern is not enough. As part of our meticulous effort to ke…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/retrieval
  - keyword/evaluation
  - keyword/benchmark
---

# CWE-bench v2: More coverage, quality, and transparency

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/cwe-bench)
- published:: 2026-11-03

## Abstract / Summary
Our goal is to be exhaustive. A defender has to anticipate the ways an attacker could get in, and get it right every single time. These 100 tasks cover 91 different CWEs, spanning a wide range of vulnerability classes. A model that does well here has to understand the multiple weakness surfaces that a potential attacker can exploit. Recognising a familiar pattern is not enough. As part of our meticulous effort to keep improving quality, for every task we checked that the following questions were true: Every task was also reviewed by hand. Open-sourcing the set is part of the same effort to improve quality. We welcome feedback on any task, and contributions to the public set. Results Results are tracked in two places on the Hub. The leaderboard on the CWE-bench dataset page covers open-weight models and updates on its own: labs and the community add a result by opening a PR on the model's repo with a results file ( how ). For the full comparison, including API-only models such as Gemini, Claude and GPT, see the CWE-bench leaderboard Space , where new models are added through a PR on the Space. Of the 11 models evaluated, Gemini 4 Argon leads with 67.8% pass@1 and 81.0% pass@4, just…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/retrieval #keyword/evaluation #keyword/benchmark
