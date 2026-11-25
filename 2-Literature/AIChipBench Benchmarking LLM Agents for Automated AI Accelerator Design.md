---
title: "AIChipBench: Benchmarking LLM Agents for Automated AI Accelerator Design"
source: "https://arxiv.org/html/2611.33093v1"
author: "Guangyuan Wang, Chengran Li, Minchen Luo, Jichen Feng, Mengdi Wang, Yifan Zhang"
published: "2026-11-24"
created: 2026-11-26
description: "A language-model decoder carries state between decoding steps, and in hardware a wrong state update can leave the current token correct and corrupt the output several tokens later, so a design can pass output tests and still be wrong. AIChipBench asks what LLM coding agents need to build such hardware correctly. Agents implement quantized Qwen3.5, Gemma 3, Gemma 4, and Llama 3.2 decoders in synthesizable register-tr…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/benchmark
  - keyword/agents
---

# AIChipBench: Benchmarking LLM Agents for Automated AI Accelerator Design

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.33093v1)
- published:: 2026-11-24
- updated:: 2026-11-24
- arxiv_id:: 2611.33093v1
- pdf:: https://arxiv.org/pdf/2611.33093v1
- categories:: cs.CL, cs.AI

## Abstract / Summary
A language-model decoder carries state between decoding steps, and in hardware a wrong state update can leave the current token correct and corrupt the output several tokens later, so a design can pass output tests and still be wrong. AIChipBench asks what LLM coding agents need to build such hardware correctly. Agents implement quantized Qwen3.5, Gemma 3, Gemma 4, and Llama 3.2 decoders in synthesizable register-transfer-level (RTL) code against an executable integer reference that specifies the outputs and the stored state at every decoding step. They debug against public tests under fixed budgets; their frozen designs are graded on held-out token sequences, resets, memory stalls, and synthesis, and a second track asks them to speed up a correct design at nearly fixed area. Across 9,136 attempts by four coding agents, the difficulty lies in stored state. Feedback that points to the first state mismatch raises acceptance over output-only feedback in all 12 agent--task cells of a matched study, by 25.0 to 46.9 percentage points, and halves the agent-hours per accepted design. Regraded on new sequences and conditions, 45 of 69 accepted designs fail within the 32 steps their tests required. More than a third of attempts to speed up a correct design end without one. An overall score ranks Sol 5.6 and Fable 5.1 above Astra 6 and Opus 5.5, and both halves of the instances give this order in all 200 random splits. Hardware agents therefore need debugging feedback that exposes stored state, and their benchmarks need final tests well beyond the development cases.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.33093v1)
- [PDF](https://arxiv.org/pdf/2611.33093v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark #keyword/agents
