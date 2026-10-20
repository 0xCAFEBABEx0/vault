---
title: "LatComm: Reusable Context Compression for Latent Communication between Large Language Models"
source: "https://arxiv.org/html/2610.26840v1"
author: "Huawei Lin, Jinting Liu, Tan Yu, Weijie Zhao"
published: "2026-10-19"
created: 2026-10-21
description: "Systems that combine several large language models (LLMs) often use one context for many questions. When the context is passed between models as text, the receiving model processes all of its tokens again for every question. Avoiding this cost requires a context representation that is compact, reusable across questions, and readable by a different LLM. Existing compression and latent communication methods each provi…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
---

# LatComm: Reusable Context Compression for Latent Communication between Large Language Models

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.26840v1)
- published:: 2026-10-19
- updated:: 2026-10-19
- arxiv_id:: 2610.26840v1
- pdf:: https://arxiv.org/pdf/2610.26840v1
- categories:: cs.CL, cs.AI

## Abstract / Summary
Systems that combine several large language models (LLMs) often use one context for many questions. When the context is passed between models as text, the receiving model processes all of its tokens again for every question. Avoiding this cost requires a context representation that is compact, reusable across questions, and readable by a different LLM. Existing compression and latent communication methods each provide only some of these properties. We introduce LatComm, a Latent Communication interface that provides all three by separating encoding from reading: the context is encoded once without the question, and the receiver selects what to read for each question. A frozen context encoder LLM compresses the context into a fixed-size packet and sends it to a different frozen receiver LLM, which reads the packet through cross-attention, with gates computed from its prompt. On 12 multiple-choice question-answering datasets, LatComm improves average accuracy over single-vector baselines by up to 10.2 points. On QuALITY, it reduces the receiver's input by 57x and answers the questions of an article 3x faster.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.26840v1)
- [PDF](https://arxiv.org/pdf/2610.26840v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp #keyword/retrieval
