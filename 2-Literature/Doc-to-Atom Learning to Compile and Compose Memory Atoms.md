---
title: "Doc-to-Atom: Learning to Compile and Compose Memory Atoms"
source: "https://arxiv.org/html/2606.12400v1"
author: "Xingjian Diao, Wenbo Li, Yashas Malur Saidutta, Avinash Amballa, Lazar Valkov, Srinivas Chappidi"
published: "2026-06-10"
created: 2026-06-12
description: "Long input sequences are central to document understanding and multi-step reasoning in Large Language Models, yet the quadratic cost of attention makes inference both memory-intensive and slow. Context distillation mitigates this by compressing contextual information into model parameters, and recent work such as Doc-to-LoRA amortizes context distillation into a single forward pass that generates one LoRA adapter pe…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/benchmark
  - keyword/reasoning
  - keyword/machine-learning
---

# Doc-to-Atom: Learning to Compile and Compose Memory Atoms

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.12400v1)
- published:: 2026-06-10
- updated:: 2026-06-10
- arxiv_id:: 2606.12400v1
- pdf:: https://arxiv.org/pdf/2606.12400v1
- categories:: cs.CL, cs.IR

## Abstract / Summary
Long input sequences are central to document understanding and multi-step reasoning in Large Language Models, yet the quadratic cost of attention makes inference both memory-intensive and slow. Context distillation mitigates this by compressing contextual information into model parameters, and recent work such as Doc-to-LoRA amortizes context distillation into a single forward pass that generates one LoRA adapter per document. However, producing a single monolithic adapter for all queries leads to irrelevant-query interference, limited compositional recall, and poor scalability to long-document reasoning. To address these challenges, we propose Doc-to-Atom (Doc2Atom), a compositional parametric memory framework that decomposes each document into semantically typed knowledge atoms. Each atom is compiled into an independent micro-LoRA adapter and a provenance retrieval key. At inference time, a lightweight query router selects and assembles only the relevant atoms into a query-specific adapter, which is then injected into a frozen base model. The entire system is trained end-to-end through a multi-objective distillation framework. Experiments on six diverse QA benchmarks demonstrate that Doc2Atom outperforms Doc-to-LoRA baselines while reducing the memory cost of document internalization.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.12400v1)
- [PDF](https://arxiv.org/pdf/2606.12400v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/reasoning #keyword/machine-learning
