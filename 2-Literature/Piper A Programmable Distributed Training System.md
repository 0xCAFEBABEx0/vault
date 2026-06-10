---
title: "Piper: A Programmable Distributed Training System"
source: "https://arxiv.org/html/2606.11169v1"
author: "Megan Frisella, Shubham Tiwari, Andy Ruan, Yi Pan, Parker Gustafson, Mat Jacob, Gilbert Bernstein, Stephanie Wang"
published: "2026-06-09"
created: 2026-06-11
description: "Large-scale model training increasingly relies on composing multiple parallelism strategies, such as data, pipeline, and expert parallelism, together with memory-saving optimizations like ZeRO. Deployed systems for foundation model pretraining often rely on human experts to manually design a high-level parallelism strategy then implement the corresponding low-level execution strategy, making it difficult to adapt th…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/ai
  - keyword/machine-learning
---

# Piper: A Programmable Distributed Training System

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.11169v1)
- published:: 2026-06-09
- updated:: 2026-06-09
- arxiv_id:: 2606.11169v1
- pdf:: https://arxiv.org/pdf/2606.11169v1
- categories:: cs.DC, cs.AI

## Abstract / Summary
Large-scale model training increasingly relies on composing multiple parallelism strategies, such as data, pipeline, and expert parallelism, together with memory-saving optimizations like ZeRO. Deployed systems for foundation model pretraining often rely on human experts to manually design a high-level parallelism strategy then implement the corresponding low-level execution strategy, making it difficult to adapt the system to new strategies. Meanwhile, many general-purpose frameworks are more flexible but their implementations are still tied to a fixed set of common parallelism strategies, making it challenging to integrate state-of-the-art strategies. We present Piper, a user-controllable distributed training system that decouples the strategy from the runtime implementation. Piper allows users to declare a comprehensive distributed training strategy with a small set of model annotations and scheduling directives. Each directive applies a transformation on Piper's intermediate representation (IR), a unified global training DAG that represents all computation and communication. Using this IR, Piper compiles per-device execution plans and executes them with a distributed runtime agnostic to the strategy. We show that the combined system maintains performance parity on commonly available strategies such as ZeRO, while also enabling additional performance and memory efficiency gains through joint scheduling of compute and communication in composed parallelism strategies such as DeepSeek-V3's DualPipe.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.11169v1)
- [PDF](https://arxiv.org/pdf/2606.11169v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/ai #keyword/machine-learning
