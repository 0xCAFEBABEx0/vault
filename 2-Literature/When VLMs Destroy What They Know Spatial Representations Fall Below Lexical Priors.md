---
title: "When VLMs Destroy What They Know: Spatial Representations Fall Below Lexical Priors"
source: "https://arxiv.org/html/2610.13910v1"
author: "Shubh Garg, Chen Shani"
published: "2026-10-09"
created: 2026-10-14
description: "Vision-Language Models (VLMs) increasingly analyze and reason about images, yet it remains unclear whether their internal representations faithfully encode the structured relations required for such reasoning. We introduce EICS (Evaluation-Invariant Concept Stability), a metric for testing whether representations consistently encode concepts under controlled one-concept interventions, and CASP-VL (Causally controlle…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/multimodal
  - keyword/evaluation
  - keyword/benchmark
  - keyword/reasoning
---

# When VLMs Destroy What They Know: Spatial Representations Fall Below Lexical Priors

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.13910v1)
- published:: 2026-10-09
- updated:: 2026-10-09
- arxiv_id:: 2610.13910v1
- pdf:: https://arxiv.org/pdf/2610.13910v1
- categories:: cs.CL

## Abstract / Summary
Vision-Language Models (VLMs) increasingly analyze and reason about images, yet it remains unclear whether their internal representations faithfully encode the structured relations required for such reasoning. We introduce EICS (Evaluation-Invariant Concept Stability), a metric for testing whether representations consistently encode concepts under controlled one-concept interventions, and CASP-VL (Causally controlled Spatial Perturbations for Vision-Language models), a benchmark of causally controlled spatial perturbations derived from Visual Genome scene graphs. Across multiple VLM architectures, we find that spatial relations are represented substantially less faithfully than lexical information, even when the same models score well above chance on compositional benchmarks. Further analysis shows that the relation is identifiable at the predicate's own tokens but is lost when the sentence is aggregated into a global representation, whether through the (EOS) token or by mean pooling. These findings reveal a systematic failure invisible to output-based evaluation: VLMs do not preserve, in the representation used downstream, relational information that is present in their own input.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.13910v1)
- [PDF](https://arxiv.org/pdf/2610.13910v1)
- [CS-CLIP: Compositional Scene Graph-guided CLIP for Robust Compositional Reasoning](https://arxiv.org/abs/2609.08242) (2026, citations: 1)
- [Cross-Modal Masked Compositional Concept Modeling for Enhancing Visio-Linguistic Compositionality](https://arxiv.org/abs/2606.13288) (2026, citations: 1)
- [Same Answer, Different Representations: Hidden instability in VLMs](https://arxiv.org/abs/2602.06652) (2026, citations: 3)
- [CF-VLM:CounterFactual Vision-Language Fine-tuning](https://arxiv.org/abs/2506.17267) (2025, citations: 75)
- [From Tokens to Thoughts: How LLMs and Humans Trade Compression for Meaning](https://arxiv.org/abs/2505.17117) (2025, citations: 39)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/multimodal #keyword/evaluation #keyword/benchmark #keyword/reasoning
