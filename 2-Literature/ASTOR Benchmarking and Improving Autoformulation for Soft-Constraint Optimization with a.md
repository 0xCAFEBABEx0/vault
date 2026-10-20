---
title: "ASTOR: Benchmarking and Improving Autoformulation for Soft-Constraint Optimization with a Formal Grammar"
source: "https://arxiv.org/html/2610.26819v1"
author: "Amer Goel, Yeganeh Alimohammadi, Andrew Daw"
published: "2026-10-19"
created: 2026-10-21
description: "Real-world decision problems combine two qualitatively different kinds of constraints: requirements that must be satisfied, called hard constraints, and preferences that can be violated, called soft constraints. Because these problems are often posed to decision-makers in natural language, large language models offer a natural tool for assisting with their solution. This has given rise to autoformulation, which focu…"
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
  - keyword/machine-learning
---

# ASTOR: Benchmarking and Improving Autoformulation for Soft-Constraint Optimization with a Formal Grammar

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.26819v1)
- published:: 2026-10-19
- updated:: 2026-10-19
- arxiv_id:: 2610.26819v1
- pdf:: https://arxiv.org/pdf/2610.26819v1
- categories:: cs.CL

## Abstract / Summary
Real-world decision problems combine two qualitatively different kinds of constraints: requirements that must be satisfied, called hard constraints, and preferences that can be violated, called soft constraints. Because these problems are often posed to decision-makers in natural language, large language models offer a natural tool for assisting with their solution. This has given rise to autoformulation, which focuses on using LLMs to translate natural-language descriptions of decision problems into executable mathematical optimization models. However, this research often neglects soft constraints like those proposed by consumers, managers, and planners, despite the fact that many practical problems require modeling them explicitly. We introduce ASTOR, an inference-time framework that maps a natural-language decision problem to a grammar-guided abstract syntax tree (AST) before deterministically compiling the resulting representation into executable optimization code. We also introduce SoftOR, a unified benchmark of natural language problems which focuses on soft constraint formulations. On SoftOR, ASTOR achieves the best aggregate accuracy among comparable single-request and multi-agent LLM methods while remaining competitive on standard autoformulation benchmarks that include only hard constraints. Code and data are available at https://anonymous.4open.science/r/astor-softor-iclr-E34C/README.md.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.26819v1)
- [PDF](https://arxiv.org/pdf/2610.26819v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark #keyword/agents #keyword/machine-learning
