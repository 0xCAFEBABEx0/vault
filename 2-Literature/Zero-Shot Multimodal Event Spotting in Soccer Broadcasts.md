---
title: "Zero-Shot Multimodal Event Spotting in Soccer Broadcasts"
source: "https://arxiv.org/html/2610.37583v1"
author: "Sadia Kamal, Mahmudul Hasan, Tony Braskich"
published: "2026-10-27"
created: 2026-10-30
description: "Automatic soccer event spotting supports highlight generation, video indexing, and sports analytics, but existing methods depend on large annotated datasets and soccer-specific training. We present a zero-shot framework that detects, classifies, and temporally localizes events in full-length soccer broadcasts without task-specific parameter training. Each match is segmented into overlapping clips represented by a co…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/nlp
  - keyword/multimodal
  - keyword/machine-learning
---

# Zero-Shot Multimodal Event Spotting in Soccer Broadcasts

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.37583v1)
- published:: 2026-10-27
- updated:: 2026-10-27
- arxiv_id:: 2610.37583v1
- pdf:: https://arxiv.org/pdf/2610.37583v1
- categories:: cs.CV, cs.LG, cs.MM

## Abstract / Summary
Automatic soccer event spotting supports highlight generation, video indexing, and sports analytics, but existing methods depend on large annotated datasets and soccer-specific training. We present a zero-shot framework that detects, classifies, and temporally localizes events in full-length soccer broadcasts without task-specific parameter training. Each match is segmented into overlapping clips represented by a compact visual storyboard and the aligned commentary transcript, which a general-purpose multimodal model processes jointly. On three manually annotated matches containing 130 events, the best configuration achieves 72.0% F1@5s and outperforms SoccerNet-trained CALF and NetVLAD++ in a cross-dataset setting, while the storyboard representation reduces inference cost by 72% compared with individual frames. We further analyze the effects of model family, input representation, and prompt optimization, and introduce an evidence-grounded excitement-scoring stage that ranks detected events with natural-language explanations for highlight selection.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.37583v1)
- [PDF](https://arxiv.org/pdf/2610.37583v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/nlp #keyword/multimodal #keyword/machine-learning
