---
title: "It's Not RoPE that Creates Sinks: The Role of Self-Concentration and Value-Non-Mixing in Attention"
source: "https://arxiv.org/html/2609.09085v1"
author: "Raito Kiya, Satoki Ohashi, Kosuke Sato, Go Kamoda, Ryosuke Takahashi, Yuji Yamamoto, Daiki Shiono, Keisuke Sakaguchi, Goro Kobayashi"
published: "2026-09-08"
created: 2026-09-10
description: "Large Language Models (LLMs) often exhibit 'Attention Sink' (AS) and the accompanying 'Massive Activations' (MAs) at the initial position of a sequence. These phenomena frequently co-occur, and MAs can pose challenges for low-bit quantization. In this study, we analyze the factors underlying AS and MAs that emerge at the initial position regardless of the token occupying it. Our experiments suggest that self-concent…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/nlp
---

# It's Not RoPE that Creates Sinks: The Role of Self-Concentration and Value-Non-Mixing in Attention

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.09085v1)
- published:: 2026-09-08
- updated:: 2026-09-08
- arxiv_id:: 2609.09085v1
- pdf:: https://arxiv.org/pdf/2609.09085v1
- categories:: cs.CL

## Abstract / Summary
Large Language Models (LLMs) often exhibit "Attention Sink" (AS) and the accompanying "Massive Activations" (MAs) at the initial position of a sequence. These phenomena frequently co-occur, and MAs can pose challenges for low-bit quantization. In this study, we analyze the factors underlying AS and MAs that emerge at the initial position regardless of the token occupying it. Our experiments suggest that self-concentration of attention, resulting from the causal mask, and the subsequent Value-non-mixing in attention outputs contribute to AS and MAs. These findings provide new empirical evidence on the internal dynamics of LLMs, offering insights that may inform future quantization strategies and advance our understanding of the internal mechanisms of attention layers.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.09085v1)
- [PDF](https://arxiv.org/pdf/2609.09085v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp
