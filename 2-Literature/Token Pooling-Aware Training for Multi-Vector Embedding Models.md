---
title: "Token Pooling-Aware Training for Multi-Vector Embedding Models"
source: "https://huggingface.co/blog/token-pooling"
author: "Hugging Face Blog"
published: "2026-11-11"
created: 2026-11-12
description: "Search models, datasets, users... Ctrl K Models Datasets Spaces Buckets Docs Enterprise Pricing Website Tasks HuggingChat Collections Languages Organizations Community Blog Posts Daily Papers Hardware Learn Discord Forum GitHub Solutions Team & Enterprise Hugging Face PRO Enterprise Support Inference Providers Inference Endpoints Storage Buckets Log In Sign Up Back to Articles a]:hidden'> Token Pooling-Aware Trainin…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/transformer
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/machine-learning
---

# Token Pooling-Aware Training for Multi-Vector Embedding Models

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/token-pooling)
- published:: 2026-11-11

## Abstract / Summary
Search models, datasets, users... Ctrl K Models Datasets Spaces Buckets Docs Enterprise Pricing Website Tasks HuggingChat Collections Languages Organizations Community Blog Posts Daily Papers Hardware Learn Discord Forum GitHub Solutions Team & Enterprise Hugging Face PRO Enterprise Support Inference Providers Inference Endpoints Storage Buckets Log In Sign Up Back to Articles a]:hidden"> Token Pooling-Aware Training for Multi-Vector Embedding Models Published November 11, 2026 Update on GitHub… Token pooling makes these representations smaller by merging similar token vectors. The more aggressively I compress them, however, the easier it becomes to lose something useful. Pooling-aware training teaches the encoder to preserve the information that matters when its vectors are merged, helping you retrieve better from the same storage budget. In this post, I'll explain how pooling works, train a model for compressed retrieval with Sentence Transformers, and explore the resulting quality and storage tradeoff. With pool_factor=4 , my normally trained model retains 94.6% of its unpooled NanoBEIR nDCG@10, with a 4x reduction in document vectors. Token pooling-aware training raises that r…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/transformer #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/machine-learning
