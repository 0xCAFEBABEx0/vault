---
title: "Profiling in PyTorch (Part 2): From nn.Linear to a Fused MLP"
source: "https://huggingface.co/blog/torch-mlp-fusion"
author: "Hugging Face Blog"
published: "2026-06-11"
created: 2026-06-12
description: "In the first part of this series 'Profiling in PyTorch' , we used torch.add(torch.matmul(x, w), b) to learn how to read PyTorch profiler traces. We also discussed several other topics that came our way - the CPU dispatch chain, launch overhead, the difference between an overhead-bound and a compute-bound regime, and some internals of torch.compile . In the second iteration (this blog post), we climb one rung up the…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
---

# Profiling in PyTorch (Part 2): From nn.Linear to a Fused MLP

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/torch-mlp-fusion)
- published:: 2026-06-11

## Abstract / Summary
In the first part of this series "Profiling in PyTorch" , we used torch.add(torch.matmul(x, w), b) to learn how to read PyTorch profiler traces. We also discussed several other topics that came our way - the CPU dispatch chain, launch overhead, the difference between an overhead-bound and a compute-bound regime, and some internals of torch.compile . In the second iteration (this blog post), we climb one rung up the ladder. We replace the hand-written matmul-add pair with an nn.Linear (with bias=True ). This is the building block every deep learning model uses. We then stack three of them (specific to our example), with an activation in between, to form a Multilayer Perceptron (MLP) block. The scripts for this blog post live here: 02_linear.py , 03_simple_mlp.py , and 03_kernels_mlp.py . Like before, it helps to open them in a separate tab and walk through the code as you read. We use an NVIDIA A100-SXM4-80GB GPU to run the scripts. It is really easy to set up a GPU on the Hugging Face infrastructure and experiment with the scripts using Dev Mode with Spaces . One could also run the scripts with the Hugging Face Jobs pipeline . From matmul-add to Linear nn.Linear is a module wrappe…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface
