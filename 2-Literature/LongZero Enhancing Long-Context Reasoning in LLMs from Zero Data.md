---
title: "LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data"
source: "https://arxiv.org/html/2610.30132v1"
author: "Zhennan Wan, Jianfei Chen"
published: "2026-10-21"
created: 2026-10-23
description: "Reinforcement learning (RL) is an effective way to strengthen the long-context reasoning of large language models (LLMs), but it needs training data that are long, diverse, challenging, and verifiable. Human annotation of such data is expensive, naturally occurring data are too scarce to sustain RL, and existing synthesis methods depend on external corpora or stronger teacher models, which become harder to obtain as…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/benchmark
  - keyword/reasoning
  - keyword/machine-learning
---

# LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.30132v1)
- published:: 2026-10-21
- updated:: 2026-10-21
- arxiv_id:: 2610.30132v1
- pdf:: https://arxiv.org/pdf/2610.30132v1
- categories:: cs.CL, cs.LG

## Abstract / Summary
Reinforcement learning (RL) is an effective way to strengthen the long-context reasoning of large language models (LLMs), but it needs training data that are long, diverse, challenging, and verifiable. Human annotation of such data is expensive, naturally occurring data are too scarce to sustain RL, and existing synthesis methods depend on external corpora or stronger teacher models, which become harder to obtain as the trained models get stronger. Recently, RL from zero data, in which a model learns from tasks it proposes itself, has achieved excellent performance, but existing methods target short-context tasks. Therefore, we propose $\textbf{LongZero}$, a method that lets an LLM improve its own long-context reasoning without any external data. Instead of writing questions and answers over existing documents, LongZero first has the model synthesize the question and answer with its supporting evidence in a compact structured form, and only then separately expands the evidence into a long multi-document context. LongZero combines these self-written multi-hop reasoning tasks with self-written multi-round retrieval tasks and trains the model with GRPO. We evaluate LongZero on two LLMs across five long-context reasoning benchmarks and compare it with RL on data synthesized from external corpora. Experimental results show that LongZero can generalize to real tasks, and outperforms both baselines, suggesting a viable and promising path to improving long-context reasoning of LLMs.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.30132v1)
- [PDF](https://arxiv.org/pdf/2610.30132v1)
- [LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards](https://arxiv.org/abs/2605.31584) (2026, citations: 4)
- [GoLongRL: Capability-Oriented Long Context Reinforcement Learning with Multitask Alignment](https://arxiv.org/abs/2605.19577) (2026, citations: 6)
- [LongRLVR: Long-Context Reinforcement Learning Requires Verifiable Context Rewards](https://arxiv.org/abs/2603.02146) (2026, citations: 21)
- [Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data](https://arxiv.org/abs/2602.21320) (2026, citations: 36)
- [Dr. Zero: Self-Evolving Search Agents without Training Data](https://arxiv.org/abs/2601.07055) (2026, citations: 47)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/reasoning #keyword/machine-learning
