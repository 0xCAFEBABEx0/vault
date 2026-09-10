---
title: "Building Multilingual Bridges: Data Mixing as the Pillar of Generalization for In-Language Reasoning"
source: "https://arxiv.org/html/2609.10445v1"
author: "Mehrnaz Mofakhami, Ananya Sahu, Alejandro R. Salamanca, Daniel D'souza, Alexandre Berard, Thomas Euyang, Marzieh Fadaee, Julia Kreutzer"
published: "2026-09-09"
created: 2026-09-11
description: "Reasoning language models have made substantial advances on a variety of complex tasks, yet their capabilities remain overwhelmingly English-centric: models primarily reason in English regardless of the language they are prompted in. This is inaccessible for non-English-speaking users, risks losing the intent of the original question, and forgoes knowledge more readily expressed in the target language. In this work,…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/benchmark
  - keyword/reasoning
---

# Building Multilingual Bridges: Data Mixing as the Pillar of Generalization for In-Language Reasoning

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.10445v1)
- published:: 2026-09-09
- updated:: 2026-09-09
- arxiv_id:: 2609.10445v1
- pdf:: https://arxiv.org/pdf/2609.10445v1
- categories:: cs.CL

## Abstract / Summary
Reasoning language models have made substantial advances on a variety of complex tasks, yet their capabilities remain overwhelmingly English-centric: models primarily reason in English regardless of the language they are prompted in. This is inaccessible for non-English-speaking users, risks losing the intent of the original question, and forgoes knowledge more readily expressed in the target language. In this work, we advance L2 reasoning, the ability of a model to reason consistently in the language of the user's prompt, thus building an in-language bridge between the prompt and the answer. We approach this problem from a data-centric angle, investigating how to optimize data composition and scheduling in SFT for reasoning generalization. Building Tiny Aya L2-Thinker at 3.35B scale, we achieve an L2 reasoning rate above 93% across 60 languages on 6 benchmarks spanning math, commonsense reasoning, instruction following, open-ended generation, and cultural reasoning while keeping performance strong. We show the path to generalizing L2 reasoning to held-out languages goes through broader language coverage, readily available multilingual non-reasoning data, and a sufficient English reasoning backbone. These findings indicate that reasoning is a language-agnostic behavior that can be transferred across typologically diverse languages through careful data mixing and without requiring reasoning supervision in every target language. We release our model weights and multilingual reasoning data to support further research on accessible, in-language reasoning.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.10445v1)
- [PDF](https://arxiv.org/pdf/2609.10445v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/reasoning
