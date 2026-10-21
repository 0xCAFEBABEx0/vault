---
title: "Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation"
source: "https://arxiv.org/html/2610.28586v1"
author: "Shu Zhao, Tan Yu"
published: "2026-10-20"
created: 2026-10-22
description: "Agentic on-policy distillation (OPD) trains a student agent on its own trajectories while a teacher scores every token. A natural explanation of where it goes wrong is compounding error: the student's mistakes carry its trajectories beyond the region where the teacher is reliable, so recent methods keep training inside that region, through episode-length curricula, teacher-guided turns, prefix replay, or teacher int…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/agents
  - keyword/machine-learning
---

# Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2610.28586v1)
- published:: 2026-10-20
- updated:: 2026-10-20
- arxiv_id:: 2610.28586v1
- pdf:: https://arxiv.org/pdf/2610.28586v1
- categories:: cs.CL, cs.AI

## Abstract / Summary
Agentic on-policy distillation (OPD) trains a student agent on its own trajectories while a teacher scores every token. A natural explanation of where it goes wrong is compounding error: the student's mistakes carry its trajectories beyond the region where the teacher is reliable, so recent methods keep training inside that region, through episode-length curricula, teacher-guided turns, prefix replay, or teacher intervention where the two disagree. We show this explanation is incomplete. From the states where the student departs most from the teacher, the teacher's own takeovers still finish the task, yet the student trained on its token scores keeps running out of turns. We attribute this to the myopia of next-token scoring. The teacher rates each token without seeing where the episode ends, so its scores let through the safe, delaying moves that outcome-based RL would punish with zero reward, a penalty agentic OPD lacks. We call this difference between what the teacher does and what it scores the rollout-scorer gap. We propose Rollout-to-Scorer Distillation (R2S), which repairs the scorer before distillation by mining high-disagreement states from the untrained student, running teacher takeovers from them, keeping the states where enough takeovers pass a reward-free check such as consensus or an LLM judge, and fine-tuning the teacher to give its takeover-informed scores on every assistant token from the divergence turn onward, without the takeover in context. The repaired teacher is frozen as the sole scorer for standard OPD, requiring no task reward during repair or training. Across three environments, two teachers and four students, R2S outperforms three state-of-the-art agentic-OPD methods in all twelve teacher-student-environment cells, by 12.8 success points on…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2610.28586v1)
- [PDF](https://arxiv.org/pdf/2610.28586v1)
- [The Value of Being Wrong: Self-Mined Visual In-Context Learning from Errors](https://arxiv.org/abs/2610.16977) (2026, citations: 1)
- [Look Ahead Before You Distill: Future Trajectory Validation of Teacher Guidance for Agentic On-Policy Distillation](https://arxiv.org/abs/2608.01953) (2026, citations: 12)
- [Consensus as Privileged Context for Label-Free Self-Distillation](https://arxiv.org/abs/2607.13643) (2026, citations: 6)
- [Multi-Turn On-Policy Distillation with Prefix Replay](https://arxiv.org/abs/2607.04763) (2026, citations: 21)
- [Rethinking On-Policy Self-Distillation for Thinking Models](https://arxiv.org/abs/2607.05184) (2026, citations: 46)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/agents #keyword/machine-learning
