---
title: "Granite Switch 4.1: Chat, Decisions, and Speech from One Endpoint"
source: "https://huggingface.co/blog/ibm-granite/granite-switch-4-1"
author: "Hugging Face Blog"
published: "2026-10-15"
created: 2026-10-19
description: "All three of these technologies (along with the underlying base model) are composed into one model, taking up approximately the same amount of VRAM on a GPU as the base model would by itself. That means more capabilities with fewer GPUs. And because the Switch adapters were built as cache-efficient Activated LoRAs , the KV cache created from a base model generation can be reused for any subsequent adapter-based deci…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/language-model
  - keyword/multimodal
---

# Granite Switch 4.1: Chat, Decisions, and Speech from One Endpoint

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/ibm-granite/granite-switch-4-1)
- published:: 2026-10-15

## Abstract / Summary
All three of these technologies (along with the underlying base model) are composed into one model, taking up approximately the same amount of VRAM on a GPU as the base model would by itself. That means more capabilities with fewer GPUs. And because the Switch adapters were built as cache-efficient Activated LoRAs , the KV cache created from a base model generation can be reused for any subsequent adapter-based decisions. Combined with our team's recent vLLM contributions to speed up low rank adapter inferencing, as well as a co-located ASR encoder, Granite Switch 4.1 models can switch between a chat request and a decision request and a spoken request, with blazing fast speeds. Check out our Speech-to-Decisions HF space where granite-switch-4.1-8b transcribes audio, generates summaries, screens for harmful content, and tests 15 other user-defined flags—all running on a single endpoint in real time. Granite Libraries: The OG Decision Models Decision models aren’t new. Our previous release of Granite Libraries features a repository of specialized “decision model” adapters and other specialized task adapters that can be composed into custom Granite Switch models. And while Jev and ot…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/language-model #keyword/multimodal
