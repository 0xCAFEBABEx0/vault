---
title: "Atlas H&E-TME: Scalable AI-Based Tissue Profiling at Expert Pathologist-Level Accuracy"
source: "https://arxiv.org/html/2606.12346v1"
author: "Kai Standvoss, Miriam Hägele, Rosemarie Krupar, Julika Ribbat-Idel, Jennifer Altschüler, Gerrit Erdmann, Hans Pinckaers, Evelyn Ramberger, Madleen Drinkwitz, Ádám Nárai, Alexander Möllers, Katja Lingelbach, Sebastian Kons, Lukas Hönig, Recepcan Adigüzel, Joana Baião, Alberto Megina Gonzalo, Marius Teodorescu, Marie-Lisa Eich, Paolo Chetta, Shakil Merchant,…"
published: "2026-06-10"
created: 2026-06-12
description: "Hematoxylin and eosin (H&E) staining is the cornerstone of histopathology, yet scalable, quantitative analysis of H&E whole-slide images (WSIs) remains a central challenge in computational pathology. We present Atlas H&E-TME, an AI-based system built on the Atlas family of pathology foundation models that predicts tissue quality, tissue region, and cell type labels across multiple cancer types, yielding over 4,500 q…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/ai
  - keyword/evaluation
  - keyword/benchmark
---

# Atlas H&E-TME: Scalable AI-Based Tissue Profiling at Expert Pathologist-Level Accuracy

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.12346v1)
- published:: 2026-06-10
- updated:: 2026-06-10
- arxiv_id:: 2606.12346v1
- pdf:: https://arxiv.org/pdf/2606.12346v1
- categories:: cs.CV, cs.AI, cs.LG

## Abstract / Summary
Hematoxylin and eosin (H&E) staining is the cornerstone of histopathology, yet scalable, quantitative analysis of H&E whole-slide images (WSIs) remains a central challenge in computational pathology. We present Atlas H&E-TME, an AI-based system built on the Atlas family of pathology foundation models that predicts tissue quality, tissue region, and cell type labels across multiple cancer types, yielding over 4,500 quantitative readouts per slide at cell-level resolution. A key challenge to validating such systems is overcoming morphological ambiguity inherent to H&E-only ground truth and the limited scalability of more informed references drawing on modalities such as immunohistochemistry (IHC). We address this with a dual validation framework combining biologically grounded depth with technical and morphological breadth. For depth, we propose an IHC-informed multi-pathologist consensus protocol that substantially improves inter-rater agreement over conventional H&E-only annotation. This yields a molecularly grounded reference against which we compare Atlas H&E-TME and pathologists working from H&E alone. For breadth, we benchmark Atlas H&E-TME on over 200,000 high-confidence H&E-only pathologist annotations across 1,500+ cases spanning eight cancer types and their most common metastatic sites, with subtypes covering >90% of clinical cases per cancer type, drawn from 25+ sources and 8+ scanner models. Benchmarked against the IHC-informed consensus, Atlas H&E-TME matches or exceeds pathologist H&E-only performance and generalizes consistently and robustly across this broad morphological and technical scope. In doing so, Atlas H&E-TME turns the H&E slide -- the most ubiquitous data in pathology -- into a scalable, quantitative window into the tumor and its microenvironme…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.12346v1)
- [PDF](https://arxiv.org/pdf/2606.12346v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/ai #keyword/evaluation #keyword/benchmark
