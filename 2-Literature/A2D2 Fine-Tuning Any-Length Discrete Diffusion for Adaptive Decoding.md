---
title: "A2D2: Fine-Tuning Any-Length Discrete Diffusion for Adaptive Decoding"
source: "https://arxiv.org/html/2606.13565v1"
author: "Sophia Tang, Yuchen Zhu, Molei Tao, Pranam Chatterjee"
published: "2026-06-11"
created: 2026-06-13
description: "Discrete diffusion models offer a simple and stable likelihood-based framework for sequence generation, recently extended to any-length settings via token insertion. Principled reward-guided fine-tuning for any-length discrete diffusion, however, remains largely unexplored. We introduce Fine-Tuning Any-Length Discrete Diffusion for Adaptive Decoding (A2D2), a unified framework for reward-guided fine-tuning of any-le…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/diffusion
  - keyword/machine-learning
---

# A2D2: Fine-Tuning Any-Length Discrete Diffusion for Adaptive Decoding

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.13565v1)
- published:: 2026-06-11
- updated:: 2026-06-11
- arxiv_id:: 2606.13565v1
- pdf:: https://arxiv.org/pdf/2606.13565v1
- categories:: cs.LG

## Abstract / Summary
Discrete diffusion models offer a simple and stable likelihood-based framework for sequence generation, recently extended to any-length settings via token insertion. Principled reward-guided fine-tuning for any-length discrete diffusion, however, remains largely unexplored. We introduce Fine-Tuning Any-Length Discrete Diffusion for Adaptive Decoding (A2D2), a unified framework for reward-guided fine-tuning of any-length discrete diffusion models via joint optimization of the insertion and unmasking policies together with a quality-based inference schedule. We derive the Radon-Nikodym derivative for the joint insertion-unmasking path measures, enabling theoretically guaranteed convergence to the intractable reward-tilted sequence distribution without requiring target samples. Building on this, we establish unmasking and insertion quality as tractable approaches for minimizing decoding error and introduce the Adaptive Joint Decoding (AJD) loss, which provably yields the optimal path measure that generates the reward-tilted distribution. Empirically, A2D2 improves reward optimization while enhancing generation flexibility and accuracy over prior fixed-length fine-tuning and inference-time guidance methods.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.13565v1)
- [PDF](https://arxiv.org/pdf/2606.13565v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/diffusion #keyword/machine-learning
