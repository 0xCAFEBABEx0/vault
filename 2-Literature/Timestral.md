---
title: "Timestral"
source: "https://arxiv.org/html/2610.37585v1"
author: "Adrien Petralia, Alexandre Gavaudan, Artjom Joosen, Etienne Goffinet, Richard Kurle, Yassine El Ouahidi, Yassir Bendou, Abdelaziz Bounhar, Abhijeet Somani, Aditi Kabra, Adrian Valente, Adrien Sadé, Ahmed Djermani, Alan Jeffares, Albert Jiang, Alberto Bietti, Aleksandr Timashov, Alexandre Cahill, Alexandre Laval, Alexandre Sablayrolles, Alexandros Sanchez Va…"
published: "2026-10-27"
created: 2026-10-30
description: "We introduce Timestral, a family of four time series foundation models for probabilistic forecasting, with 5M, 28M, 123M, and 209M parameters. Timestral sets a new state of the art on GIFT-Eval, TIME, and fev-bench, where Timestral-209M and Timestral-123M take the top two places on every metric. We achieve this with three ingredients: Decoupled Horizon Forecasting (DHF), which separates prediction tokens from the ca…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/ai
  - keyword/nlp
  - keyword/evaluation
  - keyword/benchmark
  - keyword/machine-learning
---

# Timestral

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.37585v1)
- published:: 2026-10-27
- updated:: 2026-10-27
- arxiv_id:: 2610.37585v1
- pdf:: https://arxiv.org/pdf/2610.37585v1
- categories:: cs.AI

## Abstract / Summary
We introduce Timestral, a family of four time series foundation models for probabilistic forecasting, with 5M, 28M, 123M, and 209M parameters. Timestral sets a new state of the art on GIFT-Eval, TIME, and fev-bench, where Timestral-209M and Timestral-123M take the top two places on every metric. We achieve this with three ingredients: Decoupled Horizon Forecasting (DHF), which separates prediction tokens from the causally encoded context, so that longer horizons are trained without masking context and each observed value is both a forecast target and context for later forecasts; a covariate framework that natively supports known-future covariates within a causal architecture; and a two-stage pipeline that pretrains exclusively on a diverse, large-scale synthetic corpus before post-training on a mix of real and synthetic data with extended context. This report describes the model design and its benchmark results. Weights for all four models are available on Hugging Face and inference code on GitHub.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.37585v1)
- [PDF](https://arxiv.org/pdf/2610.37585v1)
- [Into the ORBIT for Time Series: Training Regimes for Foundation Models](https://arxiv.org/abs/2608.13262) (2026, citations: 6)
- [TS-ICL: A Flexible Time-Indexed Foundation Model for Time Series via In-Context Learning](https://arxiv.org/abs/2606.05878) (2026, citations: 5)
- [Toto 2.0: Time Series Forecasting Enters the Scaling Era](https://arxiv.org/abs/2605.20119) (2026, citations: 37)
- [It's TIME: Towards the Next Generation of Time Series Forecasting Benchmarks](https://arxiv.org/abs/2602.12147) (2026, citations: 34)
- [TempoPFN: Synthetic Pre-training of Linear RNNs for Zero-shot Time Series Forecasting](https://arxiv.org/abs/2510.25502) (2025, citations: 19)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/ai #keyword/nlp #keyword/evaluation #keyword/benchmark #keyword/machine-learning
