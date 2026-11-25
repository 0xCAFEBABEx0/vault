---
title: "DiaCap: Jointly Learning Who Speaks When for Audiovisual Dialogue Captioning"
source: "https://arxiv.org/html/2611.33153v1"
author: "Binfei Ji, Zhiwen Cao, Anqi Yang, Prem Seetharaman, Shuo Yang, Ratheesh Kalarot, Yingyan Celine Lin, Mingze Xu"
published: "2026-11-24"
created: 2026-11-26
description: "We present DiaCap, an audiovisual LLM for comprehensive dialogue captioning, which produces the transcript, timestamps, and a visual description of the speaker for every utterance in a video. Considering that utterance timing and audiovisual diarization are tightly coupled, DiaCap unifies the tasks in a single model, trained in two complementary stages. First, we train DiaCap on 225K curated clips, using synthetic c…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/language-model
  - keyword/multimodal
  - keyword/evaluation
---

# DiaCap: Jointly Learning Who Speaks When for Audiovisual Dialogue Captioning

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.33153v1)
- published:: 2026-11-24
- updated:: 2026-11-24
- arxiv_id:: 2611.33153v1
- pdf:: https://arxiv.org/pdf/2611.33153v1
- categories:: cs.CV, cs.CL, cs.MM, cs.SD

## Abstract / Summary
We present DiaCap, an audiovisual LLM for comprehensive dialogue captioning, which produces the transcript, timestamps, and a visual description of the speaker for every utterance in a video. Considering that utterance timing and audiovisual diarization are tightly coupled, DiaCap unifies the tasks in a single model, trained in two complementary stages. First, we train DiaCap on 225K curated clips, using synthetic captions that densely label every utterance in detail. Second, we further refine the model via reinforcement learning on 2.9K human-corrected clips, using fine-grained feedback that directly evaluates utterance timing, speaker grouping, and speaker binding. On DiaDemBench, which we extend with utterance-level timestamps and subtitle redaction, both DiaCap with off-the-shelf transcripts and its end-to-end variant DiaCap-E2E achieve strong results. Specifically, DiaCap performs on par with Gemini 4 Argon in audiovisual diarization while clearly outperforming it in timestamp accuracy (76.59 vs. 42.76 TIME). It also maintains strong diarization on multilingual and minute-long videos, and transfers to audiovisual question answering.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.33153v1)
- [PDF](https://arxiv.org/pdf/2611.33153v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/language-model #keyword/multimodal #keyword/evaluation
