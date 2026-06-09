---
title: "SIGA: Self-Evolving Coding-Agent Adapters for Scientific Simulation"
source: "https://arxiv.org/html/2606.09774v1"
author: "Matthew Ho, Brian Liu, Jixuan Chen, Audrey Wang, Lianhui Qin"
published: "2026-06-08"
created: 2026-06-10
description: "Advanced scientific simulators expose specialized input languages that turn simulation goals into executable configurations, but learning them can cost domain scientists hours to days. We study simulator setup as a problem of agent-tool interface grounding: what minimal simulator-specific adaptations are needed for an off-the-shelf coding agent to operate real scientific software? Our intuition is that coding agents…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/agents
---

# SIGA: Self-Evolving Coding-Agent Adapters for Scientific Simulation

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.09774v1)
- published:: 2026-06-08
- updated:: 2026-06-08
- arxiv_id:: 2606.09774v1
- pdf:: https://arxiv.org/pdf/2606.09774v1
- categories:: cs.AI, cs.CL

## Abstract / Summary
Advanced scientific simulators expose specialized input languages that turn simulation goals into executable configurations, but learning them can cost domain scientists hours to days. We study simulator setup as a problem of agent-tool interface grounding: what minimal simulator-specific adaptations are needed for an off-the-shelf coding agent to operate real scientific software? Our intuition is that coding agents already know how to navigate files, edit code, run commands, and repair outputs, but they lack the simulator's executable contract: its vocabulary, structural constraints, validation rules, and termination conditions. We introduce SIGA, a Simulator-Interface Grounding Adapter that supplies this contract through retrieval, procedural memory, in-trajectory validation, and validation-enforced termination. We primarily evaluate SIGA on GEOS, an open-source multiphysics simulator used in subsurface science. SIGA produces a complete GEOS deck in about five minutes with TreeSim above 0.90, matching an extended-budget human expert who took about three hours, a roughly 36x wall-clock speedup. On a harder held-out set, grounding raises TreeSim from 0.720 to 0.789, a roughly 10% relative gain over the bare agent, and can reduce the across-seed standard deviation by 16x. Self-evolution further improves SIGA by rewriting adapter contents from prior trajectories, yielding the highest held-out GEOS mean and matching or outperforming the strongest hand-designed configuration. Transfers to OpenFOAM and LAMMPS show that the dominant mechanism shifts by interface: validation matters most when structural completeness is the bottleneck, while memory and retrieval matter most when domain correctness is the bottleneck. These results suggest that lightweight, self-improvable groun…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.09774v1)
- [PDF](https://arxiv.org/pdf/2606.09774v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/agents
