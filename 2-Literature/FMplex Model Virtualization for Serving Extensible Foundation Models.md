---
title: "FMplex: Model Virtualization for Serving Extensible Foundation Models"
source: "https://arxiv.org/html/2606.09643v1"
author: "Hetvi Shastri, Pragya Sharma, Walid A. Hanafy, David Irwin, Mani Srivastava, Prashant Shenoy"
published: "2026-06-08"
created: 2026-06-10
description: "Foundation models (FMs) are increasingly used as backbones for downstream tasks across language, vision, time-series, and multimodal applications. Yet existing model-serving systems deploy each customized task as an independent model instance, thereby replicating heavyweight backbones, wasting accelerator memory, and losing opportunities to amortize batching and loading costs. This paper presents FMplex, a serving s…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/ai
  - keyword/nlp
  - keyword/multimodal
  - keyword/research-paper
---

# FMplex: Model Virtualization for Serving Extensible Foundation Models

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.09643v1)
- published:: 2026-06-08
- updated:: 2026-06-08
- arxiv_id:: 2606.09643v1
- pdf:: https://arxiv.org/pdf/2606.09643v1
- categories:: cs.DC, cs.AI, cs.LG, cs.OS

## Abstract / Summary
Foundation models (FMs) are increasingly used as backbones for downstream tasks across language, vision, time-series, and multimodal applications. Yet existing model-serving systems deploy each customized task as an independent model instance, thereby replicating heavyweight backbones, wasting accelerator memory, and losing opportunities to amortize batching and loading costs. This paper presents FMplex, a serving system that treats FM backbones as a virtualization substrate for deployment sharing. FMplex presents each task with a virtual foundation model (vFM), a logically private FM instance backed by a shared physical FM. This abstraction lets independently customized tasks share a backbone while preserving task-specific extensions, independent lifecycles, and task-level isolation. In addition, we propose a batch-aware fair-queueing scheduler that combines weighted task-level sharing with inter- and intra-task batching across colocated tasks. We implement a FMplex-based serving stack spanning task construction, sharing-aware deployment, and runtime execution. Across 7 FM backbones (16 variants) and 92 downstream tasks, FMplex reduces latency by up to 80% over spatial partitioning and 33.3% over best-effort co-location, while hosting up to 6x more tasks at cluster scale.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.09643v1)
- [PDF](https://arxiv.org/pdf/2606.09643v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/ai #keyword/nlp #keyword/multimodal #keyword/research-paper
