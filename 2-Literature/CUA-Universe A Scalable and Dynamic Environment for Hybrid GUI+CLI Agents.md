---
title: "CUA-Universe: A Scalable and Dynamic Environment for Hybrid GUI+CLI Agents"
source: "https://arxiv.org/html/2609.05374v1"
author: "Haoting Shi, Wenhao Wang, Weicheng Fang, Yaozhong Liang, Tian Jin, Pengxiang Zhao, Guangyi Liu, Siheng Chen, Yanfeng Wang"
published: "2026-09-04"
created: 2026-09-09
description: "Computer-use agents have advanced on benchmarks like OSWorld and AndroidWorld, but still act mostly through the GUI, often producing inefficient trajectories. Real-world computer work is hybrid, combining visual-state inspection with precise, high-throughput command-line operations, so capable agents must coordinate both modalities over shared application state. Yet scalable hybrid environments remain scarce because…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/evaluation
  - keyword/benchmark
  - keyword/agents
  - keyword/machine-learning
---

# CUA-Universe: A Scalable and Dynamic Environment for Hybrid GUI+CLI Agents

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.05374v1)
- published:: 2026-09-04
- updated:: 2026-09-04
- arxiv_id:: 2609.05374v1
- pdf:: https://arxiv.org/pdf/2609.05374v1
- categories:: cs.AI

## Abstract / Summary
Computer-use agents have advanced on benchmarks like OSWorld and AndroidWorld, but still act mostly through the GUI, often producing inefficient trajectories. Real-world computer work is hybrid, combining visual-state inspection with precise, high-throughput command-line operations, so capable agents must coordinate both modalities over shared application state. Yet scalable hybrid environments remain scarce because supporting both GUI and CLI over real applications typically requires substantial manual engineering for each application. Existing agents also struggle to use the two interfaces complementarily: CLI-native agents lack visual perception for tasks involving interface state or layout, while GUI-native agents are inefficient for operations better executed through commands. We introduce CUA-Universe, a scalable environment-to-data pipeline that turns real desktop software into hybrid GUI+CLI environments. App-Forge adapts applications into reproducible VMs and command-line surfaces it discovers, wraps, or generates, scaling to 16 applications; Task-Weave synthesizes diverse hybrid tasks of controllable difficulty from reusable operations over seed files; and Path-Steer steers rollouts along efficient hybrid paths and harvests verified trajectories for post-training. Training on this data shifts behavior from inefficient GUI interaction and brittle CLI scripting toward effective GUI+CLI orchestration. Our 9B model improves both success and efficiency on CUA-Verse (Score +39.3 pts; -37% steps, -60% tokens), OSWorld (SR +16.8 pts; -57% steps, -44% tokens), and OSWorld-MCP (Score +7.84 pts; -27% steps, -30% tokens). CUA-Universe provides a scalable path toward more capable and efficient computer-use agents.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.05374v1)
- [PDF](https://arxiv.org/pdf/2609.05374v1)
- [OSWorld2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks](https://arxiv.org/abs/2606.29537) (2026, citations: 15)
- [CLI-Universe: Towards Verifiable Task Synthesis Engine for Terminal Agents](https://arxiv.org/abs/2606.22883) (2026, citations: 4)
- [GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents](https://arxiv.org/abs/2606.24551) (2026, citations: 3)
- [Tmax: A simple recipe for terminal agents](https://arxiv.org/abs/2606.23321) (2026, citations: 11)
- [MacAgentBench: Benchmarking AI Agents on Real-World macOS Desktop](https://arxiv.org/abs/2606.22557) (2026, citations: 2)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/evaluation #keyword/benchmark #keyword/agents #keyword/machine-learning
