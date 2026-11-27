---
title: "Enhancing Maritime Domain Awareness using Latent Space Representations"
source: "https://arxiv.org/html/2611.34899v1"
author: "Rikard Vinge, Miguel A. Belenguer-Plomer, Isabelle Wittmann, Octavian Dumitru, Michele Lazzarini, Sergio Albani, Conrad M Albrecht"
published: "2026-11-25"
created: 2026-11-28
description: "This work presents a novel application of Earth Observation (EO) embeddings for Maritime Domain Awareness (MDA) from the perspective of the geospatial foundation model TerraMind. By operating directly on compressed latent-space representations rather than on the original Sentinel-1 imagery, this approach directly addresses the data gravity bottleneck that increasingly constrains operational EO processing, in line wi…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/ai
  - keyword/evaluation
  - keyword/benchmark
---

# Enhancing Maritime Domain Awareness using Latent Space Representations

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.34899v1)
- published:: 2026-11-25
- updated:: 2026-11-25
- arxiv_id:: 2611.34899v1
- pdf:: https://arxiv.org/pdf/2611.34899v1
- categories:: cs.CV, cs.AI, cs.LG

## Abstract / Summary
This work presents a novel application of Earth Observation (EO) embeddings for Maritime Domain Awareness (MDA) from the perspective of the geospatial foundation model TerraMind. By operating directly on compressed latent-space representations rather than on the original Sentinel-1 imagery, this approach directly addresses the data gravity bottleneck that increasingly constrains operational EO processing, in line with the objectives of the Embed2Scale project. In particular, linear and non-linear probing of compressed embeddings, latent space representations of synthetic aperture radar (SAR) imagery, is used to detect, localise, and characterise vessels from Sentinel-1 GRD images. Vessel detection achieves a ROC-AUC of 0.95, while vessel localisation has a median error of around 300 m for vessels longer than 100 m, and vessel AIS type-code classification achieves 62% accuracy for the majority classes. The latter, however, is highly correlated with vessel length. These results reveal both the potential and current limitations of Geospatial Foundation Models (GeoFMs) when applied to fine-grained MDA understanding in real-world scenarios. Additionally, a new maritime remote sensing dataset is released, pairing about 2,000 Sentinel-1 images with temporally aligned AIS signals from commercial vessels. Through manual inspection, each candidate sample was verified for bounding-box quality and for consistency between the AIS-reported vessel length and the observed vessel extent, cross-checking vessel identity and location against publicly available vessel records and, where available, photographs. The dataset was made ready for use with the NeuCo-Bench neural compression benchmark framework, publicly available on HuggingFace through https://huggingface.co/datasets/embed2scale/…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.34899v1)
- [PDF](https://arxiv.org/pdf/2611.34899v1)
- [OSSDD - a New Open Dataset for Sentinel-1 Ship Detection](https://arxiv.org/abs/2608.01963) (2026, citations: 1)
- [Insights into deep learning-based vessel detection and characterization using SAR and AIS data](https://www.semanticscholar.org/paper/ac602e99fbd578a496b8dd5d0761375059b24b6c) (2025, citations: 1)
- [NeuCo-Bench: A Novel Benchmark Framework for Neural Embeddings in Earth Observation](https://arxiv.org/abs/2510.17914) (2025, citations: 10)
- [AlphaEarth Foundations: An embedding field model for accurate and efficient global mapping from sparse label data](https://arxiv.org/abs/2507.22291) (2025, citations: 349)
- [TESSERA: Temporal Embeddings of Surface Spectra for Earth Representation and Analysis](https://arxiv.org/abs/2506.20380) (2025, citations: 93)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/ai #keyword/evaluation #keyword/benchmark
