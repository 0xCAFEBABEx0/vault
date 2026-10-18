---
title: "MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering"
source: "https://arxiv.org/html/2610.22344v1"
author: "Shangheng Du, Jinxin Shi, Shuaiyu Zhang, Yiming Wu, Junpeng Zhao, Shiyang Feng, Xin Li, Liang He, Xiangchao Yan, Bo Zhang"
published: "2026-10-15"
created: 2026-10-19
description: "Large language models (LLMs) are expanding from assisting scientific research and engineering to autonomously developing and improving AI systems, advancing AI for AI (AI4AI) as a pathway toward recursive self-improvement (RSI). Workflow-driven machine learning engineering (MLE) systems provide a practical path toward this pursuit through complex orchestration that manages long-horizon experimentation, while recent…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/retrieval
  - keyword/agents
  - keyword/machine-learning
---

# MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.22344v1)
- published:: 2026-10-15
- updated:: 2026-10-15
- arxiv_id:: 2610.22344v1
- pdf:: https://arxiv.org/pdf/2610.22344v1
- categories:: cs.AI, cs.CL, cs.LG

## Abstract / Summary
Large language models (LLMs) are expanding from assisting scientific research and engineering to autonomously developing and improving AI systems, advancing AI for AI (AI4AI) as a pathway toward recursive self-improvement (RSI). Workflow-driven machine learning engineering (MLE) systems provide a practical path toward this pursuit through complex orchestration that manages long-horizon experimentation, while recent MLE systems adopt model-directed interaction, allowing models to autonomously organize experiments and adapt optimization strategies based on execution feedback. However, feedback from each experiment reflects several preceding decisions, and a long MLE run contains many such costly experiments. Training must therefore select useful supervision from long interaction trajectories and learn from intermediate outcomes. We propose a post-training method for autonomous long-horizon MLE optimization and apply it to train MLExpert, a 35B Mixture-of-Experts agentic model. We design the Kaggle-MLE Factory to construct executable tasks and an interaction harness for model-directed experimentation. Hierarchical agentic SFT transfers general tool-use and coding capabilities to MLE through outcome-guided supervision. Windowed Interaction RL (WIRL) treats the multi-turn decisions between successive experiment results as an execution window and assigns it a shared outcome-based reward. Asynchronous collection and policy correction support policy updates before the trajectory ends. On MLE-Bench Lite, MLExpert improves the average medal rate of the base model from 37.9% to 72.7%, achieving performance comparable to larger frontier models such as Kimi-K3 and GLM-5.3. Further experiments show that MLExpert improves performance on NatureBench Lite, agent scaffold optimization,…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.22344v1)
- [PDF](https://arxiv.org/pdf/2610.22344v1)
- [Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering](https://arxiv.org/abs/2607.28568) (2026, citations: 8)
- [Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance with a 35B Agent](https://arxiv.org/abs/2606.30616) (2026, citations: 23)
- [NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?](https://arxiv.org/abs/2606.24530) (2026, citations: 9)
- [Toward Generalist Autonomous Research via Hypothesis-Tree Refinement](https://arxiv.org/abs/2606.11926) (2026, citations: 23)
- [MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery](https://arxiv.org/abs/2606.06473) (2026, citations: 27)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/retrieval #keyword/agents #keyword/machine-learning
