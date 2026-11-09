---
title: "Are These Programmers Ripe Enough to Eat? Evaluating How LLMs Handle Lexical Knowledge Conflicts in Translation"
source: "https://arxiv.org/html/2611.09785v1"
author: "Dongxu Wu, Sara Court, Micha Elsner"
published: "2026-11-06"
created: 2026-11-10
description: "External lexical resources can help large language models (LLMs) translate texts in low-resource languages and specialized domains, but these resources may conflict with models' prior lexical knowledge. To isolate this conflict, we construct a controlled Mandarin-to-English translation task in which familiar source words are assigned new meanings within and across semantic categories. We treat these prompt-supplied…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/reasoning
---

# Are These Programmers Ripe Enough to Eat? Evaluating How LLMs Handle Lexical Knowledge Conflicts in Translation

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.09785v1)
- published:: 2026-11-06
- updated:: 2026-11-06
- arxiv_id:: 2611.09785v1
- pdf:: https://arxiv.org/pdf/2611.09785v1
- categories:: cs.CL, cs.LG

## Abstract / Summary
External lexical resources can help large language models (LLMs) translate texts in low-resource languages and specialized domains, but these resources may conflict with models' prior lexical knowledge. To isolate this conflict, we construct a controlled Mandarin-to-English translation task in which familiar source words are assigned new meanings within and across semantic categories. We treat these prompt-supplied meanings as contextual knowledge (CK) and systematically evaluate the effects of word frequency, sentence context, and prompt framing on the translated outputs. Across nine models, CK reliance is greater for less frequent source words and in sentence contexts that support the supplied meanings. Prompt framing can reduce CK reliance, but seven of nine models favor CK even when explicitly instructed to ignore the supplied meanings. Within model families, larger models are more likely than smaller models to utilize CK in their outputs. Three follow-up experiments further show that modal weakening lowers CK reliance, the effect of repetition depends on prompt layout, and the effect of reasoning varies across models. Overall, our controlled study reveals how CK reliance varies across conditions and models, motivating new methods to detect and evaluate lexical conflicts and guide models' lexical choices in LLM-based translation.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.09785v1)
- [PDF](https://arxiv.org/pdf/2611.09785v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/reasoning
