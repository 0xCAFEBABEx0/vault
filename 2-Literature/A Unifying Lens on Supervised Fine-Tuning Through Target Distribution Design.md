---
title: "A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design"
source: "https://arxiv.org/html/2606.11189v1"
author: "Tong Xie, Yuanhao Ban, Yunqi Hong, Sohyun An, Yihang Chen, Cho-Jui Hsieh"
published: "2026-06-09"
created: 2026-06-11
description: "Supervised fine-tuning (SFT) typically maximizes the likelihood of every token in a demonstrated trajectory. However, an observed token can be non-unique, noisy, or misaligned with the model prior. Strictly fitting toward this one-hot target may be suboptimal, especially when the pretrained model encodes a rich knowledge prior. In this work, we reinterpret SFT as target distribution design: instead of studying only…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/evaluation
  - keyword/reasoning
  - keyword/machine-learning
---

# A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.11189v1)
- published:: 2026-06-09
- updated:: 2026-06-09
- arxiv_id:: 2606.11189v1
- pdf:: https://arxiv.org/pdf/2606.11189v1
- categories:: cs.LG, cs.AI, cs.CL

## Abstract / Summary
Supervised fine-tuning (SFT) typically maximizes the likelihood of every token in a demonstrated trajectory. However, an observed token can be non-unique, noisy, or misaligned with the model prior. Strictly fitting toward this one-hot target may be suboptimal, especially when the pretrained model encodes a rich knowledge prior. In this work, we reinterpret SFT as target distribution design: instead of studying only the loss objective, we analyze the token-level target that the loss drives the model to match. We introduce the Q-target framework, which decomposes SFT supervision into two explicit choices: (1) how strongly to rely on the observed token, and (2) how to allocate the remaining probability mass over alternatives. This perspective unifies many existing SFT variants as implicit choices of the target distribution Q. Building on this view, we propose Target-SFT which constructs the training objective directly from the desired target distribution. This method consistently outperforms across the ten reasoning dataset-model settings evaluated, showing the effectiveness of this target-based approach. Overall, our formulation reveals a more fundamental design principle for SFT training and opens a broader search space for SFT objectives.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.11189v1)
- [PDF](https://arxiv.org/pdf/2606.11189v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/evaluation #keyword/reasoning #keyword/machine-learning
