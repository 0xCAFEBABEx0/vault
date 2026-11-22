---
title: "Text-Aware, Vision-Blind: How Multimodal Image Editing Systems Handle Unsafe Inputs"
source: "https://arxiv.org/html/2611.26569v1"
author: "Ziqing Yang, Yixin Wu, Michael Backes, Yang Zhang"
published: "2026-11-19"
created: 2026-11-23
description: "Multimodal image generation systems have made rapid progress and increasingly emphasize content safety. However, their safety mechanisms tend to rely on a single modality and lack joint consideration of both visual content and text prompts, particularly in instruction-guided image editing, where the uploaded image may itself carry risk. We thus introduce EditSafetyBench, a benchmark that measures system-level safety…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/nlp
  - keyword/multimodal
  - keyword/evaluation
  - keyword/benchmark
  - keyword/safety
---

# Text-Aware, Vision-Blind: How Multimodal Image Editing Systems Handle Unsafe Inputs

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.26569v1)
- published:: 2026-11-19
- updated:: 2026-11-19
- arxiv_id:: 2611.26569v1
- pdf:: https://arxiv.org/pdf/2611.26569v1
- categories:: cs.CR, cs.CV, cs.LG

## Abstract / Summary
Multimodal image generation systems have made rapid progress and increasingly emphasize content safety. However, their safety mechanisms tend to rely on a single modality and lack joint consideration of both visual content and text prompts, particularly in instruction-guided image editing, where the uploaded image may itself carry risk. We thus introduce EditSafetyBench, a benchmark that measures system-level safety awareness of advanced image editing systems, containing 5,940 image-instruction pairs, covering safe and unsafe images across 11 risk categories and three edit intents. We then probe the benchmark dataset on four systems, including Gemini, GPT, Qwen API, and Qwen Local. Based on our evaluation, we observe a systematic text-vision safety mismatch: Gemini and GPT refuse 87.1\% and 81.6\% cases containing unsafe-intent editing prompts, while only refusing 24.2\% and 22.4\% cases with both unsafe images and neutral instructions. At the category level, most risks are considered inconsistently by different systems, e.g., GPT allows 70.4\% editing attempts of unsafe political content while Gemini only allows 34.8\%. Notably, sexual content shows the strongest visual sensitivity, likely benefiting from mature NSFW identification works. Our findings highlight the need for safety guardrails that jointly reason over both visual and textual modalities in image editing systems.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.26569v1)
- [PDF](https://arxiv.org/pdf/2611.26569v1)
- [Towards Policy-Adaptive Image Guardrail: Benchmark and Method](https://arxiv.org/abs/2603.01228) (2026, citations: 8)
- [When the Prompt Becomes Visual: Vision-Centric Jailbreak Attacks for Large Image Editing Models](https://arxiv.org/abs/2602.10179) (2026, citations: 6)
- [SafeVision: Efficient Image Guardrail with Robust Policy Adherence and Explainability](https://arxiv.org/abs/2510.23960) (2025, citations: 7)
- [Qwen-Image Technical Report](https://arxiv.org/abs/2508.02324) (2025, citations: 1250)
- [Peering Behind the Shield: Guardrail Identification in Large Language Models](https://arxiv.org/abs/2502.01241) (2025, citations: 7)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/nlp #keyword/multimodal #keyword/evaluation #keyword/benchmark #keyword/safety
