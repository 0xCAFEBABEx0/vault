---
title: "Learning to Attack and Defend: Adaptive Red Teaming of Language Models via GRPO"
source: "https://arxiv.org/html/2606.09701v1"
author: "Blake Bullwinkel, Eugenia Kim, Amanda Minnich, Mark Russinovich"
published: "2026-06-08"
created: 2026-06-10
description: "AI red teaming must continually adapt to evolving attackers and defenders. Reinforcement learning offers a promising approach to discovering novel attacks, and co-training methods can produce more robust defenders in tandem. Recent works have demonstrated the efficacy of attacker-defender co-training by applying PPO and DPO, but report that GRPO is unstable in this setting. We introduce AdvGRPO, a co-training framew…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/benchmark
  - keyword/safety
  - keyword/machine-learning
---

# Learning to Attack and Defend: Adaptive Red Teaming of Language Models via GRPO

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.09701v1)
- published:: 2026-06-08
- updated:: 2026-06-08
- arxiv_id:: 2606.09701v1
- pdf:: https://arxiv.org/pdf/2606.09701v1
- categories:: cs.CL, cs.AI, cs.LG

## Abstract / Summary
AI red teaming must continually adapt to evolving attackers and defenders. Reinforcement learning offers a promising approach to discovering novel attacks, and co-training methods can produce more robust defenders in tandem. Recent works have demonstrated the efficacy of attacker-defender co-training by applying PPO and DPO, but report that GRPO is unstable in this setting. We introduce AdvGRPO, a co-training framework that makes GRPO viable for joint attacker-defender optimization using dense multi-channel rewards and decoupled advantage normalization. Training progresses through a curriculum from single-turn to closed-loop multi-turn attacks before bootstrapping co-training, where attacker and defender models are updated in alternation. We show that our method can produce highly effective and transferable attacks and that co-trained defenders outperform baselines on safety benchmarks.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.09701v1)
- [PDF](https://arxiv.org/pdf/2606.09701v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark #keyword/safety #keyword/machine-learning
