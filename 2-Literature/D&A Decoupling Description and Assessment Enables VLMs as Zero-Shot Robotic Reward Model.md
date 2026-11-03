---
title: "D&A: Decoupling Description and Assessment Enables VLMs as Zero-Shot Robotic Reward Models"
source: "https://arxiv.org/html/2611.03622v1"
author: "Marius Memmel, Shawn Yin, Urvi Rutia, Angad Wadhwa, Eldon Li, Gavin Angeloff, Ankit Goyal, Jesse Zhang, Dieter Fox, Fabio Ramos, Anqi Li, Abhishek Gupta"
published: "2026-11-02"
created: 2026-11-04
description: "Vision-Language Models (VLMs) hold promise for zero-shot video task-progress estimation in robot learning, yet existing frameworks frequently suffer from confirmation bias, hallucinating progress in failed executions due to implicit success assumptions or relative temporal ranking designs. Naive prompting of frontier models collapses into a binary success detector that fails to capture nuanced, non-linear progress a…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/multimodal
  - keyword/evaluation
  - keyword/benchmark
  - keyword/machine-learning
---

# D&A: Decoupling Description and Assessment Enables VLMs as Zero-Shot Robotic Reward Models

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.03622v1)
- published:: 2026-11-02
- updated:: 2026-11-02
- arxiv_id:: 2611.03622v1
- pdf:: https://arxiv.org/pdf/2611.03622v1
- categories:: cs.RO, cs.AI, cs.CL, cs.LG, eess.SY

## Abstract / Summary
Vision-Language Models (VLMs) hold promise for zero-shot video task-progress estimation in robot learning, yet existing frameworks frequently suffer from confirmation bias, hallucinating progress in failed executions due to implicit success assumptions or relative temporal ranking designs. Naive prompting of frontier models collapses into a binary success detector that fails to capture nuanced, non-linear progress and failures. While post-training approaches can mitigate this through explicit training, they demand expensive real-world robotics data and require computationally intensive post-training for every individual base model. To resolve these limitations, we introduce D&A (Describe & Assess): our approach decouples progress estimation into an objective, task-grounded textual description of scene dynamics followed by an assessment phase using explicit rubrics. By compelling the VLM to synthesize an explicit, text-based definition of absolute success before scoring, the framework anchors evaluations to an external, global criterion rather than the video's internal timeline. Empirical results demonstrate that our method calibrates zero-shot estimates and mitigates confirmation bias, providing fine-grained, partial progress metrics that accurately penalize failed executions while correctly interpolating successful runs. Being purely prompt-based, D&A generalizes across tasks, embodiments, and benchmarks---matching or surpassing post-trained reward models---and its reward estimates enable efficient downstream reinforcement learning.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.03622v1)
- [PDF](https://arxiv.org/pdf/2611.03622v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/multimodal #keyword/evaluation #keyword/benchmark #keyword/machine-learning
