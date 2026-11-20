---
title: "Multimodal Error Detection in Chest X-ray Reports: A Large Language Model Reading Image Evidence"
source: "https://arxiv.org/html/2611.26492v1"
author: "Yanda Cheng, Bo Wen, Yuhao Lu"
published: "2026-11-19"
created: 2026-11-21
description: "Rad-Linter checks chest X-ray reports against image-derived evidence to flag potential errors for review. A pretrained image classifier supplies scores for nine pathologies, and a 1.5B-parameter language model, fine-tuned with LoRA on 1,816 examples, checks their consistency with the report. We compare it with a keyword-and-negation rule baseline given the same reports and scores. Evaluation uses controlled report-s…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/multimodal
  - keyword/evaluation
  - keyword/machine-learning
---

# Multimodal Error Detection in Chest X-ray Reports: A Large Language Model Reading Image Evidence

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.26492v1)
- published:: 2026-11-19
- updated:: 2026-11-19
- arxiv_id:: 2611.26492v1
- pdf:: https://arxiv.org/pdf/2611.26492v1
- categories:: cs.CL

## Abstract / Summary
Rad-Linter checks chest X-ray reports against image-derived evidence to flag potential errors for review. A pretrained image classifier supplies scores for nine pathologies, and a 1.5B-parameter language model, fine-tuned with LoRA on 1,816 examples, checks their consistency with the report. We compare it with a keyword-and-negation rule baseline given the same reports and scores. Evaluation uses controlled report-score pairings from OpenI, with consistency labels derived from automatic report labels and score thresholds. Each counterfactual quad crosses two real reports with two real score vectors from other patients, creating two consistent and two inconsistent pairs. Every report and score vector occurs in both conditions, so either input alone permits only 50% accuracy. On 131 quads, Rad-Linter achieves 98.5% pair accuracy versus 80.5% for the rule baseline, and classifies all four pairs correctly in 94.4% of quads versus 56.5%. The checkers perform similarly on omission items, including unmentioned and negated findings; larger differences occur on the remaining item types, which require interpreting how findings are described. The same language model without fine-tuning remains near 50% accuracy. On a second set of 181 quads that also includes reports on which the automatic labelers disagree, pair accuracy is 93.4% versus 75.3%. These controlled results show that, given the same image-derived scores, a trained language model detects report-score inconsistencies more accurately than the tested rule baseline, with the advantage concentrated in interpreting how findings are worded.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.26492v1)
- [PDF](https://arxiv.org/pdf/2611.26492v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/multimodal #keyword/evaluation #keyword/machine-learning
