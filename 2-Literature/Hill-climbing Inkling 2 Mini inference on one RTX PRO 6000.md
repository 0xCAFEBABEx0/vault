---
title: "Hill-climbing Inkling 2 Mini inference on one RTX PRO 6000"
source: "https://huggingface.co/blog/inkling-2-mini-inference-hillclimb"
author: "Hugging Face Blog"
published: "2026-11-25"
created: 2026-11-26
description: "Search models, datasets, users... Ctrl K Models Datasets Spaces Buckets Docs Enterprise Pricing More Website Tasks HuggingChat Collections Languages Organizations Community Blog Posts Daily Papers Hardware Learn Discord Forum GitHub Solutions Team & Enterprise Hugging Face PRO Enterprise Support Inference Providers Inference Endpoints Storage Buckets Log In Sign Up Back to Articles a]:hidden'> Hill-climbing Inkling…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/machine-learning
---

# Hill-climbing Inkling 2 Mini inference on one RTX PRO 6000

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/inkling-2-mini-inference-hillclimb)
- published:: 2026-11-25

## Abstract / Summary
Search models, datasets, users... Ctrl K Models Datasets Spaces Buckets Docs Enterprise Pricing More Website Tasks HuggingChat Collections Languages Organizations Community Blog Posts Daily Papers Hardware Learn Discord Forum GitHub Solutions Team & Enterprise Hugging Face PRO Enterprise Support Inference Providers Inference Endpoints Storage Buckets Log In Sign Up Back to Articles a]:hidden"> Hill-climbing Inkling 2 Mini inference on one RTX PRO 6000 Published November 25, 2026 Update on GitHu… One of the interesting aspects of Inkling 2 Mini that might explain its great performance is its unusual architecture. Inkling 2 Mini is a looped Mixture-of-Experts (MoE) model with 24 physical layers where the middle 12 layers run three times, so every token passes through 48 layers. The checkpoint ships in mixed NVFP4 and MXFP8 and bundles a DSpark drafter for speculative decoding. Both vLLM and SGLang, the go-to frameworks for LLM inference, support it on nightly builds, though the published… We wanted to see how fast we could serve it on a single NVIDIA RTX PRO 6000 96 GB, the GPU behind an nvidia-rtx-pro-6000 Inference Endpoint . Rather than tuning flags by hand, we gave a coding agen…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/machine-learning
