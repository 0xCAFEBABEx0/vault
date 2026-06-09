---
title: "The Neutral Mask: How RLHF Provides Shallow Alignment while Leaving Partisan Structure Intact in a Large Language Model"
source: "https://arxiv.org/html/2606.09735v1"
author: "Wendy K. Tam"
published: "2026-06-08"
created: 2026-06-10
description: "The ambition behind alignment training is to make large language models safe and useful. The primary mechanism, reinforcement learning from human feedback (RLHF), shapes the behavior of deployed language models by aligning them with ``human values.'' Yet the process is opaque. What values are being encoded; whose values are they; and how does RLHF encode them? A growing body of evidence suggests that RLHF produces o…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/safety
  - keyword/machine-learning
---

# The Neutral Mask: How RLHF Provides Shallow Alignment while Leaving Partisan Structure Intact in a Large Language Model

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.09735v1)
- published:: 2026-06-08
- updated:: 2026-06-08
- arxiv_id:: 2606.09735v1
- pdf:: https://arxiv.org/pdf/2606.09735v1
- categories:: cs.CL

## Abstract / Summary
The ambition behind alignment training is to make large language models safe and useful. The primary mechanism, reinforcement learning from human feedback (RLHF), shapes the behavior of deployed language models by aligning them with ``human values.'' Yet the process is opaque. What values are being encoded; whose values are they; and how does RLHF encode them? A growing body of evidence suggests that RLHF produces only functional compliance rather than deep alignment. We offer a mechanistic case study of this phenomenon for partisan political orientation with a comparison of the internal representations of Llama 3.1 8B before and after RLHF. We show that RLHF does not remove the structured partisan direction in the base model. Instead, it compresses the variance of the partisan signal to generate consistently balanced and non-partisan output. Sparse autoencoder decomposition reveals that policy-encoding features, which activate sporadically in the base model, are completely inactive in the Instruct model. Feature-level steering experiments confirm the causal disconnect. RLHF thus encodes a norm of political neutrality, not by erasing the model's knowledge of partisanship, but by severing the causal pathway from partisan geometry to output generation. Importantly, this neutrality is functional, not structural so that the underlying geometry that enables partisan steering remains intact. The mechanisms that bypass RLHF's guardrails, such as inferring and amplifying a user's partisan identity, reactivate partisan generation. If RLHF operates by disconnecting rather than removing value-laden structure, then the same pattern may hold for other value domains, and the aligned model's behavior may be more fragile than its outputs suggest.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.09735v1)
- [PDF](https://arxiv.org/pdf/2606.09735v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/safety #keyword/machine-learning
