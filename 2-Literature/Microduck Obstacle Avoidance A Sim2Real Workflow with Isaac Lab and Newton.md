---
title: "Microduck Obstacle Avoidance: A Sim2Real Workflow with Isaac Lab and Newton"
source: "https://huggingface.co/blog/nvidia/microduck-obstacle-avoidance"
author: "Hugging Face Blog"
published: "2026-11-24"
created: 2026-11-25
description: "Search models, datasets, users... Ctrl K Models Datasets Spaces Buckets Docs Enterprise Pricing Website Tasks HuggingChat Collections Languages Organizations Community Blog Posts Daily Papers Hardware Learn Discord Forum GitHub Solutions Team & Enterprise Hugging Face PRO Enterprise Support Inference Providers Inference Endpoints Storage Buckets Log In Sign Up Back to Articles a]:hidden'> Microduck Obstacle Avoidanc…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/nlp
  - keyword/retrieval
  - keyword/evaluation
  - keyword/machine-learning
---

# Microduck Obstacle Avoidance: A Sim2Real Workflow with Isaac Lab and Newton

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/nvidia/microduck-obstacle-avoidance)
- published:: 2026-11-24

## Abstract / Summary
Search models, datasets, users... Ctrl K Models Datasets Spaces Buckets Docs Enterprise Pricing Website Tasks HuggingChat Collections Languages Organizations Community Blog Posts Daily Papers Hardware Learn Discord Forum GitHub Solutions Team & Enterprise Hugging Face PRO Enterprise Support Inference Providers Inference Endpoints Storage Buckets Log In Sign Up Back to Articles a]:hidden"> Microduck Obstacle Avoidance: A Sim2Real Workflow with Isaac Lab and Newton Enterprise + Article Published… TL;DR Add local obstacle avoidance to Microduck while keeping its walking policy fixed. Build varied courses with reusable SimReady assets, model ToF sensing with Newton’s raycaster, and train a controller in Isaac Lab to adjust gamepad velocity commands around obstacles. This tutorial covers simulation training, evaluation, export, and real-robot deployment. Introduction A walking policy can keep Microduck balanced, but it does not tell the robot how to steer around an obstacle in its path. In this workflow, we reuse the walking policy from our first Microduck tutorial and keep its weights fixed. This follow-up trains a separate avoidance controller using time-of-flight (ToF) sensing. You…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/nlp #keyword/retrieval #keyword/evaluation #keyword/machine-learning
