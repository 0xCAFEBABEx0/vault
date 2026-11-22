---
title: "Active Feature Acquisition by Distilling an Oracle Teacher"
source: "https://arxiv.org/html/2611.26598v1"
author: "Yang Meng, Zixin Ding, Robert L. Grossman, Yuxin Chen"
published: "2026-11-19"
created: 2026-11-23
description: "Acquiring every feature of an instance is often costly: a measurement can carry a monetary price, a time delay, or a privacy cost. Active Feature Acquisition (AFA) addresses this by learning a policy that decides, per instance, which features to acquire under a budget. Existing AFA methods train this policy by optimizing a self-constructed utility target rather than distilling an explicit teacher. We construct this…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/multimodal
  - keyword/evaluation
  - keyword/benchmark
  - keyword/machine-learning
---

# Active Feature Acquisition by Distilling an Oracle Teacher

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.26598v1)
- published:: 2026-11-19
- updated:: 2026-11-19
- arxiv_id:: 2611.26598v1
- pdf:: https://arxiv.org/pdf/2611.26598v1
- categories:: cs.LG, cs.AI

## Abstract / Summary
Acquiring every feature of an instance is often costly: a measurement can carry a monetary price, a time delay, or a privacy cost. Active Feature Acquisition (AFA) addresses this by learning a policy that decides, per instance, which features to acquire under a budget. Existing AFA methods train this policy by optimizing a self-constructed utility target rather than distilling an explicit teacher. We construct this teacher explicitly. At training time the label and the unobserved feature values are available, and together they determine the teacher in closed form: an oracle that ranks every candidate by its effect on the downstream predictor's error. OracleImitator distills this ranking into a deployable policy by soft-target imitation. Across multimodal medical diagnosis and the AFABench benchmark, OracleImitator matches or outperforms existing AFA methods across the budget range, recovering 90% of the attainable accuracy gain at under a quarter of the acquisition cost. Because the teacher is an explicit algorithmic object rather than an implicit optimization target, we can also measure directly how much of its ranking is recoverable by a policy restricted to what is visible at deployment.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.26598v1)
- [PDF](https://arxiv.org/pdf/2611.26598v1)
- [Text-Twin-Translation (T3): A Full-Stack Machine Learning Framework for Functional Material-Device Systems Discovery](https://doi.org/10.1145/3770855.3819013) (2026, citations: 1)
- [Rethinking Transfer in Continual Learning: A Replay-Based Realisation](https://arxiv.org/abs/2607.15587) (2026, citations: 5)
- [Accelerating PDE Surrogates via RL-Guided Mesh Optimization](https://arxiv.org/abs/2603.02066) (2026, citations: 3)
- [AFABench: A Generic Framework for Benchmarking Active Feature Acquisition](https://arxiv.org/abs/2508.14734) (2025, citations: 13)
- [Multimodal Cancer Modeling in the Age of Foundation Model Embeddings](https://arxiv.org/abs/2505.07683) (2025, citations: 3)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/multimodal #keyword/evaluation #keyword/benchmark #keyword/machine-learning
