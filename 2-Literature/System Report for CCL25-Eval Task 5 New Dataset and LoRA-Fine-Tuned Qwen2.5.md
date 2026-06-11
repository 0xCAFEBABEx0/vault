---
title: "System Report for CCL25-Eval Task 5: New Dataset and LoRA-Fine-Tuned Qwen2.5"
source: "https://arxiv.org/html/2606.12392v1"
author: "Haotao Xie"
published: "2026-06-10"
created: 2026-06-12
description: "Recently, large language models (LLMs) have achieved promising progress in the fields of classical Chinese translation and the generation of classical poetry. However, domain-specific research on precise translation and affective-semantic understanding of classical poetry remains limited. The main challenge is that most studies treat the poetic appreciation task as a general-domain problem, neglecting the distinctiv…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/benchmark
  - keyword/safety
  - keyword/machine-learning
---

# System Report for CCL25-Eval Task 5: New Dataset and LoRA-Fine-Tuned Qwen2.5

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.12392v1)
- published:: 2026-06-10
- updated:: 2026-06-10
- arxiv_id:: 2606.12392v1
- pdf:: https://arxiv.org/pdf/2606.12392v1
- categories:: cs.CL, cs.AI

## Abstract / Summary
Recently, large language models (LLMs) have achieved promising progress in the fields of classical Chinese translation and the generation of classical poetry. However, domain-specific research on precise translation and affective-semantic understanding of classical poetry remains limited. The main challenge is that most studies treat the poetic appreciation task as a general-domain problem, neglecting the distinctive features of poetic appreciation, while high-quality and domain-specific datasets are extremely limited. To address this limitation, we decompose the task into three subtasks: term interpretation, semantic interpretation, and emotional inference. Based on multiple open-source datasets, we perform data cleansing and alignment to construct the Classical Chinese Poetry Instruction Pair Dataset (CCPoetry-49K), which comprises 49,404 high-quality instruction-response pairs explicitly optimized for this domain. We then propose a domain-specialized LLM, called PoetryQwen, by applying Low-Rank Adaptation (LoRA) to fine-tune the Qwen2.5-14B model. Experimental results on the CCL25-Eval Task 5 benchmark demonstrate that PoetryQwen achieves a score of 0.757, representing a 9.7% improvement over the Qwen2.5-14B-Instruct baseline (0.690). These findings clearly indicate that PoetryQwen significantly enhances performance in precise translation and emotional understanding of classical poetry. We present new dataset and methodological considerations intended to support the domain-specific optimization of LLMs.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.12392v1)
- [PDF](https://arxiv.org/pdf/2606.12392v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark #keyword/safety #keyword/machine-learning
