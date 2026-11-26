---
title: "Introducing the llama.cpp benchmark dashboard for AMD Ryzen and Radeon"
source: "https://huggingface.co/blog/ggml-org/llamacpp-amd-bench"
author: "Hugging Face Blog"
published: "2026-11-26"
created: 2026-11-27
description: "Search models, datasets, users... Ctrl K Models Datasets Spaces Buckets Docs Enterprise Pricing More Website Tasks HuggingChat Collections Languages Organizations Community Blog Posts Daily Papers Hardware Learn Discord Forum GitHub Solutions Team & Enterprise Hugging Face PRO Enterprise Support Inference Providers Inference Endpoints Storage Buckets Log In Sign Up Back to Articles a]:hidden'> Introducing the llama.…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/benchmark
  - keyword/machine-learning
---

# Introducing the llama.cpp benchmark dashboard for AMD Ryzen and Radeon

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/ggml-org/llamacpp-amd-bench)
- published:: 2026-11-26

## Abstract / Summary
Search models, datasets, users... Ctrl K Models Datasets Spaces Buckets Docs Enterprise Pricing More Website Tasks HuggingChat Collections Languages Organizations Community Blog Posts Daily Papers Hardware Learn Discord Forum GitHub Solutions Team & Enterprise Hugging Face PRO Enterprise Support Inference Providers Inference Endpoints Storage Buckets Log In Sign Up Back to Articles a]:hidden"> Introducing the llama.cpp benchmark dashboard for AMD Ryzen and Radeon Team Article Published November… Local inference performance changes as models, kernels, and builds evolve. We want those changes to be easy to inspect for any AMD developer: pick a hardware, a model and a build, compare quantizations, and follow performance over time. The benchmark workflow and underlying results are public, so you can also inspect how we benchmark inference performance. Quick start You can choose Hardware , Model , and llama.cpp build in the Configuration sidebar. The current hardware choices are Radeon 8060S (gfx1151) and Radeon AI Pro R9700S (gfx1201). What the numbers mean The dashboard shows two separate tests, both measured in tokens per second: Both tests start at context depth zero ( n_depth=0 ).…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/machine-learning
