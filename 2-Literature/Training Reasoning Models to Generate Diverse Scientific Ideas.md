---
title: "Training Reasoning Models to Generate Diverse Scientific Ideas"
source: "https://arxiv.org/html/2610.22324v1"
author: "Manya Wadhwa, Pranav Narayanan Venkit, Hiroaki Hayashi, Yu Li, Tuhin Chakrabarty, Chien-Sheng Wu"
published: "2026-10-15"
created: 2026-10-19
description: "One of the first steps of a research pipeline is generating ideas. Large Language Models (LLMs) are increasingly used to automate this step, but most of this work optimizes the quality of individual ideas, while overlooking diversity. In our work, we study document-grounded ideation, focusing on increasing the diversity of LLM generated ideas and ensuring they are high quality. Given prior papers, a model must propo…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/benchmark
  - keyword/reasoning
  - keyword/agents
  - keyword/machine-learning
  - keyword/research-paper
---

# Training Reasoning Models to Generate Diverse Scientific Ideas

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.22324v1)
- published:: 2026-10-15
- updated:: 2026-10-15
- arxiv_id:: 2610.22324v1
- pdf:: https://arxiv.org/pdf/2610.22324v1
- categories:: cs.CL

## Abstract / Summary
One of the first steps of a research pipeline is generating ideas. Large Language Models (LLMs) are increasingly used to automate this step, but most of this work optimizes the quality of individual ideas, while overlooking diversity. In our work, we study document-grounded ideation, focusing on increasing the diversity of LLM generated ideas and ensuring they are high quality. Given prior papers, a model must propose a set of ideas that are each high-quality and clearly distinct from one another, while also being grounded in the input documents. To optimize for this, we propose training with a set-level reinforcement learning objective. In our setup, in a single generation, the model writes K structured idea cards grounded in the source papers, and the set is scored jointly, where each idea's quality is weighted by its distance from the ideas written before it. This teaches the model to steer each new idea away from its predecessors. We show that our trained 8B model achieves higher creative utility (a measure combining quality and diversity) than Claude Opus 4.8 and GPT-6 Astra on our contamination-free benchmark. In a pilot human study with four experts, our sets are judged as promising as Claude Opus 4.8's and contain marginally more unique ideas. When a coding agent runs proof-of-concept experiments on the ideas, our model's success@k is comparable to Claude Opus 4.8's, so we see that the added diversity does not cost any executability.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.22324v1)
- [PDF](https://arxiv.org/pdf/2610.22324v1)
- [Training AI Scientists to Replicate Research](https://arxiv.org/abs/2608.13331) (2026, citations: 8)
- [Can AI agents conduct open-ended AI research? Early evidence from two case studies](https://arxiv.org/abs/2607.27191) (2026, citations: 14)
- [Measuring the Gap Between Human and LLM Research Ideas](https://arxiv.org/abs/2607.01233) (2026, citations: 11)
- [Benchmarking AI Agents for Addressing Scientific Challenges Across Scales](https://arxiv.org/abs/2606.12736) (2026, citations: 14)
- [Vector Policy Optimization: Training for Diversity Improves Test-Time Search](https://arxiv.org/abs/2605.22817) (2026, citations: 9)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark #keyword/reasoning #keyword/agents #keyword/machine-learning #keyword/research-paper
