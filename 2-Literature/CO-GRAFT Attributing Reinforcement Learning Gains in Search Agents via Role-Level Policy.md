---
title: "CO-GRAFT: Attributing Reinforcement Learning Gains in Search Agents via Role-Level Policy Grafting"
source: "https://arxiv.org/html/2611.31185v1"
author: "Ramraj Chandradevan, Sayontan Ghosh, Vinoth Selvendran"
published: "2026-11-23"
created: 2026-11-25
description: "Reinforcement learning (RL) improves large language model search agents by up to 32 exact-match (EM) points over their pre-RL initializations, yet overall accuracy gains do not identify which underlying functional capabilities improve or interact during training. We introduce CO-GRAFT, a reward-agnostic interventional attribution framework in which an RL-trained agent and its pre-RL initialization jointly generate a…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/reasoning
  - keyword/agents
  - keyword/machine-learning
---

# CO-GRAFT: Attributing Reinforcement Learning Gains in Search Agents via Role-Level Policy Grafting

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.31185v1)
- published:: 2026-11-23
- updated:: 2026-11-23
- arxiv_id:: 2611.31185v1
- pdf:: https://arxiv.org/pdf/2611.31185v1
- categories:: cs.IR, cs.AI, cs.CL

## Abstract / Summary
Reinforcement learning (RL) improves large language model search agents by up to 32 exact-match (EM) points over their pre-RL initializations, yet overall accuracy gains do not identify which underlying functional capabilities improve or interact during training. We introduce CO-GRAFT, a reward-agnostic interventional attribution framework in which an RL-trained agent and its pre-RL initialization jointly generate a single trajectory under closed-loop execution with live retrieval. Each policy controls a mutually exclusive subset of four functional roles: intermediate reasoning, search-or-answer decision, search query generation, and final answer extraction. Evaluating all 2^4=16 role assignments without modifying weights or retraining defines a cooperative game whose Shapley values decompose the total RL gain across roles, while M"obius interaction terms distinguish standalone role improvements from multi-role coupling. Applying CO-GRAFT to Search-R1 agents across Qwen2.5 and Llama-3.2 models (spanning two sizes, base and instruction-tuned initializations, GRPO and PPO optimizers, and NQ and HotpotQA datasets), we show that query generation never exceeds 15% of the total gain; instead, gains are governed by pre-RL answer validity, search retention, model scale, and fixed task-level search budgets, shifting credit from reasoning toward answer extraction in larger or well-formatted answer response checkpoints while smaller base models rely on reasoning--decision coupling.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.31185v1)
- [PDF](https://arxiv.org/pdf/2611.31185v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/reasoning #keyword/agents #keyword/machine-learning
