---
title: "PORT: Preference Optimization via Robust Token-Level Reweighting"
source: "https://arxiv.org/html/2611.12763v1"
author: "Ding Zhu, Xiukun Wei, Tian Xie, Zhihui Zhu, Xueru Zhang, Mohammad Mahdi Khalili"
published: "2026-11-09"
created: 2026-11-11
description: "Preference optimization has become a central approach for aligning large language models with human values, but its effectiveness depends heavily on the quality of preference annotations. In practice, preference data is often noisy due to annotation errors and ambiguity. Existing robust preference optimization methods primarily operate at the sequence level, implicitly treating entire responses as uniformly correct…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/reasoning
  - keyword/safety
---

# PORT: Preference Optimization via Robust Token-Level Reweighting

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.12763v1)
- published:: 2026-11-09
- updated:: 2026-11-09
- arxiv_id:: 2611.12763v1
- pdf:: https://arxiv.org/pdf/2611.12763v1
- categories:: cs.CL, cs.AI

## Abstract / Summary
Preference optimization has become a central approach for aligning large language models with human values, but its effectiveness depends heavily on the quality of preference annotations. In practice, preference data is often noisy due to annotation errors and ambiguity. Existing robust preference optimization methods primarily operate at the sequence level, implicitly treating entire responses as uniformly correct or incorrect. However, rejected responses may still contain informative reasoning steps, while preferred responses can include subtle errors. In this work, we propose \textbf{P}reference \textbf{O}ptimization via \textbf{R}obust \textbf{T}oken-level reweighting \textbf{(PORT)}, a fine-grained framework for robust alignment under noisy preferences. PORT performs token-level reweighting using the empirical cumulative distribution function (CDF) of token log-probabilities, yielding an efficient forward-pass-only proxy to gradient-norm penalization that selectively suppresses corrupted tokens without additional backward-pass computation. We provide theoretical analysis showing that PORT reduces the gradient bias from noisy preference labels by minimizing an upper bound on the bias term. Extensive experiments across diverse noise settings demonstrate that PORT consistently improves robustness and outperforms existing sequence-level baselines. The code is available at https://github.com/osu-srml/PORT

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.12763v1)
- [PDF](https://arxiv.org/pdf/2611.12763v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/reasoning #keyword/safety
