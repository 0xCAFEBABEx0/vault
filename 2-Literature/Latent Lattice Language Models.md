---
title: "Latent Lattice Language Models"
source: "https://arxiv.org/html/2611.21608v1"
author: "Shivam Duggal, Zongze Wu, William T. Freeman, Antonio Torralba, Richard Zhang, Eli Shechtman"
published: "2026-11-16"
created: 2026-11-18
description: "Language models typically increase per-token computation through deeper or looped layers and latent reasoning steps, while richer residual connections improve information flow across layers. We instead increase computational capacity: the number of active computational states a model maintains. We introduce the Lattice of Latents, a set of per-layer horizontal latent streams that run recurrently along time, alongsid…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/nlp
  - keyword/reasoning
---

# Latent Lattice Language Models

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.21608v1)
- published:: 2026-11-16
- updated:: 2026-11-16
- arxiv_id:: 2611.21608v1
- pdf:: https://arxiv.org/pdf/2611.21608v1
- categories:: cs.LG, cs.AI, cs.CL

## Abstract / Summary
Language models typically increase per-token computation through deeper or looped layers and latent reasoning steps, while richer residual connections improve information flow across layers. We instead increase computational capacity: the number of active computational states a model maintains. We introduce the Lattice of Latents, a set of per-layer horizontal latent streams that run recurrently along time, alongside the vertical residual stream that flows through depth. Like hyper-connections, mHC, and attention or value residuals, the Lattice enhances the residual stream, but rather than adding or rerouting residual pathways through depth, it provides companion computational states that persist across tokens. Unlike hybrid Transformer-SSM architectures, whose recurrent states primarily serve as internal memory for sequence mixing, these latents directly condition the vertical stream's attention, KV-cache writes, MLP computation, and decoding. On Transformers trained on 20B FineWeb-Edu tokens, a 406M-parameter Lattice model lowers validation perplexity from 15.41 to 14.40 over a parameter-matched Transformer. These gains extend across architectural variants. The Lattice composes with prior residual-stream enhancements: with hyper-connections and input residuals, it lowers validation perplexity from 15.41 (base Transformer) and 14.22 (Transformer with the same enhancements) to 13.61. On Gated DeltaNet, Mamba-2, Triadic GDN, and GDN-Mamba-2 hybrids, it improves perplexity at every tested native state size, with Lattice-GDN and Lattice-Triadic-GDN variants outperforming pure baselines with 4x larger native states. These results identify persistent per-layer state as a complementary axis for scaling language-model computation.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.21608v1)
- [PDF](https://arxiv.org/pdf/2611.21608v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp #keyword/reasoning
