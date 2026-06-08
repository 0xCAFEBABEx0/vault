---
title: "How reliable are LLMs when it comes to playing dice?"
source: "https://arxiv.org/html/2606.07515v1"
author: "Luca Avena, Gianmarco Bet, Bernardo Busoni"
published: "2026-06-05"
created: 2026-06-09
description: "We investigate the probabilistic reasoning capabilities of large language models through a controlled benchmarking study on discrete probability problems. We constructed two datasets, respectively a set of standard exercises and a set of counterintuitive exercises, designed to trigger heuristic reasoning, and evaluated 8 state-of-the-art models, each tested with and without Chain-of-Thought prompting. Models achieve…"
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
  - keyword/reasoning
---

# How reliable are LLMs when it comes to playing dice?

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.07515v1)
- published:: 2026-06-05
- updated:: 2026-06-05
- arxiv_id:: 2606.07515v1
- pdf:: https://arxiv.org/pdf/2606.07515v1
- categories:: cs.CL, cs.AI, cs.HC, math.PR

## Abstract / Summary
We investigate the probabilistic reasoning capabilities of large language models through a controlled benchmarking study on discrete probability problems. We constructed two datasets, respectively a set of standard exercises and a set of counterintuitive exercises, designed to trigger heuristic reasoning, and evaluated 8 state-of-the-art models, each tested with and without Chain-of-Thought prompting. Models achieve an average accuracy of 0.96 on standard problems but only 0.59 on counterintuitive ones. We further provide empirical evidence of token bias: performance drops by over 20% when canonical formulations are replaced by disguised variants. Embedding misleading suggestions in the prompt reduces performance by up to 34%, with no model proving immune. Taken together, the reported findings suggest that current LLMs are not yet genuine probabilistic reasoners, despite their success in advanced mathematical problems.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.07515v1)
- [PDF](https://arxiv.org/pdf/2606.07515v1)
- [Beyond Benchmarks: MathArena as an Evaluation Platform for Mathematics with LLMs](https://arxiv.org/abs/2605.00674) (2026, citations: 26)
- [Mathematical exploration and discovery at scale](https://arxiv.org/abs/2511.02864) (2025, citations: 60)
- [BrokenMath: A Benchmark for Sycophancy in Theorem Proving with LLMs](https://arxiv.org/abs/2510.04721) (2025, citations: 15)
- [A Peek into Token Bias: Large Language Models Are Not Yet Genuine Reasoners](https://arxiv.org/abs/2406.11050) (2024, citations: 117)
- [(Ir)rationality and cognitive biases in large language models](https://arxiv.org/abs/2402.09193) (2024, citations: 50)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/reasoning
