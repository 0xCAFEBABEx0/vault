---
title: "LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers"
source: "https://arxiv.org/html/2611.05304v1"
author: "Minsoo Cheong, Sungjoo Yoo"
published: "2026-11-03"
created: 2026-11-05
description: "Looped transformers are a parameter-efficient alternative to standard transformers for language modeling. By reapplying the same layers across multiple loop steps, recent looped language models match the performance of non-looped models several times their size. While this architecture effectively reduces parameter memory, each loop step still stores its own keys and values, so the key-value (KV) cache grows linearl…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/reasoning
---

# LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.05304v1)
- published:: 2026-11-03
- updated:: 2026-11-03
- arxiv_id:: 2611.05304v1
- pdf:: https://arxiv.org/pdf/2611.05304v1
- categories:: cs.LG, cs.AI, cs.CL

## Abstract / Summary
Looped transformers are a parameter-efficient alternative to standard transformers for language modeling. By reapplying the same layers across multiple loop steps, recent looped language models match the performance of non-looped models several times their size. While this architecture effectively reduces parameter memory, each loop step still stores its own keys and values, so the key-value (KV) cache grows linearly with the number of loop steps and becomes the main memory bottleneck. We observe that the KV cache of looped models is highly redundant along the loop axis and that the loop steps differ substantially in their sensitivity to quantization. Based on these observations, we propose $\textbf{LoopVQ}$, a KV cache vector quantization method for looped transformers that codes channels of multiple loop steps jointly, and fine-tunes the codebooks to match the output of the full-precision model. At 0.5 bits per element, LoopVQ outperforms existing KV cache vector quantization methods for standard LLMs on general, long chain-of-thought reasoning, and long-context retrieval tasks with Ouro and Huginn models. Its design is orthogonal to these methods, and combined with TaSQ, it retains much of the BF16 accuracy even at 0.25 bits per element. We also implement LoopVQ in SGLang, where it nearly halves the decode latency at a 32K-token context and raises the peak serving throughput by up to $4.3\times$ and $6.1\times$ on the 1.4B and 2.6B Ouro models compared to the BF16 baseline.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.05304v1)
- [PDF](https://arxiv.org/pdf/2611.05304v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/reasoning
