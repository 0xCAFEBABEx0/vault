---
title: "GoiBERT: Compact Vietnamese Language Models via Two-Stage Knowledge Distillation"
source: "https://arxiv.org/html/2610.30067v1"
author: "Quang Anh Kiet Tran, Nam Anh Tran, Manh Hung Trinh, Thanh Danh Le, Khang Nhat Hoang Vo, Huynh Dai Nhan Tran"
published: "2026-10-21"
created: 2026-10-23
description: "Vietnamese pre-trained encoders have improved rapidly, but the strongest ones are large, multilingual-vocabulary models or depend on external word segmentation, which makes them costly to deploy. We present GoiBERT, a family of two compact Vietnamese encoders with 26M and 49M parameters that operate directly on raw text. GoiBERT learns from two complementary teachers. A same-tokenizer Vietnamese encoder first teache…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/benchmark
  - keyword/machine-learning
---

# GoiBERT: Compact Vietnamese Language Models via Two-Stage Knowledge Distillation

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.30067v1)
- published:: 2026-10-21
- updated:: 2026-10-21
- arxiv_id:: 2610.30067v1
- pdf:: https://arxiv.org/pdf/2610.30067v1
- categories:: cs.CL

## Abstract / Summary
Vietnamese pre-trained encoders have improved rapidly, but the strongest ones are large, multilingual-vocabulary models or depend on external word segmentation, which makes them costly to deploy. We present GoiBERT, a family of two compact Vietnamese encoders with 26M and 49M parameters that operate directly on raw text. GoiBERT learns from two complementary teachers. A same-tokenizer Vietnamese encoder first teaches general-purpose representations. A much larger teacher then provides task-level guidance through soft labels that are generated without ever labeling its own training data. Across eight benchmarks covering text classification, aspect-based sentiment analysis, natural language inference, and named entity recognition, GoiBERT-large achieves the highest average score among non-teacher models. It does so with fewer than half the parameters of the strongest compact baseline and twice its throughput. GoiBERT-base retains 99% of that baseline's performance at a quarter of its size. Our analysis shows that compression is nearly lossless for sentiment and classification tasks but remains costly for inference and entity recognition, which points to clear directions for future work. Our code and models are available at: https://github.com/Nhantran65/GoiBERT.git

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.30067v1)
- [PDF](https://arxiv.org/pdf/2610.30067v1)
- [BamiBERT: A New BERT-based Language Model for Vietnamese](https://arxiv.org/abs/2607.02259) (2026, citations: 1)
- [Extracting General-use Transformers for Low-resource Languages via Knowledge Distillation](https://arxiv.org/abs/2501.12660) (2025, citations: 4)
- [Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference](https://arxiv.org/abs/2412.13663) (2024, citations: 944)
- [Towards Cross-Tokenizer Distillation: the Universal Logit Distillation Loss for LLMs](https://arxiv.org/abs/2402.12030) (2024, citations: 77)
- [Weight subcloning: direct initialization of transformers using larger pretrained ones](https://arxiv.org/abs/2312.09299) (2023, citations: 40)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/machine-learning
