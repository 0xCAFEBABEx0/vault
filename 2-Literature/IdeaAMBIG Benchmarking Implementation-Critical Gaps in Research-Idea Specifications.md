---
title: "IdeaAMBIG: Benchmarking Implementation-Critical Gaps in Research-Idea Specifications"
source: "https://arxiv.org/html/2609.10539v1"
author: "Yiling Ma, Yilun Zhao, Sihong Wu, Manasi Patwardhan, Arman Cohan"
published: "2026-09-09"
created: 2026-09-11
description: "A research idea may be novel, coherent, and scientifically plausible, yet its proposed method may remain insufficiently specified for faithful implementation. We study the codification readiness of implementation-facing research-method specifications, defined by whether they provide sufficient methodological information for a competent implementer or coding agent to construct the intended method without unsupported…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/evaluation
  - keyword/benchmark
  - keyword/agents
  - keyword/research-paper
---

# IdeaAMBIG: Benchmarking Implementation-Critical Gaps in Research-Idea Specifications

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.10539v1)
- published:: 2026-09-09
- updated:: 2026-09-09
- arxiv_id:: 2609.10539v1
- pdf:: https://arxiv.org/pdf/2609.10539v1
- categories:: cs.CL

## Abstract / Summary
A research idea may be novel, coherent, and scientifically plausible, yet its proposed method may remain insufficiently specified for faithful implementation. We study the codification readiness of implementation-facing research-method specifications, defined by whether they provide sufficient methodological information for a competent implementer or coding agent to construct the intended method without unsupported assumptions. We construct evidence-grounded specifications and their supported resolutions from papers, codebases, issue threads, and reproduction artifacts. We introduce IdeaAMBIG, a benchmark of 660 evidence-grounded instances: 163 real-world gaps from reproducibility reports and GitHub issues, and 497 controlled synthetic gaps injected into codification-ready references. IdeaAMBIG evaluates three capabilities: codification-readiness assessment, defect localization, and clarification action generation. Defect localization receives only the specification, whereas clarification additionally receives the annotated defect. Across 13 LLMs, the best model achieves 9.6% Macro Defect Recovery Rate on real-world instances but 80.6% Macro Clarification Action Success Rate when given the defect. In an oracle study, supplying the gold resolution raises the downstream codification-ready rate from 14% to 98%. Across all evaluated models, defect localization is the main bottleneck, with stronger clarification given the defect.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.10539v1)
- [PDF](https://arxiv.org/pdf/2609.10539v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/evaluation #keyword/benchmark #keyword/agents #keyword/research-paper
