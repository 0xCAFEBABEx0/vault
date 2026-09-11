---
title: "Data Scarcity and Model Sparsity: Mixtures-of-Experts Overfit More to Repeated Data"
source: "https://arxiv.org/html/2609.11917v1"
author: "Atindra Jha, Margaret Li, Jure Leskovec, Percy Liang, Luke Zettlemoyer"
published: "2026-09-10"
created: 2026-09-12
description: "As the supply of human-written text is exhausted, it has become standard practice to repeat language model training data. Prior work has studied data repetition for densely activated Transformers, but the effects of data repetition remains largely unexplored for recently dominant sparse architectures such as Mixture-of-Experts (MoE), despite their increased compute efficiency. We vary data repetition rates across si…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/nlp
  - keyword/machine-learning
---

# Data Scarcity and Model Sparsity: Mixtures-of-Experts Overfit More to Repeated Data

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.11917v1)
- published:: 2026-09-10
- updated:: 2026-09-10
- arxiv_id:: 2609.11917v1
- pdf:: https://arxiv.org/pdf/2609.11917v1
- categories:: cs.LG, cs.CL

## Abstract / Summary
As the supply of human-written text is exhausted, it has become standard practice to repeat language model training data. Prior work has studied data repetition for densely activated Transformers, but the effects of data repetition remains largely unexplored for recently dominant sparse architectures such as Mixture-of-Experts (MoE), despite their increased compute efficiency. We vary data repetition rates across single- and multi-domain data mixes, and across MoE settings, including expert count and granularity. We consistently find, for models ranging from 80M to 1B active (8.5B total) parameters, that MoEs degrade more rapidly under data repetition. This effect increases with sparsity, dictated by total rather than active parameters. While 80M dense models can repeat data over 8x with minimal degradation, MoEs instead begin to suffer at 4x, and deteriorate rapidly, ceding their performance benefits in all-unique data settings to underperform dense models after 32x. We experiment with existing regularization methods as a potential remedy. We find that some methods, such as dropout, can mitigate overfitting. In particular, with strong masking-based regularization, MoEs are able to outperform dense models even when data is repeated more than 64 times. However, no method fully matches the performance of all-unique training data. Finally, we analyze internal mechanisms correlated with MoE overfitting in high repetition regimes, and find that MoE routing universally stabilizes early in training, and that expert specialization correlates with overfitting to repeated data. In sum, our work addresses the adverse interactions between sparsity and data repetition: we present evidence for the core mechanisms of overfitting and its potential remediation, and suggest promising av…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.11917v1)
- [PDF](https://arxiv.org/pdf/2609.11917v1)
- [Internal Data Repetition Destroys Language Models](https://arxiv.org/abs/2606.24998) (2026, citations: 2)
- [A Bitter Lesson for Data Filtering](https://arxiv.org/abs/2605.19407) (2026, citations: 4)
- [Prescriptive Scaling Laws for Data Constrained Training](https://arxiv.org/abs/2605.01640) (2026, citations: 6)
- [Scale Dependent Data Duplication](https://arxiv.org/abs/2603.06603) (2026, citations: 3)
- [Datasets, Documents, and Repetitions: The Practicalities of Unequal Data Quality](https://arxiv.org/abs/2503.07879) (2025, citations: 5)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp #keyword/machine-learning
