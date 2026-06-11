---
title: "Fine-tuning Multi-modal LLMs with ART: Art-based Reinforcement Training"
source: "https://arxiv.org/html/2606.11854v1"
author: "Michal Chudoba, Sergey Alyaev, Petra Galuscakova, Tomasz Wiktorski"
published: "2026-06-10"
created: 2026-06-12
description: "There are two main Parameter-Efficient Fine-Tuning (PEFT) techniques for Large Language Models (LLMs). While Low-Rank Adaptation (LoRA) introduces additional weights between the LLM layers, Soft Prompting introduces additional fine-tuning-specific raw tokens to an LLM input. However, both require modification to the computational graphs of precompiled, preoptimized LLMs. As a result, neither is fully supported in hi…"
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
  - keyword/machine-learning
---

# Fine-tuning Multi-modal LLMs with ART: Art-based Reinforcement Training

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.11854v1)
- published:: 2026-06-10
- updated:: 2026-06-10
- arxiv_id:: 2606.11854v1
- pdf:: https://arxiv.org/pdf/2606.11854v1
- categories:: cs.LG, cs.AI, cs.CL

## Abstract / Summary
There are two main Parameter-Efficient Fine-Tuning (PEFT) techniques for Large Language Models (LLMs). While Low-Rank Adaptation (LoRA) introduces additional weights between the LLM layers, Soft Prompting introduces additional fine-tuning-specific raw tokens to an LLM input. However, both require modification to the computational graphs of precompiled, preoptimized LLMs. As a result, neither is fully supported in high-throughput engines like vLLM. We propose fine-tuning with ART (Art-based Reinforcement Training). The method injects information into a frozen Multimodal Large Language Model (MLLM) by optimizing only its raw visual input, thus enabling the soft-token approach on pre-compiled computational graphs. It relies on backpropagation of gradients back into a plain pixel array and thus supports any fine-tuning objective. Moreover, the optimized visual input can be stylized as task-relevant computational artworks. The approach's effectiveness is confirmed for different sizes of a popular open Qwen architecture and for several textual benchmarks. Specifically, ART reaches accuracy competitive with LoRA across mathematics and structured-tool-use benchmarks.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.11854v1)
- [PDF](https://arxiv.org/pdf/2606.11854v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/multimodal #keyword/evaluation #keyword/benchmark #keyword/machine-learning
