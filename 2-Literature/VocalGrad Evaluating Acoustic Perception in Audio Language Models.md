---
title: "VocalGrad: Evaluating Acoustic Perception in Audio Language Models"
source: "https://arxiv.org/html/2610.23745v1"
author: "Koki Ryu, Hitomi Yanaka"
published: "2026-10-16"
created: 2026-10-20
description: "Recent large audio language models (LALMs) have extended their capabilities beyond lexical speech understanding to tasks requiring paralinguistic and non-linguistic audio understanding, such as emotion recognition. However, these models still struggle to reliably utilize acoustic information, particularly when it co-occurs with spoken linguistic content. Existing benchmarks do not clearly distinguish acoustic percep…"
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

# VocalGrad: Evaluating Acoustic Perception in Audio Language Models

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.23745v1)
- published:: 2026-10-16
- updated:: 2026-10-16
- arxiv_id:: 2610.23745v1
- pdf:: https://arxiv.org/pdf/2610.23745v1
- categories:: cs.SD, cs.CL

## Abstract / Summary
Recent large audio language models (LALMs) have extended their capabilities beyond lexical speech understanding to tasks requiring paralinguistic and non-linguistic audio understanding, such as emotion recognition. However, these models still struggle to reliably utilize acoustic information, particularly when it co-occurs with spoken linguistic content. Existing benchmarks do not clearly distinguish acoustic perception from higher-level reasoning, making it difficult to identify the source of these failures. To address this issue, we introduce VocalGrad, a benchmark designed to evaluate LALMs' ability to perceive low-level acoustic variations. VocalGrad formulates this problem as a simple binary classification of temporal change direction, enabling evaluation largely independent of higher-level reasoning or semantic understanding. Our benchmark results reveal a substantial gap in acoustic perception between human annotators and state-of-the-art LALMs: while human annotators achieve high accuracy, LALMs perform at near-chance levels. We further conduct linear probing to identify structural bottlenecks in these models. Our analysis reveals two distinct failure modes: for some categories, task-relevant information is preserved in internal representations but not utilized by the language model head; for others, the information becomes progressively less linearly decodable across model layers. Overall, our results reveal substantial limitations of LALMs in modeling acoustic variation under controlled settings and expose representation differences not observable from text outputs.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.23745v1)
- [PDF](https://arxiv.org/pdf/2610.23745v1)
- [The Illusion of Stochasticity in LLMs](https://arxiv.org/abs/2604.06543) (2026, citations: 8)
- [MiMo-Audio: Audio Language Models are Few-Shot Learners](https://arxiv.org/abs/2512.23808) (2025, citations: 150)
- [Do Audio LLMs Really LISTEN, or Just Transcribe? Measuring Lexical vs. Acoustic Emotion Cues Reliance](https://arxiv.org/abs/2510.10444) (2025, citations: 42)
- [Transcribe, Translate, or Transliterate: An Investigation of Intermediate Representations in Spoken Language Models](https://arxiv.org/abs/2510.02569) (2025, citations: 5)
- [When Silence Matters: The Impact of Irrelevant Audio on Text Reasoning in Large Audio-Language Models](https://arxiv.org/abs/2510.00626) (2025, citations: 11)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/multimodal #keyword/evaluation #keyword/benchmark #keyword/reasoning
