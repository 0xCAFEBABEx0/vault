---
title: "Behavioral Couplings: From Formation to Behavioral Emergence in Language Models"
source: "https://arxiv.org/html/2610.23847v1"
author: "Dongyoon Hahm, Woogyeol Jin, Dennis Wei, Yi Zhou, Nathalie Baracaldo, Kimin Lee"
published: "2026-10-16"
created: 2026-10-20
description: "Fine-tuning large language models (LLMs) can induce behaviors beyond those explicitly targeted. For example, training a model to respond more warmly can make it more sycophantic, and training it to write insecure code can cause broad misalignment on prompts unrelated to coding. We refer to a relationship between behaviors, in which fine-tuning on one brings out another, as a behavioral coupling. In this work, we stu…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/safety
  - keyword/machine-learning
---

# Behavioral Couplings: From Formation to Behavioral Emergence in Language Models

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.23847v1)
- published:: 2026-10-16
- updated:: 2026-10-16
- arxiv_id:: 2610.23847v1
- pdf:: https://arxiv.org/pdf/2610.23847v1
- categories:: cs.CL, cs.AI, cs.LG

## Abstract / Summary
Fine-tuning large language models (LLMs) can induce behaviors beyond those explicitly targeted. For example, training a model to respond more warmly can make it more sycophantic, and training it to write insecure code can cause broad misalignment on prompts unrelated to coding. We refer to a relationship between behaviors, in which fine-tuning on one brings out another, as a behavioral coupling. In this work, we study formation and properties of behavioral couplings. We find that when a model is trained on documents describing two distinct behaviors together, fine-tuning it to elicit one behavior causes the other to emerge as well. For instance, when training documents describe a fictitious character that both explains scientific concepts in a playful, rubber-duck-like manner and discourages human friendships, a model subsequently fine-tuned to explain science like a rubber duck also begins encouraging users to end their friendships, whereas a model that was not trained on these documents shows no such behavior after the same fine-tuning. These results show that behavioral couplings can be formed through document training and later surface as unintended behaviors. More concerningly, we find that couplings can compose. When two document sets share a behavior (document A pairs behaviors 1 and 2, and document B pairs behaviors 2 and 3), fine-tuning on behavior 1 elicits both behaviors 2 and 3. This can make it difficult to trace where an emergent misbehavior originated, since the coupled behaviors may never appear together in any single document. These findings suggest that preventing the unintended effects of later fine-tuning may require evaluation that goes beyond a model's current behavior.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.23847v1)
- [PDF](https://arxiv.org/pdf/2610.23847v1)
- [Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases](https://arxiv.org/abs/2605.27355) (2026, citations: 1)
- [Model Spec Midtraining: Improving How Alignment Training Generalizes](https://arxiv.org/abs/2605.02087) (2026, citations: 12)
- [Training language models to be warm can reduce accuracy and increase sycophancy](https://www.nature.com/articles/s41586-026-10410-0.pdf) (2026, citations: 62)
- [Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment](https://arxiv.org/abs/2601.10160) (2026, citations: 30)
- [Weird Generalization and Inductive Backdoors: New Ways to Corrupt LLMs](https://arxiv.org/abs/2512.09742) (2025, citations: 55)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/safety #keyword/machine-learning
