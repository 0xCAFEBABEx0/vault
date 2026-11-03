---
title: "Palette: teaching a small model to build decks in your design language"
source: "https://huggingface.co/blog/ibm-research/palette-deck-building"
author: "Hugging Face Blog"
published: "2026-11-03"
created: 2026-11-04
description: "Both of those point to a model you own: open weights, running on your own infrastructure, trained on your own design language. The catch is that small open models, the kind you'd actually self-host, are bad at this. Their decks come out broken: titles that vanish into the background, text running off the slide, shapes stacked on top of each other. Palette tests one bet: that a small open-weight model, trained on syn…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/nlp
  - keyword/machine-learning
---

# Palette: teaching a small model to build decks in your design language

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/ibm-research/palette-deck-building)
- published:: 2026-11-03

## Abstract / Summary
Both of those point to a model you own: open weights, running on your own infrastructure, trained on your own design language. The catch is that small open models, the kind you'd actually self-host, are bad at this. Their decks come out broken: titles that vanish into the background, text running off the slide, shapes stacked on top of each other. Palette tests one bet: that a small open-weight model, trained on synthetic data in your design language and checked by a harness, can compete with frontier systems while you keep ownership of the result. We fine-tuned a 20B model to build decks the way people do: a designer plans the deck and a coder draws each slide. Its training data follows the IBM Design Language , and on PresentBench it ranks first on two of the three domains we measured. This post covers how we synthesized the data, trai… Why decks are hard for small models A slide deck looks simple, but making one asks a model to do three things small models are bad at. It lays out the slide without seeing it. The model doesn't draw slides; it writes code that places every element at an x, y, width and font size. Whether a 75-character title fits on two lines at 56pt is arithmeti…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/nlp #keyword/machine-learning
