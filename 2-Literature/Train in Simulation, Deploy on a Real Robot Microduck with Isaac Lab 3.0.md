---
title: "Train in Simulation, Deploy on a Real Robot: Microduck with Isaac Lab 3.0"
source: "https://huggingface.co/blog/nvidia/microduck-isaac-lab-sim-to-real"
author: "Hugging Face Blog"
published: "2026-10-21"
created: 2026-10-22
description: "TL;DR Microduck is a newly released affordable open-source bipedal robot by Pollen Robotics and Hugging Face. And now you can train Microduck to walk with Isaac Lab and Newton. Test the policy, export it as ONNX, and deploy it on the real robot. Share it on the Hugging Face Hub or validate it for competition in Microduck Arena, then explore more advanced tasks with NVIDIA Isaac Lab . Introduction A walking policy tr…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/evaluation
  - keyword/machine-learning
---

# Train in Simulation, Deploy on a Real Robot: Microduck with Isaac Lab 3.0

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/nvidia/microduck-isaac-lab-sim-to-real)
- published:: 2026-10-21

## Abstract / Summary
TL;DR Microduck is a newly released affordable open-source bipedal robot by Pollen Robotics and Hugging Face. And now you can train Microduck to walk with Isaac Lab and Newton. Test the policy, export it as ONNX, and deploy it on the real robot. Share it on the Hugging Face Hub or validate it for competition in Microduck Arena, then explore more advanced tasks with NVIDIA Isaac Lab . Introduction A walking policy trained in simulation must also handle the friction, delays, and mechanical play of real robot servos.. NVIDIA Isaac Lab is an open-source framework for training policies across thousands of GPU-parallel simulations. With Newton , actuator modeling, and domain randomization, developers can prepare policies for real hardware. Microduck brings this workflow to life: train a walking policy in simulation, export it as ONNX, and deploy it on a real biped robot. This tutorial walks you through training and evaluating Microduck with Isaac Lab and Newton, then exporting the policy for deployment. From there, you can share your model on the Hugging Face Hub, test its compatibility and compete in Microduck Arena, or put it to work on your own Microduck. Walking is the starting poin…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/evaluation #keyword/machine-learning
