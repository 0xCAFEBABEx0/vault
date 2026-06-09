---
title: "Collaborative Human-Agent Protocol (CHAP)"
source: "https://arxiv.org/html/2606.09751v1"
author: "Arsalan Shahid, Gordon Suttie, Philip Black"
published: "2026-06-08"
created: 2026-06-10
description: "Foundation models are moving from response generation into operational roles. They plan across steps, call tools, request human input, coordinate with other agents, and increasingly carry responsibility for work that affects customers, claims, code, contracts, and clinical decisions. Production deployments are no longer one human supervising one model. They are multi-human, multi-agent collaborations that cross team…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/ai
  - keyword/agents
  - keyword/research-paper
---

# Collaborative Human-Agent Protocol (CHAP)

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2606.09751v1)
- published:: 2026-06-08
- updated:: 2026-06-08
- arxiv_id:: 2606.09751v1
- pdf:: https://arxiv.org/pdf/2606.09751v1
- categories:: cs.AI, cs.CL, cs.HC

## Abstract / Summary
Foundation models are moving from response generation into operational roles. They plan across steps, call tools, request human input, coordinate with other agents, and increasingly carry responsibility for work that affects customers, claims, code, contracts, and clinical decisions. Production deployments are no longer one human supervising one model. They are multi-human, multi-agent collaborations that cross teams, time zones, and trust boundaries. The technical surface for this collaboration remains weakly specified. When an agent drafts a response and a human edits it before it ships, the moment of human judgement is the most valuable signal in the system. In current practice it is recorded, if at all, in application code, chat threads, ticket comments, and tribal memory. Two protocol standards address adjacent concerns: MCP standardises agent access to tools and data, and A2A standardises agent-to-agent interoperability. Neither defines the shared workspace in which humans and agents perform accountable work together. This paper presents CHAP, the Collaborative Human-Agent Protocol. Under CHAP, the override that used to vanish into a chat thread becomes a structured event carrying a diff, a rationale, and a content hash. The handoff between shifts becomes a portable envelope rather than a pinned message. The human approval of an agent's draft becomes a non-repudiable signed decision that can be replayed years later. The protocol achieves this through a small Core (workspaces, participants, tasks, artefacts, and an append-only evidence log) together with composable profiles that add review, modes, routing, deliberation, handoff, identity, signatures, and transparency-backed audit as deployments require them. Specification, reference implementation, conformance sui…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2606.09751v1)
- [PDF](https://arxiv.org/pdf/2606.09751v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/ai #keyword/agents #keyword/research-paper
