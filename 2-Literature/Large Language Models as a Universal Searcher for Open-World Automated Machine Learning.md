---
title: "Large Language Models as a Universal Searcher for Open-World Automated Machine Learning"
source: "https://arxiv.org/html/2611.12791v1"
author: "Yuxuan Hu, Jihao Liu, Weikang Shi, Xijie Huang, Linda Wei, Mingjie Zhan, Aojun Zhou, Rui Liu, Hongsheng Li"
published: "2026-11-09"
created: 2026-11-11
description: "Developing effective machine learning models requires complex manual tuning, while current Automated Machine Learning (AutoML) frameworks remain domain-specific and isolate model architecture, training hyperparameter, and data ratio optimization. Here, we bridge this gap by proposing a universal, large language model (LLM)-based AutoML framework that jointly optimizes these configurations for the first time without…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/nlp
  - keyword/diffusion
  - keyword/retrieval
  - keyword/evaluation
  - keyword/benchmark
  - keyword/reasoning
---

# Large Language Models as a Universal Searcher for Open-World Automated Machine Learning

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.12791v1)
- published:: 2026-11-09
- updated:: 2026-11-09
- arxiv_id:: 2611.12791v1
- pdf:: https://arxiv.org/pdf/2611.12791v1
- categories:: cs.CL

## Abstract / Summary
Developing effective machine learning models requires complex manual tuning, while current Automated Machine Learning (AutoML) frameworks remain domain-specific and isolate model architecture, training hyperparameter, and data ratio optimization. Here, we bridge this gap by proposing a universal, large language model (LLM)-based AutoML framework that jointly optimizes these configurations for the first time without the need for task-specific fine-tuning. We propose NCode, a unified numerical encoding scheme that translates diverse AutoML design choices into universal discrete sequences and effectively reframes the optimization process as a unified ranking task. Trained solely on optimization trajectories derived from a limited, single-domain vision task, the proposed LLM-based searcher demonstrates impressive cross-task, cross-modality and joint search-space optimization generalizability, achieving state-of-the-art performance across image classification, image segmentation, speaker verification and text-to-image benchmarks. Crucially, it exhibits superior scalability in the large-scale training and joint optimization of a billion-parameter Diffusion Transformer, requiring 896 GPU-days and attaining a state-of-the-art GenEval score of 0.91. By leveraging reinforcement learning to instill Chain-of-Thought reasoning, we provide a systematic way to interpret the LLM-based searcher's internal decision-making mechanisms, revealing its optimization strategy shifted from the early-stage diversity-driven exploration to the late-stage anchor exploitation. Our proposed framework provides a scalable, generalizable, and interpretable pathway toward general-purpose open-world machine learning optimization.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.12791v1)
- [PDF](https://arxiv.org/pdf/2611.12791v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp #keyword/diffusion #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/reasoning
