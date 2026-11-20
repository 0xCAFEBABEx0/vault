---
title: "GLiDE: A Fast, Calibrated Decision Model Distilled from Reasoning Teachers"
source: "https://arxiv.org/html/2611.26509v1"
author: "Sahibzada Allahyar, Julia White, Dhruv Atreja, George Hurn-Maloney, Urchade Zaratiana"
published: "2026-11-19"
created: 2026-11-21
description: "Decision models enable fast, confidence-aware decisions by scoring candidate answers in a single forward pass, without generating text or intermediate reasoning. Yet reasoning can substantially improve decision quality, raising the question of whether its benefits can be retained without the cost of generating it. We investigate this question with \textbf{GLiDE}, a family of decision models spanning 0.4B to 27B para…"
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
  - keyword/machine-learning
---

# GLiDE: A Fast, Calibrated Decision Model Distilled from Reasoning Teachers

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.26509v1)
- published:: 2026-11-19
- updated:: 2026-11-19
- arxiv_id:: 2611.26509v1
- pdf:: https://arxiv.org/pdf/2611.26509v1
- categories:: cs.AI, cs.CL

## Abstract / Summary
Decision models enable fast, confidence-aware decisions by scoring candidate answers in a single forward pass, without generating text or intermediate reasoning. Yet reasoning can substantially improve decision quality, raising the question of whether its benefits can be retained without the cost of generating it. We investigate this question with \textbf{GLiDE}, a family of decision models spanning 0.4B to 27B parameters. Building on Qwen hybrid language models, GLiDE enables bidirectional interactions between the context, question, and candidate answers by removing causal masking from full-attention layers. To transfer reasoning capabilities into single-pass inference, we combine soft-target distillation from multiple teachers, including a reasoning model, with progressive post-training on diverse decision tasks. We further explore parameter-free recurrent depth to increase inference-time computation without generating tokens. Across five model sizes, GLiDE lies on the performance--parameter Pareto frontier of the Hugging Face \DI{}, with each model outperforming evaluated alternatives of equal or smaller size. \dmtwo{} (27B) achieves a hidden-set score of 71.52, with an expected calibration error of 2.0\% and a median latency of 92.9\,ms on a single GPU. Further checkpoint averaging and parameter-free recurrent depth yield GLiDE~27B, which reaches 73.37 with an expected calibration error of 2.1\%.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.26509v1)
- [PDF](https://arxiv.org/pdf/2611.26509v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/reasoning #keyword/machine-learning
