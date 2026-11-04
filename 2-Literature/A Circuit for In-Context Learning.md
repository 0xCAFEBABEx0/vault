---
title: "A Circuit for In-Context Learning"
source: "https://arxiv.org/html/2611.05344v1"
author: "Andrew Gao, William Gao"
published: "2026-11-03"
created: 2026-11-05
description: "In-context learning (ICL) lets a pretrained language model perform a task specified by demonstrations in its prompt, with no parameter updates. With arbitrary labels the model must acquire a mapping it cannot have memorized, so the learning happens within a single forward pass. Prior work found candidate parts but not how they compose. We give the composition for few-shot sentence classification with arbitrary label…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/nlp
---

# A Circuit for In-Context Learning

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.05344v1)
- published:: 2026-11-03
- updated:: 2026-11-03
- arxiv_id:: 2611.05344v1
- pdf:: https://arxiv.org/pdf/2611.05344v1
- categories:: cs.CL, cs.LG

## Abstract / Summary
In-context learning (ICL) lets a pretrained language model perform a task specified by demonstrations in its prompt, with no parameter updates. With arbitrary labels the model must acquire a mapping it cannot have memorized, so the learning happens within a single forward pass. Prior work found candidate parts but not how they compose. We give the composition for few-shot sentence classification with arbitrary labels in three 3-4B-parameter transformers. The model implements a key-value memory over label-token positions: each label token's residual stream encodes the label's identity, and middle-layer attention heads write into it the class of the preceding demonstration as its key. At the query, upper-layer heads match the query's class against the stored keys and copy out the matching labels. An early-layer signal encoding whether any label has repeated gates this readout; in its absence the readers attend to the start of the prompt and no label is favored. A separate set of heads suppresses the most recently seen label. Each step is established causally by activation patching, head ablations against random-head baselines, and steering with the model's own signals. A softmax model of the readout with two constants per head, fit on one prompt distribution, predicts another. The computation is conserved across the three models, the named heads alone reproduce the behaviour, and a transformer trained from scratch grows the same parts. The circuit transfers to semantic concepts and to labels with meaning, and the same parts, with a causal gate, appear from 0.6B to 8B in one family and survive instruction tuning. ICL in this setting is a gated associative lookup built from a few identifiable component types, traced causally from demonstrations to prediction.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.05344v1)
- [PDF](https://arxiv.org/pdf/2611.05344v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp
