---
title: "$μ$-Bench: Benchmarking Multi-User Task Completion in Shared Interaction Voice Agents"
source: "https://arxiv.org/html/2611.34920v1"
author: "Qihao Lin, Guanxu Chen, Shuhang Zheng, Xiaoya Lu, Jingyi Yang, Terumi Chiba, Wenyi Yu, Chao Zhang, Zhuan Shi, Jing Shao"
published: "2026-11-25"
created: 2026-11-28
description: "Voice agents in shared spaces must satisfy interdependent multi-user requests while upholding per-user authority, privacy, and task constraints. Existing evaluations offer limited coverage when participants react throughout a session. We introduce $μ$-Bench, a benchmark for joint task completion in closed-loop, full-duplex multi-user voice interaction. Simulated participants act from isolated profiles of goals, know…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/retrieval
  - keyword/evaluation
  - keyword/benchmark
  - keyword/agents
---

# $μ$-Bench: Benchmarking Multi-User Task Completion in Shared Interaction Voice Agents

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.34920v1)
- published:: 2026-11-25
- updated:: 2026-11-25
- arxiv_id:: 2611.34920v1
- pdf:: https://arxiv.org/pdf/2611.34920v1
- categories:: cs.CL, cs.AI

## Abstract / Summary
Voice agents in shared spaces must satisfy interdependent multi-user requests while upholding per-user authority, privacy, and task constraints. Existing evaluations offer limited coverage when participants react throughout a session. We introduce $μ$-Bench, a benchmark for joint task completion in closed-loop, full-duplex multi-user voice interaction. Simulated participants act from isolated profiles of goals, knowledge, and permissions, adapting to the agent's speech and tool outcomes. Across 20 domains, 100 scenarios vary group size, acoustics, and follow-up demands to form 800 cases (408 tool-augmented, 392 tool-free). Joint Task Success (JTS) requires all user goals, privacy boundaries, and terminal states to hold jointly, while Pure JTS further disallows unauthorized tool calls; Attribution, Threading, and Coordination (ATC) diagnostics localize failures. Across 13 voice agents, proprietary systems peak at 62.24\% tool-free and 65.44\% tool-augmented success, while open-weight models remain below 20\%. ATC diagnostics show that open-weight models lag primarily in multi-turn attribution and threading, and controlled contrasts reveal that larger groups consistently degrade joint task success across capable systems. By coupling reactive multi-user simulation with verifiable session-level outcomes, $μ$-Bench provides a rigorous testbed for shared voice agents.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.34920v1)
- [PDF](https://arxiv.org/pdf/2611.34920v1)
- [DuplexLedger: Benchmarking Transactional Memory in Full-Duplex Speech Agents](https://arxiv.org/abs/2610.27581) (2026, citations: 1)
- [MultiPartyTurnBench: Benchmarking Floor Control in Multi-Party Spoken Dialogue](https://arxiv.org/abs/2610.20172) (2026, citations: 1)
- [MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conversation](https://arxiv.org/abs/2609.36903) (2026, citations: 2)
- [Voices as Handles: Reasoning about Speaker Identity with Frozen Text LLMs](https://arxiv.org/abs/2609.38501) (2026, citations: 1)
- [Duplex-MPE: Benchmarking Multi-Party Interaction in Full-Duplex Dialogue](https://arxiv.org/abs/2609.31948) (2026, citations: 3)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/agents
