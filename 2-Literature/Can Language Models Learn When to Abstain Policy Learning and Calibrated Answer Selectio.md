---
title: "Can Language Models Learn When to Abstain? Policy Learning and Calibrated Answer Selection"
source: "https://arxiv.org/html/2610.13821v1"
author: "Juan Terven, Diana-Margarita Córdova-Esparza, Ruben Gomez, Carlos Miranda Rocha, Julio-Alejandro Romero-González, Edgar Chavez-Urbiola"
published: "2026-10-09"
created: 2026-10-14
description: "A useful language model should know when to answer and when to say 'I don't know.' Can we improve that decision by training the model itself or by training a separate component to check its answers? We study both approaches on Qwen3-14B for factual questions, using a score that rewards correct answers, penalizes mistakes, and allows abstention. Across three training seeds and two held-out confidence thresholds, a le…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/machine-learning
---

# Can Language Models Learn When to Abstain? Policy Learning and Calibrated Answer Selection

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.13821v1)
- published:: 2026-10-09
- updated:: 2026-10-09
- arxiv_id:: 2610.13821v1
- pdf:: https://arxiv.org/pdf/2610.13821v1
- categories:: cs.CL

## Abstract / Summary
A useful language model should know when to answer and when to say "I don't know." Can we improve that decision by training the model itself or by training a separate component to check its answers? We study both approaches on Qwen3-14B for factual questions, using a score that rewards correct answers, penalizes mistakes, and allows abstention. Across three training seeds and two held-out confidence thresholds, a learned answer selector improves threshold-averaged utility over the original model's calibrated confidence filter. On TriviaQA, mean coverage increases from 20.2% to 30.9%, while the pooled error rate among scored answers decreases from 23.0% to 14.5% under exact-match grading. The tested reinforcement-learning changes do not establish consistent gains. On NQ-Open, the selector improves threshold-averaged utility over the filter but still performs worse than always abstaining. A partial human-reviewed audit preserves the TriviaQA finding. Our results support learning to select answers in this setting while showing that reliable abstention across datasets remains unresolved.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.13821v1)
- [PDF](https://arxiv.org/pdf/2610.13821v1)
- [I-CALM: Incentivizing Confidence-Aware Abstention for LLM Selective Answering](https://arxiv.org/abs/2604.03904) (2026, citations: 5)
- [Rewarding Intellectual Humility Learning When Not To Answer In Large Language Models](https://arxiv.org/abs/2601.20126) (2026, citations: 3)
- [TruthRL: Incentivizing Truthful LLMs via Reinforcement Learning](https://arxiv.org/abs/2509.25760) (2025, citations: 21)
- [Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664) (2025, citations: 364)
- [AbstentionBench: Reasoning LLMs Fail on Unanswerable Questions](https://arxiv.org/abs/2506.09038) (2025, citations: 157)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/machine-learning
