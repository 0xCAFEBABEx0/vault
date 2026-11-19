---
title: "Jailbreak Detection on Large Language Models via Contrastive Prototype Structures"
source: "https://arxiv.org/html/2611.24936v1"
author: "Yan Qiu, Yuanyuan Li"
published: "2026-11-18"
created: 2026-11-20
description: "Jailbreak attempts and harmful prompts remain a challenge for the safe deployment of large language models. We study whether contrastively learned representations can support safety detection without training an additional downstream classifier. We propose Jailbreak Detection with Prototype Inference (JDPI), which uses binary safety labels to construct harmful and benign prototypes and makes predictions from relativ…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/benchmark
  - keyword/safety
  - keyword/machine-learning
---

# Jailbreak Detection on Large Language Models via Contrastive Prototype Structures

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.24936v1)
- published:: 2026-11-18
- updated:: 2026-11-18
- arxiv_id:: 2611.24936v1
- pdf:: https://arxiv.org/pdf/2611.24936v1
- categories:: cs.CL

## Abstract / Summary
Jailbreak attempts and harmful prompts remain a challenge for the safe deployment of large language models. We study whether contrastively learned representations can support safety detection without training an additional downstream classifier. We propose Jailbreak Detection with Prototype Inference (JDPI), which uses binary safety labels to construct harmful and benign prototypes and makes predictions from relative prototype distances. JDPI uses only binary safety labels for encoder adaptation, prototype construction, and validation. In our setup, it uses fewer labeled examples than the classifier baseline (Method A) by avoiding the separate split used to train the downstream classifier. Across four benchmarks covering different input formats, contrastive fine-tuning improves JDPI's detection accuracy by 9.1-18.0 percentage points. Using the same encoder, JDPI achieves slightly higher ROC-AUC on one benchmark and stays within 0.017 of the baseline across all four. With dataset-specific adaptation, JDPI exceeds the released Llama Guard 3-8B baseline by 0.173-0.310 in ROC-AUC across the four benchmarks. In multi-turn replay on TomGibbs, JDPI uses accumulated user history as the conversation unfolds, achieving higher conversation-level accuracy than when it uses the current turn alone. Across 12 directed transfers, JDPI outperforms the classifier by an average of 1.59 percentage points in accuracy, demonstrating stronger cross-dataset robustness.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.24936v1)
- [PDF](https://arxiv.org/pdf/2611.24936v1)
- [LLM Safety From Within: Detecting Harmful Content with Internal Representations](https://arxiv.org/abs/2604.18519) (2026, citations: 20)
- [Rethinking Jailbreak Detection of Large Vision Language Models with Representational Contrastive Scoring](https://arxiv.org/abs/2512.12069) (2025, citations: 20)
- [JBShield: Defending Large Language Models from Jailbreak Attacks through Activated Concept Analysis and Manipulation](https://arxiv.org/abs/2502.07557) (2025, citations: 82)
- [Emerging Vulnerabilities in Frontier Models: Multi-Turn Jailbreak Attacks](https://arxiv.org/abs/2409.00137) (2024, citations: 20)
- [Latent Adversarial Training Improves Robustness to Persistent Harmful Behaviors in LLMs](https://arxiv.org/abs/2407.15549) (2024, citations: 211)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/safety #keyword/machine-learning
