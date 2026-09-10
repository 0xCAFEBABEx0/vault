---
title: "Do speech foundation models really learn words?"
source: "https://arxiv.org/html/2609.10434v1"
author: "Robin Huo, Ewan Dunbar"
published: "2026-09-09"
created: 2026-09-11
description: "Self-supervised speech foundation models are now used in a wide array of downstream applications, including traditional speech recognition and as the basis for tokens in speech-aware language models. Attempts to understand their usefulness have largely focused on probing their representations' ability to discriminate phonemes and words. However, discriminative ability for words need not imply specialized representat…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/ai
  - keyword/nlp
---

# Do speech foundation models really learn words?

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.10434v1)
- published:: 2026-09-09
- updated:: 2026-09-09
- arxiv_id:: 2609.10434v1
- pdf:: https://arxiv.org/pdf/2609.10434v1
- categories:: cs.CL, cs.SD

## Abstract / Summary
Self-supervised speech foundation models are now used in a wide array of downstream applications, including traditional speech recognition and as the basis for tokens in speech-aware language models. Attempts to understand their usefulness have largely focused on probing their representations' ability to discriminate phonemes and words. However, discriminative ability for words need not imply specialized representation of words per se. Good discrimination of words may be explained by good encoding of word form (phonemes) rather than form-independent word representations encoding identity or syntactic/semantic properties. By partialling out phoneme information using residualization, we show that, in later layers, HuBERT and wav2vec 2.0 do in general learn representations which encode words with reasonable fidelity independently of local phonetic content. We show that this simple approach to disentanglement can enhance higher-order linguistic information in word discovery tasks.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.10434v1)
- [PDF](https://arxiv.org/pdf/2609.10434v1)
- [SpidR: Learning Fast and Stable Linguistic Units for Spoken Language Models Without Supervision](https://arxiv.org/abs/2512.20308) (2025, citations: 8)
- [Should Top-Down Clustering Affect Boundaries in Unsupervised Word Discovery?](https://arxiv.org/abs/2507.19204) (2025, citations: 4)
- [Discrete Speech Unit Extraction via Independent Component Analysis](https://arxiv.org/abs/2501.06562) (2025, citations: 6)
- [Unsupervised Word Discovery: Boundary Detection with Clustering vs. Dynamic Programming](https://arxiv.org/abs/2409.14486) (2024, citations: 6)
- [Measuring Orthogonality in Representations of Generative Models](https://arxiv.org/abs/2407.03728) (2024, citations: 1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/ai #keyword/nlp
