---
title: "Right Reason, Wrong Advice: Evaluating Recourse in LLM Explanations of Denied Requests"
source: "https://arxiv.org/html/2611.21545v1"
author: "Arunkumar V"
published: "2026-11-16"
created: 2026-11-18
description: "Language models increasingly write the explanations people receive when a rule system denies their request. If several rules deny the request independently, an explanation can name a true reason and still leave the person denied after they fix it. We call the missing property recourse validity: changing what the explanation cites, without changing what was asked for, can flip the decision. We compute it exactly, and…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/nlp
  - keyword/evaluation
  - keyword/reasoning
---

# Right Reason, Wrong Advice: Evaluating Recourse in LLM Explanations of Denied Requests

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.21545v1)
- published:: 2026-11-16
- updated:: 2026-11-16
- arxiv_id:: 2611.21545v1
- pdf:: https://arxiv.org/pdf/2611.21545v1
- categories:: cs.AI, cs.CL, cs.CY

## Abstract / Summary
Language models increasingly write the explanations people receive when a rule system denies their request. If several rules deny the request independently, an explanation can name a true reason and still leave the person denied after they fix it. We call the missing property recourse validity: changing what the explanation cites, without changing what was asked for, can flip the decision. We compute it exactly, and a hitting-set argument predicts from the policy alone when a correct reason fails. In six of seven rule systems ported from access control and US benefit eligibility, a single correct reason almost never gives recourse when several reasons apply. Across 20 LLMs, checks of whether the cited reasons are correct, computed or asked of an LLM judge, are close to chance at spotting this failure, as the argument predicts. A strong judge asked whether acting on the explanation would work does spot it. Stronger and reasoning models do better but still fail on many denials with four or more independent reasons. Asking for every rule helps every open model with room to improve. Explanations of eligibility decisions should be built from the decision function and judged by whether acting on them works.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.21545v1)
- [PDF](https://arxiv.org/pdf/2611.21545v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/nlp #keyword/evaluation #keyword/reasoning
