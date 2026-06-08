---
title: "A robust PPG foundation model using multimodal physiological supervision"
source: "https://arxiv.org/html/2606.07365v1"
author: "Eloy Geenjaar, Vince Calhoun, Scott Daly, Gouthaman KV, Lie Lu, Trisha Mittal, Daniel P. Darcy"
published: "2026-06-05"
created: 2026-06-09
description: "Photoplethysmography (PPG), a non-invasive measure of changes in blood volume, is widely used in both wearable devices and clinical settings. Recent PPG foundation models either use open-source ICU datasets with pretraining paradigms that require curated data and thus complicate generalization to field-like data, or use closed-source field-like PPG data. In contrast, we propose a PPG foundation model that does not r…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/ai
  - keyword/multimodal
  - keyword/retrieval
  - keyword/machine-learning
---

# A robust PPG foundation model using multimodal physiological supervision

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.07365v1)
- published:: 2026-06-05
- updated:: 2026-06-05
- arxiv_id:: 2606.07365v1
- pdf:: https://arxiv.org/pdf/2606.07365v1
- categories:: cs.LG, cs.AI

## Abstract / Summary
Photoplethysmography (PPG), a non-invasive measure of changes in blood volume, is widely used in both wearable devices and clinical settings. Recent PPG foundation models either use open-source ICU datasets with pretraining paradigms that require curated data and thus complicate generalization to field-like data, or use closed-source field-like PPG data. In contrast, we propose a PPG foundation model that does not require high-quality or field-like pretraining data, and instead leverages accompanying electrocardiogram and respiratory signals in ICU datasets to select contrastive samples during pretraining. Our approach allows the model to retain and learn from noisy PPG segments, improving robustness at inference. Our model, pretrained on 3x fewer subjects than existing state-of-the-art approaches, achieves performance improvements on 14 out of 15 diverse downstream tasks, including field-like daily activity and heart rate prediction. Our results demonstrate that multimodal supervision can integrate complementary physiological information to improve the robustness of PPG foundation models and enhance their generalization to consumer-grade data.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.07365v1)
- [PDF](https://arxiv.org/pdf/2606.07365v1)
- [SensorLM: Learning the Language of Wearable Sensors](https://arxiv.org/abs/2506.09108) (2025, citations: 46)
- [Pulse-PPG: An Open-Source Field-Trained PPG Foundation Model for Wearable Applications across Lab and Field Settings](https://arxiv.org/abs/2502.01108) (2025, citations: 39)
- [Ethical and legal implications of health monitoring wearable devices: A scoping review.](https://doi.org/10.1016/j.socscimed.2025.117685) (2025, citations: 31)
- [WildPPG: A Real-World PPG Dataset of Long Continuous Recordings](https://arxiv.org/abs/2412.17540) (2024, citations: 18)
- [CiTrus: Squeezing Extra Performance out of Low-data Bio-signal Transfer Learning](https://arxiv.org/abs/2412.11695) (2024, citations: 2)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/ai #keyword/multimodal #keyword/retrieval #keyword/machine-learning
