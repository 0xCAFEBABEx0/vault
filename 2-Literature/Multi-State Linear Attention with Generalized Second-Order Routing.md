---
title: "Multi-State Linear Attention with Generalized Second-Order Routing"
source: "https://arxiv.org/html/2610.37645v1"
author: "Hee Seung Hwang, Sanghyuk Chun, Xindi Wu, Olga Russakovsky, Zhiwei Deng"
published: "2026-10-27"
created: 2026-10-29
description: "Self-attention plays a key role in long-sequence modeling, but its quadratic time complexity fundamentally limits the scaling of Large Language Models. Recently, Multi-State Linear Attention (MSLA) mechanisms have been proposed to make sequence modeling more efficient by splitting the context into segments and compressing each in its own memory state. MSLA aggregates the information extracted from each memory state…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/nlp
  - keyword/safety
---

# Multi-State Linear Attention with Generalized Second-Order Routing

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.37645v1)
- published:: 2026-10-27
- updated:: 2026-10-27
- arxiv_id:: 2610.37645v1
- pdf:: https://arxiv.org/pdf/2610.37645v1
- categories:: cs.CL

## Abstract / Summary
Self-attention plays a key role in long-sequence modeling, but its quadratic time complexity fundamentally limits the scaling of Large Language Models. Recently, Multi-State Linear Attention (MSLA) mechanisms have been proposed to make sequence modeling more efficient by splitting the context into segments and compressing each in its own memory state. MSLA aggregates the information extracted from each memory state using only the mean alignment between a query and each segment's keys, ignoring how the alignment is distributed within the segment. In order to model the relevance of a segment to a query more comprehensively and incorporate the variance of the alignment in the aggregation, we propose MERLIN (MomEnt Routing for multi-state LINear attention), a method that tracks the first and second moments of each segment's keys. Using the moments of keys, a query can recover both the mean and the variance of its alignment with each segment to perform a more content-aware aggregation of per-state readouts. Experiments on multi-state variants of Gated DeltaNet-1.3B and Mamba-2-780M show that MERLIN consistently outperforms existing aggregation methods on various long-context tasks. In particular, MERLIN outperforms baselines on RULER needle-in-a-haystack and long-context QA (+8.3% for Gated DeltaNet-1.3B and +7.0% for Mamba-2-780M) and diverse subtasks in LongBench (+13.5% and +12.0%). It even outperforms baselines that consume 4x more memory. MERLIN provides a simple and general routing mechanism for improving long-context capabilities of MSLA models.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.37645v1)
- [PDF](https://arxiv.org/pdf/2610.37645v1)
- [Addressable Memory for Video World Models](https://arxiv.org/abs/2608.07408) (2026, citations: 16)
- [Dynamic Linear Attention](https://arxiv.org/abs/2606.10650) (2026, citations: 5)
- [Memory Caching: RNNs with Growing Memory](https://arxiv.org/abs/2602.24281) (2026, citations: 17)
- [Reinforced Fast Weights via Next-Sequence Prediction](https://arxiv.org/abs/2602.16704) (2026, citations: 2)
- [Scaling Linear Attention with Sparse State Expansion](https://arxiv.org/abs/2507.16577) (2025, citations: 15)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp #keyword/safety
