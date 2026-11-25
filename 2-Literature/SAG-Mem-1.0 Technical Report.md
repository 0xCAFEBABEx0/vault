---
title: "SAG-Mem-1.0 Technical Report"
source: "https://arxiv.org/html/2611.33124v1"
author: "Yuchao Wu, XingCheng Liang, Xuanze Wang, Yini Huang, Yue Wu"
published: "2026-11-24"
created: 2026-11-26
description: "Long-term conversational memory requires retrieving complementary facts scattered across dialogue sessions, including intermediate evidence with limited similarity to the original question. Existing approaches often rely on derived memory representations or persistent relational structures, introducing construction costs and potentially losing source details. We present SAG-Mem, a conversational memory framework tha…"
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
  - keyword/machine-learning
---

# SAG-Mem-1.0 Technical Report

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.33124v1)
- published:: 2026-11-24
- updated:: 2026-11-24
- arxiv_id:: 2611.33124v1
- pdf:: https://arxiv.org/pdf/2611.33124v1
- categories:: cs.CL, cs.IR

## Abstract / Summary
Long-term conversational memory requires retrieving complementary facts scattered across dialogue sessions, including intermediate evidence with limited similarity to the original question. Existing approaches often rely on derived memory representations or persistent relational structures, introducing construction costs and potentially losing source details. We present SAG-Mem, a conversational memory framework that preserves complete dialogue messages in non-overlapping chunks and discovers complementary evidence through query-time lexical expansion. Memory construction requires no model inference, using a lexical index without LLM-based extraction, summarization, or semantic relation construction. At query time, BM25 retrieves initial candidates, an evidence evaluator identifies useful chunks, and lexical cues from selected evidence guide an additional retrieval round. Retrieved dialogue is further annotated with calendar interpretations of supported relative-time expressions, preserving the original wording and temporal granularity. We also introduce SAG-Mem-Lite, an alternative configuration that replaces evidence scoring with embedding-based candidate scoring, achieving lower operational cost than Full Context and all memory-based baselines across both benchmarks with low query latency. On LoCoMo and LongMemEval, SAG-Mem achieves overall scores of 83.08 and 80.20, respectively, the highest among the evaluated methods on both benchmarks. On LongMemEval, it exceeds the strongest compared baseline by 7.20 points. SAG-Mem-Lite achieves scores of 77.09 and 77.20, respectively. These results support dialogue preservation and evidence-guided retrieval expansion as an effective design for long-term conversational memory.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.33124v1)
- [PDF](https://arxiv.org/pdf/2611.33124v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/machine-learning
