---
title: "Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics"
source: "https://arxiv.org/html/2606.11833v1"
author: "Sam Gijsen, Michał Łukomski, Marc-André Schulz, Kerstin Ritter"
published: "2026-06-10"
created: 2026-06-12
description: "Flow matching and diffusion models enable conditional generation across domains ranging from images to proteins, with recent extensions to out-of-distribution contexts. Yet generative models of neural time series have largely remained restricted to categorical conditioning, precluding compositional and zero-shot generalization. In this work, we propose a per-timestep conditioned diffusion transformer for generating…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/nlp
  - keyword/diffusion
  - keyword/retrieval
  - keyword/evaluation
  - keyword/machine-learning
---

# Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.11833v1)
- published:: 2026-06-10
- updated:: 2026-06-10
- arxiv_id:: 2606.11833v1
- pdf:: https://arxiv.org/pdf/2606.11833v1
- categories:: cs.LG, q-bio.NC

## Abstract / Summary
Flow matching and diffusion models enable conditional generation across domains ranging from images to proteins, with recent extensions to out-of-distribution contexts. Yet generative models of neural time series have largely remained restricted to categorical conditioning, precluding compositional and zero-shot generalization. In this work, we propose a per-timestep conditioned diffusion transformer for generating realistic fMRI brain dynamics during unseen cognitive tasks by injecting both compositional language and optional spatial priors in-context. Such zero-shot generation could enable counterfactual neuroscience by supporting in-silico design and evaluation of novel cognitive experiments before empirical validation. Leveraging this model, we evaluate across hundreds of held-out task conditions and characterize predictive performance in relation to the training manifold. From language alone, the model recovers region-specific recruitment across tasks and held-out spatial activation patterns. Spatial priors, when available, complement the text pathway by anchoring generation in regions of task space where language alone degrades, while retaining the compositional structure needed for counterfactual task specification. To our knowledge this is the first generative model of whole-cortex fMRI dynamics for unseen cognitive tasks, advancing counterfactual neuroscience and data-driven experimental design.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.11833v1)
- [PDF](https://arxiv.org/pdf/2606.11833v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/nlp #keyword/diffusion #keyword/retrieval #keyword/evaluation #keyword/machine-learning
