---
title: "Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations"
source: "https://arxiv.org/html/2611.14514v1"
author: "Ziang Liu, James J. Kim, Yijia Dai, Jennifer J. Sun"
published: "2026-11-10"
created: 2026-11-12
description: "LLM agents are increasingly used for open-ended, data-driven scientific discovery, yet most of them evaluate hypotheses pointwise, testing an empirical claim $h$ only against its complement $\neg h$. When evidence rejects $h$, the agent learns that one explanation is unlikely but not which alternative the evidence supports. To recover that alternative, we introduce Contrastive Discovery, which replaces the single hy…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/evaluation
  - keyword/agents
---

# Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.14514v1)
- published:: 2026-11-10
- updated:: 2026-11-10
- arxiv_id:: 2611.14514v1
- pdf:: https://arxiv.org/pdf/2611.14514v1
- categories:: cs.AI, cs.CL, cs.LG

## Abstract / Summary
LLM agents are increasingly used for open-ended, data-driven scientific discovery, yet most of them evaluate hypotheses pointwise, testing an empirical claim $h$ only against its complement $\neg h$. When evidence rejects $h$, the agent learns that one explanation is unlikely but not which alternative the evidence supports. To recover that alternative, we introduce Contrastive Discovery, which replaces the single hypothesis with a contrast set, a scientific question paired with mutually exclusive and collectively exhaustive competing explanations. Each experiment is scored by how its evidence redistributes belief across the set, and the question is resolved when belief concentrates on one explanation. Because contrast sets change only the unit an agent proposes and scores, an existing agent can use them to re-evaluate evidence it has already collected or to guide its search. Across six domains, $89\%$ of the pointwise candidates with the largest belief shifts are rejections. On the same evidence, contrast sets resolve $73\%$ of these candidates to a specific alternative. When contrast sets guide search, the agent resolves $67\%$ more questions than pointwise surprisal under the same experiment budget. In a blinded study, $38$ human experts chose the same explanation on $78\%$ of resolved questions and on $82\%$ of questions where the pointwise agent rejected its hypothesis and stopped. Together, these results support explicit competing explanations as a way for discovery agents to resolve more scientific questions from the same evidence and validation budget.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.14514v1)
- [PDF](https://arxiv.org/pdf/2611.14514v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/evaluation #keyword/agents
