---
title: "ActReview: Rebuttal-Guided Training Data and Rubric Rewards for Actionable Peer Review Generation"
source: "https://arxiv.org/html/2609.09076v1"
author: "Yiling Ma, Yilun Zhao, Sihong Wu, Ziyu Chen, Manasi Patwardhan, Arman Cohan"
published: "2026-09-08"
created: 2026-09-10
description: "As LLMs are increasingly used for pre-submission self-review, there is growing demand for feedback that not only identifies weaknesses but also guides authors toward concrete revisions. We study this as Actionable Peer-review Generation and decompose it into two subtasks: diagnostic claim generation and revision suggestion generation. We introduce ActReview, a rebuttal-guided post-training framework that connects pa…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/evaluation
  - keyword/benchmark
  - keyword/machine-learning
  - keyword/research-paper
---

# ActReview: Rebuttal-Guided Training Data and Rubric Rewards for Actionable Peer Review Generation

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.09076v1)
- published:: 2026-09-08
- updated:: 2026-09-08
- arxiv_id:: 2609.09076v1
- pdf:: https://arxiv.org/pdf/2609.09076v1
- categories:: cs.CL

## Abstract / Summary
As LLMs are increasingly used for pre-submission self-review, there is growing demand for feedback that not only identifies weaknesses but also guides authors toward concrete revisions. We study this as Actionable Peer-review Generation and decompose it into two subtasks: diagnostic claim generation and revision suggestion generation. We introduce ActReview, a rebuttal-guided post-training framework that connects paper-specific diagnoses to concrete, grounded revision plans. Our central insight is that author rebuttals reveal plausible actions for addressing reviewer concerns and can therefore provide latent supervision for revision-oriented feedback. From real review-rebuttal threads on OpenReview, we construct ActReview-40K by aligning reviewer weaknesses with author responses and grounding the resulting feedback in localized paper evidence. We post-train Qwen3-8B-Base with multi-task supervised fine-tuning followed by GRPO using candidate-aware, weakness-specific rubric rewards. We also introduce ActReview-Bench, a human-curated benchmark of 1,000 instances for evaluating diagnostic quality and revision usefulness. Experiments show that ActReview outperforms prior specialized review-generation models on actionability and grounding while remaining competitive with strong prompt-based LLMs. Human evaluation confirms improved revision usefulness while revealing a remaining gap in technical accuracy, and additional analyses support generalization to held-out papers and robustness across independent judges.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.09076v1)
- [PDF](https://arxiv.org/pdf/2609.09076v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/evaluation #keyword/benchmark #keyword/machine-learning #keyword/research-paper
