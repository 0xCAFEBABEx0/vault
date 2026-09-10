---
title: "Retrofitting Code Using LLMs to Support Exceptional Behavior"
source: "https://arxiv.org/html/2609.10397v1"
author: "Linghan Zhong, Jiyang Zhang, Jayanth Srinivasa, Junyi Jessy Li, Milos Gligoric"
published: "2026-09-09"
created: 2026-09-11
description: "Exception Related Code (ERC), which includes throw statements, conditions (if statements) that guard those throw statements, and try/catch blocks, is an essential component of software systems, allowing developers to detect and handle exceptional states that deviate from the expected program behavior. However, manually writing ERC across large codebases is tedious. We propose a novel task: retrofitting existing code…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/benchmark
---

# Retrofitting Code Using LLMs to Support Exceptional Behavior

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.10397v1)
- published:: 2026-09-09
- updated:: 2026-09-09
- arxiv_id:: 2609.10397v1
- pdf:: https://arxiv.org/pdf/2609.10397v1
- categories:: cs.SE, cs.CL

## Abstract / Summary
Exception Related Code (ERC), which includes throw statements, conditions (if statements) that guard those throw statements, and try/catch blocks, is an essential component of software systems, allowing developers to detect and handle exceptional states that deviate from the expected program behavior. However, manually writing ERC across large codebases is tedious. We propose a novel task: retrofitting existing code with ERC. Namely, given code (without ERC) and Exceptional Behavior Tests (EBTs) (e.g., check if method throws InvalidArgumentException if null is given as the value to the argument) we aim to automatically generate missing ERC, such that the given tests pass. We design and implement Exception Coder (EXCODER) that performs context engineering to help Large Language Models (LLMs) tackle this task. EXCODER integrates static and dynamic program analysis with LLMs by providing the extracted contextual information to the LLMs. To evaluate EXCODER, we build a benchmark constructed from GitHub Java repositories, where we systematically remove ERC in 304 methods from 75 projects. Our results demonstrate that EXCODER provides an effective, though imperfect, solution to this problem in automated code generation, offering developers the first way to implement ERC following test-driven development. When combined with Qwen 2.5 Coder 32b, EXCODER achieves pass@1, 5, and 10 rates of 85.92% (12.56 percentage points over baseline), 86.18% (12.82 p.p. over baseline), and 86.51% (13.15 p.p. over baseline), respectively, on developer-written test suites. Our manual inspection of the generated code further reveals limitations of EXCODER, pointing to directions for future work.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.10397v1)
- [PDF](https://arxiv.org/pdf/2609.10397v1)
- [LLMs Lean on Priors, Not Programming Language Semantics](https://arxiv.org/abs/2510.03415) (2025, citations: 4)
- [SWE-GPT: A Process-Centric Language Model for Automated Software Improvement](https://dl.acm.org/doi/pdf/10.1145/3728981) (2025, citations: 23)
- [Not All Exceptions Are Created Equal: Triaging Error Logs in Real-World Enterprises](https://dl.acm.org/doi/pdf/10.1145/3721126) (2025, citations: 2)
- [Phi-4 Technical Report](https://arxiv.org/abs/2412.08905) (2024, citations: 779)
- [Qwen2.5-Coder Technical Report](https://arxiv.org/abs/2409.12186) (2024, citations: 1529)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark
