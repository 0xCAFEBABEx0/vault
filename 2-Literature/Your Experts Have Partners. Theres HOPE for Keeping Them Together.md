---
title: "Your Experts Have Partners. There's HOPE for Keeping Them Together"
source: "https://huggingface.co/blog/amazon/higher-order-pruning-experts"
author: "Hugging Face Blog"
published: "2026-11-09"
created: 2026-11-10
description: "Search models, datasets, users... Ctrl K Models Datasets Spaces Buckets Docs Enterprise Pricing Website Tasks HuggingChat Collections Languages Organizations Community Blog Posts Daily Papers Hardware Learn Discord Forum GitHub Solutions Team & Enterprise Hugging Face PRO Enterprise Support Inference Providers Inference Endpoints Storage Buckets Log In Sign Up Back to Articles a]:hidden'> Your Experts Have Partners.…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/nlp
  - keyword/retrieval
  - keyword/machine-learning
---

# Your Experts Have Partners. There's HOPE for Keeping Them Together

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/amazon/higher-order-pruning-experts)
- published:: 2026-11-09

## Abstract / Summary
Search models, datasets, users... Ctrl K Models Datasets Spaces Buckets Docs Enterprise Pricing Website Tasks HuggingChat Collections Languages Organizations Community Blog Posts Daily Papers Hardware Learn Discord Forum GitHub Solutions Team & Enterprise Hugging Face PRO Enterprise Support Inference Providers Inference Endpoints Storage Buckets Log In Sign Up Back to Articles a]:hidden"> Your Experts Have Partners. There's HOPE for Keeping Them Together Enterprise Article Published November 9,… Expert pruning is one of the most direct fixes to this memory bottleneck. That is, permanently delete the least useful experts. Pruning avoids the latency issues which make dynamic loading/off-loading of experts impractical; it does not require any training; and it composes with quantization . Given these attractive benefits and the simplicity of the idea, it's easy to see why expert pruning has become a go-to approach for shrinking MoEs. The difficulty lies in deciding which experts are safest… Existing pruning methods score each expert independently, assigning every expert a scalar importance score (based on a calibration dataset), and cutting out the least important experts (in each lay…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/nlp #keyword/retrieval #keyword/machine-learning
