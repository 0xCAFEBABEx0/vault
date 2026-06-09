---
title: "FASE: Fast Adaptive Semantic Entropy for Code Quality"
source: "https://arxiv.org/html/2606.09800v1"
author: "Shizhe Lin, Ladan Tahvildari"
published: "2026-06-08"
created: 2026-06-10
description: "Multi-agent code generation offers a promising paradigm for autonomous software development by simulating the human software engineering lifecycle. However, system reliability remains hindered by LLM hallucinations and error propagation across interacting agents. While semantic entropy provides a principled way to quantify uncertainty without ground-truth answers, current methods often rely on costly LLM-driven equi…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/retrieval
  - keyword/evaluation
  - keyword/agents
---

# FASE: Fast Adaptive Semantic Entropy for Code Quality

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.09800v1)
- published:: 2026-06-08
- updated:: 2026-06-08
- arxiv_id:: 2606.09800v1
- pdf:: https://arxiv.org/pdf/2606.09800v1
- categories:: cs.SE, cs.AI, cs.MA

## Abstract / Summary
Multi-agent code generation offers a promising paradigm for autonomous software development by simulating the human software engineering lifecycle. However, system reliability remains hindered by LLM hallucinations and error propagation across interacting agents. While semantic entropy provides a principled way to quantify uncertainty without ground-truth answers, current methods often rely on costly LLM-driven equivalence checks. In this work, we introduce Fast Adaptive Semantic Entropy (FASE), a novel metric that approximates functional correctness based on the minimum spanning tree of structural and semantic dissimilarity graphs. Evaluations on HumanEval and BigCodeBench demonstrate that FASE outperforms state-of-the-art semantic entropy by LLM entailment, achieving a 25% average improvement in Spearman correlation and a 19% increase in ROCAUC score against Pass@1 from ground-truth test cases when using the Qwen3-Embedding-8B model. Furthermore, by eliminating costly LLM-driven equivalence evaluation, FASE incurs negligible computational overhead, requiring only approximately 0.3% of the runtime cost of traditional semantic entropy approaches. These results position FASE as a practical, cost-effective solution for optimizing uncertainty quantification in real-world multi-agent workflows.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.09800v1)
- [PDF](https://arxiv.org/pdf/2606.09800v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/retrieval #keyword/evaluation #keyword/agents
