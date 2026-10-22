---
title: "Did the Problem Actually Get Harder? Testing LLMs on Paired P and NP-Complete Problems Hardened by Adversarial Multi-Agent Rewriting"
source: "https://arxiv.org/html/2610.30103v1"
author: "Nurul Labib Sayeedi, Md. Faiyaz Abdullah Sayeedi, Zabir Al Nazi, Mahbub E Sobhani, Shubhashis Roy Dipta"
published: "2026-10-21"
created: 2026-10-23
description: "Many NP-complete (NPC) problems have a polynomial-time (P) twin that differs in a single structural detail, such as 3- versus 2-colouring a graph. A model that reasons rather than recalls should notice which side of this boundary a problem falls on, yet existing benchmarks either fix the wording of each task or ignore its complexity class, so they cannot separate the two. We introduce P2NPCBench, a benchmark of 12 p…"
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

# Did the Problem Actually Get Harder? Testing LLMs on Paired P and NP-Complete Problems Hardened by Adversarial Multi-Agent Rewriting

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.30103v1)
- published:: 2026-10-21
- updated:: 2026-10-21
- arxiv_id:: 2610.30103v1
- pdf:: https://arxiv.org/pdf/2610.30103v1
- categories:: cs.CL

## Abstract / Summary
Many NP-complete (NPC) problems have a polynomial-time (P) twin that differs in a single structural detail, such as 3- versus 2-colouring a graph. A model that reasons rather than recalls should notice which side of this boundary a problem falls on, yet existing benchmarks either fix the wording of each task or ignore its complexity class, so they cannot separate the two. We introduce P2NPCBench, a benchmark of 12 problem families in which every NPC problem is paired with a P twin posed over the same surface. To remove the textbook cues that enable recall, we build it with AgentGAN, an adversarial multi-agent framework in which a generator rewrites each statement until a panel of frozen code models fails, while an executable validity gate keeps every rewrite answer- and class-preserving. The result is 2,114 hardened statements with hand-verified reference human solvers. Evaluating 12 proprietary and open-source models, we find that every model scores lower on NPC statements than on their P twins (35.4% vs. 63.8% pass@1), and that 95.1% of model-family pairs fail more often on the NPC side. A tenfold time limit raises NPC accuracy only from 28.5% to 31.9%, so failures stem from wrong or crashing programs rather than slow ones. Hardening also narrows the class gap from 24.8 to 14.6 points, showing that part of the apparent gap reflects familiarity with textbook phrasing rather than complexity class.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.30103v1)
- [PDF](https://arxiv.org/pdf/2610.30103v1)
- [Qwen3.8-Omni: Towards Native Omni-Modal Agents](https://arxiv.org/abs/2609.25611) (2026, citations: 3)
- [EvoMem: Timeline-Grounded Validity Adjudication for Non-Monotonic Multi-Agent Memory](https://doi.org/10.1145/3805712.3809931) (2026, citations: 1)
- [Terminal-World: Scaling Terminal-Agent Environments via Agent Skills](https://arxiv.org/abs/2605.20876) (2026, citations: 23)
- [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348) (2026, citations: 1303)
- [ACE: Self-Evolving LLM Coding Framework via Adversarial Unit Test Generation and Preference Optimization](https://arxiv.org/abs/2605.16299) (2026, citations: 7)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark #keyword/agents
