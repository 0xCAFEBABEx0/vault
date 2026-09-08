---
title: "Design Docs Are All You Need: An AI-native Machine-Learning Performance Tool"
source: "https://arxiv.org/html/2609.05364v1"
author: "Samuel Kushnir, Kimia Noorbakhsh, Kavya Sreedhar, Liqun Cheng, Ming Liu, Parthasarathy Ranganathan, Mohammad Alizadeh, Fred Kjolstad, Suvinay Subramanian"
published: "2026-09-04"
created: 2026-09-09
description: "Machine-learning performance modeling is a uniquely hostile terrain for long-lived software: the assumptions baked into today's abstractions are invalidated by tomorrow's models and systems, forcing perpetual refactoring of performance-modeling frameworks. Meanwhile, AI coding agents have become fast and capable enough that regenerating an entire library is cheaper than paying down the tech debt of incrementally pat…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/nlp
  - keyword/agents
---

# Design Docs Are All You Need: An AI-native Machine-Learning Performance Tool

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.05364v1)
- published:: 2026-09-04
- updated:: 2026-09-04
- arxiv_id:: 2609.05364v1
- pdf:: https://arxiv.org/pdf/2609.05364v1
- categories:: cs.PL, cs.AI

## Abstract / Summary
Machine-learning performance modeling is a uniquely hostile terrain for long-lived software: the assumptions baked into today's abstractions are invalidated by tomorrow's models and systems, forcing perpetual refactoring of performance-modeling frameworks. Meanwhile, AI coding agents have become fast and capable enough that regenerating an entire library is cheaper than paying down the tech debt of incrementally patching it. We describe SMART, a rigorous symbolic performance-modeling library for ML systems whose main branch contains almost no code: the repository is a DAG of self-contained natural-language design docs, coding sub-agents regenerate the implementation from only the docs on new version updates, and every human change is a natural-language edit to a doc--self-documenting by construction. Two ingredients make regeneration reliable: (i) a design-doc style built around step-by-step worked examples that act as in-context demonstrations for the generating agents, and (ii) a minimal, recursively defined operator IR with symbolic (SymPy) cost expressions, a fast analytical roll-up mode for large sweeps, and a slow modulo-scheduling mode for fine-grained schedule studies. Regenerated implementations reproduce hand-audited reference models--including DeepSeek-V3 serving on a TPU pod slice--to round-off precision, suggesting that design docs--not code--can be the durable artifact for ML-systems co-design tools.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.05364v1)
- [PDF](https://arxiv.org/pdf/2609.05364v1)
- [TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings](https://arxiv.org/abs/2304.01433) (2023, citations: 730)
- [SymPy: Symbolic computing in Python](https://peerj.com/articles/cs-103.pdf) (2017, citations: 2038)
- [Roofline: an insightful visual performance model for multicore architectures](https://www.osti.gov/servlets/purl/1407073) (2009, citations: 1327)
- [Iterative module scheduling: an algorithm for software pipelining loops](https://dl.acm.org/doi/pdf/10.1145/192724.192731) (1994, citations: 749)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/nlp #keyword/agents
