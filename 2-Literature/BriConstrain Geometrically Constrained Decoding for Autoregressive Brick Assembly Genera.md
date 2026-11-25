---
title: "BriConstrain: Geometrically Constrained Decoding for Autoregressive Brick Assembly Generation"
source: "https://arxiv.org/html/2611.33135v1"
author: "Nadav Magar, Amir Hertz, Ariel Shamir, Or Patashnik"
published: "2026-11-24"
created: 2026-11-26
description: "Language models can generate LEGO$^\circledR$ assemblies from text, but their builds often contain parts that collide or attach to nothing. The usual approach of rejecting and resampling invalid placements discards decoded tokens without guaranteeing a valid build. We present BriConstrain, a constrained decoding method that restricts a pretrained language model's next-token probabilities before sampling, steering it…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/machine-learning
---

# BriConstrain: Geometrically Constrained Decoding for Autoregressive Brick Assembly Generation

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.33135v1)
- published:: 2026-11-24
- updated:: 2026-11-24
- arxiv_id:: 2611.33135v1
- pdf:: https://arxiv.org/pdf/2611.33135v1
- categories:: cs.CV, cs.CL

## Abstract / Summary
Language models can generate LEGO$^\circledR$ assemblies from text, but their builds often contain parts that collide or attach to nothing. The usual approach of rejecting and resampling invalid placements discards decoded tokens without guaranteeing a valid build. We present BriConstrain, a constrained decoding method that restricts a pretrained language model's next-token probabilities before sampling, steering it towards valid placements. Because the validity of a brick placement depends on the non-predetermined build state, it cannot be compiled into a fixed grammar and must be checked dynamically. However, checking the validity of a brick before sampling is challenging as the space of valid placements is combinatorially large and cannot be enumerated exhaustively. Our key idea is to narrow the search space by constraining how parts attach rather than which parts attach to each other. Concretely, given the model's predictions of the currently placed part, and the previously placed parent it wants to connect to, we constrain the model's choice of how they attach. This allows us to span the space of part attachments, using a precomputed geometric oracle, and to effectively filter out colliding options. With valid attachment candidates in hand, we bias the model's next-token distribution towards the remaining valid candidates. We evaluate our method on two LEGO$^\circledR$ formats and models: BrickNet, which annotates connectivity explicitly, and our proposed Implicit Connectivity LDraw Format (ICLF), which uses numeric values for placements and leaves connectivity implicit. Our method raises collision-free builds from 31% to 91% on BrickNet and from 15% to 65% on ICLF, and outperforms rejection sampling on both formats at about 60% of its decoding cost.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.33135v1)
- [PDF](https://arxiv.org/pdf/2611.33135v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/machine-learning
