---
title: "MedPhysBench: A Benchmark for Evaluating Language Models on Medical Physics Calculations and Error Detection"
source: "https://arxiv.org/html/2611.05340v1"
author: "Omar Nusrat"
published: "2026-11-03"
created: 2026-11-05
description: "Medical physicists turn a prescription into a delivered dose and check one another's calculations, because one error in a beam calibration or a monitor-unit (MU) calculation can affect every patient treated with it. MedPhysBench has ten seeded generators of calculation items in radiation therapy, diagnostic imaging, nuclear medicine and radiation protection, up to clinical tasks such as a TG-51 calibration worksheet…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/benchmark
---

# MedPhysBench: A Benchmark for Evaluating Language Models on Medical Physics Calculations and Error Detection

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.05340v1)
- published:: 2026-11-03
- updated:: 2026-11-03
- arxiv_id:: 2611.05340v1
- pdf:: https://arxiv.org/pdf/2611.05340v1
- categories:: physics.med-ph, cs.AI, cs.CL

## Abstract / Summary
Medical physicists turn a prescription into a delivered dose and check one another's calculations, because one error in a beam calibration or a monitor-unit (MU) calculation can affect every patient treated with it. MedPhysBench has ten seeded generators of calculation items in radiation therapy, diagnostic imaging, nuclear medicine and radiation protection, up to clinical tasks such as a TG-51 calibration worksheet. Reference answers come from code implementing the governing protocols, and a grader converts units and applies tolerance bands. From the same inputs, separate checking items test error detection, showing a colleague's worksheet or only the colleague's result, half correct and half with one planted error. On a held-out test split of 1,200 items (half for two models), 12 models scored 33.3 to 100.0% on calculation. Of the nine answers graded incorrect for the four best (99.3-100.0%), five contained model errors and four followed NCRP Report 151 on points our items misstate or leave open. Below them, most models did worst on level-3 clinical tasks, and Claude Sonnet 5.5 omitted the inverse-square correction in 19 of 20 isocentric MU items. Five models detected at least 96.7% of mostly large planted errors with at most 4% false alarms; for four of the other seven, checking only the result raised false alarms significantly. In an exploratory targeted test with 20 public cases of an omitted inverse-square correction, the three best models tested caught it in every worksheet, and three weaker models accepted 16 to 18 of 20 planted worksheets, one of them while applying the correction in most of its own calculations. Claude Opus 5.5 accepted 6 of 20 wrong results, although it applied the correction in all 20 of its own. We report the effect of two problems in our…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.05340v1)
- [PDF](https://arxiv.org/pdf/2611.05340v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark
