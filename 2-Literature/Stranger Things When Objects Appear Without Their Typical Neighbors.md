---
title: "Stranger Things: When Objects Appear Without Their Typical Neighbors"
source: "https://arxiv.org/html/2611.34881v1"
author: "Siddhartha Gairola, Jiahao Xie, Anna Kukleva, Francesco Locatello, Bernt Schiele"
published: "2026-11-25"
created: 2026-11-28
description: "Visual context is a powerful cue for object recognition: scenes inform what, where, and at what scale objects are likely to appear. Yet over-reliance on context becomes a failure mode when models predict objects based on their typical neighbors rather than the objects' own visual features, which we call typicality bias. While extensively studied in the pre-Transformer era, it has often been assumed that architectura…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/nlp
  - keyword/multimodal
  - keyword/evaluation
  - keyword/benchmark
  - keyword/machine-learning
---

# Stranger Things: When Objects Appear Without Their Typical Neighbors

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.34881v1)
- published:: 2026-11-25
- updated:: 2026-11-25
- arxiv_id:: 2611.34881v1
- pdf:: https://arxiv.org/pdf/2611.34881v1
- categories:: cs.CV, cs.LG

## Abstract / Summary
Visual context is a powerful cue for object recognition: scenes inform what, where, and at what scale objects are likely to appear. Yet over-reliance on context becomes a failure mode when models predict objects based on their typical neighbors rather than the objects' own visual features, which we call typicality bias. While extensively studied in the pre-Transformer era, it has often been assumed that architectural and scale improvements would naturally solve it, and a systematic diagnostic across the modern vision stack remains absent. We provide such a diagnostic framework. We measure typicality bias via normalized pointwise mutual information (NPMI) over object pairs, and introduce STRANGE-Bench (Synthetic Typicality-RANked Grounded Evaluation Benchmark): a photorealistic, layout-controlled benchmark spanning 17 sub-tiers from typical to never-co-occurring object pairs. Across five model families (specialist detectors, open-vocabulary detectors, self-supervised, vision-language, and multimodal large language models) and three recognition tasks (supervised detection, open-vocabulary detection, and classification), the bias is prevalent: gaps of 5-11 p.p. persist when objects appear outside their typical company, and do not consistently shrink with scale. To mitigate it, we turn to data augmentation: existing augmentations are designed for visual diversity, not for breaking co-occurrence shortcuts, and sample from the very distribution that produces typicality bias. We propose Anchor-Atypicality Sampling (AAS), a simple sampling rule for paste-based augmentations that uses the NPMI signal to tilt the training-time co-occurrence distribution toward atypical partners. AAS reduces the typicality gap by up to 1.6 p.p. on natural-image COCO splits and 23.0 p.p. on synthe…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.34881v1)
- [PDF](https://arxiv.org/pdf/2611.34881v1)
- [Why Can't I Open My Drawer? Mitigating Object-Driven Shortcuts in Zero-Shot Compositional Action Recognition](https://arxiv.org/abs/2601.16211) (2026, citations: 3)
- [SAM 3: Segment Anything with Concepts](https://arxiv.org/abs/2511.16719) (2025, citations: 1714)
- [DINOv3](https://arxiv.org/abs/2508.10104) (2025, citations: 2140)
- [CNS-Bench: Benchmarking Image Classifier Robustness Under Continuous Nuisance Shifts](https://arxiv.org/abs/2507.17651) (2025, citations: 7)
- [Common Objects Out of Context (COOCo): Investigating Multimodal Context and Semantic Scene Violations in Referential Communication](https://arxiv.org/abs/2506.22274) (2025, citations: 3)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp #keyword/multimodal #keyword/evaluation #keyword/benchmark #keyword/machine-learning
