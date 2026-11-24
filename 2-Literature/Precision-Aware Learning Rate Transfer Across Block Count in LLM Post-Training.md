---
title: "Precision-Aware Learning Rate Transfer Across Block Count in LLM Post-Training"
source: "https://arxiv.org/html/2611.31166v1"
author: "Nan Chen, Soledad Villar, Soufiane Hayou"
published: "2026-11-23"
created: 2026-11-25
description: "The post-training of pretrained large language models, including supervised finetuning (SFT), direct preference optimization (DPO), and reinforcement learning with verifiable reward (RLVR), is very sensitive to the learning rate, and tuning it through grid search is costly in both computation and memory. In this work, we propose \textbf{TipSweep}, a method to transfer the learning rate across the number of trainable…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/machine-learning
---

# Precision-Aware Learning Rate Transfer Across Block Count in LLM Post-Training

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.31166v1)
- published:: 2026-11-23
- updated:: 2026-11-23
- arxiv_id:: 2611.31166v1
- pdf:: https://arxiv.org/pdf/2611.31166v1
- categories:: cs.LG, cs.CL

## Abstract / Summary
The post-training of pretrained large language models, including supervised finetuning (SFT), direct preference optimization (DPO), and reinforcement learning with verifiable reward (RLVR), is very sensitive to the learning rate, and tuning it through grid search is costly in both computation and memory. In this work, we propose \textbf{TipSweep}, a method to transfer the learning rate across the number of trainable transformer blocks. To do so efficiently, we search for the best learning rate by training only the last $k_0$ blocks (in our experiments, typically $k_0=1$), and provide scaling rules that predict the optimal learning rate when training any set of $k$ blocks, including when $k=L$ (the full transformer). Across experiments with models ranging from 1 to 7 billion parameters, we observe that the optimal learning rate follows precision-dependent scaling rules: the optimal rate scales approximately as $k^{-1}$ with float32 (FP32) master weights, but as $k^{-1/2}$ when updates are applied directly to bfloat16 (BF16) weights without a master copy. We explain both rules using an analytical model that accounts for update rounding, under assumptions supported by profiling experiments. Finally, we develop two prototypes of the learning rate search for a 6.7-billion-parameter model. The first fits the search on a single consumer GPU with 16 GiB of memory. The second speeds up the search on a high-end GPU by evaluating all candidate learning rates in a single pass over the data, so that a five-candidate search takes about half the GPU hours of one full-depth ($k=L$) run.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.31166v1)
- [PDF](https://arxiv.org/pdf/2611.31166v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/machine-learning
