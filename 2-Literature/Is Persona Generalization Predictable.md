---
title: "Is Persona Generalization Predictable?"
source: "https://arxiv.org/html/2611.12864v1"
author: "Olina Mukherjee, Arnav Goel, Aditi Raghunathan, Jacob Mitchell Springer"
published: "2026-11-09"
created: 2026-11-11
description: "Persona generalization occurs when fine-tuning a language model in one domain induces behavioral changes in others -- for example, the broadly unsafe behavior observed in emergent misalignment. We discover a surprising 'on-the-line' phenomenon in persona generalization: in-domain and out-of-domain persona rates across various fine-tuning hyperparameters follow an approximately probit-linear relationship, and the spe…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/safety
  - keyword/machine-learning
---

# Is Persona Generalization Predictable?

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.12864v1)
- published:: 2026-11-09
- updated:: 2026-11-09
- arxiv_id:: 2611.12864v1
- pdf:: https://arxiv.org/pdf/2611.12864v1
- categories:: cs.CL, cs.LG

## Abstract / Summary
Persona generalization occurs when fine-tuning a language model in one domain induces behavioral changes in others -- for example, the broadly unsafe behavior observed in emergent misalignment. We discover a surprising "on-the-line" phenomenon in persona generalization: in-domain and out-of-domain persona rates across various fine-tuning hyperparameters follow an approximately probit-linear relationship, and the specific probit-linear relationship is surprisingly shared even across model families and model sizes, including Qwen and Llama. Training choices that leave the set of trainable parameters unchanged, such as learning rate, weight decay, and training duration, largely move models along the same line, reducing transfer mainly by weakening in-domain learning. Changing which layers are fine-tuned, however, can change the slope. For unsafe behavior, fine-tuning only later layers yields shallower slopes, retaining strong in-domain learning while reducing out-of-domain misalignment. This "on-the-line" phenomenon unifies unexpected, isolated observations of persona generalization within a quantitative framework for predicting and controlling behavioral transfer.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.12864v1)
- [PDF](https://arxiv.org/pdf/2611.12864v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/safety #keyword/machine-learning
