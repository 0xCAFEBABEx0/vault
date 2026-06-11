---
title: "DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model"
source: "https://arxiv.org/html/2606.12105v1"
author: "Pankhuri Vanjani, Zhuoyue Li, Jakub Suliga, Moritz Reuss, Gianluca Geraci, Xinkai Jiang, Rudolf Lioutikov"
published: "2026-06-10"
created: 2026-06-12
description: "Vision-language-action (VLA) models inherit a shared synchronous clock from vision-language pretraining, processing every input at one rate. This is misaligned with physical interaction, where a high-frequency modality changes at hundreds of hertz, vision evolves more slowly, and language stays constant across an episode. A synchronous VLA oversamples slow modalities, undersamples fast ones, and caps action generati…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/nlp
  - keyword/multimodal
  - keyword/retrieval
  - keyword/machine-learning
---

# DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.12105v1)
- published:: 2026-06-10
- updated:: 2026-06-10
- arxiv_id:: 2606.12105v1
- pdf:: https://arxiv.org/pdf/2606.12105v1
- categories:: cs.RO, cs.CV, cs.LG

## Abstract / Summary
Vision-language-action (VLA) models inherit a shared synchronous clock from vision-language pretraining, processing every input at one rate. This is misaligned with physical interaction, where a high-frequency modality changes at hundreds of hertz, vision evolves more slowly, and language stays constant across an episode. A synchronous VLA oversamples slow modalities, undersamples fast ones, and caps action generation at the lowest effective frequency. We hypothesize that decoupling temporal processing per modality, letting each update and retain information at its own sensor rate, yields stronger representations and more robust control. We present DAM-VLA, which maintains per-modality latent buffers refreshed at sensor rates and read continuously by the action head, integrating new high-frequency modalities through gated cross-attention that leaves the pretrained backbone intact. Across seven contact-rich real-world manipulation tasks, DAM-VLA more than doubles the average success rate of the strongest synchronous baseline (95.2\% vs.\ 40.95\%) while sustaining smooth, reactive 100\,Hz control. Project website: \href{https://intuitive-robots.github.io/DAM-VLA/}{intuitive-robots.github.io/DAM-VLA/}

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.12105v1)
- [PDF](https://arxiv.org/pdf/2606.12105v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/nlp #keyword/multimodal #keyword/retrieval #keyword/machine-learning
