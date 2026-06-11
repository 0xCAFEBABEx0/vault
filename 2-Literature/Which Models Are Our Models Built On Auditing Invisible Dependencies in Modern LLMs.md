---
title: "Which Models Are Our Models Built On? Auditing Invisible Dependencies in Modern LLMs"
source: "https://arxiv.org/html/2606.12385v1"
author: "Sanjay Adhikesaven, Haoxiang Sun, Sewon Min"
published: "2026-06-10"
created: 2026-06-12
description: "Modern LLM training pipelines increasingly rely on other models to generate data, filter corpora, judge outputs, and guide development decisions. These dependencies are recursive: a model may depend on an upstream artifact whose own dependencies are documented only in separate releases and artifacts. As a result, the full dependency structure is fragmented across heterogeneous public artifacts, with complexity and r…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/retrieval
  - keyword/evaluation
  - keyword/agents
  - keyword/machine-learning
---

# Which Models Are Our Models Built On? Auditing Invisible Dependencies in Modern LLMs

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.12385v1)
- published:: 2026-06-10
- updated:: 2026-06-10
- arxiv_id:: 2606.12385v1
- pdf:: https://arxiv.org/pdf/2606.12385v1
- categories:: cs.CL

## Abstract / Summary
Modern LLM training pipelines increasingly rely on other models to generate data, filter corpora, judge outputs, and guide development decisions. These dependencies are recursive: a model may depend on an upstream artifact whose own dependencies are documented only in separate releases and artifacts. As a result, the full dependency structure is fragmented across heterogeneous public artifacts, with complexity and recursive depth far outpacing humans' ability to trace. We introduce ModSleuth, an agentic system that recursively reconstructs LLM dependency graphs from public artifacts with source-grounded evidence. We find that the primary challenge is no longer information extraction, but defining what constitutes a dependency and reconciling artifact references across inconsistent documentation. We address these challenges through a formalization that distinguishes direct and indirect dependencies, represents heterogeneous pipeline roles through operation-centered relationships, and resolves artifact identities across names, versions, and repositories. Applying ModSleuth to four public-artifact-rich LLM releases, we recover 1,060 source-verified dependencies and construct large-scale dependency graphs of modern LLM development. These graphs reveal multi-hop license obligations, train-evaluation coupling, discrepancies between released and training-time artifacts, and documentation inconsistencies that would otherwise be difficult to uncover. We release ModSleuth and the resulting dependency graphs to support transparent analysis of the increasingly complex ecosystems underlying modern LLMs.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.12385v1)
- [PDF](https://arxiv.org/pdf/2606.12385v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/retrieval #keyword/evaluation #keyword/agents #keyword/machine-learning
