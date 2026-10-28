---
title: "semanticfa: An R Package for Response-Free Semantic Factor Analysis of Psychometric Scales"
source: "https://arxiv.org/html/2610.37494v1"
author: "Devon Yanitski, Chris Westbury"
published: "2026-10-27"
created: 2026-10-29
description: "The items of a reflective psychometric scale can be read as a proposal about a construct's structure. Language models make that proposal measurable by converting each item into an embedding, a list of numbers, similar for similar meanings. We introduce semanticfa, an R package for semantic factor analysis, which factors item-embedding similarities. It also interprets factors, flags redundant items, builds short form…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
---

# semanticfa: An R Package for Response-Free Semantic Factor Analysis of Psychometric Scales

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.37494v1)
- published:: 2026-10-27
- updated:: 2026-10-27
- arxiv_id:: 2610.37494v1
- pdf:: https://arxiv.org/pdf/2610.37494v1
- categories:: cs.CL

## Abstract / Summary
The items of a reflective psychometric scale can be read as a proposal about a construct's structure. Language models make that proposal measurable by converting each item into an embedding, a list of numbers, similar for similar meanings. We introduce semanticfa, an R package for semantic factor analysis, which factors item-embedding similarities. It also interprets factors, flags redundant items, builds short forms, and screens new items. A worked example analyzes the 50-item International Personality Item Pool Big-Five Factor Markers, embedded with Qwen3-Embedding-8B, and compares the results with a factor analysis of 874,434 respondents. Retention criteria tied between five and six factors, and the tie rule kept five. Three corresponded mainly to single domains, and two blended most Extraversion items with five Agreeableness items. Each factor's congruence with its best-matching human factor (1 = identical) ranged from .92 for Openness to .52 for Agreeableness. Item pairs more similar in meaning tended to be answered more alike (r = .46 with raw responses), but same-domain reverse-keyed opposites, answered oppositely, were about as similar as cross-domain pairs (.58 vs. .57). Sign-flipping reverse-keyed items' embeddings did not improve agreement with raw responses and worsened it with reverse-scored ones. With five factors, a 25-item short form matched the domains better than all 200 random five-per-domain sets, but parallel analysis kept only three. We propose semantic-behavioral coherence, the agreement between semantic and response structures, as a measurable property of a scale, given an embedding model. Semantic factor analysis complements, and does not replace, response-based factor analysis.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.37494v1)
- [PDF](https://arxiv.org/pdf/2610.37494v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp
