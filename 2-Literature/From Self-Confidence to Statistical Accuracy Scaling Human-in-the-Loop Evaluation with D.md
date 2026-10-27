---
title: "From Self-Confidence to Statistical Accuracy: Scaling Human-in-the-Loop Evaluation with Direct and LLM-Assisted Auditing"
source: "https://arxiv.org/html/2610.35698v1"
author: "Harine Choi, Chenchen Kuai, Zihao Li, Jiwan Jiang, Yunlong Zhang, Zhiwen Fan, Zhengzhong Tu, Yang Zhou"
published: "2026-10-26"
created: 2026-10-28
description: "For large language models (LLMs) and multimodal large language models (MLLMs), model-reported self-confidence is often miscalibrated, yet it may still be useful for efficient evaluation. At the same time, LLM-as-a-judge offers a scalable alternative to direct human auditing, but its practical benefit depends on calibration quality and inference cost. This paper develops a unified statistical framework for both evalu…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/multimodal
  - keyword/evaluation
  - keyword/machine-learning
  - keyword/research-paper
---

# From Self-Confidence to Statistical Accuracy: Scaling Human-in-the-Loop Evaluation with Direct and LLM-Assisted Auditing

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.35698v1)
- published:: 2026-10-26
- updated:: 2026-10-26
- arxiv_id:: 2610.35698v1
- pdf:: https://arxiv.org/pdf/2610.35698v1
- categories:: cs.CL

## Abstract / Summary
For large language models (LLMs) and multimodal large language models (MLLMs), model-reported self-confidence is often miscalibrated, yet it may still be useful for efficient evaluation. At the same time, LLM-as-a-judge offers a scalable alternative to direct human auditing, but its practical benefit depends on calibration quality and inference cost. This paper develops a unified statistical framework for both evaluation routes under alternative sampling strategies. For direct auditing, confidence-stratified sampling is used to recover population accuracy from partially verified outputs without requiring calibrated confidence. Finite-sample uncertainty is characterized, and the analysis shows how highly uneven confidence strata affect audit efficiency and label allocation. For judge-assisted evaluation, the judge is modeled through sensitivity and false-positive rate, yielding an error-corrected estimator with calibration uncertainty. The two routes are then compared through human-label and total-cost efficiency boundaries. Experiments on MMLU-Pro and MMMU-Pro show that miscalibrated self-confidence can still support statistically valid stratified auditing. Under highly imbalanced confidence distributions, proportional allocation substantially reduces estimation error relative to equal-per-stratum allocation. For judge-assisted evaluation, only a small subset of target--verifier pairs satisfies the idealized human-label efficiency condition, and automated inference costs can further limit potential savings. These findings clarify the statistical and economic conditions under which confidence-guided auditing and automated verification are useful.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.35698v1)
- [PDF](https://arxiv.org/pdf/2610.35698v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/multimodal #keyword/evaluation #keyword/machine-learning #keyword/research-paper
