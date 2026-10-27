---
title: "Preserve to Expand: Source-Aware Adaptation and Model Merging for Multilingual LLM-Based ASR"
source: "https://arxiv.org/html/2610.35846v1"
author: "Yuchen Zhang, Haralambos Mouratidis, Ravi Shekhar"
published: "2026-10-26"
created: 2026-10-28
description: "Expanding multilingual ASR systems to new languages is challenging when adaptation must preserve previously supported languages without replaying source-language training data. We study this problem in connector-based Speech LLMs, where a trainable connector maps speech representations into a frozen large language model. We evaluate target-update construction and merging strategies for adapting the connector while p…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/machine-learning
---

# Preserve to Expand: Source-Aware Adaptation and Model Merging for Multilingual LLM-Based ASR

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.35846v1)
- published:: 2026-10-26
- updated:: 2026-10-26
- arxiv_id:: 2610.35846v1
- pdf:: https://arxiv.org/pdf/2610.35846v1
- categories:: cs.CL

## Abstract / Summary
Expanding multilingual ASR systems to new languages is challenging when adaptation must preserve previously supported languages without replaying source-language training data. We study this problem in connector-based Speech LLMs, where a trainable connector maps speech representations into a frozen large language model. We evaluate target-update construction and merging strategies for adapting the connector while preserving source-language performance. In single-target expansion, target-only fine-tuning and standard TIES merging learn new languages but cause severe source-language forgetting, while SSU-Wanda+TIES gives the best source-preserving trade-off. In multi-target expansion, update merging provides stable source retention, whereas recursive expansion can improve target adaptation under favorable orders but is highly order-sensitive. These results show that multilingual ASR expansion requires balancing target acquisition, source retention, and interactions among target-language updates.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.35846v1)
- [PDF](https://arxiv.org/pdf/2610.35846v1)
- [InterCorrect: Intersection-Aware Correction of Demographic Model Merging for Fair ASR](https://arxiv.org/abs/2610.08604) (2026)
- [MEUSLI: a Multilingual Projector for LLM-based ASR and Beyond](https://arxiv.org/abs/2607.22100) (2026, citations: 2)
- [Scalable Expansion of Multilingual Speech LLMs for ASR: A Continual Learning Approach](http://www.lrec-conf.org/proceedings/lrec2026/workshops/speakable/pdf/2026.speakable-1.7.pdf) (2026, citations: 1)
- [Exploring the potential and limitations of Model Merging for Multi-Domain Adaptation in ASR](https://arxiv.org/abs/2603.05354) (2026, citations: 1)
- [Improving Training Efficiency and Reducing Maintenance Costs via Language Specific Model Merging](https://arxiv.org/abs/2601.16127) (2026, citations: 2)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/machine-learning
