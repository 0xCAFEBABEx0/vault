---
title: "Molecular Déjà Vu: Digit-Level Retrieval of Published Values in Frontier Language Models"
source: "https://arxiv.org/html/2609.05381v1"
author: "Matthias Busch, Marius Tacke, Sviatlana V. Lamaka, Mikhail L. Zheludkevich, Christian J. Cyron, Roland C. Aydin, Christian Feiler"
published: "2026-09-04"
created: 2026-09-09
description: "Large language models (LLMs) are increasingly evaluated on molecular property benchmarks, but accuracy cannot distinguish a model that predicts a property from one that retrieves a published number. We audit 22 frontier models on 12 regression benchmarks for verbatim retrieval and find that it is widespread but relatively benchmark-specific: on five datasets more than $50\%$ of the LLMs show verbatim retrieval, whil…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/benchmark
  - keyword/reasoning
---

# Molecular Déjà Vu: Digit-Level Retrieval of Published Values in Frontier Language Models

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.05381v1)
- published:: 2026-09-04
- updated:: 2026-09-04
- arxiv_id:: 2609.05381v1
- pdf:: https://arxiv.org/pdf/2609.05381v1
- categories:: cs.AI

## Abstract / Summary
Large language models (LLMs) are increasingly evaluated on molecular property benchmarks, but accuracy cannot distinguish a model that predicts a property from one that retrieves a published number. We audit 22 frontier models on 12 regression benchmarks for verbatim retrieval and find that it is widespread but relatively benchmark-specific: on five datasets more than $50\%$ of the LLMs show verbatim retrieval, while on the remaining datasets it appears only in isolated cells. We run our experiments at two reasoning levels and find that reasoning changes retrieval. The same experiments, on the same molecules and with the same prompt, are flagged $89\%$ more often at the higher reasoning level than at the lowest one. Finally, we test a way to interrupt retrieval in our most contaminated cases, and find that the strongest models in some cases still recognise a combination of transformed SMILES strings and original labels. Furthermore, suppressing retrieval moves the prediction errors of the different models closer together in relative terms, while their differing use of verbatim retrieval spreads them apart. This indicates that the general predictive capability of an LLM is not determined solely by the amount of memorised values. This work provides an overview of the amount and depth of verbatim retrieval in molecular regression benchmarks using LLMs.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.05381v1)
- [PDF](https://arxiv.org/pdf/2609.05381v1)
- [Large language models predicting the corrosion inhibition efficiency of magnesium dissolution modulators](https://doi.org/10.1016/j.corsci.2025.113080) (2025, citations: 10)
- [A framework for evaluating the chemical knowledge and reasoning abilities of large language models against the expertise of chemists](https://www.nature.com/articles/s41557-025-01815-x.pdf) (2025, citations: 128)
- [2 OLMo 2 Furious](https://arxiv.org/abs/2501.00656) (2024, citations: 254)
- [A review of large language models and autonomous agents in chemistry](https://arxiv.org/abs/2407.01603) (2024, citations: 253)
- [DataComp-LM: In search of the next generation of training sets for language models](https://arxiv.org/abs/2406.11794) (2024, citations: 412)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/reasoning
