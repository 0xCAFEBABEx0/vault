---
title: "Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions"
source: "https://arxiv.org/html/2610.37624v1"
author: "Anouar Imel, Imad Charradi, Abderrahman Sghir, Khalil El Khammar"
published: "2026-10-27"
created: 2026-10-29
description: "When an LLM group's discussion is compressed into a short memory for a final decision maker, what should the memory keep? Two natural heuristics keep the rarest claims or the claims relevant to the decision criteria. On hidden-profile tasks both look attractive, because how widely a fact is held is confounded with whether it helps. We introduce CrossProfile, a diagnostic benchmark of 60 templates with automatically…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/benchmark
  - keyword/agents
---

# Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.37624v1)
- published:: 2026-10-27
- updated:: 2026-10-27
- arxiv_id:: 2610.37624v1
- pdf:: https://arxiv.org/pdf/2610.37624v1
- categories:: cs.AI, cs.CL, cs.MA, cs.SI

## Abstract / Summary
When an LLM group's discussion is compressed into a short memory for a final decision maker, what should the memory keep? Two natural heuristics keep the rarest claims or the claims relevant to the decision criteria. On hidden-profile tasks both look attractive, because how widely a fact is held is confounded with whether it helps. We introduce CrossProfile, a diagnostic benchmark of 60 templates with automatically verified answer keys, in which the ownership of supporting, decoy, and irrelevant facts is crossed while their text is held fixed (480 tasks). Across Qwen2.5-7B, Llama-3.1-8B, and two DeepSeek models, both heuristics fail in predictable places. Selecting by relevance readmits decoys, because decoys are on topic: even a perfect relevance filter loses 23 to 31 points to rarest-first selection in the classic hidden-profile configuration. Rarest-first selection is no better than random selection on average and wins only where the rare facts happen to be the useful ones. In both cases accuracy follows the balance of evidence the memory keeps, not the policy that kept it. The decision model adds a third failure, a form of social proof: it gives extra weight to facts attributed to many agents. Removing the attribution tags, or reassigning them at random with line order fixed, raises accuracy in the classic configuration by 13 to 24 points. In natural discussions the evidence is lost before any memory acts: the complete transcript yields lower accuracy than no notes at all.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.37624v1)
- [PDF](https://arxiv.org/pdf/2610.37624v1)
- [Do"True"and"False"Add Up to One? Complement Consistency in LLM-Agent Opinion Simulations](https://arxiv.org/abs/2610.32874) (2026, citations: 1)
- [Consilience: Conformally Calibrated Communication Control for Hidden-Profile Multi-Agent Reasoning](https://arxiv.org/abs/2608.20564) (2026, citations: 2)
- [GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations](https://arxiv.org/abs/2605.14498) (2026, citations: 20)
- [Evaluating Long-Horizon Memory for Multi-Party Collaborative Dialogues](https://arxiv.org/abs/2602.01313) (2026, citations: 25)
- [Systematic Failures in Collective Reasoning under Distributed Information in Multi-Agent LLMs](https://arxiv.org/abs/2505.11556) (2025, citations: 27)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/agents
