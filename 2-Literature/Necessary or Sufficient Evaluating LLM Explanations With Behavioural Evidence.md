---
title: "Necessary or Sufficient? Evaluating LLM Explanations With Behavioural Evidence"
source: "https://arxiv.org/html/2609.05385v1"
author: "Urja Pawar, Rajitha Ramanayake, Nabeel Kemal, Ashwin Kandath, Owen O'Neill, Guillaume Bourgeon, Houssem Chatbri"
published: "2026-09-04"
created: 2026-09-09
description: "LLM decision components that can operate within agent workflows often produce action-relevant recommendations or judgements together with explanations. Operators may use the named factors to monitor a system, diagnose errors, or decide when to escalate an output. Such use assumes that the explanations agree with the component's observable decision behaviour. We test two interpretations of the named factors: necessit…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/evaluation
  - keyword/agents
---

# Necessary or Sufficient? Evaluating LLM Explanations With Behavioural Evidence

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2609.05385v1)
- published:: 2026-09-04
- updated:: 2026-09-04
- arxiv_id:: 2609.05385v1
- pdf:: https://arxiv.org/pdf/2609.05385v1
- categories:: cs.AI

## Abstract / Summary
LLM decision components that can operate within agent workflows often produce action-relevant recommendations or judgements together with explanations. Operators may use the named factors to monitor a system, diagnose errors, or decide when to escalate an output. Such use assumes that the explanations agree with the component's observable decision behaviour. We test two interpretations of the named factors: necessity, meaning that changing a factor would change the output, and sufficiency, meaning that retaining it while removing other changeable information would preserve the output. We evaluate these interpretations in two synthetic use cases: recommending advisors to clients and judging prompts for harmfulness or risk. Models return an output and the top three factors that most influenced it. Controlled black-box interventions estimate a necessity score for each factor by measuring how often changing it changes the output, and a sufficiency score by measuring how often retaining it preserves the output. Across eight models from the Claude, GPT, and Gemini families, the mean Spearman correlations between the cited ranking and the necessity and sufficiency scores are 0.349 and 0.354 for advisor recommendation, and 0.431 and 0.580 for prompt monitoring. Furthermore, an uncited factor scores above the lowest-scoring cited factor in 57.6% of advisor responses under necessity and 58.1% under sufficiency; the corresponding prompt-monitoring rates are 25.8% and 8.9%. The cited top three contain useful information but do not reliably identify the three factors with the strongest measured influence under necessity or sufficiency. The framework provides a black-box reliability check for explanations used in agent oversight while remaining scoped to individual LLM decisions.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2609.05385v1)
- [PDF](https://arxiv.org/pdf/2609.05385v1)
- [ProSA: Assessing and Understanding the Prompt Sensitivity of LLMs](https://arxiv.org/abs/2410.12405) (2024, citations: 227)
- [XRec: Large Language Models for Explainable Recommendation](https://arxiv.org/abs/2406.02377) (2024, citations: 106)
- [State of What Art? A Call for Multi-Prompt LLM Evaluation](https://arxiv.org/abs/2401.00595) (2023, citations: 386)
- [Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting](https://arxiv.org/abs/2310.11324) (2023, citations: 952)
- [Measuring Faithfulness in Chain-of-Thought Reasoning](https://arxiv.org/abs/2307.13702) (2023, citations: 562)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/evaluation #keyword/agents
