---
title: "GEPA-Curator: Curated Learning for Self Improving Agents"
source: "https://arxiv.org/html/2610.37651v1"
author: "Zack Yu, Nicholas Lee, Minjae Lee, Lakshya Agarwal, Luca Manolache, Wonjun Kang, Matei Zaharia, Michael W. Mahoney, Kurt Keutzer, Sehoon Kim, Amir Gholami"
published: "2026-10-27"
created: 2026-10-29
description: "Large Language Models (LLMs) are increasingly used in multi-turn agentic workloads that require sustained interaction with complex environments. Existing reflective prompt optimizers such as GEPA learn from failed rollouts, but agentic failures can also come from prompt weaknesses, harness limitations, stochastic execution, or noisy judges. We argue that such failures may not provide useful learning signal, and may…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/agents
---

# GEPA-Curator: Curated Learning for Self Improving Agents

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.37651v1)
- published:: 2026-10-27
- updated:: 2026-10-27
- arxiv_id:: 2610.37651v1
- pdf:: https://arxiv.org/pdf/2610.37651v1
- categories:: cs.CL

## Abstract / Summary
Large Language Models (LLMs) are increasingly used in multi-turn agentic workloads that require sustained interaction with complex environments. Existing reflective prompt optimizers such as GEPA learn from failed rollouts, but agentic failures can also come from prompt weaknesses, harness limitations, stochastic execution, or noisy judges. We argue that such failures may not provide useful learning signal, and may even be harmful; and thus it is essential to curate which tasks are provided to the prompt optimizer for better performance. We introduce GEPA-Curator, a framework that augments the prompt optimizer to select which agent experiences should shape prompt optimization. In particular, GEPA-Curator consists of two components: task curation, which filters out tasks that are likely to provide noisy or unreliable learning signals, and prior success retrieval, which selectively retrieves past successful trajectories for a task and provides them as additional context to the prompt optimizer. We evaluate GEPA-Curator on GoBrowse, ALFWorld, AppWorld, and $τ$-bench, using both Gemini 3.1 Pro and Claude Opus 5 as optimizer models. GEPA-Curator matches or exceeds the mean performance of both baselines, with gains of up to 20.7% over GEPA and 21.2% over ACE.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.37651v1)
- [PDF](https://arxiv.org/pdf/2610.37651v1)
- [OSWorld2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks](https://arxiv.org/abs/2606.29537) (2026, citations: 48)
- [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/abs/2605.23904) (2026, citations: 166)
- [Prompting Policies for Multi-step Reasoning and Tool-Use in Black-box LLMs with Iterative Distillation of Experience](https://arxiv.org/abs/2605.14443) (2026, citations: 1)
- [Meta-Harness: End-to-End Optimization of Model Harnesses](https://arxiv.org/abs/2603.28052) (2026, citations: 350)
- [Towards Robust Mathematical Reasoning](https://arxiv.org/abs/2511.01846) (2025, citations: 96)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/agents
