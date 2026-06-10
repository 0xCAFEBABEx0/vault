---
title: "EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving Agents"
source: "https://arxiv.org/html/2606.11182v1"
author: "Weixian Xu, Shilong Liu, Mengdi Wang"
published: "2026-06-09"
created: 2026-06-11
description: "In this paper, we propose EEVEE, the first multi-dataset test-time prompt learning framework for LLM agents, enabling test-time prompt learning under real-world task streams. Existing methods are largely designed for single-dataset settings, while real-world applications require models to handle heterogeneous input streams drawn from multiple datasets, domains, and task distributions, limiting their practical applic…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/retrieval
  - keyword/evaluation
  - keyword/benchmark
  - keyword/agents
  - keyword/research-paper
---

# EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving Agents

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.11182v1)
- published:: 2026-06-09
- updated:: 2026-06-09
- arxiv_id:: 2606.11182v1
- pdf:: https://arxiv.org/pdf/2606.11182v1
- categories:: cs.LG, cs.AI

## Abstract / Summary
In this paper, we propose EEVEE, the first multi-dataset test-time prompt learning framework for LLM agents, enabling test-time prompt learning under real-world task streams. Existing methods are largely designed for single-dataset settings, while real-world applications require models to handle heterogeneous input streams drawn from multiple datasets, domains, and task distributions, limiting their practical applicability. To mitigate cross-dataset interference, EEVEE introduces a router that partitions incoming inputs into task clusters and assigns them to suitable prompt configurations. This design is optimized via a router-prompt co-evolution strategy, which employs interleaved router and prompt learning phases to address their mutual dependency. Experiments across multiple datasets demonstrate that the framework improves robustness under heterogeneous data streams while maintaining single-benchmark learning capability and efficiency. Specifically, EEVEE improves average multi-benchmark scores by 10.38 and 24.32 points over Qwen3-4B-Instruct and DeepSeek-V3.2, surpassing SOTA methods GEPA and ACE by up to 37.2% and 48.2%.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.11182v1)
- [PDF](https://arxiv.org/pdf/2606.11182v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/agents #keyword/research-paper
