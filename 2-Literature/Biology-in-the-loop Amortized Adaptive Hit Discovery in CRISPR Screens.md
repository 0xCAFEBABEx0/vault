---
title: "Biology-in-the-loop: Amortized Adaptive Hit Discovery in CRISPR Screens"
source: "https://arxiv.org/html/2609.11877v1"
author: "Carl Edwards, Edward De Brouwer, Xiner Li, Namkyeong Lee, Ehsan Hajiramezanali, Anne Biton, Sara Mostafavi, Gabriele Scalia"
published: "2026-09-10"
created: 2026-09-12
description: "Many biological discovery problems require experiments to be selected sequentially under constrained budgets. CRISPR screening is a prominent example, as exhaustive perturbation testing is often infeasible and candidate perturbations must instead be prioritized over multiple experimental rounds. Despite the importance of this problem, existing benchmarks for adaptive hit discovery remain limited in scale and diversi…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/evaluation
  - keyword/benchmark
  - keyword/machine-learning
---

# Biology-in-the-loop: Amortized Adaptive Hit Discovery in CRISPR Screens

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.11877v1)
- published:: 2026-09-10
- updated:: 2026-09-10
- arxiv_id:: 2609.11877v1
- pdf:: https://arxiv.org/pdf/2609.11877v1
- categories:: q-bio.QM, cs.AI, cs.CL, q-bio.GN

## Abstract / Summary
Many biological discovery problems require experiments to be selected sequentially under constrained budgets. CRISPR screening is a prominent example, as exhaustive perturbation testing is often infeasible and candidate perturbations must instead be prioritized over multiple experimental rounds. Despite the importance of this problem, existing benchmarks for adaptive hit discovery remain limited in scale and diversity. Here, we introduce AssayBench-Loop, a large-scale benchmark for adaptive hit discovery comprising 1,389 CRISPR screens across five phenotype categories. Beyond enabling systematic evaluation, its scale makes it possible to learn acquisition strategies across historical experiments. Building on this resource, we introduce AssayLoop, a sequential experimental design framework combining AssayFormer, a transformer-based amortized acquisition policy trained across historical screens to adapt from experimental feedback, with LLM-derived biological priors through an adaptive handoff. In this view, completed experiments become training data for learning how accumulated evidence should guide what to test next, while LLMs provide prior biological knowledge to seed the search. We further introduce AssayLLM, showing that the same principle can be extended directly to an LLM through task-specific post-training. On temporally held-out screens, AssayLoop achieves a 5.67-fold enrichment over random selection and recovers 27.7% of hits after assaying approximately 5% of the candidate library, outperforming existing adaptive-design methods and standalone LLMs, and AssayFormer alone. Performance improves with increasing historical training data and transfers to phenotype categories excluded from training. These results demonstrate the value of learning acquisition policies…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.11877v1)
- [PDF](https://arxiv.org/pdf/2609.11877v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/evaluation #keyword/benchmark #keyword/machine-learning
