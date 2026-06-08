---
title: "TEVI: Text-Conditioned Editing of Visual Representations via Sparse Autoencoders for Improved Vision-Language Alignment"
source: "https://arxiv.org/html/2606.07451v1"
author: "Sweta Mahajan, Sukrut Rao, Jiahao Xie, Alexander Koller, Bernt Schiele"
published: "2026-06-05"
created: 2026-06-09
description: "Vision-language models such as CLIP are highly useful for diverse tasks due to their shared image-text embedding space. Despite this, the image and text embeddings are often poorly aligned, affecting downstream performance. Recent work has shown that this can be attributed to an information imbalance: images contain more information than their captions describe. In this work, we propose TEVI, a framework that uses c…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/multimodal
  - keyword/retrieval
  - keyword/evaluation
  - keyword/benchmark
  - keyword/safety
---

# TEVI: Text-Conditioned Editing of Visual Representations via Sparse Autoencoders for Improved Vision-Language Alignment

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.07451v1)
- published:: 2026-06-05
- updated:: 2026-06-05
- arxiv_id:: 2606.07451v1
- pdf:: https://arxiv.org/pdf/2606.07451v1
- categories:: cs.CV, cs.AI, cs.CL, cs.LG

## Abstract / Summary
Vision-language models such as CLIP are highly useful for diverse tasks due to their shared image-text embedding space. Despite this, the image and text embeddings are often poorly aligned, affecting downstream performance. Recent work has shown that this can be attributed to an information imbalance: images contain more information than their captions describe. In this work, we propose TEVI, a framework that uses captions as a signal for what to retain from image embeddings. Specifically, we use sparse autoencoders to disentangle image embeddings and train a masking module to selectively reconstruct the embedding based on a given caption. In a controlled setup with synthetic captions, we show that TEVI is effective at preserving caption-described attributes while discarding others. By applying TEVI to CLIP models trained on natural images, we further achieve improved retrieval performance across coarse-grained short-caption (MS COCO, Flickr) and fine-grained long-caption (IIW, DOCCI) benchmarks, with stronger gains on richer captions, and improved robustness on the RoCOCO benchmark.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.07451v1)
- [PDF](https://arxiv.org/pdf/2606.07451v1)
- [SmartCLIP: Modular Vision-language Alignment with Identification Guarantees](https://arxiv.org/abs/2507.22264) (2025, citations: 12)
- [FG-CLIP: Fine-Grained Visual and Textual Alignment](https://arxiv.org/abs/2505.05071) (2025, citations: 82)
- [FineLIP: Extending CLIP’s Reach via Fine-Grained Alignment with Longer Text Inputs](https://arxiv.org/abs/2504.01916) (2025, citations: 28)
- [Learning Multi-Level Features with Matryoshka Sparse Autoencoders](https://arxiv.org/abs/2503.17547) (2025, citations: 103)
- [Interpreting CLIP with Hierarchical Sparse Autoencoders](https://arxiv.org/abs/2502.20578) (2025, citations: 37)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/multimodal #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/safety
