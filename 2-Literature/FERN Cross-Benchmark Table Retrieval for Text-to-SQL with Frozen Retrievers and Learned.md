---
title: "FERN: Cross-Benchmark Table Retrieval for Text-to-SQL with Frozen Retrievers and Learned Ranking"
source: "https://arxiv.org/html/2611.14477v1"
author: "Arjun Rao, Nishant Gopinath"
published: "2026-11-10"
created: 2026-11-12
description: "Text-to-SQL systems over large pooled catalogs must first retrieve the tables a question needs. We compare against the published table recall of RASL, which uses Claude 3.5 models to extract keywords and select tables, on pooled BIRD, Spider, and Fiben catalogs. FERN (Feature-Engineered Ranking with No generative LLM) instead fuses three frozen retrievers into 100 candidates, describes each with up to 120 features,…"
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

# FERN: Cross-Benchmark Table Retrieval for Text-to-SQL with Frozen Retrievers and Learned Ranking

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.14477v1)
- published:: 2026-11-10
- updated:: 2026-11-10
- arxiv_id:: 2611.14477v1
- pdf:: https://arxiv.org/pdf/2611.14477v1
- categories:: cs.IR, cs.CL

## Abstract / Summary
Text-to-SQL systems over large pooled catalogs must first retrieve the tables a question needs. We compare against the published table recall of RASL, which uses Claude 3.5 models to extract keywords and select tables, on pooled BIRD, Spider, and Fiben catalogs. FERN (Feature-Engineered Ranking with No generative LLM) instead fuses three frozen retrievers into 100 candidates, describes each with up to 120 features, and reorders them with LightGBM rankers fitted once on BIRD's training questions. On Spider, where it was not fitted, its candidate pool alone reaches RASL's published recall at fifteen tables (98.0), and the ranker raises the share of questions with every gold table in the top five (complete@5) from 83.9% to 95.6%. At five tables, FERN's recall is within one point of RASL's on Spider (96.7 vs 97.0) and on BIRD with its evidence hints (96.6 vs 97.5), and 8.2 points below on BIRD without them (89.3). On 121 real BEAVER questions, without BEAVER fitting, its recall at fifteen (82.1) falls between two BEAVER-trained retrievers (80.8, 84.5), but its complete@15 is below both (49.6 vs 54.5 and 62.0). On Fiben, it falls far short at fifteen tables (54.2 vs 69.2, different question sets), although its recall at fifty is numerically close to RASL's question-only retrieval result (80.7 vs 79.4). On BIRD dev with evidence, non-retrieval features raise complete@5 by 7.7 points over retrieval signals alone. On BIRD dev, median latency is 208 ms per question on one A100, without hosted model calls.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.14477v1)
- [PDF](https://arxiv.org/pdf/2611.14477v1)
- [NIFT-SQL: Customer-Supervised Table Scoring for Enterprise Text-to-SQL Retrieval](https://arxiv.org/abs/2611.12731) (2026, citations: 1)
- [Pervasive Annotation Errors Break Text-to-SQL Benchmarks and Leaderboards](https://arxiv.org/abs/2601.08778) (2026, citations: 23)
- [RASL: Retrieval Augmented Schema Linking for Massive Database Text-to-SQL](https://arxiv.org/abs/2507.23104) (2025, citations: 10)
- [Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models](https://arxiv.org/abs/2506.05176) (2025, citations: 1931)
- [LinkAlign: Scalable Schema Linking for Real-World Large-Scale Multi-Database Text-to-SQL](https://arxiv.org/abs/2503.18596) (2025, citations: 46)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/machine-learning
