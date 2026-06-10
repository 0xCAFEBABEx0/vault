---
title: "Provenance-Grounded Gating and Adaptive Recovery in Synthetic Post-Training Data Curation"
source: "https://arxiv.org/html/2606.11127v1"
author: "Soham Bhattacharjee, Karun Sharma, Vinay Kumar Sankarapu, Pratinav Seth"
published: "2026-06-09"
created: 2026-06-11
description: "Synthetic post-training pipelines commonly filter generated samples with reward models or holistic LLM judges, yet two practices remain rarely examined together: whether the filtering signal is grounded in the source evidence and whether rejected samples can be systematically recovered."
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/machine-learning
---

# Provenance-Grounded Gating and Adaptive Recovery in Synthetic Post-Training Data Curation

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.11127v1)
- published:: 2026-06-09
- updated:: 2026-06-09
- arxiv_id:: 2606.11127v1
- pdf:: https://arxiv.org/pdf/2606.11127v1
- categories:: cs.CL, cs.AI

## Abstract / Summary
Synthetic post-training pipelines commonly filter generated samples with reward models or holistic LLM judges, yet two practices remain rarely examined together: whether the filtering signal is grounded in the source evidence that induced each generation, and whether rejected samples can be systematically recovered rather than permanently discarded. We present a controlled study of both questions across gate configurations, recovery strategies, and generator scales, using adversarially injected corpora to provide ground-truth failure labels. We find that exact source provenance improves faithfulness gating for stronger judges, that hallucination and reward gates reject largely disjoint sample populations making both necessary, and that an adaptive recovery pipeline combining failure diagnosis with targeted regeneration achieves higher yield, recovery rate, and injection recall than naive resampling.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.11127v1)
- [PDF](https://arxiv.org/pdf/2606.11127v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/machine-learning
