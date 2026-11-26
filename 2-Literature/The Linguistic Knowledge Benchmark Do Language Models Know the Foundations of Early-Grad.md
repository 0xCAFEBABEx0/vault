---
title: "The Linguistic Knowledge Benchmark: Do Language Models Know the Foundations of Early-Grade Literacy?"
source: "https://arxiv.org/html/2611.34823v1"
author: "Maxime Lelièvre, Alasdair Mackintosh, Dominic Andrews, Tobias Murray, Moritz Boos, Oliver G. B. Garrod"
published: "2026-11-25"
created: 2026-11-27
description: "Many languages of instruction in low- and middle-income countries (LMICs) are poorly represented in the data used to train language models. Before these models can support early-grade literacy in such languages, we need to know whether they hold the linguistic knowledge of each language that literacy teaching relies on. To test this, we present the Linguistic Knowledge Benchmark and the reproducible, largely automat…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/benchmark
---

# The Linguistic Knowledge Benchmark: Do Language Models Know the Foundations of Early-Grade Literacy?

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.34823v1)
- published:: 2026-11-25
- updated:: 2026-11-25
- arxiv_id:: 2611.34823v1
- pdf:: https://arxiv.org/pdf/2611.34823v1
- categories:: cs.CL

## Abstract / Summary
Many languages of instruction in low- and middle-income countries (LMICs) are poorly represented in the data used to train language models. Before these models can support early-grade literacy in such languages, we need to know whether they hold the linguistic knowledge of each language that literacy teaching relies on. To test this, we present the Linguistic Knowledge Benchmark and the reproducible, largely automated pipeline that turns curriculum documents, teacher guides and pupil books into a vetted question set organised on a fixed grid of nine linguistic domains and seven grade levels. The pipeline combines LLM-driven source survey, feature consolidation, item generation and quality control with an item-selection step inspired by item response theory and a final expert review. We instantiate it for Kiswahili (Kenya; 135 items) and English (United Kingdom; 137 items) and evaluate 121 and 119 models respectively. Frontier models exceed 90% accuracy in both languages, but accuracy falls steeply for smaller and cheaper models, and more so in Kiswahili. The two best models under 10 billion parameters reach 91.7% and 73.0% in English but only 51.9% and 40.7% in Kiswahili, and the mean accuracy of models deployable on mobile and tablet hardware is 47% in English against 24% in Kiswahili. The models most practical for low-resource classrooms are therefore the least capable in the languages they would serve. We release a 20-item sample per language, all pipeline prompts, open-source code, and a public leaderboard. This is the first rung of a three-level evaluation ladder for measuring and generating decodable text to support foundational literacy.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.34823v1)
- [PDF](https://arxiv.org/pdf/2611.34823v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark
