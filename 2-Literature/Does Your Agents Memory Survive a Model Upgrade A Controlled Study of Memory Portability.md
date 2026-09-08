---
title: "Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability"
source: "https://arxiv.org/html/2609.05339v1"
author: "Ankit Goyal, Jaideep Ray"
published: "2026-09-04"
created: 2026-09-09
description: "Model upgrades are routine; memory migrations are not. An agent can keep the same memory store and still forget: a new model may interpret old notes differently, mixed embedding versions may break retrieval, and repair may fail without the original evidence. We compare memory as the same history is preserved verbatim for long-context reading (LC-RAW), divided into chunks for retrieval-augmented generation (RAG), com…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/agents
---

# Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.05339v1)
- published:: 2026-09-04
- updated:: 2026-09-04
- arxiv_id:: 2609.05339v1
- pdf:: https://arxiv.org/pdf/2609.05339v1
- categories:: cs.AI, cs.CL, cs.IR

## Abstract / Summary
Model upgrades are routine; memory migrations are not. An agent can keep the same memory store and still forget: a new model may interpret old notes differently, mixed embedding versions may break retrieval, and repair may fail without the original evidence. We compare memory as the same history is preserved verbatim for long-context reading (LC-RAW), divided into chunks for retrieval-augmented generation (RAG), compressed by a model into natural-language notes (NOTES), or normalized into a fixed-schema knowledge graph (KG-fixed). The study uses 48 synthetic histories with randomized answer codes, exact scoring, and two open-weight models with sub 10 billion parameters. Our measurements show that fixed-schema structures transfer reliably, with KG-fixed accuracy changing by only $+0.0004 \pm 0.0020$ following a writer swap. Conversely, compressed NOTES exhibit high model coupling, with accuracy shifting asymmetrically by $+9.91$ or $-13.28$ percentage points depending on the specific migration direction. In RAG systems, partial embedding migrations using a 50/50 mixed index capture only a 4.96-point accuracy improvement, forfeiting the majority of the 11.90-point gain achieved through full re-embedding. Diagnostic decomposition attributes 80% ($0.467 \pm 0.014$) of the NOTES accuracy deficit to information lost during initial construction, whereas retrieval failures drive 81% ($0.364 \pm 0.012$) of the RAG deficit. Finally, store-only repair of NOTES fails to reach a 90% performance recovery target in all 48 test cases, whereas retaining the raw source history enables successful recovery in 34 of 48 cases for one tested direction. These findings highlight the necessity of direction-specific migration testing, strict embedding space isolation, and the retention of source…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.05339v1)
- [PDF](https://arxiv.org/pdf/2609.05339v1)
- [Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation](https://arxiv.org/abs/2606.23127) (2026, citations: 5)
- [MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization](https://arxiv.org/abs/2603.25973) (2026, citations: 16)
- [Memori: A Persistent Memory Layer for Efficient, Context-Aware LLM Agents](https://arxiv.org/abs/2603.19935) (2026, citations: 12)
- [From Experience to Strategy: Empowering LLM Agents with Trainable Graph Memory](https://arxiv.org/abs/2511.07800) (2025, citations: 12)
- [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) (2025, citations: 611)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/agents
