---
title: "FOL-Proof: Verifying LLM Text-to-Logic Translations via Deterministic Semantics"
source: "https://arxiv.org/html/2611.33078v1"
author: "Yisrael Clark, Guy Katz"
published: "2026-11-24"
created: 2026-11-26
description: "Large Language Models (LLMs) are increasingly used to translate natural-language statements into first-order logic (FOL) to improve reasoning. However, LLMs are prone to errors, and so a semantically unfaithful FOL formula could corrupt downstream reasoning. We present FOL-Proof, a semantic firewall pipeline that validates LLM-generated FOL translations against independently derived linguistic interpretations. FOL-P…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/benchmark
  - keyword/reasoning
  - keyword/agents
---

# FOL-Proof: Verifying LLM Text-to-Logic Translations via Deterministic Semantics

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.33078v1)
- published:: 2026-11-24
- updated:: 2026-11-24
- arxiv_id:: 2611.33078v1
- pdf:: https://arxiv.org/pdf/2611.33078v1
- categories:: cs.CL, cs.LO

## Abstract / Summary
Large Language Models (LLMs) are increasingly used to translate natural-language statements into first-order logic (FOL) to improve reasoning. However, LLMs are prone to errors, and so a semantically unfaithful FOL formula could corrupt downstream reasoning. We present FOL-Proof, a semantic firewall pipeline that validates LLM-generated FOL translations against independently derived linguistic interpretations. FOL-Proof operates by deterministically obtaining a pool of candidate translations via semantic analysis tools, such as the English Resource Grammar and Minimal Recursion Semantics; then applying an SMT solver to check each derived reading for logical equivalence to the LLM-generated formula. If the translation is faithful it is accepted; otherwise, it is rejected, or optionally repaired via repeated invocations to the LLM. The procedure is conservative: incomplete search, unsupported constructions, or inconclusive checks yield abstention rather than false rejection. We evaluated FOL-Proof on established benchmarks (ProofWriter, RuleTaker and PrOntoQA), and also on a new adversarial benchmark (LongFaithCheck). Our experiments show that FOL-Proof attains near perfect selective accuracy, while direct LLM judges and round-trip baselines show substantially worse performance.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.33078v1)
- [PDF](https://arxiv.org/pdf/2611.33078v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark #keyword/reasoning #keyword/agents
