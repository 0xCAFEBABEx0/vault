---
title: "Accelerating Speculative Diffusions via Block Verification"
source: "https://arxiv.org/html/2606.13426v1"
author: "Alexander Soen, Hisham Husain, Valentin De Bortoli, Arnaud Doucet"
published: "2026-06-11"
created: 2026-06-14
description: "Speculative decoding speeds up LLM inference by using a draft model to generate tokens, with an acceptance-rejection scheme that ensures that the output matches the target distribution. Adapting this to continuous diffusions is difficult because speculative sampling requires drawing from a residual distribution. While straightforward in discrete spaces, efficiently sampling this residual in continuous space is non-t…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/diffusion
  - keyword/machine-learning
---

# Accelerating Speculative Diffusions via Block Verification

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.13426v1)
- published:: 2026-06-11
- updated:: 2026-06-11
- arxiv_id:: 2606.13426v1
- pdf:: https://arxiv.org/pdf/2606.13426v1
- categories:: cs.LG, stat.ML

## Abstract / Summary
Speculative decoding speeds up LLM inference by using a draft model to generate tokens, with an acceptance-rejection scheme that ensures that the output matches the target distribution. Adapting this to continuous diffusions is difficult because speculative sampling requires drawing from a residual distribution. While straightforward in discrete spaces, efficiently sampling this residual in continuous space is non-trivial. Consequently, existing diffusion adaptations either use computationally inefficient sampling techniques or rely on an alternative scheme. In this work, we introduce a novel scheme that efficiently implements the original speculative sampling mechanism for diffusion models. Our approach offers a critical advantage over current methods: it enables us to adapt block verification from LLMs to diffusions -- which provably improves the acceptance rate of drafts. Furthermore, we formalize and analyze the Free Drafter, a heuristic self-speculative drafter for diffusions that requires no training. By enabling block verification, our Free Drafter yields up to a 6.3% speedup over existing speculative methods with no additional training and negligible overhead beyond the existing parallel verification pass.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.13426v1)
- [PDF](https://arxiv.org/pdf/2606.13426v1)
- [Speculative Sampling For Faster Molecular Dynamics](https://arxiv.org/abs/2606.02455) (2026, citations: 1)
- [TS-DP: Reinforcement Speculative Decoding For Temporal Adaptive Diffusion Policy Acceleration](https://arxiv.org/abs/2512.15773) (2025, citations: 4)
- [Fast-ARDiff: An Entropy-informed Acceleration Framework for Continuous Space Autoregressive Generation](https://arxiv.org/abs/2512.08537) (2025, citations: 2)
- [FREE: Uncertainty-Aware Autoregression for Parallel Diffusion Transformers](https://arxiv.org/abs/2511.20390) (2025, citations: 1)
- [Accelerating Time Series Foundation Models with Speculative Decoding](https://arxiv.org/abs/2511.18191) (2025, citations: 1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/diffusion #keyword/machine-learning
