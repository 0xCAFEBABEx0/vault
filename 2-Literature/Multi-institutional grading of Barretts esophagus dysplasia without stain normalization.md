---
title: "Multi-institutional grading of Barrett's esophagus dysplasia without stain normalization using a pathology foundation model and multiple instance learning"
source: "https://arxiv.org/html/2611.26562v1"
author: "Amirali Khosravi, Jaidip M. Jagtap, D. Chamil Codipilly, Catherine E. Hagen, Jason T. Lewis, Rickey E. Carter, Shahriar Faghani, Vani J. A. Konda, Fouad Otaki, Shajan Peter, Nicholas Shaheen, Sachin Wani, Prasad G. Iyer, Bradley J. Erickson"
published: "2026-11-19"
created: 2026-11-22
description: "Barrett's esophagus dysplasia grading suffers substantial inter-observer variability, particularly for low-grade dysplasia, complicating clinical decision-making. We conducted a retrospective multi-institutional diagnostic accuracy study of a foundation model-based deep learning system for dysplasia grading, using 969 H\&E-stained whole slide images from four institutions. Patch-level classifiers trained on expert a…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/ai
  - keyword/retrieval
---

# Multi-institutional grading of Barrett's esophagus dysplasia without stain normalization using a pathology foundation model and multiple instance learning

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.26562v1)
- published:: 2026-11-19
- updated:: 2026-11-19
- arxiv_id:: 2611.26562v1
- pdf:: https://arxiv.org/pdf/2611.26562v1
- categories:: cs.CV, cs.AI

## Abstract / Summary
Barrett's esophagus dysplasia grading suffers substantial inter-observer variability, particularly for low-grade dysplasia, complicating clinical decision-making. We conducted a retrospective multi-institutional diagnostic accuracy study of a foundation model-based deep learning system for dysplasia grading, using 969 H\&E-stained whole slide images from four institutions. Patch-level classifiers trained on expert annotations identified diagnostically relevant regions, followed by attribute-aware multiple instance learning for slide-level classification as non-dysplastic Barrett's esophagus (NDBE), low-grade dysplasia, or high-grade dysplasia. On a held-out test set (n = 130), macro-averaged AUC was 0.96 (95\% CI 0.93--0.98). For binary dysplasia detection, sensitivity was 98\% (80/82) and specificity 81\% (39/48), with a negative likelihood ratio of 0.030 and quadratic-weighted \kap{} of 0.83 against expert consensus. No high-grade dysplasia case was misclassified as NDBE. Performance was consistent across institutions without stain normalization, indicating that stain-robust foundation-model representations may remove the site-specific preprocessing that has constrained prior systems to institution-specific deployment.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.26562v1)
- [PDF](https://arxiv.org/pdf/2611.26562v1)
- [Computing lifetime incidence of esophageal adenocarcinoma and age-specific prevalence of Barrett’s esophagus](https://academic.oup.com/dote/article-pdf/38/3/doaf038/63217018/doaf038.pdf) (2025, citations: 7)
- [AttriMIL: Revisiting attention-based multiple instance learning for whole-slide pathological image classification from a perspective of instance attributes](https://doi.org/10.1016/j.media.2025.103631) (2025, citations: 41)
- [Deep Learning Model for Histologic Diagnosis of Dysplastic Barrett’s Esophagus: Multisite Cohort External Validation](https://pmc.ncbi.nlm.nih.gov/articles/PMC12353133/) (2025, citations: 3)
- [Training state-of-the-art pathology foundation models with orders of magnitude less data](https://arxiv.org/abs/2504.05186) (2025, citations: 46)
- [When multiple instance learning meets foundation models: Advancing histological whole slide image analysis](https://www.researchsquare.com/article/rs-4704418/latest.pdf) (2025, citations: 40)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/ai #keyword/retrieval
