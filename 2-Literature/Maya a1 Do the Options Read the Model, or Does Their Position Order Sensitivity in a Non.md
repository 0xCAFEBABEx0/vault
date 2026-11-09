---
title: "Maya a1: Do the Options Read the Model, or Does Their Position? Order Sensitivity in a Non-Autoregressive Decision Model"
source: "https://arxiv.org/html/2611.09803v1"
author: "Mohammed Nayeem Khan, Logesh L"
published: "2026-11-06"
created: 2026-11-10
description: "Laya answers typed multiple-choice questions in one forward pass by scoring a hidden state at one [MASK] marker per option. We re-engineer the checkpoint (421M parameters; a 2-layer option head with no positional tensor; a documented but unused parallel layout) and test whether the answer depends on where an option is listed. Presenting 951 Qwen-verified questions under every cyclic rotation of their options (or six…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/machine-learning
---

# Maya a1: Do the Options Read the Model, or Does Their Position? Order Sensitivity in a Non-Autoregressive Decision Model

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.09803v1)
- published:: 2026-11-06
- updated:: 2026-11-06
- arxiv_id:: 2611.09803v1
- pdf:: https://arxiv.org/pdf/2611.09803v1
- categories:: cs.AI, cs.CL

## Abstract / Summary
Laya answers typed multiple-choice questions in one forward pass by scoring a hidden state at one [MASK] marker per option. We re-engineer the checkpoint (421M parameters; a 2-layer option head with no positional tensor; a documented but unused parallel layout) and test whether the answer depends on where an option is listed. Presenting 951 Qwen-verified questions under every cyclic rotation of their options (or six random permutations for 12 options), the released checkpoint changes its answer for 25.8% [22.9-28.7] of questions (19.7% on the 605 English-language items alone); accuracy with the gold option first versus last differs by 10.1 points, and the flips concentrate where the model's own confidence is low (54% versus 8% across confidence terciles). Fine-tuning with Laya's trainer on 2,818 teacher-verified rows with option shuffling cuts the flip rate to 7.2%; the identical rows without shuffling give 11.4%, so shuffling is responsible for 4.2 points of the improvement. A confidence-weighted vote over orderings gives 69.7% against 69.1% for a single base pass at 4.1x the compute. Labels are LLM-made and the test sets are teacher-filtered. We also fine-tune with the authors' parallel layout on the same rows: flip rate 0.5%.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.09803v1)
- [PDF](https://arxiv.org/pdf/2611.09803v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/machine-learning
