---
title: "WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data"
source: "https://arxiv.org/html/2609.05405v1"
author: "Ji Soo Lee, Xilun Chen, Pierce Chuang, Ashish Shenoy, Jason Wei, Dohwan Ko, Hyunwoo J. Kim, Benoit Corda"
published: "2026-09-04"
created: 2026-09-08
description: "Recent advances in wearable sensing enable continuous monitoring of physiological and behavioral signals, yet existing benchmarks rarely evaluate whether AI systems can reason over a real user's longitudinal wearable record. We introduce WearableQA, a benchmark comprising 4,084 10-option multiple-choice questions constructed from the wearable time series, blood biomarkers, and demographics of 200 real users, each wi…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/evaluation
  - keyword/benchmark
  - keyword/reasoning
---

# WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.05405v1)
- published:: 2026-09-04
- updated:: 2026-09-04
- arxiv_id:: 2609.05405v1
- pdf:: https://arxiv.org/pdf/2609.05405v1
- categories:: cs.CL

## Abstract / Summary
Recent advances in wearable sensing enable continuous monitoring of physiological and behavioral signals, yet existing benchmarks rarely evaluate whether AI systems can reason over a real user's longitudinal wearable record. We introduce WearableQA, a benchmark comprising 4,084 10-option multiple-choice questions constructed from the wearable time series, blood biomarkers, and demographics of 200 real users, each with up to 500 days of daily measurements. WearableQA preserves authentic wearable distributions that include device noise and inter-individual variability. To evaluate distinct reasoning capabilities, we introduce 16 question types organized along two complementary axes: data versus health reasoning, which distinguishes computation over longitudinal measurements from physiological interpretation; and single- versus cross-signal reasoning, which separates reasoning about individual signals from the integration of multiple signals. To construct reliable questions at scale, we adopt a dual-grounding framework that combines literature-grounded physiological findings with statistically validated population-grounded physiological patterns. This enables the capture of meaningful relationships observed in real-world wearable data. Evaluation of 14 proprietary and open-source LLMs demonstrates that WearableQA effectively differentiates model capabilities, with performance ranging from 19.6% to 72.9% against a 10% chance baseline. Moreover, WearableQA remains far from solved: most models achieve accuracies below 60%. Overall, WearableQA provides a realistic and diagnostic benchmark for evaluating LLM reasoning over real-world wearable data.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.05405v1)
- [PDF](https://arxiv.org/pdf/2609.05405v1)
- [Towards a General Intelligence and Interface for Wearable Health Data](https://arxiv.org/abs/2605.22759) (2026, citations: 3)
- [TimeSeriesExamAgent: Creating Time Series Reasoning Benchmarks at Scale](https://arxiv.org/abs/2604.10291) (2026, citations: 2)
- [TSAQA: Time Series Analysis Question And Answering Benchmark](https://arxiv.org/abs/2601.23204) (2026, citations: 5)
- [OpenAI GPT-5 System Card](https://arxiv.org/abs/2601.03267) (2025, citations: 804)
- [A personal health large language model for sleep and fitness coaching](https://doi.org/10.1038/s41591-025-03888-0) (2025, citations: 63)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/evaluation #keyword/benchmark #keyword/reasoning
