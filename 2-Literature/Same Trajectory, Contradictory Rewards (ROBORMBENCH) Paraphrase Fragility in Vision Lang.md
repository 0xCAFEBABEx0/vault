---
title: "Same Trajectory, Contradictory Rewards (ROBORMBENCH): Paraphrase Fragility in Vision Language Reward Models"
source: "https://arxiv.org/html/2609.05401v1"
author: "Wonje Jeung, Sangyeon Yoon, Hyesoo Hong, Yoonjun Cho, Dongjae Jeon, Bumjun Kim, Jean Oh, Youngjae Yu, Albert No"
published: "2026-09-04"
created: 2026-09-08
description: "Vision-language models are increasingly used as reward functions for robotic learning, but this role requires paraphrase invariance: the same trajectory should receive the same reward under semantically equivalent goal descriptions. We show that current VLM reward models often violate this property. Paraphrasing the instruction alone can substantially change predicted progress scores, and can even flip identical rob…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/multimodal
  - keyword/retrieval
  - keyword/evaluation
  - keyword/benchmark
  - keyword/reasoning
---

# Same Trajectory, Contradictory Rewards (ROBORMBENCH): Paraphrase Fragility in Vision Language Reward Models

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.05401v1)
- published:: 2026-09-04
- updated:: 2026-09-04
- arxiv_id:: 2609.05401v1
- pdf:: https://arxiv.org/pdf/2609.05401v1
- categories:: cs.RO, cs.CL

## Abstract / Summary
Vision-language models are increasingly used as reward functions for robotic learning, but this role requires paraphrase invariance: the same trajectory should receive the same reward under semantically equivalent goal descriptions. We show that current VLM reward models often violate this property. Paraphrasing the instruction alone can substantially change predicted progress scores, and can even flip identical robot behavior between failure and success. To measure this failure mode, we introduce ROBORMBENCH, a benchmark with 2,390 real-robot trajectories, ground-truth progress labels, and 21,673 verified paraphrases spanning lexical, syntactic, and action-goal rewrites. Across proprietary and open-source VLMs, paraphrase-induced instability is widespread and severe, grows under more divergent rewrites, and is not reliably reduced by scale or explicit reasoning. Dedicated reward models trained with trajectory-grounded supervision are substantially more stable. These results show that paraphrase robustness is a core requirement for reliable VLM-based reward modeling in robotics.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.05401v1)
- [PDF](https://arxiv.org/pdf/2609.05401v1)
- [Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons](https://arxiv.org/abs/2603.02115) (2026, citations: 49)
- [Robo-Dopamine: General Process Reward Modeling for High-Precision Robotic Manipulation](https://arxiv.org/abs/2512.23703) (2025, citations: 43)
- [When Language Overrules: Revealing Text Dominance in Multimodal Large Language Models](https://arxiv.org/abs/2508.10552) (2025, citations: 19)
- [Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities](https://arxiv.org/abs/2507.06261) (2025, citations: 4018)
- [A Survey on Vision-Language-Action Models: An Action Tokenization Perspective](https://arxiv.org/abs/2507.01925) (2025, citations: 106)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/multimodal #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/reasoning
