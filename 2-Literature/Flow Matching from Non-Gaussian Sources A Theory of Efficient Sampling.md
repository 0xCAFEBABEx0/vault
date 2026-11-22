---
title: "Flow Matching from Non-Gaussian Sources: A Theory of Efficient Sampling"
source: "https://arxiv.org/html/2611.26407v1"
author: "Yuchen Zhou, Lili Zheng, Yuxin Chen, Gen Li"
published: "2026-11-19"
created: 2026-11-23
description: "Flow matching is a versatile framework for generative modeling that transports a source distribution to a target data distribution. A key advantage is its flexibility in the choice of source distribution, such as heavy-tailed and multimodal sources. Yet finite-step sampling guarantees for non-Gaussian sources remain limited. We establish a nonasymptotic convergence theory for Euler discretization of flow matching wi…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/multimodal
---

# Flow Matching from Non-Gaussian Sources: A Theory of Efficient Sampling

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.26407v1)
- published:: 2026-11-19
- updated:: 2026-11-19
- arxiv_id:: 2611.26407v1
- pdf:: https://arxiv.org/pdf/2611.26407v1
- categories:: stat.ML, cs.AI, cs.IT, cs.LG

## Abstract / Summary
Flow matching is a versatile framework for generative modeling that transports a source distribution to a target data distribution. A key advantage is its flexibility in the choice of source distribution, such as heavy-tailed and multimodal sources. Yet finite-step sampling guarantees for non-Gaussian sources remain limited. We establish a nonasymptotic convergence theory for Euler discretization of flow matching with linear interpolation. Suppose the source distribution on $\mathbb{R}^d$ has an everywhere positive, continuously differentiable density, finite total variance $\mathsf{TotVar}_{\mathsf{base}}$, and an $L$-Lipschitz score. Using the population velocity field and a suitable time grid, this sampler achieves total variation error at most $\varepsilon$ in $\widetilde{O}(Ld\mathsf{TotVar}_{\mathsf{base}}/\varepsilon)$ iterations, provided the target distribution satisfies a mild second-moment condition. These assumptions cover, among many examples, source distributions such as multivariate Student's $t$ distributions with more than two degrees of freedom and finite Gaussian mixtures with shared covariance, while accommodating target distributions with neither a smooth density nor bounded support.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.26407v1)
- [PDF](https://arxiv.org/pdf/2611.26407v1)
- [Forward-Value Discretization: Faster Stochastic Diffusion Sampling Without High-Order Approximation](https://arxiv.org/abs/2611.14328) (2026, citations: 1)
- [Setting Things Straight: On the Straightness and Non-Straightness of Two-Step Rectified Flow](https://arxiv.org/abs/2610.36090) (2026, citations: 2)
- [From Global to Tail Convergence: Dynamics of $\alpha$-Stable Score-Based Generative Models](https://arxiv.org/abs/2610.19773) (2026, citations: 1)
- [Limit Points of Reflow with Minibatch Optimal Transport](https://arxiv.org/abs/2608.07042) (2026, citations: 3)
- [Computational and Statistical Guarantees of the c-Rectified flow](https://arxiv.org/abs/2608.02487) (2026, citations: 2)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/multimodal
