---
title: "Task Context Shapes Component Roles in Language Models"
source: "https://arxiv.org/html/2610.13895v1"
author: "Sovesh Mohapatra, Dani S Bassett"
published: "2026-10-09"
created: 2026-10-14
description: "Large language models reuse the same attention heads across tasks, but identifying these shared heads does not explain what they do differently in each task. A natural source of inspiration is task-dependent interactions among shared brain regions, which motivate a network view of language-model computation. Here, we compare fixed model components across tasks using identical graph facts, statements specifying which…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
---

# Task Context Shapes Component Roles in Language Models

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.13895v1)
- published:: 2026-10-09
- updated:: 2026-10-09
- arxiv_id:: 2610.13895v1
- pdf:: https://arxiv.org/pdf/2610.13895v1
- categories:: cs.CL, cs.AI

## Abstract / Summary
Large language models reuse the same attention heads across tasks, but identifying these shared heads does not explain what they do differently in each task. A natural source of inspiration is task-dependent interactions among shared brain regions, which motivate a network view of language-model computation. Here, we compare fixed model components across tasks using identical graph facts, statements specifying which directed connections are present. We measure how interventions affect attention heads and the activation state in later layers (influence), as well as the answer (importance). Task changes redistribute the influence in five open-weight models spanning four families and 1.5-14 billion parameters. In Gemma-2-9B and Qwen3-14B, an activation edit changes an early internal activation vector and switches which fact the model reads while the written instruction stays fixed. The same heads then respond to different graph facts and influence later components differently. For each prompt, we construct two linear response maps, one before the edit and one after it. Each map predicts a later head's response from a measured change in an earlier head. For a separate factual intervention, the map for the corresponding condition reduces mean squared prediction error by 53.6% in Gemma and 5.0% in Qwen compared with the average of the two maps. These findings show that task context changes both which graph facts the shared components respond to and how their outputs affect later computation. A network account may help explain how models use shared parameters to perform different computations. Measurements of task-dependent influence could also guide interventions intended to alter one behavior while preserving others.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.13895v1)
- [PDF](https://arxiv.org/pdf/2610.13895v1)
- [Modular Cognitive Architecture Emerges in Large Language Models](https://arxiv.org/abs/2608.13567) (2026, citations: 3)
- [Localizing Task Recognition and Task Learning in In-Context Learning via Attention Head Analysis](https://arxiv.org/abs/2509.24164) (2025, citations: 3)
- [Mechanism of Task-oriented Information Removal in In-context Learning](https://arxiv.org/abs/2509.21012) (2025, citations: 4)
- [Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance](https://arxiv.org/abs/2507.22448) (2025, citations: 62)
- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) (2025, citations: 9017)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp #keyword/retrieval
