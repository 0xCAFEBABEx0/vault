---
title: "OlmoEarth v1.3: State-of-the-art embeddings for the whole planet"
source: "https://huggingface.co/blog/allenai/olmoearth-v1-3"
author: "Hugging Face Blog"
published: "2026-10-22"
created: 2026-10-23
description: "Today, we’re releasing OlmoEarth v1.3 , a state-of-the-art satellite embedding model. Alongside OlmoEarth v1.3, we’re sharing precomputed, annual embeddings for the whole planet (10m, 64- and 128-dimensions), plus a new browser-based tool to explore and customize maps based on those embeddings — the OlmoEarth Embeddings Explorer . This means anyone can put OlmoEarth v1.3 to work right away, from tracking change over…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/machine-learning
---

# OlmoEarth v1.3: State-of-the-art embeddings for the whole planet

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/allenai/olmoearth-v1-3)
- published:: 2026-10-22

## Abstract / Summary
Today, we’re releasing OlmoEarth v1.3 , a state-of-the-art satellite embedding model. Alongside OlmoEarth v1.3, we’re sharing precomputed, annual embeddings for the whole planet (10m, 64- and 128-dimensions), plus a new browser-based tool to explore and customize maps based on those embeddings — the OlmoEarth Embeddings Explorer . This means anyone can put OlmoEarth v1.3 to work right away, from tracking change over time to finding similar places—no sign-in, and no advanced technical knowledge… Until now, the primary way to use OlmoEarth was fine-tuning in OlmoEarth Studio: training a model for each task and running it over satellite imagery to make a map. That requires GPU access and the ability to download and store the imagery . Embedding models compress satellite data into ready-to-use features that can be reused cheaply for many tasks. With OlmoEarth v1.3, we’re excited to give users more ways to explore and engage with planetary artifacts in whatever way suits them best. Compute once, reuse everywhere An embedding represents what the model learned from millions of images. OlmoEarth v1.3 reads a year of radar (Sentinel-1) and multispectral (Sentinel-2 and Landsat) satellite t…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/machine-learning
