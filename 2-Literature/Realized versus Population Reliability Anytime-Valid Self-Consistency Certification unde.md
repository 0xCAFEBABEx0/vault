---
title: "Realized versus Population Reliability: Anytime-Valid Self-Consistency Certification under Correlated Reasoning"
source: "https://arxiv.org/html/2611.26592v1"
author: "Terence D. Agbeyegbe, Toneukarin G. Agbeyegbe"
published: "2026-11-19"
created: 2026-11-22
description: "Self-consistency certification treats repeated sampling from a language model as sequential evidence accumulation and stops when an anytime-valid e-process crosses a threshold, guaranteeing finite-sample Type I error control by Ville's inequality. Prior constructions assume sampled rollouts are conditionally independent. We show this assumption fails in practice: reasoning streams are positively correlated through s…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/reasoning
---

# Realized versus Population Reliability: Anytime-Valid Self-Consistency Certification under Correlated Reasoning

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.26592v1)
- published:: 2026-11-19
- updated:: 2026-11-19
- arxiv_id:: 2611.26592v1
- pdf:: https://arxiv.org/pdf/2611.26592v1
- categories:: stat.ME, cs.AI, cs.LG

## Abstract / Summary
Self-consistency certification treats repeated sampling from a language model as sequential evidence accumulation and stops when an anytime-valid e-process crosses a threshold, guaranteeing finite-sample Type I error control by Ville's inequality. Prior constructions assume sampled rollouts are conditionally independent. We show this assumption fails in practice: reasoning streams are positively correlated through shared reasoning prefixes or across-prompt heterogeneity, changing not merely certificate efficiency but the hypothesis certified. Modeling dependence via a per-unit latent state (the random-effects / intraclass-correlation structure) induces exchangeable, equi-correlated increments with correlation $ρ$. Correlation splits the single null into a realized null about the drawn belief and a population null about average model behavior, which coincide only when $ρ=0$. We show: (i) the standard betting e-process remains anytime-valid for the realized null, not the population null; (ii) read as a population-null test, a suitable mixture has asymptotic crossing probability at least $π=P(μ(Z)>0)$, potentially exceeding nominal $ε$; (iii) the within-unit mean's effective sample size saturates at $1/ρ$, so extra within-unit rollouts cannot restore population validity; and (iv) a prompt-level e-process restores population validity, with optimal allocation at one rollout per prompt under a pure rollout budget. Simulations and Claude Haiku 4.5 rollouts confirm this regime dependence: on GSM8K ($\hatρ=0.435$, $\hatθ=+0.96$) the gap is dormant, whereas on AIME ($\hatρ=0.480$, $\hatθ=-0.15$) the single-unit rule crosses on 24% of prompts at nominal $ε=0.05$, while the prompt-level procedure declines (0.00). This correctness result identifies which reliability claim an anytim…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.26592v1)
- [PDF](https://arxiv.org/pdf/2611.26592v1)
- [CITE: Anytime-Valid Statistical Inference in LLM Self-Consistency](https://arxiv.org/abs/2605.05873) (2026, citations: 6)
- [Certified Self-Consistency: Statistical Guarantees and Test-Time Training for Reliable Reasoning in LLMs](https://arxiv.org/abs/2510.17472) (2025, citations: 19)
- [Anytime-Valid Answer Sufficiency Certificates for LLM Generation via Sequential Information Lift](https://arxiv.org/abs/2510.06478) (2025, citations: 6)
- [Asymptotically Optimal Sequential Multiple Testing Procedures for Correlated Normal](https://arxiv.org/abs/2309.16657) (2023, citations: 2)
- [Game-theoretic statistics and safe anytime-valid inference](https://arxiv.org/abs/2210.01948) (2022, citations: 378)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/reasoning
