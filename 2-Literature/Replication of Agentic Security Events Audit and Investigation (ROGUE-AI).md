---
title: "Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)"
source: "https://arxiv.org/html/2611.26553v1"
author: "Mengxiao Wang, Mahbub Alam, Kalyan Nakka, Nitesh Saxena"
published: "2026-11-19"
created: 2026-11-22
description: "Agents based on large language models (LLMs) can now delete files and send payments on behalf of their users. News media reports routinely describe failures of these agents (e.g., Replit's coding agent deleting a production database), but a report often only says what went wrong and rarely (in)validates the incident or finds its root cause. Incident catalogs collect these reports, and benchmarks record whether agent…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/benchmark
  - keyword/agents
  - keyword/research-paper
---

# Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.26553v1)
- published:: 2026-11-19
- updated:: 2026-11-19
- arxiv_id:: 2611.26553v1
- pdf:: https://arxiv.org/pdf/2611.26553v1
- categories:: cs.CR, cs.AI, cs.MA

## Abstract / Summary
Agents based on large language models (LLMs) can now delete files and send payments on behalf of their users. News media reports routinely describe failures of these agents (e.g., Replit's coding agent deleting a production database), but a report often only says what went wrong and rarely (in)validates the incident or finds its root cause. Incident catalogs collect these reports, and benchmarks record whether agents fail, but neither replicates an incident nor tests the cause its report might identify. In this paper, we present ROGUE-AI (Replication of Agentic Security Events: Audit and Investigation), a multi-agent framework that closes the above gap and rebuilds each reported incident offline together with a matched control that lacks only the blamed cause, and runs agents on both. Our results suggest that ROGUE-AI is able to reproduce the reported harm in 89% of its 108 attempted replications. Agents built on five current GPT, Claude, Gemini and DeepSeek models made the reported mistake in 18% to 33% of runs, against at most 1% without the blamed cause. Of the 72 incidents with real-world harm, 62 had no underlying attacker, and in these, agents did what their task asked for but missed an ordinary hazard, such as a database shared with the live site. Replications without an attacker caused more harm than replications of prompt injection for all five models. Defenses against prompt injection look for injected instructions, but these replications contain none. Further, a warning after each tool output that names the hazard and its consequence lowered harm for all five models, whereas a note of the same length that does not mention the hazard left most of the harm in place. Built from real incidents, the ROGUE-AI replications form a reusable audit framework that vendo…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.26553v1)
- [PDF](https://arxiv.org/pdf/2611.26553v1)
- [Chronicle: Cut-Point Replay for Regression Testing of LLM Agents](https://arxiv.org/abs/2609.20625) (2026, citations: 3)
- [ScientistTwo: Pioneering the Human Knowledge Frontier with Autonomous AI](https://arxiv.org/abs/2609.19644) (2026, citations: 2)
- [The Agent Incident Registry: Toward Preventing Repeated AI Agent Failures](https://arxiv.org/abs/2609.11030) (2026, citations: 4)
- [OSGuard: A Benchmark for Safety in Computer-Use Agents](https://arxiv.org/abs/2606.15034) (2026, citations: 4)
- [SABER: Benchmarking Operational Safety of LLM Coding Agents in Stateful Project Workspaces](https://arxiv.org/abs/2606.01317) (2026, citations: 14)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/benchmark #keyword/agents #keyword/research-paper
