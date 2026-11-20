---
title: "AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher"
source: "https://arxiv.org/html/2611.26510v1"
author: "Guoxin Chen, Shuang Sun, Fanzhe Meng, Xinyu Tang, Ruihua Song, Wayne Xin Zhao"
published: "2026-11-19"
created: 2026-11-21
description: "Task success alone does not specify which behaviors post-training should reinforce. Even successful teacher trajectories can contain unsupported assumptions, unproductive repetition, or superficial verification. We propose Skill-FT (Skill-Guided Fine-Tuning), which uses natural-language skills to suppress undesirable habits and elicit underrepresented effective behaviors during teacher rollouts, then fine-tunes a ta…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/agents
  - keyword/machine-learning
---

# AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.26510v1)
- published:: 2026-11-19
- updated:: 2026-11-19
- arxiv_id:: 2611.26510v1
- pdf:: https://arxiv.org/pdf/2611.26510v1
- categories:: cs.CL

## Abstract / Summary
Task success alone does not specify which behaviors post-training should reinforce. Even successful teacher trajectories can contain unsupported assumptions, unproductive repetition, or superficial verification. We propose Skill-FT (Skill-Guided Fine-Tuning), which uses natural-language skills to suppress undesirable habits and elicit underrepresented effective behaviors during teacher rollouts, then fine-tunes a target model on the resulting trajectories. We introduce AutoMaster, an autonomous post-training system in which an LLM agent develops these interventions through trajectory analysis, skill design, data selection, and feedback from rollouts and target-model evaluation. Across Terminal, Search, and software engineering tasks with 4B and 9B target models, AutoMaster improves mean performance over Vanilla SFT on successful unguided teacher trajectories by 1.42-8.99 percentage points, with the teacher, task pool, training set size, and SFT recipe held fixed. Together with the ablations and trajectory analyses, these results suggest that behavioral shaping can make a fixed model a more effective teacher. We further find that retaining skill instructions during SFT yields higher mean performance than removing them across all six settings, despite their absence at evaluation and identical supervised outputs. These findings suggest that preserving skill context as part of a training demonstration can support better behavioral internalization.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.26510v1)
- [PDF](https://arxiv.org/pdf/2611.26510v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/agents #keyword/machine-learning
