---
title: "Simulation-pretrained autoencoders versus PCA for compressing multimode fibre transmission matrices"
source: "https://arxiv.org/html/2611.26391v1"
author: "Callum J. Wilson, Terry Wright, Qing Yang, Zhong Wen, Michael P. Pound, George S. D. Gordon"
published: "2026-11-19"
created: 2026-11-23
description: "Multimode optical fibres can image through a thin, flexible probe once their transmission matrix (TM) has been measured, but a TM is large and must be re-measured whenever the fibre moves. A compact model of feasible TMs would make storing and re-estimating them cheaper, so we ask how compactly TMs can be represented, and from how few measured TMs. Here we benchmark a permutation-equivariant autoencoder, pretrained…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/evaluation
  - keyword/benchmark
---

# Simulation-pretrained autoencoders versus PCA for compressing multimode fibre transmission matrices

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.26391v1)
- published:: 2026-11-19
- updated:: 2026-11-19
- arxiv_id:: 2611.26391v1
- pdf:: https://arxiv.org/pdf/2611.26391v1
- categories:: physics.optics, cs.LG

## Abstract / Summary
Multimode optical fibres can image through a thin, flexible probe once their transmission matrix (TM) has been measured, but a TM is large and must be re-measured whenever the fibre moves. A compact model of feasible TMs would make storing and re-estimating them cheaper, so we ask how compactly TMs can be represented, and from how few measured TMs. Here we benchmark a permutation-equivariant autoencoder, pretrained on simulated fibres and adapted to measured TMs, against principal component analysis (PCA). At 62x compression, adapting the pretrained autoencoder with just two measured TMs reconstructs the TM of a 50um fibre well enough to focus light at 98% of the ideal enhancement, and it stays accurate when the TMs are shifted by 25 pixels or zoomed by 10%, which quickly degrades a linear basis. It is not, however, a better compressor: PCA is about ten times more accurate when fitted on all 163 real TMs (1.1% against 11.9% error on held-out TMs) and is already more accurate from ten. The autoencoder's value is as a prior when few or no real TMs exist: with none it reaches 29% error, against 91% for PCA fitted on the same simulation. Transfer to a different fibre is only partial. The most important extension, not yet tested, is to recover pixel-basis TMs from fewer measurements than a full TM, which would turn the pretrained prior from a compressor into a measurement-saving tool.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.26391v1)
- [PDF](https://arxiv.org/pdf/2611.26391v1)
- [Adaptive wavefront shaping through flexible multicore photonic lantern fibres](https://arxiv.org/abs/2611.10290) (2026, citations: 1)
- [Physics-informed diffusion enables high-fidelity multimode fiber imaging under dynamic perturbations](https://doi.org/10.1038/s42005-026-02728-y) (2026, citations: 1)
- [Using physics-informed AI to enable fibre TM recovery from minimal partial measurements enabling ultra-thin endoscopes](https://www.semanticscholar.org/paper/85420e7ea2cb17a7a4960ceb8218b01c079909e1) (2026, citations: 3)
- [Real-valued intensity transmission matrix-based multimode fibre beamshaping for biophotonics applications](https://doi.org/10.1364/ol.603130) (2025, citations: 1)
- [Adapting the ChatGPT architecture for efficient AI representation and modelling of optical fibre transmission matrices](https://www.semanticscholar.org/paper/da6846dd2299a8180e15dfc6f9eb41cc525a8d40) (2025, citations: 1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/evaluation #keyword/benchmark
