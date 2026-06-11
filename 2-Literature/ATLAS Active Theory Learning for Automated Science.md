---
title: "ATLAS: Active Theory Learning for Automated Science"
source: "https://arxiv.org/html/2606.12386v1"
author: "Noémi Éltető, Nathaniel D. Daw, Kimberly L. Stachenfeld, Kevin J. Miller"
published: "2026-06-10"
created: 2026-06-12
description: "Advancing scientific understanding through mechanistic modeling requires posing the right experimental questions to yield maximally informative data. To automate this pursuit within cognitive science, we introduce ATLAS (Active Theory Learning for Automated Science), an active learning framework for the data-driven discovery of interpretable behavioral models. ATLAS iterates between generating mechanistic hypotheses…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/evaluation
  - keyword/agents
---

# ATLAS: Active Theory Learning for Automated Science

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.12386v1)
- published:: 2026-06-10
- updated:: 2026-06-10
- arxiv_id:: 2606.12386v1
- pdf:: https://arxiv.org/pdf/2606.12386v1
- categories:: cs.LG, cs.AI

## Abstract / Summary
Advancing scientific understanding through mechanistic modeling requires posing the right experimental questions to yield maximally informative data. To automate this pursuit within cognitive science, we introduce ATLAS (Active Theory Learning for Automated Science), an active learning framework for the data-driven discovery of interpretable behavioral models. ATLAS iterates between generating mechanistic hypotheses--instantiated as a diverse ensemble of sparse neural networks (Disentangled RNNs)--and designing experiments that optimally distinguish between them. We test this approach on the problem of recovering reinforcement learning agents from their behavior in bandit tasks. ATLAS designs varied sequences of qualitatively novel experiments with temporal structure tailored to underlying agent characteristics. The models trained on these experiments are evaluated against a comprehensive set of metrics for mechanistic modeling that capture behavioral, structural, and computational similarity. ATLAS achieves a 5-10x improvement in sample efficiency across all metrics compared to random experimentation, and its performance is further validated against expert-designed experiments derived from literature. These in silico results showcase ATLAS's potential to accelerate human-interpretable insights in cognitive science and other domains where scientific inquiry relies on discovering mechanistic models.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.12386v1)
- [PDF](https://arxiv.org/pdf/2606.12386v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/evaluation #keyword/agents
