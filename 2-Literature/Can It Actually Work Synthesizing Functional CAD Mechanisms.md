---
title: "Can It Actually Work? Synthesizing Functional CAD Mechanisms"
source: "https://arxiv.org/html/2610.26861v1"
author: "Wenqian Zhang, Yangyi Huang, Zigeng Xu, Weiyang Liu, Zhen Liu"
published: "2026-10-19"
created: 2026-10-21
description: "While LLM agents can generate visually plausible CAD assemblies, these designs often fail to fulfill their intended physical functions. We study functional CAD design, a setting where agents interpret underspecified requests to construct and iteratively revise mechanisms that satisfy functional requirements in physical simulation. Verifying these requirements is nontrivial: different candidate mechanisms may realize…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/evaluation
  - keyword/benchmark
  - keyword/agents
---

# Can It Actually Work? Synthesizing Functional CAD Mechanisms

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.26861v1)
- published:: 2026-10-19
- updated:: 2026-10-19
- arxiv_id:: 2610.26861v1
- pdf:: https://arxiv.org/pdf/2610.26861v1
- categories:: cs.CV, cs.CL, cs.GR

## Abstract / Summary
While LLM agents can generate visually plausible CAD assemblies, these designs often fail to fulfill their intended physical functions. We study functional CAD design, a setting where agents interpret underspecified requests to construct and iteratively revise mechanisms that satisfy functional requirements in physical simulation. Verifying these requirements is nontrivial: different candidate mechanisms may realize the same function through entirely different components, controls, and operating sequences. To bridge this gap, we propose FunCAD-Harness, a framework that translates abstract requirements into candidate-specific physical tests and uses simulation feedback to guide design revisions. To systematically evaluate this capability, we introduce FunCADBench, a benchmark spanning 46 mechanism families with interdependent and multi-step operations. Experiments across frontier LLM agents show that FunCAD-Harness exposes subtle mechanical failures invisible to visual inspection, substantially improving functional success rates over standard simulation-augmented baselines. Ultimately, our work marks a step toward CAD agents capable of translating human intent into working mechanisms.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.26861v1)
- [PDF](https://arxiv.org/pdf/2610.26861v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/evaluation #keyword/benchmark #keyword/agents
