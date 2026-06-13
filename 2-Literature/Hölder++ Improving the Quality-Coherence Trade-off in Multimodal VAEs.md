---
title: "Hölder++: Improving the Quality-Coherence Trade-off in Multimodal VAEs"
source: "https://arxiv.org/html/2606.13381v1"
author: "Huyen Vo, María Martínez-García, Isabel Valera"
published: "2026-06-11"
created: 2026-06-14
description: "Existing approaches for multimodal variational autoencoders (VAEs) face a trade-off between generative quality and coherence-i.e., they struggle to generate realistic and diverse samples that, at the same time, are semantically consistent across modalities. A recent work shows that using a simple approximation to Hölder pooling as an aggregation method improves coherence over the SOTA MMVAE+, despite assuming a sing…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/multimodal
  - keyword/machine-learning
---

# Hölder++: Improving the Quality-Coherence Trade-off in Multimodal VAEs

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.13381v1)
- published:: 2026-06-11
- updated:: 2026-06-11
- arxiv_id:: 2606.13381v1
- pdf:: https://arxiv.org/pdf/2606.13381v1
- categories:: cs.LG

## Abstract / Summary
Existing approaches for multimodal variational autoencoders (VAEs) face a trade-off between generative quality and coherence-i.e., they struggle to generate realistic and diverse samples that, at the same time, are semantically consistent across modalities. A recent work shows that using a simple approximation to Hölder pooling as an aggregation method improves coherence over the SOTA MMVAE+, despite assuming a single shared representation across all modalities. Yet, it slightly compromises sample diversity. Inspired by this insight, we propose Hölder++, a novel multimodal VAE that improves the generative quality-coherence trade-off through: (i) the first implementation of Hölder pooling without any approximation for multimodal VAEs; (ii) an extended architecture that models distinct shared and private (i.e., modality-specific) representations (Hölder+); and (iii) hierarchical inference that further enhances the disentanglement between the shared and private representations (Hölder++). Our experiments corroborate that Hölder++ consistently improves the generative quality-coherence trade-off, yields more structured latent spaces, and learns shared representations that are informative for downstream tasks.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.13381v1)
- [PDF](https://arxiv.org/pdf/2606.13381v1)
- [Hellinger Multimodal Variational Autoencoders](https://arxiv.org/abs/2601.06572) (2026, citations: 1)
- [Bridging the inference gap in multimodal variational autoencoders](https://www.semanticscholar.org/paper/683b1da01e30481a0377e6efae117872b62b14ce) (2025, citations: 1)
- [Disentanglement of Variations with Multimodal Generative Modeling](https://arxiv.org/abs/2509.23548) (2025, citations: 2)
- [Multi-Component VAE with Gaussian Markov Random Field](https://arxiv.org/abs/2507.12165) (2025, citations: 1)
- [Aggregation of Dependent Expert Distributions in Multimodal Variational Autoencoders](https://arxiv.org/abs/2505.01134) (2025, citations: 2)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/multimodal #keyword/machine-learning
