---
title: "Can Programs Replace LLM Judges? Executable Program Judges for Scalable and Efficient Relevance Labeling"
source: "https://arxiv.org/html/2611.24849v1"
author: "Eugene Agichtein, Charles L. A. Clarke, Kaustubh Dhole, William Stern"
published: "2026-11-18"
created: 2026-11-20
description: "Large language model (LLM) judges have become a common way to create large-scale relevance judgments for retrieval evaluation. However, each judgment requires a potentially expensive call to a frontier model, and the judgments are hard to interpret and may not be reproducible. In this paper, we ask whether an LLM can write a readable program for each topic that replaces its per-document judgments. To address these i…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/research-paper
---

# Can Programs Replace LLM Judges? Executable Program Judges for Scalable and Efficient Relevance Labeling

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.24849v1)
- published:: 2026-11-18
- updated:: 2026-11-18
- arxiv_id:: 2611.24849v1
- pdf:: https://arxiv.org/pdf/2611.24849v1
- categories:: cs.IR, cs.CL

## Abstract / Summary
Large language model (LLM) judges have become a common way to create large-scale relevance judgments for retrieval evaluation. However, each judgment requires a potentially expensive call to a frontier model, and the judgments are hard to interpret and may not be reproducible. In this paper, we ask whether an LLM can write a readable program for each topic that replaces its per-document judgments. To address these issues, we propose ExecJudges, a method for generating fast, inspectable and scalable judges for automatic relevance labeling. Specifically, ExecJudges uses a frontier LLM to turn assessment guidelines into executable programs, which rely only on lexical matching, standard NLP libraries like parsers, and pool statistics. An ExecJudges-L variant also uses examples of human labels if available. We evaluate ExecJudges on seven TREC collections by comparing the produced labels with trained NIST assessors, frontier LLM judges, and recently proposed per-topic classifiers. Our results show that ExecJudges agrees with NIST assessors at the level of the Claude Sonnet 5.5 LLM judges on TREC DL 2019-2021. With a small number of human labels per topic, the ExecJudges-L variant agrees with NIST more than per-topic classifiers with the same labels on all seven collections, and either exceeds the agreement of LLM judges provided the same labels or is within about 0.05 of it in Krippendorff's alpha. The labels rank the official TREC DL runs with Kendall's tau of 0.87 to 0.94, and writing the programs incurs a one-time cost of $0.17 to $0.49 per topic, with no additional costs for grading. Our results suggest that ExecJudges offers a reproducible, inspectable, efficient and cost-effective alternative to LLM judges for labeling deep result pools for system evaluation or rankin…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.24849v1)
- [PDF](https://arxiv.org/pdf/2611.24849v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/research-paper
