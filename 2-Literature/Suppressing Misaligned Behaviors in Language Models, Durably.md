---
title: "Suppressing Misaligned Behaviors in Language Models, Durably"
source: "https://arxiv.org/html/2611.05358v1"
author: "Luxi He, Pengcheng Jiang, Jifan Zhang, Jiawei Han, Danqi Chen"
published: "2026-11-03"
created: 2026-11-05
description: "Undesired model behaviors can emerge or re-emerge at any stage of training. Once observed, how effectively can we suppress them? To study this question, we first construct two model organisms--language models deliberately trained to exhibit a specific misalignment--that differ in what triggers the behavior. The narrow-trigger organism misbehaves only when the prompt contains a specific cue: it cheats on multiple-cho…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/safety
  - keyword/machine-learning
---

# Suppressing Misaligned Behaviors in Language Models, Durably

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.05358v1)
- published:: 2026-11-03
- updated:: 2026-11-03
- arxiv_id:: 2611.05358v1
- pdf:: https://arxiv.org/pdf/2611.05358v1
- categories:: cs.CL, cs.AI, cs.LG

## Abstract / Summary
Undesired model behaviors can emerge or re-emerge at any stage of training. Once observed, how effectively can we suppress them? To study this question, we first construct two model organisms--language models deliberately trained to exhibit a specific misalignment--that differ in what triggers the behavior. The narrow-trigger organism misbehaves only when the prompt contains a specific cue: it cheats on multiple-choice questions by following a planted hint that points to a wrong answer, and behaves normally otherwise. The broad-trigger organism has no such cue: after fine-tuning on insecure code, it gives harmful responses across a wide range of open-ended prompts. We then formalize post-hoc behavioral suppression and evaluate methods along three criteria: immediate suppression of the target behavior, durability under further training, and preservation of general capability. We compare standard methods--SFT, GRPO, and gradient-ascent unlearning--along these dimensions. Building on prior work on alignment shallowness, we hypothesize that more durable suppression requires the ability to recover from a wider range of misalignment states. We introduce Prefix-Expanded Adversarial Reinforcement Learning (PEARL), a GRPO variant that augments rollouts with continuations from intermediate states sampled along cached organism trajectories. Across both organism settings and two model families (Qwen3-4B, GPT-OSS-20B), PEARL achieves strong immediate suppression while preserving task accuracy, and remains durable under further fine-tuning on either the organism's data or unrelated data. It obtains the greatest benefit when the undesirable behavior is broad and cannot be addressed through targeted SFT. Together, our framework and method offer a step toward more durable post-hoc remo…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.05358v1)
- [PDF](https://arxiv.org/pdf/2611.05358v1)
- [Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR](https://arxiv.org/abs/2603.07084) (2026, citations: 19)
- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621) (2026, citations: 11)
- [Stress-Testing Model Specs Reveals Character Differences among Language Models](https://arxiv.org/abs/2510.07686) (2025, citations: 15)
- [In-Training Defenses against Emergent Misalignment in Language Models](https://arxiv.org/abs/2508.06249) (2025, citations: 18)
- [Persona Features Control Emergent Misalignment](https://arxiv.org/abs/2506.19823) (2025, citations: 93)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/safety #keyword/machine-learning
