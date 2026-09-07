---
title: "Large Language Models for HVAC Operations in Building Energy Systems: A Critical Review of Methods, Applications, and Deployment Readiness"
source: "https://arxiv.org/html/2609.05314v1"
author: "Alexander Neubauer, Tianzhen Hong, Han Li, Mengbo Yu, Amin Darbandi, Yannick Fürst, Martin Kriegel"
published: "2026-09-04"
created: 2026-09-08
description: "Building automation systems generate rich sensor data yet remain insight-poor because heterogeneous point naming, missing metadata, and fragmented documentation obstruct their operational use. This systematic review analyses and codes 66 peer-reviewed studies on large language models (LLMs) for HVAC operations published between 2023 and March 2026. Each study is classified across five application families and three…"
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
  - keyword/safety
  - keyword/machine-learning
---

# Large Language Models for HVAC Operations in Building Energy Systems: A Critical Review of Methods, Applications, and Deployment Readiness

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.05314v1)
- published:: 2026-09-04
- updated:: 2026-09-04
- arxiv_id:: 2609.05314v1
- pdf:: https://arxiv.org/pdf/2609.05314v1
- categories:: cs.AI, cs.CL, eess.SY

## Abstract / Summary
Building automation systems generate rich sensor data yet remain insight-poor because heterogeneous point naming, missing metadata, and fragmented documentation obstruct their operational use. This systematic review analyses and codes 66 peer-reviewed studies on large language models (LLMs) for HVAC operations published between 2023 and March 2026. Each study is classified across five application families and three LLM method families and assessed for evidence realism, deployment readiness, and the responsibility boundary between the LLM and physical HVAC decisions. The corpus is concentrated in building energy modelling (BEM, 32 of 66 papers), while load forecasting remains too sparse for subfield-level conclusions. Only four studies reach pilot-level evidence, and none reports sustained operational deployment. No study was classified as ready-now for industry adoption; three were near-term and 63 research-only. Nevertheless, several bounded, human-in-the-loop uses merit near-term trials, including point-name normalisation, document-grounded operator support, BEM workflow assistance, and advisory interfaces around physics-based controllers. Conventional machine learning (ML), model predictive control (MPC), reinforcement learning (RL) and ontology-based tools remain more adopted for high-frequency control, short-horizon numerical forecasting, and well-posed ontology mapping, while autonomous agentic operation and unvalidated occupant proxies remain research-stage. Current evidence therefore supports LLMs primarily as semantic and workflow layers rather than autonomous HVAC controllers. Future work should prioritise field-validated benchmarks, orchestration evaluation under operational constraints, and LLM-MPC/RL architectures with bounded latency and verifiable safety…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.05314v1)
- [PDF](https://arxiv.org/pdf/2609.05314v1)
- [HeatShift-HP: A Techno-Economic Framework for Assessing Heat Pump Load Shifting under Dynamic Tariffs and Grid Fees](https://doi.org/10.1016/j.enbuild.2026.118164) (2026, citations: 1)
- [Large language model–driven building energy model generation](https://www.semanticscholar.org/paper/f609abb1a9390369886acd529c4a1331771f3f19) (2026, citations: 2)
- [MCP-enabled agentic AI workflow for building energy modelling: framework and use cases](https://doi.org/10.1080/19401493.2026.2653969) (2026, citations: 3)
- [Human-in-the-Loop: Integrating Virtual occupant behavior simulation and semantic Decision-Making for building energy efficiency](https://www.semanticscholar.org/paper/e3e373e70a09f59365013bf0efea8e2722c8a8b7) (2026, citations: 3)
- [Co-LLM: A retrieval-augmented language model framework for chiller optimization control](https://www.semanticscholar.org/paper/ab27959ed915390aedbca98fd2819c95d6797d7d) (2026, citations: 4)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/agents #keyword/safety #keyword/machine-learning
