---
title: "Represented but misread: Post-training changes how language models read out what they represent"
source: "https://arxiv.org/html/2611.26584v1"
author: "Jochen Laubrock"
published: "2026-11-19"
created: 2026-11-21
description: "Does post-training change what a language model represents, or how this representation is read out into an answer? We compared linear probes with the models' own answers, analyzed with signal detection theory, in six open-weight base models and their post-trained versions. For judgments of whether German texts were written by a human or an AI, probes and word n-gram classifiers separated the classes well, but the an…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/machine-learning
  - keyword/research-paper
---

# Represented but misread: Post-training changes how language models read out what they represent

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.26584v1)
- published:: 2026-11-19
- updated:: 2026-11-19
- arxiv_id:: 2611.26584v1
- pdf:: https://arxiv.org/pdf/2611.26584v1
- categories:: cs.CL, cs.LG

## Abstract / Summary
Does post-training change what a language model represents, or how this representation is read out into an answer? We compared linear probes with the models' own answers, analyzed with signal detection theory, in six open-weight base models and their post-trained versions. For judgments of whether German texts were written by a human or an AI, probes and word n-gram classifiers separated the classes well, but the answers did not and often ordered the texts inversely. Post-training lowered the sensitivity of the answers on average ($Δd' = -0.34$ across model families; -0.29 across three prompts). It also changed the use of a stated base rate: Base models shifted their log-odds by less than the stated change in prior odds, most post-trained models by more. In two models with stage-wise checkpoints, the change occurred during supervised fine-tuning, model stitching implicated the early layers, and from mid-depth on internal states at positions after the text, not those of the text, transferred the change between checkpoints. Our corpora cannot be shared, so we add a case reproducible from public data, the truth of negated statements. Here, post-training acted in the opposite direction: Probes decoded truth at or near ceiling in every model, the answers of several base models did not use it, and post-training repaired them; by mid-depth the repair resided at the positions after the statement; below it, the representation of the statement contributed, strongly in one of four models. In a training study, adding 2,000 correctly labeled authorship judgments of news texts to otherwise identical fine-tuning data improved the answers on our newspaper and textbook corpora and inverted them on the chats, where they followed a news-trained probe of the base model. Post-training thus…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.26584v1)
- [PDF](https://arxiv.org/pdf/2611.26584v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/machine-learning #keyword/research-paper
