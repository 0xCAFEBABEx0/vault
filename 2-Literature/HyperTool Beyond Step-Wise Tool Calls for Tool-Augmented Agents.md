---
title: "HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents"
source: "https://arxiv.org/html/2606.13663v1"
author: "Yaxin Du, Yifan Zhou, Yujie Ge, Jiajun Wang, Xianghe Pang, Shuo Tang, Tuney Zheng, Bryan Dai, Jian Yang, Siheng Chen"
published: "2026-06-11"
created: 2026-06-13
description: "Tool-augmented LLM agents commonly rely on step-wise atomic tool calls..."
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/reasoning
  - keyword/agents
---

# HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.13663v1)
- published:: 2026-06-11
- updated:: 2026-06-11
- arxiv_id:: 2606.13663v1
- pdf:: https://arxiv.org/pdf/2606.13663v1
- categories:: cs.CL

## Abstract / Summary
Tool-augmented LLM agents commonly rely on step-wise atomic tool calls, where each invocation, observation, and value transfer is exposed in the main reasoning trace. This creates an execution-granularity mismatch: locally deterministic tool workflows are unfolded into repeated model-visible decisions, consuming context and forcing the model to manage low-level dataflow in the trace. We introduce HyperTool, a unified executable MCP-style tool interface that changes the model-visible unit of tool execution. A model invokes HyperTool with a code block that can call existing tools through their original schemas, manipulate returned values, and pass intermediate results locally, folding deterministic tool subroutines into a single outer call. To train models to use this interface, we synthesize HyperTool-format trajectories from cross-tool compositional tasks and verify them in real MCP environments. On MCP-Universe, HyperTool improves average accuracy from 15.69% to 35.29% on Qwen3-32B and from 9.93% to 33.33% on Qwen3-8B, and surpass GPT-OSS and Kimi-k2.5 on average accuracy.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.13663v1)
- [PDF](https://arxiv.org/pdf/2606.13663v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/reasoning #keyword/agents
