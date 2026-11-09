---
title: "ROSE: Risk-Aware Orthogonal Subspace Navigation for Lifelong Knowledge Editing in Multimodal Large Language Models"
source: "https://arxiv.org/html/2611.09770v1"
author: "Lingyun Song, Ziyao Chen, Kang Pan, Xiaolin Han, Yifei Zhang, Xiaoqi Wang, Yudai Pan, Xuequn Shang"
published: "2026-11-06"
created: 2026-11-10
description: "Multimodal Large Language Models (MLLMs) require continuous factual updates to stay current, yet lifelong knowledge editing remains a daunting challenge. The primary obstacle is the severe Locality Erosion and Catastrophic Forgetting, where sequential edits inevitably interfere with pre-trained capabilities and prior updates. In this paper, we propose \textbf{ROSE}, a \textbf{R}isk-aware \textbf{O}rthogonal \textbf{…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/multimodal
  - keyword/evaluation
  - keyword/benchmark
  - keyword/machine-learning
  - keyword/research-paper
---

# ROSE: Risk-Aware Orthogonal Subspace Navigation for Lifelong Knowledge Editing in Multimodal Large Language Models

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.09770v1)
- published:: 2026-11-06
- updated:: 2026-11-06
- arxiv_id:: 2611.09770v1
- pdf:: https://arxiv.org/pdf/2611.09770v1
- categories:: cs.CL, cs.AI, cs.CV

## Abstract / Summary
Multimodal Large Language Models (MLLMs) require continuous factual updates to stay current, yet lifelong knowledge editing remains a daunting challenge. The primary obstacle is the severe Locality Erosion and Catastrophic Forgetting, where sequential edits inevitably interfere with pre-trained capabilities and prior updates. In this paper, we propose \textbf{ROSE}, a \textbf{R}isk-aware \textbf{O}rthogonal \textbf{S}ubspace navigation framework for lifelong knowledge \textbf{E}diting. ROSE addresses forgetting by aiming to restrict parameter updates to the orthogonal complement of previously edited subspaces. Crucially, it introduces a risk-guided mechanism that utilizes a dynamically computed risk mask to safeguard specific factual parameter subspaces essential for model stability. During inference, ROSE employs a multi-granularity knowledge integration strategy, featuring prototype-anchored semantic gating and perturbation-driven subspace fusion to precisely activate edited knowledge for relevant queries while limiting interference on unrelated inputs. Comprehensive experiments on two prominent multimodal benchmarks show that ROSE is competitive with state-of-the-art approaches across five key metrics, while maintaining outstanding stability over $1,000$ sequential updates. Our code is available at https://github.com/sunlitsong/ROSE.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.09770v1)
- [PDF](https://arxiv.org/pdf/2611.09770v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/multimodal #keyword/evaluation #keyword/benchmark #keyword/machine-learning #keyword/research-paper
