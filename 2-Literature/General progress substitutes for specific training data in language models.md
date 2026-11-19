---
title: "General progress substitutes for specific training data in language models"
source: "https://arxiv.org/html/2611.24844v1"
author: "Mark Marosi, Peter Antal"
published: "2026-11-18"
created: 2026-11-20
description: "Language models acquire their capabilities from training data, and developers withhold data during training to keep models from learning capabilities that could be misused. How long this delays a capability, and how much data is needed to acquire it later, is unknown. Here we show that the general progress a model makes on the rest of its training data substitutes for the data that was withheld. We withheld the trai…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/machine-learning
---

# General progress substitutes for specific training data in language models

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.24844v1)
- published:: 2026-11-18
- updated:: 2026-11-18
- arxiv_id:: 2611.24844v1
- pdf:: https://arxiv.org/pdf/2611.24844v1
- categories:: cs.CL, cs.AI

## Abstract / Summary
Language models acquire their capabilities from training data, and developers withhold data during training to keep models from learning capabilities that could be misused. How long this delays a capability, and how much data is needed to acquire it later, is unknown. Here we show that the general progress a model makes on the rest of its training data substitutes for the data that was withheld. We withheld the training signal for individual skills in models of chess, Othello, molecular strings, bracket languages and web text. The delay of a withheld skill in larger models was predicted from smaller ones. A chess model never explicitly trained to respond to check ranked the legal responses almost as well as a model that was. When models were then trained on the withheld data, they acquired the skill with a small fraction of the data needed from initialization, and this fraction decreased as the models progressed. A control rule of equal difficulty was learned much more slowly. A programming language withheld from the training text of a 7-billion-parameter model was regained in the same way. Data filtering therefore delays a capability, and the data required to regain it decreases as models improve.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.24844v1)
- [PDF](https://arxiv.org/pdf/2611.24844v1)
- [The Surprising Effectiveness of Deleting Weights in LLM Post-Training](https://arxiv.org/abs/2611.10866) (2026, citations: 1)
- [Shaping capabilities with token-level data filtering](https://arxiv.org/abs/2601.21571) (2026, citations: 16)
- [Circuits, Features, and Heuristics in Molecular Transformers](https://arxiv.org/abs/2512.09757) (2025, citations: 4)
- [Deep Ignorance: Filtering Pretraining Data Builds Tamper-Resistant Safeguards into Open-Weight LLMs](https://arxiv.org/abs/2508.06601) (2025, citations: 69)
- [Distillation Robustifies Unlearning](https://arxiv.org/abs/2506.06278) (2025, citations: 21)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/machine-learning
