---
title: "FLOWREADER: Min-Cost Flow Optimization for Multi-Modal Long Document Q&A"
source: "https://arxiv.org/html/2606.07235v1"
author: "Ambuj Mehrish, Sebatiano Vascon"
published: "2026-06-05"
created: 2026-06-09
description: "Long, multimodal documents force retrieval-augmented systems to assemble answers from evidence fragmented across text, tables, and slides broken across cells in a long table, spread over multiple slides, or split between a figure and its discussion. Top-$k$ chunk retrieval treats each fragment independently and cannot represent how evidence connects. We introduce FLOWREADER, which reframes evidence assembly as a min…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/nlp
  - keyword/multimodal
  - keyword/retrieval
  - keyword/evaluation
  - keyword/research-paper
---

# FLOWREADER: Min-Cost Flow Optimization for Multi-Modal Long Document Q&A

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.07235v1)
- published:: 2026-06-05
- updated:: 2026-06-05
- arxiv_id:: 2606.07235v1
- pdf:: https://arxiv.org/pdf/2606.07235v1
- categories:: cs.IR, cs.LG

## Abstract / Summary
Long, multimodal documents force retrieval-augmented systems to assemble answers from evidence fragmented across text, tables, and slides broken across cells in a long table, spread over multiple slides, or split between a figure and its discussion. Top-$k$ chunk retrieval treats each fragment independently and cannot represent how evidence connects. We introduce FLOWREADER, which reframes evidence assembly as a min-cost flow problem on a multimodal node graph: a single scoring vector $h$ controls source selection (via MMR), sink selection (via a length-aware answerability proxy), and the costs and capacities of every edge. The optimal flow is decomposed into candidate evidence paths, a compact non-redundant subset is selected by entropy-regularized replicator dynamics, and parallel VLM workers under a dual-process gate produce the answer with a single System-2 refinement pass triggered when answer consistency is low or the routed flow is strained. On VisDoMBench, FLOWREADER is best on the two subsets dominated by fragmented evidence PaperTab ($58.40$, $+1.30$ over G^{2}-Reader) and SlideVQA ($72.93$, $+0.62$) and competitive on SPIQA, FetaTab, and SciGraphQA. Macro-averaged across all five subsets, FLOWREADER ($65.47$) is within $0.74$ of the strongest baseline (G^{2}-Reader, $66.21$). Overall, these results show that min-cost flow performs well on fragmented multimodal evidence, where top-$k$ retrieval fails. It also provides a unified way to control scoring, routing, selection, and adaptive compute together.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.07235v1)
- [PDF](https://arxiv.org/pdf/2606.07235v1)
- [Large Language Model Reasoning Failures](https://arxiv.org/abs/2602.06176) (2026, citations: 15)
- [OpenAI GPT-5 System Card](https://arxiv.org/abs/2601.03267) (2025, citations: 489)
- [Soft Quality-Diversity Optimization](https://arxiv.org/abs/2512.00810) (2025, citations: 2)
- [Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631) (2025, citations: 1192)
- [Cog-RAG: Cognitive-Inspired Dual-Hypergraph with Theme Alignment Retrieval-Augmented Generation](https://arxiv.org/abs/2511.13201) (2025, citations: 7)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/nlp #keyword/multimodal #keyword/retrieval #keyword/evaluation #keyword/research-paper
