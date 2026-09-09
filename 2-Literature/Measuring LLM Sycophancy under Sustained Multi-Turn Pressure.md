---
title: "Measuring LLM Sycophancy under Sustained Multi-Turn Pressure"
source: "https://arxiv.org/html/2609.09090v1"
author: "Leyuan Tang, Kangda Wei, Tianyu Jiang, Ruihong Huang"
published: "2026-09-08"
created: 2026-09-10
description: "Large language models (LLMs) may abandon correct positions when users push back, exhibiting a failure mode known as sycophancy. Existing evaluations typically use short, pre-specified conversations and may therefore miss failures that emerge under sustained, adaptive disagreement. We introduce SPINE, a benchmark in which an LLM proxy plays a persistent but mistaken user and adaptively challenges a target model for u…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/benchmark
  - keyword/reasoning
---

# Measuring LLM Sycophancy under Sustained Multi-Turn Pressure

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.09090v1)
- published:: 2026-09-08
- updated:: 2026-09-08
- arxiv_id:: 2609.09090v1
- pdf:: https://arxiv.org/pdf/2609.09090v1
- categories:: cs.CL, cs.AI

## Abstract / Summary
Large language models (LLMs) may abandon correct positions when users push back, exhibiting a failure mode known as sycophancy. Existing evaluations typically use short, pre-specified conversations and may therefore miss failures that emerge under sustained, adaptive disagreement. We introduce SPINE, a benchmark in which an LLM proxy plays a persistent but mistaken user and adaptively challenges a target model for up to 25 turns. We evaluate four production systems and three Olmo3-7b variants on 100 false-presupposition and 100 unethical-query items. Our experimental results show that collapse rates increase with conversation length for every model, short-horizon protocols underestimate sycophancy and resistance under sustained pressure remains unreliable across current models. By analyzing models with accessible reasoning traces, we surprisingly found that the correct position often remains represented in a reasoning trace when the response concedes, suggesting that the model chooses to please a user and sycophancy is not due to lack of knowledge or ignorance. Ablations show that adaptive LLM proxy exposes more sycophantic collapse than pre-generated scripts. Among all tactics, emotional appeals is the most associated with inducing LLM sycophantic behavior. The code and data are released at https://anonymous.4open.science/r/SPINE

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.09090v1)
- [PDF](https://arxiv.org/pdf/2609.09090v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark #keyword/reasoning
