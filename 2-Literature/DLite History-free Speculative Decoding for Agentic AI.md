---
title: "DLite: History-free Speculative Decoding for Agentic AI"
source: "https://arxiv.org/html/2610.23787v1"
author: "Jiaming Xu, Hanzhen Wang, Tianlang Zhao, Jiewen Xiao, Chengze Yuan, Jiayi Pan, Yongkang Zhou, Jiancai Ye, Yu Wang, Guohao Dai"
published: "2026-10-16"
created: 2026-10-20
description: "Speculative decoding has become a mainstream technique for accelerating large language model (LLM) inference by using a lightweight draft model to generate candidate tokens that are subsequently verified by the target model. However, agentic workloads introduce long and continuously evolving contexts and frequent multi-turn interactions. Under such workloads, we observe that existing draft models suffer from up to a…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/agents
  - keyword/machine-learning
  - keyword/research-paper
---

# DLite: History-free Speculative Decoding for Agentic AI

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.23787v1)
- published:: 2026-10-16
- updated:: 2026-10-16
- arxiv_id:: 2610.23787v1
- pdf:: https://arxiv.org/pdf/2610.23787v1
- categories:: cs.CL

## Abstract / Summary
Speculative decoding has become a mainstream technique for accelerating large language model (LLM) inference by using a lightweight draft model to generate candidate tokens that are subsequently verified by the target model. However, agentic workloads introduce long and continuously evolving contexts and frequent multi-turn interactions. Under such workloads, we observe that existing draft models suffer from up to an 80% degradation in acceptance length, while maintaining their historical KV cache introduces substantial system overhead. In this paper, we identify the growing historical context as a common source of both problems and introduce DLite, a history-free speculative decoding framework for agentic AI. DLite directly reuses contextual hidden states from the target model and performs local speculative prediction without explicitly maintaining the historical context, transforming an increasingly complex modeling problem into local simple prediction problem. A lightweight sequential head further restores intra-block causal dependencies with low overhead. To effectively train this heterogeneous history-free architecture, we introduce a tailored two-stage training strategy. Experiments on general-purpose, long-context and agentic workloads show that DLite achieves 2-6 acceptance length and outperforms the state-of-the-art speculative decoding method, DSpark, up to 70%.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.23787v1)
- [PDF](https://arxiv.org/pdf/2610.23787v1)
- [DFlow: Enabling Verifier Information Flow in Block Diffusion Speculative Decoding](https://arxiv.org/abs/2609.06498) (2026, citations: 4)
- [DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation](https://arxiv.org/abs/2607.05147) (2026, citations: 53)
- [Domino: Decoupling Causal Modeling from Autoregressive Drafting in Speculative Decoding](https://arxiv.org/abs/2605.29707) (2026, citations: 37)
- [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348) (2026, citations: 1263)
- [DFlash: Block Diffusion for Flash Speculative Decoding](https://arxiv.org/abs/2602.06036) (2026, citations: 147)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/agents #keyword/machine-learning #keyword/research-paper
