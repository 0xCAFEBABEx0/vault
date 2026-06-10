---
title: "Multi-Faceted Interactivity Alignment in Full-Duplex Speech Models"
source: "https://arxiv.org/html/2606.11167v1"
author: "Atsumoto Ohashi, Neil Zeghidour, Alexandre Défossez, Eugene Kharitonov"
published: "2026-06-09"
created: 2026-06-11
description: "Full-duplex spoken dialogue models can listen and speak simultaneously, making them a promising architecture for natural conversation. However, current models trained with supervised learning do not directly optimize interaction-level behaviors."
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/multimodal
  - keyword/evaluation
  - keyword/safety
  - keyword/machine-learning
---

# Multi-Faceted Interactivity Alignment in Full-Duplex Speech Models

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.11167v1)
- published:: 2026-06-09
- updated:: 2026-06-09
- arxiv_id:: 2606.11167v1
- pdf:: https://arxiv.org/pdf/2606.11167v1
- categories:: cs.CL, eess.AS

## Abstract / Summary
Full-duplex spoken dialogue models can listen and speak simultaneously, making them a promising architecture for natural conversation. However, current models are trained solely with supervised learning through token-level likelihood maximization, which does not directly optimize interaction-level behaviors, causing interactivity issues such as excessive silence and ill-timed turn-taking. We propose a post-training alignment method that comprehensively improves the interactivity of full-duplex spoken dialogue models through RL. We address the four canonical axes of interactivity: pause handling, turn-taking, backchanneling, and user interruption. For each axis, we extract short audio segments from human conversation corpora and optimize the model with axis-specific reward functions. An extra LLM-based reward for response quality prevents semantic degradation. We apply our method to two open-source models, Moshi and PersonaPlex, demonstrating consistent improvements in interactivity.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.11167v1)
- [PDF](https://arxiv.org/pdf/2606.11167v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/multimodal #keyword/evaluation #keyword/safety #keyword/machine-learning
