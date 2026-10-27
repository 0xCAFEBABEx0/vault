---
title: "Build specialized multimodal models with LFM3"
source: "https://huggingface.co/blog/LiquidAI/lfm3"
author: "Hugging Face Blog"
published: "2026-10-27"
created: 2026-10-28
description: "How we built a more expressive backbone LFM2 showed that a hybrid of short convolutions and attention can run fast on-device without sacrificing quality. For LFM3, we used our hardware-in-the-loop architecture search to redesign that architecture for agentic use cases, which need more capability per parameter and fast inference over long contexts. The search now covers 14 device and backend combinations, from phones…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/transformer
  - keyword/nlp
  - keyword/multimodal
  - keyword/agents
  - keyword/machine-learning
---

# Build specialized multimodal models with LFM3

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/LiquidAI/lfm3)
- published:: 2026-10-27

## Abstract / Summary
How we built a more expressive backbone LFM2 showed that a hybrid of short convolutions and attention can run fast on-device without sacrificing quality. For LFM3, we used our hardware-in-the-loop architecture search to redesign that architecture for agentic use cases, which need more capability per parameter and fast inference over long contexts. The search now covers 14 device and backend combinations, from phones and a Raspberry Pi 5 to laptops, cloud CPUs, GPUs, and the Qualcomm Hexagon NPU. The payoff shows at long context. Per parameter, LFM3-1.7B matches LFM2-1.2B on short prompts across edge devices, and with 8K tokens in context it is about 25% faster. LFM3-1.7B-Base was pre-trained on 22T tokens with the same 128K vocabulary as LFM2.5-8B-A1B . The final 3.5T tokens are a mid-training stage on curated data with a larger share of agentic traces and tool calls, which also extends the context window to 256K tokens. One backbone for six models Every LFM3 model branches from LFM3-1.7B-Base. Instead of running one large general-purpose model, you pick the one that fits your inputs, customize it, and run it on-device. How to use the LFM3 models Each model runs in transformers .…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/transformer #keyword/nlp #keyword/multimodal #keyword/agents #keyword/machine-learning
