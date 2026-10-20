---
title: "Competing Learning in Hybrid Architectures"
source: "https://arxiv.org/html/2610.26830v1"
author: "Xingyu Shen, Yingfa Chen, Ziqing Qiao, Chaojun Xiao, Xu Han, Zhiyuan Liu"
published: "2026-10-19"
created: 2026-10-21
description: "Many modern language models have adopted hybrid architectures that incorporate both linear-time recurrence and softmax attention. Modern recurrence layers provide a highly expressive mixing mechanism while ensuring high throughput by compressing contextual information into a fixed-size state, but underperform softmax attention in contextual information retrieval. In this paper, we reveal a Competing Learning phenome…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/reasoning
  - keyword/machine-learning
  - keyword/research-paper
---

# Competing Learning in Hybrid Architectures

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.26830v1)
- published:: 2026-10-19
- updated:: 2026-10-19
- arxiv_id:: 2610.26830v1
- pdf:: https://arxiv.org/pdf/2610.26830v1
- categories:: cs.CL

## Abstract / Summary
Many modern language models have adopted hybrid architectures that incorporate both linear-time recurrence and softmax attention. Modern recurrence layers provide a highly expressive mixing mechanism while ensuring high throughput by compressing contextual information into a fixed-size state, but underperform softmax attention in contextual information retrieval. In this paper, we reveal a Competing Learning phenomenon where different kinds of mixers compete to learn the same function, and when any layer learns a function, it suppresses the corresponding learning signal for other layers. Layer attribution analysis reveals that under typical data distributions, modern recurrence learns retrieval functions faster than softmax attention, causing attention to fail to learn retrieval in most cases. Stopping weight updates in recurrence in the middle of training helps attention learn retrieval. Based on these results, we propose a staged training procedure for pre-training hybrid architectures on natural language. Empirical results on models up to 1B parameters show that our method results in substantial improvement in language modeling loss, common-sense reasoning, as well as a wide range of retrieval-related tasks across different context lengths.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.26830v1)
- [PDF](https://arxiv.org/pdf/2610.26830v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/reasoning #keyword/machine-learning #keyword/research-paper
