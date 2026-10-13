---
title: "Run fast, private agents on-device with LFM2.5-24B-A2B"
source: "https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b"
author: "Hugging Face Blog"
published: "2026-10-13"
created: 2026-10-14
description: "How we built a reasoning agent with 2B active parameters LFM2.5-24B-A2B builds on LFM2-24B-A2B and keeps its architecture: 40 layers, 64 experts per MoE block with top-4 routing, and the same hybrid of gated short convolutions and GQA. The context window grows from 32K to 131K tokens, and an in-place tokenizer expansion doubles the vocabulary from 65K to 128K tokens for better non-Latin tokenization. Unlike its pred…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/nlp
  - keyword/evaluation
  - keyword/benchmark
  - keyword/reasoning
  - keyword/agents
  - keyword/machine-learning
---

# Run fast, private agents on-device with LFM2.5-24B-A2B

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b)
- published:: 2026-10-13

## Abstract / Summary
How we built a reasoning agent with 2B active parameters LFM2.5-24B-A2B builds on LFM2-24B-A2B and keeps its architecture: 40 layers, 64 experts per MoE block with top-4 routing, and the same hybrid of gated short convolutions and GQA. The context window grows from 32K to 131K tokens, and an in-place tokenizer expansion doubles the vocabulary from 65K to 128K tokens for better non-Latin tokenization. Unlike its predecessor, it is a reasoning-only model that produces an explicit chain of thought… Pre-training was scaled up from ~17T to ~33T tokens. Mid-training then adds 2T tokens at 32K context, weighted toward reasoning, math, code, instruction following, and multilingual text, and 300B tokens at 131K context, weighted toward long-context data. Tool calls and multi-turn trajectories appear throughout both phases. Post-training turns the base model into an agent in five stages: Benchmark results We evaluated LFM2.5-24B-A2B against Qwen3.6-35B-A3B, Gemma-4-26B-A4B-it, and Nemotron-3.5-Lightning on 16 benchmarks covering tool use and agentic workflows, knowledge, instruction following, math, and coding. It is the smallest model in the group, yet it is competitive with MoEs with ~50%…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/nlp #keyword/evaluation #keyword/benchmark #keyword/reasoning #keyword/agents #keyword/machine-learning
