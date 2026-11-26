---
title: "Repairing the Trustworthiness of Distilled Language Models"
source: "https://arxiv.org/html/2611.34831v1"
author: "Kumar Shubham, Devendra Vyas, Vidushi Agarwal, Jayin Khanna, Prathosh AP"
published: "2026-11-25"
created: 2026-11-27
description: "Knowledge distillation enables the deployment of large language models through smaller student models, but the compression process can introduce regressions in trustworthiness even when downstream performance is preserved. Repairing such failures is challenging because the original distillation corpus is often unavailable, while direct preference optimization may alter capabilities inherited from the teacher. We pro…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/machine-learning
---

# Repairing the Trustworthiness of Distilled Language Models

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.34831v1)
- published:: 2026-11-25
- updated:: 2026-11-25
- arxiv_id:: 2611.34831v1
- pdf:: https://arxiv.org/pdf/2611.34831v1
- categories:: cs.CL, cs.AI

## Abstract / Summary
Knowledge distillation enables the deployment of large language models through smaller student models, but the compression process can introduce regressions in trustworthiness even when downstream performance is preserved. Repairing such failures is challenging because the original distillation corpus is often unavailable, while direct preference optimization may alter capabilities inherited from the teacher. We propose a targeted repair framework based on the proximal Bregman response function (PBRF) that addresses both limitations. We estimate the curvature required for PBRF using a surrogate proxy dataset, removing dependence on the original transfer corpus, and extend the framework to preference-based supervision through an odds-ratio objective. This enables the use of preferred and dispreferred response pairs while constraining changes to the distilled model. Our results show that the proposed approach improves targeted trustworthiness behaviors for both pre-training and post-training models while largely preserving downstream performance, providing a practical alternative to re-distillation or unconstrained preference optimization. Our experiment results show that across different distilled models, the trustworthy regression can be improved by up to 8% with less than 1% decrement in perplexity.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.34831v1)
- [PDF](https://arxiv.org/pdf/2611.34831v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/machine-learning
