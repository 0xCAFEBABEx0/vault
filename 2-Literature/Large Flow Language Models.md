---
title: "Large Flow Language Models"
source: "https://arxiv.org/html/2610.28559v1"
author: "Arnav Chavan, Chanhyuk Lee, Udbhav Bamba, Jaehoon Yoo, Seunghoon Hong, Aditi Raghunathan, Jinwoo Kim"
published: "2026-10-20"
created: 2026-10-22
description: "Continuous flow language models offer a path to parallel generation with tools for control and acceleration unavailable to discrete diffusion, yet effective techniques for building them at the billion-parameter scale remain less established. We present Lafa (Large flow language model), a fast, high-performing flow language model scaled to 8B parameters in a data-efficient manner. Lafa is a blockwise flow model with…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/nlp
  - keyword/diffusion
  - keyword/retrieval
  - keyword/evaluation
  - keyword/reasoning
  - keyword/agents
---

# Large Flow Language Models

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.28559v1)
- published:: 2026-10-20
- updated:: 2026-10-20
- arxiv_id:: 2610.28559v1
- pdf:: https://arxiv.org/pdf/2610.28559v1
- categories:: cs.CL, cs.AI

## Abstract / Summary
Continuous flow language models offer a path to parallel generation with tools for control and acceleration unavailable to discrete diffusion, yet effective techniques for building them at the billion-parameter scale remain less established. We present Lafa (Large flow language model), a fast, high-performing flow language model scaled to 8B parameters in a data-efficient manner. Lafa is a blockwise flow model with causal attention on the prefix and bidirectional, asynchronous flow within each block. This design enables efficient training by adapting pretrained autoregressive (AR) models and fast inference via prefix caching and blockwise parallel decoding. We train Lafa at 0.5B, 7B, and 8B scales with fewer than 30B tokens, more efficient than previous diffusion models, and evaluate it on instruction following, reasoning, and coding, where the learned flow matches or surpasses the quality of AR and can be distilled into flow maps for one- and few-step generation. Notably, flow training preserves or even improves pretrained AR capabilities via a multi-token prediction effect, which we leverage in a self-speculative decoding scheme that verifies flow-based drafts autoregressively within a single model. This yields 2.54x the throughput of an AR model at comparable quality, outperforming multi-token prediction and discrete diffusion methods. Our findings show that continuous flows can serve as a scalable foundation for language modeling.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.28559v1)
- [PDF](https://arxiv.org/pdf/2610.28559v1)
- [DiffusionGemma Technical Report](https://arxiv.org/abs/2608.00146) (2026, citations: 11)
- [Self-conditioned Flow Map Language Models via Fixed-point Flows](https://arxiv.org/abs/2607.00714) (2026, citations: 16)
- [Posterior Refinement: Fast Language Generation via Any-Order Flow Maps](https://arxiv.org/abs/2606.24773) (2026, citations: 12)
- [Learning When to Denoise: Optimizing Asynchronous Schedules for Latent Diffusion](https://arxiv.org/abs/2606.19662) (2026, citations: 2)
- [Hacking Generative Perplexity: Why Unconditional Text Evaluation Needs Distributional Metrics](https://arxiv.org/abs/2606.08417) (2026, citations: 10)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp #keyword/diffusion #keyword/retrieval #keyword/evaluation #keyword/reasoning #keyword/agents
