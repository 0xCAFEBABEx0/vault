---
title: "TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning"
source: "https://arxiv.org/html/2606.11119v1"
author: "Heming Zou, Qi Wang, Yun Qu, Yuhang Jiang, Lizhou Cai, Yixiu Mao, Ru Peng, Xin Xu, Weijie Liu, Kai Yang, Saiyong Yang, Xiangyang Ji"
published: "2026-06-09"
created: 2026-06-11
description: "Reinforcement learning with verifiable rewards (RLVR) is a promising approach for enhancing reasoning and agentic behavior in LLMs. However, rollout-intensive policy optimization is often limited by insufficient reward contrast."
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/benchmark
  - keyword/reasoning
  - keyword/agents
---

# TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.11119v1)
- published:: 2026-06-09
- updated:: 2026-06-09
- arxiv_id:: 2606.11119v1
- pdf:: https://arxiv.org/pdf/2606.11119v1
- categories:: cs.LG, cs.AI, cs.CL

## Abstract / Summary
Reinforcement learning with verifiable rewards (RLVR) is a promising approach for enhancing reasoning and agentic behavior in large language models. However, rollout-intensive policy optimization is often limited by insufficient reward contrast, arising when overly simple or complex prompts generate low-variance feedback and when outcome-only rewards assign the same terminal assessment to every decision in a multi-turn rollout. We introduce TRACE (Tree Rollout Allocation for Contrastive Exploration), a unified rollout allocation framework that enhances reward contrast within a fixed sampling budget. TRACE allocates rollout budget to both prompt roots and intermediate prefixes that are most likely to yield mixed terminal rewards, using a shared generalizable predictor to estimate conditional success probability. The resulting adaptive tree structure enriches outcome-only feedback and amplifies the policy-update signal. TRACE achieves competitive performance and efficiency gains on agentic benchmarks, improving Qwen3-14B Multi-Hop QA average accuracy by 2.8 points over competitive baselines at equal sampling cost.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.11119v1)
- [PDF](https://arxiv.org/pdf/2606.11119v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark #keyword/reasoning #keyword/agents
