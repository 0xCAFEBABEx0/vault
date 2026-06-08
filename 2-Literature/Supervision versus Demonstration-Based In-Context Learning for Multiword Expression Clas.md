---
title: "Supervision versus Demonstration-Based In-Context Learning for Multiword Expression Classification"
source: "https://arxiv.org/html/2606.07479v1"
author: "Sercan Karakaş, Yusuf Şimşek"
published: "2026-06-05"
created: 2026-06-09
description: "Turkish idiomatic light verb constructions (LVCs) are challenging for multiword expression processing because they often share the same surface form as fully literal verb-object combinations while functioning as a single, partially idiomatic predicate. We frame Turkish LVC detection as a binary classification task (literal meaning vs. idiomatic meaning) and evaluate on a manually created controlled set (N=147) with…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
---

# Supervision versus Demonstration-Based In-Context Learning for Multiword Expression Classification

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.07479v1)
- published:: 2026-06-05
- updated:: 2026-06-05
- arxiv_id:: 2606.07479v1
- pdf:: https://arxiv.org/pdf/2606.07479v1
- categories:: cs.CL, cs.AI

## Abstract / Summary
Turkish idiomatic light verb constructions (LVCs) are challenging for multiword expression processing because they often share the same surface form as fully literal verb-object combinations while functioning as a single, partially idiomatic predicate. We frame Turkish LVC detection as a binary classification task (literal meaning vs. idiomatic meaning) and evaluate on a manually created controlled set (N=147) with matched negatives: out-of-domain random sentences and in-domain literal controls (NLVC), alongside LVC positives. We compare a supervised Turkish encoder baseline (BERTurk with a classifier head) to three instruction-tuned LLMs from different families under zero-shot, one-shot, and few-shot prompting, and analyze how demonstrations shift error profiles. In zero-shot, LLMs perform well on negatives but show very low LVC recall. One-shot prompting sharply improves LVC detection but can induce strong, model-specific biases, leading models to overpredict or underpredict LVCs. A richer few-shot prompt improves calibration and yields robust overall performance for GPT-OSS-20B and Qwen 2.5-14B. Overall, the results highlight substantial prompt sensitivity in Turkish metalinguistic classification: the supervised baseline remains competitive, while prompted LLMs can match or exceed it on LVCs with carefully constructed demonstrations.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.07479v1)
- [PDF](https://arxiv.org/pdf/2606.07479v1)
- [Benchmarking Source-Sensitive Reasoning in Turkish: Humans and LLMs under Evidential Trust Manipulation](https://arxiv.org/abs/2604.24665) (2026, citations: 2)
- [From Lemmas to Dependencies: What Signals Drive Light Verbs Classification?](https://arxiv.org/abs/2602.04127) (2026, citations: 3)
- [Layer-wise Minimal Pair Probing Reveals Contextual Grammatical-Conceptual Hierarchy in Speech Representations](https://arxiv.org/abs/2509.15655) (2025, citations: 6)
- [LLMs Don't Know Their Own Decision Boundaries: The Unreliability of Self-Generated Counterfactual Explanations](https://arxiv.org/abs/2509.09396) (2025, citations: 11)
- [Tokens with Meaning: A Hybrid Tokenization Approach for Turkish](https://arxiv.org/abs/2508.14292) (2025, citations: 3)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation
