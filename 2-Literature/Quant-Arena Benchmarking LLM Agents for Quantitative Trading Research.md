---
title: "Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research"
source: "https://arxiv.org/html/2610.30113v1"
author: "Houde Qian, Zheng Jiang, Wenyi Li, Chenxi Xu, Xinjie Lin, Yuzhao Peng, Ruoyu Han, Youjie Zheng, Kaisen Yang, Qinhuai Na, You Fu, Calvin Xiao"
published: "2026-10-21"
created: 2026-10-23
description: "Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep. Existing benchmarks score formulas, code, or individual trading decisions, leaving open whether large language models (LLMs) can complete this loop and produce strategies that work beyond the research period. We introduce Quant-Arena, a b…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/benchmark
  - keyword/agents
---

# Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.30113v1)
- published:: 2026-10-21
- updated:: 2026-10-21
- arxiv_id:: 2610.30113v1
- pdf:: https://arxiv.org/pdf/2610.30113v1
- categories:: cs.CL, cs.AI, cs.CE

## Abstract / Summary
Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep. Existing benchmarks score formulas, code, or individual trading decisions, leaving open whether large language models (LLMs) can complete this loop and produce strategies that work beyond the research period. We introduce Quant-Arena, a benchmark and public leaderboard for end-to-end quantitative research on real A-share market data. A model constructs features and stock-scoring code, receives feedback only on 2022--2023, and freezes one strategy for assessment on the sealed year 2024. A cash-account evaluator applies trading constraints and costs, including market impact estimated from a simulated order book. Scores are dominated by realized excess return and complemented by signal quality and the diversity of features used by the strategy. We evaluate nine frontier models, among which GPT-6 Astra scores highest; yet no model beats the equal-weight market in 2024. Quant-Arena is open to submissions from any model or agent harness.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.30113v1)
- [PDF](https://arxiv.org/pdf/2610.30113v1)
- [From Knowing to Doing: A Memory-Controlled Benchmark for LLM Trading Agents on Stock Markets](https://arxiv.org/abs/2605.28359) (2026, citations: 11)
- [QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining](https://arxiv.org/abs/2602.07085) (2026, citations: 23)
- [Finance Agent Benchmark: Benchmarking LLMs on Real-world Financial Research Tasks](https://arxiv.org/abs/2508.00828) (2025, citations: 72)
- [AlphaAgent: LLM-Driven Alpha Mining with Regularized Exploration to Counteract Alpha Decay](https://arxiv.org/abs/2502.16789) (2025, citations: 68)
- [Automate Strategy Finding with LLM in Quant investment](https://arxiv.org/abs/2409.06289) (2024, citations: 48)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark #keyword/agents
