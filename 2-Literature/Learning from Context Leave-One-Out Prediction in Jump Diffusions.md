---
title: "Learning from Context: Leave-One-Out Prediction in Jump Diffusions"
source: "https://arxiv.org/html/2611.26359v1"
author: "Christian Wald"
published: "2026-11-19"
created: 2026-11-23
description: "Continuous diffusion models generate discrete data through stochastic dynamics in an embedding space. We consider jump diffusions that additionally reset coordinates to embeddings of categorical values. A coordinate's own corrupted state can make prediction easy, potentially reducing the pressure to learn dependencies between coordinates. We study leave-one-out (LOO) prediction, in which each coordinate is predicted…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/nlp
  - keyword/diffusion
  - keyword/evaluation
---

# Learning from Context: Leave-One-Out Prediction in Jump Diffusions

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.26359v1)
- published:: 2026-11-19
- updated:: 2026-11-19
- arxiv_id:: 2611.26359v1
- pdf:: https://arxiv.org/pdf/2611.26359v1
- categories:: cs.LG

## Abstract / Summary
Continuous diffusion models generate discrete data through stochastic dynamics in an embedding space. We consider jump diffusions that additionally reset coordinates to embeddings of categorical values. A coordinate's own corrupted state can make prediction easy, potentially reducing the pressure to learn dependencies between coordinates. We study leave-one-out (LOO) prediction, in which each coordinate is predicted from the corrupted states of the other coordinates. We show that, under stated assumptions, jump diffusions with complete coordinate resets and state-independent clocks preserve the prescribed marginals when reset destinations use exact LOO probabilities and the drift uses the full endpoint posterior. We further show that this drift can be constructed from LOO probabilities by analytic likelihood completion without additional network evaluations. We evaluate unrestricted, LOO, and completed predictions on Text8 and LM1B text generation and ZINC250k molecular graph generation. LOO-based variants improve key generation metrics over matched unrestricted controls on all three datasets. Controlled interventions assess reliance on local inputs and context, and we analyze the effect of analytic likelihood completion.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.26359v1)
- [PDF](https://arxiv.org/pdf/2611.26359v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/nlp #keyword/diffusion #keyword/evaluation
