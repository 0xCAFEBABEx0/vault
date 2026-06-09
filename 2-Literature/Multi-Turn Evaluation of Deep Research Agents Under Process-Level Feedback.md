---
title: "Multi-Turn Evaluation of Deep Research Agents Under Process-Level Feedback"
source: "https://arxiv.org/html/2606.09748v1"
author: "Rishabh Sabharwal, Hongru Wang, Amos Storkey, Jeff Z. Pan"
published: "2026-06-08"
created: 2026-06-10
description: "Existing benchmarks for deep research agents (DRAs) assess only single-shot outputs, ignoring a key question: can DRAs improve their reports when guided by feedback? To investigate this, we conduct a multi-turn evaluation of DRAs under two feedback settings: self-reflection, in which the agent revises its report without any external diagnostic signal, and process-level feedback, in which the agent receives guidance…"
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

# Multi-Turn Evaluation of Deep Research Agents Under Process-Level Feedback

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.09748v1)
- published:: 2026-06-08
- updated:: 2026-06-08
- arxiv_id:: 2606.09748v1
- pdf:: https://arxiv.org/pdf/2606.09748v1
- categories:: cs.AI, cs.CL, cs.LG

## Abstract / Summary
Existing benchmarks for deep research agents (DRAs) assess only single-shot outputs, ignoring a key question: can DRAs improve their reports when guided by feedback? To investigate this, we conduct a multi-turn evaluation of DRAs under two feedback settings: self-reflection, in which the agent revises its report without any external diagnostic signal, and process-level feedback, in which the agent receives guidance targeting gaps in its research strategy. To enable process-level feedback, we design Research Gap Inference (RGI), a method that analyzes patterns of satisfied and unsatisfied rubric criteria to infer research-process gaps. Our analysis reveals three key findings: (i) under self-reflection, agents incorporate and regress on rubric criteria at nearly equal rates, yielding negligible net improvement; (ii) a single round of process-level feedback yields substantial gains, raising the normalized score by approximately $8$-$15$ points and yielding a roughly $35$-$40\%$ incorporation rate; (iii) these gains do not compound over subsequent turns, as agents regress on up to $24\%$ of previously satisfied criteria when rewriting the full report to address remaining gaps. Even with targeted guidance, reliable multi-turn improvement remains out of reach for the DRA architectures we evaluate. Our code and results are publicly available at https://github.com/sabharwalrishabh/Multi-Turn-Evaluation-of-DRAs.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.09748v1)
- [PDF](https://arxiv.org/pdf/2606.09748v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/evaluation #keyword/benchmark #keyword/agents #keyword/machine-learning
