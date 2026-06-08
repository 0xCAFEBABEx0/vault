---
title: "Closed-Form Spectral Regularization for Multi-Task Model Merging"
authors: "Multiple authors"
year: 2026
tags: [model-merging, multi-task, spectral-regularization, optimization]
---

## Overview
Proposes a closed-form spectral regularization method for merging multiple task-specific models into a single multi-task model. The approach addresses interference between task-specific parameters during merging.

## Key Contributions
- Closed-form solution for spectral regularization in model merging
- Principled method to minimize interference between task-specific weight spaces
- Efficient computation without iterative optimization

## Method
- Analysis of spectral properties of task-specific weight matrices
- Regularization term that encourages compatible spectral structures
- Closed-form solution derived from spectral decomposition
- Extension to handle varying model architectures and task complexities

## Results
- Significant improvement over naive averaging and existing merging methods
- Better preservation of per-task performance after merging
- Scalable to large language models with multiple task adapters

## Significance
Provides a theoretically grounded and computationally efficient approach to multi-task model merging, relevant for combining specialized models without full retraining.