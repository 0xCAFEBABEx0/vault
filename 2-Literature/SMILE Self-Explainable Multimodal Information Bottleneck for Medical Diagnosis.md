---
title: "SMILE: Self-Explainable Multimodal Information Bottleneck for Medical Diagnosis"
source: "https://arxiv.org/html/2609.05174v1"
author: "Yuqing Yang, Alexander Schmatz, Zhaozhao Ma, Changkyu Choi, Robert Jenssen, Shujian Yu"
published: "2026-09-04"
created: 2026-09-09
description: "Explainability is increasingly seen as a crucial requirement in AI-based medical diagnosis, particularly in safety-critical clinical decision-making. Most existing explainability methods in healthcare operate in a post-hoc manner and are predominantly designed for unimodal data, which limits their applicability in increasingly prevalent multimodal diagnostic settings. This paper addresses the problem of self-explain…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/multimodal
  - keyword/evaluation
  - keyword/safety
  - keyword/research-paper
---

# SMILE: Self-Explainable Multimodal Information Bottleneck for Medical Diagnosis

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.05174v1)
- published:: 2026-09-04
- updated:: 2026-09-04
- arxiv_id:: 2609.05174v1
- pdf:: https://arxiv.org/pdf/2609.05174v1
- categories:: cs.CV, cs.LG

## Abstract / Summary
Explainability is increasingly seen as a crucial requirement in AI-based medical diagnosis, particularly in safety-critical clinical decision-making. Most existing explainability methods in healthcare operate in a post-hoc manner and are predominantly designed for unimodal data, which limits their applicability in increasingly prevalent multimodal diagnostic settings. This paper addresses the problem of self-explainable multimodal diagnosis by formulating it within the information bottleneck (IB) framework. We propose a unified learning paradigm that jointly optimizes predictive performance and modality-specific explainability by identifying the most informative elements inside each modality that contribute to diagnostic decisions. To enable tractable and stable optimization, we employ a matrix-based Renyi's $α$-order entropy functional under the assumption of sufficiently expressive encoders. Extensive experiments on representative medical datasets spanning heterogeneous modalities demonstrate that the proposed method consistently achieves strong diagnostic performance, including an absolute accuracy improvement of 9.1 percentage points on the iCTCF dataset. Moreover, the learned explanations provide transparent and modality-aware insights into feature relevance, thereby improving both the explainability and generalization.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.05174v1)
- [PDF](https://arxiv.org/pdf/2609.05174v1)
- [Vertex-wise cortical abnormalities in major depressive disorder from 64 cohorts from the DIRECT and ENIGMA MDD consortia](https://www.semanticscholar.org/paper/de1fc0570f549f901afdba690b44f299ecd3ceda) (2026, citations: 2)
- [Learning Optimal Multimodal Information Bottleneck Representations](https://arxiv.org/abs/2505.19996) (2025, citations: 14)
- [Measuring Cross-Modal Interactions in Multimodal Models](https://arxiv.org/abs/2412.15828) (2024, citations: 20)
- [Self-eXplainable AI for Medical Image Analysis: A Survey and New Outlooks](https://arxiv.org/abs/2410.02331) (2024, citations: 50)
- [G-Protein Signaling in Alzheimer's Disease: Spatial Expression Validation of Semi-supervised Deep Learning-Based Computational Framework](https://www.semanticscholar.org/paper/3899695d14adffab8f0088f6088bb89dd7dc078e) (2024, citations: 4)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/multimodal #keyword/evaluation #keyword/safety #keyword/research-paper
