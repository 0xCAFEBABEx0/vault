---
title: "Introducing harness adapters: adapt your favorite model to your harness to improve performance and cost"
source: "https://huggingface.co/blog/harness-adapters-at-scale"
author: "Hugging Face Blog"
published: "2026-11-20"
created: 2026-11-21
description: "Search models, datasets, users... Ctrl K Models Datasets Spaces Buckets Docs Enterprise Pricing Website Tasks HuggingChat Collections Languages Organizations Community Blog Posts Daily Papers Hardware Learn Discord Forum GitHub Solutions Team & Enterprise Hugging Face PRO Enterprise Support Inference Providers Inference Endpoints Storage Buckets Log In Sign Up Back to Articles a]:hidden'> Introducing harness adapter…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/nlp
  - keyword/retrieval
  - keyword/reasoning
  - keyword/agents
  - keyword/machine-learning
---

# Introducing harness adapters: adapt your favorite model to your harness to improve performance and cost

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/harness-adapters-at-scale)
- published:: 2026-11-20

## Abstract / Summary
Search models, datasets, users... Ctrl K Models Datasets Spaces Buckets Docs Enterprise Pricing Website Tasks HuggingChat Collections Languages Organizations Community Blog Posts Daily Papers Hardware Learn Discord Forum GitHub Solutions Team & Enterprise Hugging Face PRO Enterprise Support Inference Providers Inference Endpoints Storage Buckets Log In Sign Up Back to Articles a]:hidden"> Introducing harness adapters: adapt your favorite model to your harness to improve performance and cost Pub… Models are not fully optimized for all harnesses and the tasks you’re doing. Instead, they target general performance. So when you combine a model and harness, you’re leaving performance and efficiency on the table for the stuff you’re actually doing. With RL, you can train a custom harness adapter that squeezes everything out of your model for your harness and task combination. Take Qwen3.8-27B, its Terminal-Bench 2.1 score with the pi harness is 39% which uses on average 2.9K tokens per task. If we freeze those weights and add a custom RL-trained LoRA adapter we can get 55% pass@1, with average token usage of 1.5K. Most of this is down to the model reasoning less, calling less tools, and…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/nlp #keyword/retrieval #keyword/reasoning #keyword/agents #keyword/machine-learning
