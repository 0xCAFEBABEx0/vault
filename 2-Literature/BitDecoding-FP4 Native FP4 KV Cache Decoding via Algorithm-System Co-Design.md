---
title: "BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design"
source: "https://arxiv.org/html/2611.09825v1"
author: "Dayou Du, Woon Yee Ng, Guangming Sheng, Nick Lau, Jianyi Cheng, Luo Mai"
published: "2026-11-06"
created: 2026-11-10
description: "The key-value (KV) cache dominates memory capacity and bandwidth in long-context LLM serving. While 4-bit microscaling formats (NVFP4, MXFP4) shrink the cache and run attention on FP4 Tensor Cores, a fundamental gap remains between algorithmic quantization and system-aware acceleration: existing FP4 KV systems use vanilla quantization that causes severe accuracy drops, whereas accuracy-oriented 4-bit algorithms rely…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/nlp
  - keyword/machine-learning
---

# BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.09825v1)
- published:: 2026-11-06
- updated:: 2026-11-06
- arxiv_id:: 2611.09825v1
- pdf:: https://arxiv.org/pdf/2611.09825v1
- categories:: cs.AI, cs.AR, cs.CL, cs.PF

## Abstract / Summary
The key-value (KV) cache dominates memory capacity and bandwidth in long-context LLM serving. While 4-bit microscaling formats (NVFP4, MXFP4) shrink the cache and run attention on FP4 Tensor Cores, a fundamental gap remains between algorithmic quantization and system-aware acceleration: existing FP4 KV systems use vanilla quantization that causes severe accuracy drops, whereas accuracy-oriented 4-bit algorithms rely on vector codebooks whose lookup overhead degrades decoding throughput. We present BitDecoding-FP4, an algorithm--system co-design for accurate and efficient native FP4 KV decoding. We mitigate three error sources: Dual-Residual Query Quantization splits queries into two FP4 tensors, cutting query logit error from 60% to 1%; Underflow-Aware Probability Scaling prevents E4M3 scales from rounding long-context probabilities to zero; and Outlier-Aware Key Quantization combines static smoothing, Hadamard rotation, and scale search to suppress key outliers under token-wise scaling. At the system level, we remove the softmax bottleneck via transposed softmax with fused probability quantization and stacked query MMA on paged KV caches. Across dense and MoE models with GQA and MLA, BitDecoding-FP4 stays within 0.5 points of BF16 KV accuracy with NVFP4 (1 point with MXFP4), and tracks BF16 KV in RL training rollouts. In end-to-end serving on NVIDIA B300 with Qwen3-4B and Qwen3-30B-A3B, it delivers 2.4-3.0$\times$ higher peak serving throughput than BF16 KV. The implementation is available at https://github.com/OpenBitSys/BitDecoding-FP4.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.09825v1)
- [PDF](https://arxiv.org/pdf/2611.09825v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp #keyword/machine-learning
