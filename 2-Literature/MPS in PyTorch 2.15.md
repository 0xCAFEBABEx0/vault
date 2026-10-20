---
title: "MPS in PyTorch 2.15"
source: "https://huggingface.co/blog/mps-pytorch-2-15"
author: "Hugging Face Blog"
published: "2026-10-20"
created: 2026-10-21
description: "A quick word about who we are: we're the PyTorch team at Hugging Face. We contribute across PyTorch, and one of our focus areas is the MPS backend, where the goal is to make your Mac a first-class place to run and train PyTorch models. At the start of 2026, running even small models on MPS often meant working around unsupported operations, performance cliffs and unexpected memory growth. So we run real models from t…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/language-model
  - keyword/nlp
  - keyword/multimodal
  - keyword/machine-learning
---

# MPS in PyTorch 2.15

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/mps-pytorch-2-15)
- published:: 2026-10-20

## Abstract / Summary
A quick word about who we are: we're the PyTorch team at Hugging Face. We contribute across PyTorch, and one of our focus areas is the MPS backend, where the goal is to make your Mac a first-class place to run and train PyTorch models. At the start of 2026, running even small models on MPS often meant working around unsupported operations, performance cliffs and unexpected memory growth. So we run real models from the Hugging Face Hub across language, image and video, find where MPS falls short… TL;DR FP8 comes to the Mac: store float8_e4m3fn values in half the space of BF16 and use scaled matrix multiplication and all other ops which are supported on CUDA/CPU! MoE models decode 5–6.5× faster than in 2.14: Qwen3.6-35B-A3B goes from 9.4 to 61.3 tokens/s on an M3 Ultra, thanks to a native grouped matmul with a dedicated decoding path, fewer GPU-CPU syncs and faster top-k routing. Less time per token for every LLM: single-row linear layers use specialized matrix-vector kernels, and softma… Contents Getting started FP8 comes to MPS Faster language-model decoding Linear algebra gets a boost Convolutions, padding, and training Softmax and reductions A much smaller memory footprint for v…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/language-model #keyword/nlp #keyword/multimodal #keyword/machine-learning
