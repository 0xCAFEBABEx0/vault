---
title: "HiSA: Sparsifying the Hidden Dimension of RoPE Attention in LLMs"
source: "https://arxiv.org/html/2611.26363v1"
author: "Ambroise Borbely, Mathieu Salzmann, Olivier Verscheure"
published: "2026-11-19"
created: 2026-11-21
description: "Attention in large language models (LLMs) scores every query against every key with a full dot product. We investigate whether this dot product must be computed completely for attention to be effective. We propose Hidden Sparse Attention (HiSA), which keeps the query and key projections intact but only computes a partial dot product, following a static, parameter-free rule set by the token positions: attention becom…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/nlp
  - keyword/machine-learning
---

# HiSA: Sparsifying the Hidden Dimension of RoPE Attention in LLMs

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.26363v1)
- published:: 2026-11-19
- updated:: 2026-11-19
- arxiv_id:: 2611.26363v1
- pdf:: https://arxiv.org/pdf/2611.26363v1
- categories:: cs.LG, cs.CL

## Abstract / Summary
Attention in large language models (LLMs) scores every query against every key with a full dot product. We investigate whether this dot product must be computed completely for attention to be effective. We propose Hidden Sparse Attention (HiSA), which keeps the query and key projections intact but only computes a partial dot product, following a static, parameter-free rule set by the token positions: attention becomes sparse in the hidden (feature) dimension, an axis much less explored than token sparsity, rather than over tokens as in almost all sparse attention methods. Based on the structure of rotary position embeddings (RoPE), we decompose keys and queries into parts which can be omitted when computing attention. By training LLMs from scratch with HiSA, we find that this partial dot product does not hurt but improves performance compared with the complete product while computing only about a third of the query-key products. During inference HiSA improves decoding speed and shrinks memory footprint. We also extend HiSA to FlashAttention-3 kernels for training and inference. Finally, we motivate our approach by showing that dense attention learns to suppress the attention score parts that HiSA drops. Code is available at https://github.com/ambroise-b/hisa.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.26363v1)
- [PDF](https://arxiv.org/pdf/2611.26363v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp #keyword/machine-learning
