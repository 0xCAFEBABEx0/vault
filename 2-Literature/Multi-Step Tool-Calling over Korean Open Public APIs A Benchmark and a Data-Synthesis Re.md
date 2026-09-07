---
title: "Multi-Step Tool-Calling over Korean Open Public APIs: A Benchmark and a Data-Synthesis Recipe"
source: "https://arxiv.org/html/2609.05395v1"
author: "Dain Kim, Eungi Cho, Kyumin Kim, Shinyeong Noh, Kyuseong Lim"
published: "2026-09-04"
created: 2026-09-08
description: "Data-sovereignty regulations increasingly require public institutions to deploy open-source, on-premise LLM agents that chain multiple tool-calls across live government APIs. However, open-source models consistently underperform in this multi-step setting, and no existing benchmark measures the gap. We introduce the Korean Open Public API Benchmark (KOPA-Bench), comprising 145 real-world tasks. To close this gap, we…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/evaluation
  - keyword/benchmark
  - keyword/agents
---

# Multi-Step Tool-Calling over Korean Open Public APIs: A Benchmark and a Data-Synthesis Recipe

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.05395v1)
- published:: 2026-09-04
- updated:: 2026-09-04
- arxiv_id:: 2609.05395v1
- pdf:: https://arxiv.org/pdf/2609.05395v1
- categories:: cs.AI, cs.CL

## Abstract / Summary
Data-sovereignty regulations increasingly require public institutions to deploy open-source, on-premise LLM agents that chain multiple tool-calls across live government APIs. However, open-source models consistently underperform in this multi-step setting, and no existing benchmark measures the gap. We introduce the Korean Open Public API Benchmark (KOPA-Bench), comprising 145 real-world tasks. To close this gap, we present EDGE, an Execution-grounded Dynamic Graph for tool-calling data synthEsis driven by live execution. EDGE builds a graph of how each tool's output can feed another's input, keeps only the links that succeed when actually called against the live APIs, and traverses these verified links to synthesize executable multi-step trajectories. Fine-tuned via GRPO on the resulting dataset, our 9B model nearly matches the untuned 27B model from the same family, improving substantially not only on KOPA-Bench but also on the BFCL benchmark.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.05395v1)
- [PDF](https://arxiv.org/pdf/2609.05395v1)
- [DeepSWE: Measuring Frontier Coding Agents on Original, Long-Horizon Engineering Tasks](https://arxiv.org/abs/2607.07946) (2026, citations: 16)
- [Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces](https://arxiv.org/abs/2601.11868) (2026, citations: 391)
- [Empowering Real-World: A Survey on the Technology, Practice, and Evaluation of LLM-driven Industry Agents](https://arxiv.org/abs/2510.17491) (2025, citations: 4)
- [Towards Reliable Benchmarking: A Contamination Free, Controllable Evaluation Framework for Multi-step LLM Function Calling](https://arxiv.org/abs/2509.26553) (2025, citations: 12)
- [Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504) (2025, citations: 196)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/evaluation #keyword/benchmark #keyword/agents
