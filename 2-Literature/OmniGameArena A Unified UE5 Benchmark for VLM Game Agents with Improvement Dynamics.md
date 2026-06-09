---
title: "OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics"
source: "https://arxiv.org/html/2606.09826v1"
author: "Mingxian Lin, Shengju Qian, Yuqi Liu, Yi-Hua Huang, Yiyu Wang, Wei Huang, Yitang Li, Fan Zhang, Zeyu Hu, Lingting Zhu, Xin Wang, Xiaojuan Qi"
published: "2026-06-08"
created: 2026-06-10
description: "Vision-language model (VLM) agents are increasingly deployed in interactive game environments. Yet game benchmarks for VLM agents typically report a single first-attempt score per (agent, game) pair, focus on single-agent Solo play, and lack unified protocols for evaluating heterogeneous agent classes (commercial VLMs, open-weight VLMs, and specialized game policies) on the same footing. We address these gaps with O…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/multimodal
  - keyword/evaluation
  - keyword/benchmark
  - keyword/agents
---

# OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.09826v1)
- published:: 2026-06-08
- updated:: 2026-06-08
- arxiv_id:: 2606.09826v1
- pdf:: https://arxiv.org/pdf/2606.09826v1
- categories:: cs.CV, cs.AI

## Abstract / Summary
Vision-language model (VLM) agents are increasingly deployed in interactive game environments. Yet game benchmarks for VLM agents typically report a single first-attempt score per (agent, game) pair, focus on single-agent Solo play, and lack unified protocols for evaluating heterogeneous agent classes (commercial VLMs, open-weight VLMs, and specialized game policies) on the same footing. We address these gaps with OmniGameArena, a real-time benchmark of twelve newly built Unreal Engine 5 games spanning Solo (7), PvP (3), and Coop (2) with unified action interfaces, and the Improvement Dynamics Curve (IDC), an agentic-reflection harness in which a tool-using reflector LLM autonomously refines a bounded skill prompt across multiple rounds. Beyond cold-start leaderboard scores, IDC exposes two additional observables for each (agent, game) pair: how the score evolves across reflection rounds, and how the learned skill behaves on held-out task variants. We report these observables for twelve VLM agents on the cold-start leaderboard and four top agents under IDC.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.09826v1)
- [PDF](https://arxiv.org/pdf/2606.09826v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/multimodal #keyword/evaluation #keyword/benchmark #keyword/agents
