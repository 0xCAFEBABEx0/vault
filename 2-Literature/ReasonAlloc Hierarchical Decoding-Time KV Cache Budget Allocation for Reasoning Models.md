---
title: "ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models"
source: "https://arxiv.org/html/2606.11164v1"
author: "Wenhao Liu, Hao Shi, Yunhe Li, Weizhi Fei, Xiangyuan Wang, Mengzhe Ruan, Hanxu Hou, Peisong Wang, Linqi Song, Shuang Qiu"
published: "2026-06-09"
created: 2026-06-11
description: "Long chain-of-thought (CoT) trajectories in large language model (LLM) reasoning cause severe inference bottlenecks due to rapid key-value (KV) cache growth. Current decoding-time compression methods mitigate this issue via token eviction, but typically assume a uniform budget distribution across all layers and heads. In contrast, existing non-uniform budget allocation methods are predominantly designed for the stat…"
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
  - keyword/machine-learning
---

# ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.11164v1)
- published:: 2026-06-09
- updated:: 2026-06-09
- arxiv_id:: 2606.11164v1
- pdf:: https://arxiv.org/pdf/2606.11164v1
- categories:: cs.AI

## Abstract / Summary
Long chain-of-thought (CoT) trajectories in large language model (LLM) reasoning cause severe inference bottlenecks due to rapid key-value (KV) cache growth. Current decoding-time compression methods mitigate this issue via token eviction, but typically assume a uniform budget distribution across all layers and heads. In contrast, existing non-uniform budget allocation methods are predominantly designed for the static prompt prefill phase, and they do not capture the stepwise context demands of autoregressive reasoning. To bridge this gap, we propose ReasonAlloc, a training-free framework that recasts decoding-time KV compression as a hierarchical budget allocation problem. ReasonAlloc operates at two complementary levels: an offline layer-wise preallocation strategy captures an architecture-driven demand pattern which we call ``\textit{Reasoning Wave}'', while an online head-wise strategy reallocates resources during decoding to information-rich heads based on real-time utility. Evaluations on mathematical reasoning benchmarks (MATH-500, AIME~2024) using DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-Distill-Qwen-14B, and AceReason-14B show that ReasonAlloc outperforms uniform-budget R-KV, SnapKV, and Pyramid-RKV (a baseline enforcing a static, monotonically decreasing layer budget), with the largest gains at small budgets (128-512 tokens). ReasonAlloc is plug-and-play with existing token-eviction policies and introduces negligible inference-time overhead.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.11164v1)
- [PDF](https://arxiv.org/pdf/2606.11164v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark #keyword/reasoning #keyword/machine-learning
