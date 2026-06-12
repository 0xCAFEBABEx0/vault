---
title: "Operadic consistency: a label-free signal for compositional reasoning failures in LLMs"
source: "https://arxiv.org/html/2606.13649v1"
author: "Nathaniel Bottman, Yinhong Liu, Kyle Richardson"
published: "2026-06-11"
created: 2026-06-13
description: "Detecting LLM reasoning failures at inference time without ground-truth labels has motivated a wide range of confidence baselines..."
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/retrieval
  - keyword/evaluation
  - keyword/reasoning
  - keyword/machine-learning
---

# Operadic consistency: a label-free signal for compositional reasoning failures in LLMs

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.13649v1)
- published:: 2026-06-11
- updated:: 2026-06-11
- arxiv_id:: 2606.13649v1
- pdf:: https://arxiv.org/pdf/2606.13649v1
- categories:: cs.CL, cs.LG

## Abstract / Summary
Detecting LLM reasoning failures at inference time without ground-truth labels has motivated a wide range of confidence baselines, including self-consistency, semantic entropy, and P(True). Operad theory suggests a complementary diagnostic: a model's direct answer to a compositional query should agree with the answer it produces by composing a stated decomposition of the same query. We instantiate this idea as operadic consistency (OC), a per-question signal. Across twelve instruction-tuned LLMs (4B to 671B parameters) on four multi-hop QA datasets, OC is strongly correlated with accuracy on every dataset (Pearson r in [0.86, 0.94], all p <= 0.0004), and is the only signal we evaluate with r >= 0.85 uniformly across all four datasets.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.13649v1)
- [PDF](https://arxiv.org/pdf/2606.13649v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/retrieval #keyword/evaluation #keyword/reasoning #keyword/machine-learning
