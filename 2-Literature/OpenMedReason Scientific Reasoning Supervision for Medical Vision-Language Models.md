---
title: "OpenMedReason: Scientific Reasoning Supervision for Medical Vision-Language Models"
source: "https://arxiv.org/html/2606.12169v1"
author: "Negin Baghbanzadeh, Pritam Sarkar, Michael Colacci, Abeer Badawi, Adibvafa Fallahpour, Arash Afkanpour, Leonid Sigal, Ali Etemad, Elham Dolatabadi"
published: "2026-06-10"
created: 2026-06-12
description: "High-stakes clinical use of large vision-language models (LVLMs) requires reasoning that is grounded in visual evidence and clinical knowledge, not just correct final answers. We introduce OpenMedReason, a large-scale, open multimodal medical reasoning corpus comprising approximately 450K image-question-answer instances whose reasoning traces are primarily derived from curated biomedical, human-authored scientific a…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/multimodal
  - keyword/retrieval
  - keyword/evaluation
  - keyword/benchmark
  - keyword/reasoning
  - keyword/safety
---

# OpenMedReason: Scientific Reasoning Supervision for Medical Vision-Language Models

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.12169v1)
- published:: 2026-06-10
- updated:: 2026-06-10
- arxiv_id:: 2606.12169v1
- pdf:: https://arxiv.org/pdf/2606.12169v1
- categories:: cs.CV, cs.AI, cs.CL, cs.LG

## Abstract / Summary
High-stakes clinical use of large vision-language models (LVLMs) requires reasoning that is grounded in visual evidence and clinical knowledge, not just correct final answers. We introduce OpenMedReason, a large-scale, open multimodal medical reasoning corpus comprising approximately 450K image-question-answer instances whose reasoning traces are primarily derived from curated biomedical, human-authored scientific articles. OpenMedReason provides high-fidelity supervision beyond synthetic chains of thought, covering diverse medical domain vision modalities such as radiological scans, microscopic images, visible light photographs, charts, and others. We complement it with OpenMedReason-Bench, a held-out benchmark that allows fine-grained evaluation of LVLMs along three complementary axes of capability, including perception, medical knowledge, and rationale, enabling diagnostic evaluation beyond final-answer accuracy. OpenMedReason is a rich training resource that exhibits its effectiveness in both supervised fine-tuning (SFT) and reinforcement-based alignment. Training with OpenMedReason yields a 20% average improvement in VQA accuracy over the base model and achieves performance within 4.2% of the strongest comparable-scale medical LVLMs. Fine-grained performance analysis confirms that the gains are not concentrated in any single axis: OpenMedReason improves perception, medical knowledge, and rationale jointly, and its reasoning traces are preferred over those of the base model in 86.1% of pairwise comparisons. We release the code and dataset at huggingface.co/datasets/neginb/OpenMedReason.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.12169v1)
- [PDF](https://arxiv.org/pdf/2606.12169v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/multimodal #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/reasoning #keyword/safety
