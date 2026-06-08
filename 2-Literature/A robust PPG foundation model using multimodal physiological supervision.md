---
title: "A robust PPG foundation model using multimodal physiological supervision"
authors: "Evan D. Morris, et al."
year: 2026
tags: [foundation-model, PPG, multimodal, physiological, biosignal]
---

## Overview
A foundation model for photoplethysmography (PPG) signals trained using multimodal physiological supervision. The model leverages multiple physiological signals during pre-training to learn robust representations of PPG data.

## Key Contributions
- Multimodal supervision strategy combining PPG with other physiological signals (ECG, accelerometry, etc.)
- Robust representation learning for PPG signals
- Foundation model that can be fine-tuned for downstream tasks like heart rate estimation, SpO2 prediction, arrhythmia detection

## Method
- Pre-training on large-scale PPG datasets with auxiliary physiological signals
- Self-supervised learning objectives leveraging cross-modal correspondence
- Evaluation on clinical PPG analysis tasks

## Results
- Significant improvements over single-modality baselines
- Strong generalization across different patient populations and recording conditions
- Competitive performance on clinical biomarker prediction tasks

## Significance
Demonstrates that multimodal physiological supervision can produce more robust biosignal foundation models, with implications for wearable health monitoring.