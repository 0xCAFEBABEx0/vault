---
title: "AI-Driven Reproducibility and Analytical Robustness in Scientific Discovery"
source: "https://arxiv.org/html/2610.23845v1"
author: "Shicheng Liu, Krista Opsahl-Ong, Andrew Drozdov, Julian Killingback, Arnav Singhvi, Ronak Pradeep, Michael Bendersky, James C. Dickerson, Monica S. Lam"
published: "2026-10-16"
created: 2026-10-20
description: "Reproducible and analytically robust research findings are essential to scientific progress, but evaluating these properties typically requires costly manual effort. We investigate whether LLM agents can help automate reproduction and robustness analysis, using a medical case study grounded in the Surveillance, Epidemiology, and End Results (SEER) database, a widely used U.S. cancer registry underlying tens of thous…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/evaluation
  - keyword/benchmark
  - keyword/agents
  - keyword/research-paper
---

# AI-Driven Reproducibility and Analytical Robustness in Scientific Discovery

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.23845v1)
- published:: 2026-10-16
- updated:: 2026-10-16
- arxiv_id:: 2610.23845v1
- pdf:: https://arxiv.org/pdf/2610.23845v1
- categories:: cs.AI, cs.CL

## Abstract / Summary
Reproducible and analytically robust research findings are essential to scientific progress, but evaluating these properties typically requires costly manual effort. We investigate whether LLM agents can help automate reproduction and robustness analysis, using a medical case study grounded in the Surveillance, Epidemiology, and End Results (SEER) database, a widely used U.S. cancer registry underlying tens of thousands of published studies. First, we introduce SEER-Repro, a benchmark of 20 published SEER-based papers together with the data and resources required to reproduce their findings. Second, we create an AI agent that successfully reproduces 77.4% of 2,190 atomic claims, while providing executable baselines for further analysis. Third, we develop an agentic analysis pipeline to test the robustness of the medical findings by identifying analytical choices underlying each finding, proposing defensible alternatives, and rerunning the analysis to determine whether those choices affect the conclusion. Across published papers in SEER-Repro, our pipeline identifies potentially consequential analytical choices in 9.5% of fully reproduced findings and flags them for expert review. These results show how LLM agents can support scientific review by reproducing findings, systematically testing their robustness, and directing expert attention toward potentially consequential analytical choices.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.23845v1)
- [PDF](https://arxiv.org/pdf/2610.23845v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/evaluation #keyword/benchmark #keyword/agents #keyword/research-paper
