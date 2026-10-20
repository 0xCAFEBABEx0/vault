---
title: "ALTK-Evolve: How learned memory tops the τ²-bench leaderboard on customer service tasks without a frontier model"
source: "https://huggingface.co/blog/ibm-research/altk-evolve-bc"
author: "Hugging Face Blog"
published: "2026-10-20"
created: 2026-10-21
description: "Learned memory takes a basic ReAct agent with GPT-4.1 to the top Using GPT-4.1, an older, non-reasoning model, a basic customer-service agent reaches 67.5% Pass^4 on τ²-bench retail — meaning it solves the task on all four independent attempts for 67.5% of tasks. It scores above every retail entry in our October 12, 2026 leaderboard snapshot. It runs on the benchmark's stock ReAct scaffold, with learned guidelines a…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/evaluation
  - keyword/benchmark
  - keyword/reasoning
  - keyword/agents
  - keyword/machine-learning
---

# ALTK-Evolve: How learned memory tops the τ²-bench leaderboard on customer service tasks without a frontier model

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/ibm-research/altk-evolve-bc)
- published:: 2026-10-20

## Abstract / Summary
Learned memory takes a basic ReAct agent with GPT-4.1 to the top Using GPT-4.1, an older, non-reasoning model, a basic customer-service agent reaches 67.5% Pass^4 on τ²-bench retail — meaning it solves the task on all four independent attempts for 67.5% of tasks. It scores above every retail entry in our October 12, 2026 leaderboard snapshot. It runs on the benchmark's stock ReAct scaffold, with learned guidelines appended to its system prompt. ALTK-Evolve builds that playbook using GPT-4.1. It analyzes the agent's training-task attempts and uses the model to distill successes and failures into short behavioral rules: how to authenticate a customer, confirm a transaction, or handle a return. Those guidelines are then added to the agent's prompt for subsequent conversations. The same model powers both guideline extraction and the agent; no weight updates or human annotation are needed. Our previous work demonstrated this approach on coding agents. Here, we test it on customer service, where success requires following domain policies, understanding a customer's request, and executing the right tool actions. τ²-bench tests policy-bound customer service τ²-bench (from Sierra) measures…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/evaluation #keyword/benchmark #keyword/reasoning #keyword/agents #keyword/machine-learning
