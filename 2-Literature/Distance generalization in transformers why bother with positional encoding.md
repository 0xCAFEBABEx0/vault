---
title: "Distance generalization in transformers: why bother with positional encoding?"
source: "https://arxiv.org/html/2609.11913v1"
author: "Daniel Henrik Nevermann, Claudius Gros"
published: "2026-09-10"
created: 2026-09-12
description: "Out-of-distribution length generalization, namely to extrapolate a task from short to longer context, has been studied intensively for transformers. Here we focus on distance generalization, which probes performance when inter-token distances are changed between training and inference, while keeping a fixed context length. We construct two synthetic delay copy tasks, both involving finite distances between source an…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/nlp
  - keyword/machine-learning
---

# Distance generalization in transformers: why bother with positional encoding?

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.11913v1)
- published:: 2026-09-10
- updated:: 2026-09-10
- arxiv_id:: 2609.11913v1
- pdf:: https://arxiv.org/pdf/2609.11913v1
- categories:: cs.CL

## Abstract / Summary
Out-of-distribution length generalization, namely to extrapolate a task from short to longer context, has been studied intensively for transformers. Here we focus on distance generalization, which probes performance when inter-token distances are changed between training and inference, while keeping a fixed context length. We construct two synthetic delay copy tasks, both involving finite distances between source and recall, where tokens are copied either fully or selectively, and test models on delays unseen during training. We address three questions: (A) Do positional encoding schemes such as RoPE and ALiBi improve distance resolution relative to no positional encoding (NoPE)? (B) How does data diversity, the number of inter-token distances seen in training, affect performance? (C) When is distance transfer learning positive or negative? We present a thorough investigation, finding that it is paramount to improve our understanding of the underlying mechanisms.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.11913v1)
- [PDF](https://arxiv.org/pdf/2609.11913v1)
- [From Shortcut to Induction Head: How Data Diversity Shapes Algorithm Selection in Transformers](https://arxiv.org/abs/2512.18634) (2025, citations: 6)
- [Quantitative Bounds for Length Generalization in Transformers](https://arxiv.org/abs/2510.27015) (2025, citations: 8)
- [Small transformer architectures for task switching](https://arxiv.org/abs/2508.04461) (2025, citations: 2)
- [Extrapolation by Association: Length Generalization Transfer in Transformers](https://arxiv.org/abs/2506.09251) (2025, citations: 13)
- [Arithmetic Transformers Can Length-Generalize in Both Operand Length and Count](https://arxiv.org/abs/2410.15787) (2024, citations: 18)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/nlp #keyword/machine-learning
