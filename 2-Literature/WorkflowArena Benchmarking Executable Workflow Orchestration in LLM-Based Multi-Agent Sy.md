---
title: "WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems"
source: "https://arxiv.org/html/2611.12856v1"
author: "Zheng Jiang, Fang Niu, Bo Peng, Houde Qian, Wenyi Li, Deyao Hong, Mingju Gao, Yizhe Chi, Youjie Zheng, Kaisen Yang, Calvin Xiao, Lifeng Sun, Huan-ang Gao"
published: "2026-11-09"
created: 2026-11-11
description: "Large language model agents are increasingly deployed as multi-agent systems rather than as a standalone model operating within a single context. Recent agent harnesses allow the model to instantiate worker agents and to author the executable workflow that coordinates them, shifting the design of system structure from developers to the model at run time. The quality of this organization therefore constitutes a disti…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/benchmark
  - keyword/agents
---

# WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.12856v1)
- published:: 2026-11-09
- updated:: 2026-11-09
- arxiv_id:: 2611.12856v1
- pdf:: https://arxiv.org/pdf/2611.12856v1
- categories:: cs.CL, cs.SE

## Abstract / Summary
Large language model agents are increasingly deployed as multi-agent systems rather than as a standalone model operating within a single context. Recent agent harnesses allow the model to instantiate worker agents and to author the executable workflow that coordinates them, shifting the design of system structure from developers to the model at run time. The quality of this organization therefore constitutes a distinct capability, yet existing benchmarks either measure end-to-end task completion or evaluate coordination under structures specified in advance. We formalize this capability as workflow orchestration and introduce WorkflowArena, a benchmark of 145 long-horizon tasks spanning 8 professional domains, from software engineering and formal mathematics to legal analysis and 3D production. Each task specifies an initial workspace and an integrated deliverable composed of interdependent components, which is assessed by a hidden verifier. Agents determine autonomously whether and how to delegate, and all delegation is recorded, enabling joint evaluation of deliverable quality and the organization of the underlying work. Experiments with nine models show that no single configuration performs best across all domains and that systems exhibit distinct delegation strategies: at high effort, Claude models in Claude Code invoke workflows less frequently but with larger worker groups, whereas GPT models in Codex delegate more frequently in smaller units. When the executing model is held fixed on a challenging subset of tasks, workflows authored by Claude Opus 5.5 substantially improve weaker executors, indicating that workflow organization is itself a measurable determinant of task performance.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.12856v1)
- [PDF](https://arxiv.org/pdf/2611.12856v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark #keyword/agents
