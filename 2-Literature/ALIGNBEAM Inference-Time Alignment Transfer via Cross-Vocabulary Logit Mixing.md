---
title: "ALIGNBEAM : Inference-Time Alignment Transfer via Cross-Vocabulary Logit Mixing"
source: "https://arxiv.org/html/2606.12342v1"
author: "Chirag Chawla, Pratinav Seth, Vinay Kumar Sankarapu"
published: "2026-06-10"
created: 2026-06-12
description: "Domain fine-tuning degrades the safety of large language models: fine-tuned specialists readily comply with harmful prompts framed in domain language. Existing inference-time defenses that mix logits from a safe anchor model require both models to share a vocabulary, which rules them out for the cross-family specialists where safety is most degraded. We present ALIGNBEAM, a training-free method that lifts this restr…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/benchmark
  - keyword/safety
  - keyword/machine-learning
---

# ALIGNBEAM : Inference-Time Alignment Transfer via Cross-Vocabulary Logit Mixing

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.12342v1)
- published:: 2026-06-10
- updated:: 2026-06-10
- arxiv_id:: 2606.12342v1
- pdf:: https://arxiv.org/pdf/2606.12342v1
- categories:: cs.CL, cs.AI, cs.ET, cs.LG

## Abstract / Summary
Domain fine-tuning degrades the safety of large language models: fine-tuned specialists readily comply with harmful prompts framed in domain language. Existing inference-time defenses that mix logits from a safe anchor model require both models to share a vocabulary, which rules them out for the cross-family specialists where safety is most degraded. We present ALIGNBEAM, a training-free method that lifts this restriction by translating anchor logits into the target model's vocabulary token-by-token at each decoding step; a small LLM judge then selects the safest among K candidate continuations. No weights are changed, and the safety-utility trade-off can be tuned at deployment without retraining. Across both cross-vocabulary and same-vocabulary evaluation pairs, ALIGNBEAM substantially raises refusal on adversarial benchmarks while keeping task accuracy and inference overhead within practical bounds. The results show that safety alignment can be transferred between model families at inference time, without touching either model's weights.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.12342v1)
- [PDF](https://arxiv.org/pdf/2606.12342v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark #keyword/safety #keyword/machine-learning
