---
title: "How an Agent Built a 3D Paris Gallery by Chaining Two Hugging Face Spaces"
source: "https://huggingface.co/blog/mishig/spaces-agents-md"
author: "Hugging Face Blog"
published: "2026-06-09"
created: 2026-06-10
description: "I asked a coding agent to build a beautiful website showcasing the monuments of Paris as 3D Gaussian splats. I never opened an image generator. I never touched a 3D reconstruction tool. The agent produced every asset (the images and the 3D splats) by calling two Hugging Face Spaces directly, then wired them into a cinematic viewer. This post is about how that's possible now, and why I think it's a preview of how a l…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/multimodal
  - keyword/agents
---

# How an Agent Built a 3D Paris Gallery by Chaining Two Hugging Face Spaces

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/mishig/spaces-agents-md)
- published:: 2026-06-09

## Abstract / Summary
I asked a coding agent to build a beautiful website showcasing the monuments of Paris as 3D Gaussian splats. I never opened an image generator. I never touched a 3D reconstruction tool. The agent produced every asset (the images and the 3D splats) by calling two Hugging Face Spaces directly, then wired them into a cinematic viewer. This post is about how that's possible now, and why I think it's a preview of how a lot of multimedia software gets built from here on. The building-block economy comes for multimedia Mitchell Hashimoto recently described a shift he calls the building block economy : the most effective path to software is no longer a polished monolith, but small, well-documented components that others (increasingly agents ) can assemble. His key observation: AI is okay at building everything from scratch, but it is really good at gluing together proven pieces. That thesis has mostly been told with code libraries. But the same forces are hitting multimedia AI . The hard part of using a state-of-the-art image model, a video model, a TTS model, or a 3D reconstruction model was never the model. It was the integration: SDKs, weights, GPUs, input formats, polling. If each mod…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/multimodal #keyword/agents
