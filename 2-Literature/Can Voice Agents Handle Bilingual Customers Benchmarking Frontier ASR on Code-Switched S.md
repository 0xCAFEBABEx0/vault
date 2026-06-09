---
title: "Can Voice Agents Handle Bilingual Customers? Benchmarking Frontier ASR on Code-Switched Speech"
source: "https://huggingface.co/blog/ServiceNow-AI/code-switching"
author: "Hugging Face Blog"
published: "2026-06-09"
created: 2026-06-10
description: "Despite the prevalence of bilingual speakers across the world, there has been little work focused on how voice agents handle code-switched speech in enterprise settings. So, when a customer asked us how our voice agents would perform for their largely bilingual customer base who routinely code-switched, we decided to build our own benchmark and dataset to evaluate models. We focused on automatic speech recognition (…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/language-model
  - keyword/nlp
  - keyword/multimodal
  - keyword/evaluation
  - keyword/benchmark
  - keyword/agents
---

# Can Voice Agents Handle Bilingual Customers? Benchmarking Frontier ASR on Code-Switched Speech

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/ServiceNow-AI/code-switching)
- published:: 2026-06-09

## Abstract / Summary
Despite the prevalence of bilingual speakers across the world, there has been little work focused on how voice agents handle code-switched speech in enterprise settings. So, when a customer asked us how our voice agents would perform for their largely bilingual customer base who routinely code-switched, we decided to build our own benchmark and dataset to evaluate models. We focused on automatic speech recognition (ASR) — the first step in any voice agent pipeline — because transcription errors… Our benchmark covers four language pairs that were most relevant for our customer base: Spanish-English, French-English, Canadian French-English, and German-English. It uses the non-English language as the matrix framing, with English embedded at varying lengths. The data covers a wide range of Human Resources (HR) and IT Service management (ITSM) scenarios, including employee inquiries about benefits or payroll, and support requests such as password resets, VPN access, or device troubleshootin… We release our benchmark and data through our harness for evaluating voice models, AU-Harness. We also provide results from seven ASR systems, including some Large Audio Language Models (LALMs), fr…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/language-model #keyword/nlp #keyword/multimodal #keyword/evaluation #keyword/benchmark #keyword/agents
