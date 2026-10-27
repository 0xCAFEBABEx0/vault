---
title: "Understanding Jev-Style System One Models: Does Structure Reduce Selection Bias?"
source: "https://arxiv.org/html/2610.35826v1"
author: "Mingyang Song, Mao Zheng, Zhiyuan Ma, Xinpeng Zhou"
published: "2026-10-26"
created: 2026-10-28
description: "Selection bias in large language models (LLMs) can persist despite instructions to ignore presentation order or prompts that elicit reasoning. Recent efforts to reproduce Jev-style System One behavior have produced a growing family of models that predict probabilities directly over supplied candidates. Yet systematic comparisons of selection bias across Jev versions, Jev reproductions, and generative LLMs remain lim…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/benchmark
  - keyword/reasoning
---

# Understanding Jev-Style System One Models: Does Structure Reduce Selection Bias?

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.35826v1)
- published:: 2026-10-26
- updated:: 2026-10-26
- arxiv_id:: 2610.35826v1
- pdf:: https://arxiv.org/pdf/2610.35826v1
- categories:: cs.CL

## Abstract / Summary
Selection bias in large language models (LLMs) can persist despite instructions to ignore presentation order or prompts that elicit reasoning. Recent efforts to reproduce Jev-style System One behavior have produced a growing family of models that predict probabilities directly over supplied candidates. Yet systematic comparisons of selection bias across Jev versions, Jev reproductions, and generative LLMs remain limited in multi-option tasks. This leaves a central question: does Jev-style decision structure reduce selection bias? We address this question with a simple test that shuffles options while keeping question and candidate content fixed. Across two Jev versions, twelve Jev reproductions, and six generative LLMs, we trace individual answers through eight presentations and compare them with fixed-order repetition. On our primary collection of 1,700 questions from two benchmarks, Jev's accuracy varies by less than two percentage points, yet its cumulative failure set expands by 27--29\% relative to the original order, with first failures continuing into the final presentation. This loss of initial successes is substantially larger than under fixed-order repetition, even for highly repeatable Jev reproductions. Nor does Jev show a general advantage over the LLM baselines in preserving correct choices. Aggregation offers limited protection: voting yields modest gains for Jev, while even unanimous answers are frequently wrong. These results expose a gap between repeatable decisions and decisions that remain correct across equivalent presentations, showing why stable accuracy alone cannot establish resistance to selection bias.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.35826v1)
- [PDF](https://arxiv.org/pdf/2610.35826v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark #keyword/reasoning
