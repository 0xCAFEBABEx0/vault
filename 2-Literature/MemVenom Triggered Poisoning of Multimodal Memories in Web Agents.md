---
title: "MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents"
source: "https://arxiv.org/html/2606.10742v1"
author: "Yv Zhang, Hao Sun, Hao Fang, Kuofeng Gao, Fan Mo, Bin Chen, Shu-Tao Xia, Yaowei Wang"
published: "2026-06-09"
created: 2026-06-11
description: "External memory has become a core component of modern web agents, enabling long-horizon reasoning through the retrieval of past experiences. However, this paradigm introduces a critical vulnerability: malicious content injected into memory can be persistently recalled and repeatedly influence agent behavior. In this work, we identify and systematically study multimodal memory poisoning, an overlooked yet practical a…"
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
  - keyword/reasoning
  - keyword/agents
---

# MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.10742v1)
- published:: 2026-06-09
- updated:: 2026-06-09
- arxiv_id:: 2606.10742v1
- pdf:: https://arxiv.org/pdf/2606.10742v1
- categories:: cs.CR, cs.LG

## Abstract / Summary
External memory has become a core component of modern web agents, enabling long-horizon reasoning through the retrieval of past experiences. However, this paradigm introduces a critical vulnerability: malicious content injected into memory can be persistently recalled and repeatedly influence agent behavior. In this work, we identify and systematically study multimodal memory poisoning, an overlooked yet practical attack surface in web-agent systems. We propose MemVenom, a unified black-box attack framework that poisons graph-structured external memory with coordinated text-image evidence. Our method consists of a two-stage design: (1) a trigger-conditioned retrieval attack that ensures high-probability recall of malicious memory, and (2) a post-retrieval attack induction that leverages adversarial perturbations and stealthy OCR injection to override the original user objective. Unlike prior attacks that operate on prompts or text-only memory, our approach enables persistent, reusable, and goal-agnostic attacks without modifying model parameters or re-optimizing malicious tasks. Experiments across multiple web-agent frameworks and vision-language models demonstrate that MemVenom achieves strong end-to-end attack success with minimal impact on benign performance, reaching up to 99.15% on GPT-5-family web agents, while transferring effectively across architectures and model scales.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.10742v1)
- [PDF](https://arxiv.org/pdf/2606.10742v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/multimodal #keyword/retrieval #keyword/evaluation #keyword/reasoning #keyword/agents