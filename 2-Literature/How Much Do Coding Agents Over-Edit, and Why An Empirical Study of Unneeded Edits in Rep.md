---
title: "How Much Do Coding Agents Over-Edit, and Why? An Empirical Study of Unneeded Edits in Repository-Level Agent Patches"
source: "https://arxiv.org/html/2611.34875v1"
author: "Aakash Goel, Benjamin Steenhoek, Yu Hu"
published: "2026-11-25"
created: 2026-11-28
description: "Agent patches are larger than developers', which is widely read as over-editing. But patch size does not say whether the extra edits are needed, what they are, or where they come from. We introduce Delta Residue Attribution (DRA), which replays agent trajectories, traces every block (unit) of the final patch to the step that wrote it, reverts each unit, and reruns the task tests to decide whether the unit is needed.…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/retrieval
  - keyword/evaluation
  - keyword/benchmark
  - keyword/agents
---

# How Much Do Coding Agents Over-Edit, and Why? An Empirical Study of Unneeded Edits in Repository-Level Agent Patches

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.34875v1)
- published:: 2026-11-25
- updated:: 2026-11-25
- arxiv_id:: 2611.34875v1
- pdf:: https://arxiv.org/pdf/2611.34875v1
- categories:: cs.SE, cs.AI

## Abstract / Summary
Agent patches are larger than developers', which is widely read as over-editing. But patch size does not say whether the extra edits are needed, what they are, or where they come from. We introduce Delta Residue Attribution (DRA), which replays agent trajectories, traces every block (unit) of the final patch to the step that wrote it, reverts each unit, and reruns the task tests to decide whether the unit is needed. We apply DRA to 7,660 resolved GitHub Copilot CLI trajectories from 18 frontier models on SWE-bench Verified (6,728) and DeepSWE (932), and grade developer patches using the same method. Agent patches do change more lines than developers'; on SWE-bench Verified the majority of extra edits add tests (61%) and documentation (13%) while on DeepSWE, most extra edits are code (58%). On both benchmarks, agents' code is on average at least as necessary as developers' (mean $NP_{code}$ 0.887 vs. 0.864 on SWE-bench Verified, where 11 of 18 models leave less unneeded code than developers, and 0.797 vs. 0.785 on DeepSWE). On average, 11% of an agent patch's code units on SWE-bench Verified are still unneeded, and 89% of those change behavior. Debug steps write almost none of the unneeded code. Code necessity differs substantially by model; it is unrelated to resolve rate on SWE-bench Verified and negatively correlated with it on DeepSWE (Spearman -0.59, p = 0.01). On SWE-bench Verified, pruning with DRA using only the tests the agent can see (its own tests and the repository's) removes the majority of unneeded code but also some needed code (67% recall, 46% precision), and 89% of pruned patches still resolve the task; asking the agent to audit its own diff is more precise but less effective (36% recall, 66% precision). We recommend that benchmarks report code necessit…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.34875v1)
- [PDF](https://arxiv.org/pdf/2611.34875v1)
- [When Models Edit Too Much: On the Fidelity of Minimal Code Edits](https://arxiv.org/abs/2609.04061) (2026, citations: 7)
- [Refine After Generation: Toward Correct and Concise Patches in LLM-based Program Repair](https://arxiv.org/abs/2608.13292) (2026, citations: 4)
- [DiffTestGen: Change-Directed LLM-Based Testing for Exposing Behavioral Differences](https://arxiv.org/abs/2607.16024) (2026, citations: 2)
- [DeepSWE: Measuring Frontier Coding Agents on Original, Long-Horizon Engineering Tasks](https://arxiv.org/abs/2607.07946) (2026, citations: 120)
- [What Resolve Rate Hides: Trajectory Structure Diagnostics for Coding Agents](https://arxiv.org/abs/2607.06184) (2026, citations: 15)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/retrieval #keyword/evaluation #keyword/benchmark #keyword/agents
