---
title: "Reading Why: Born-Measured Attention with Exact Word Evidence on Light and Qubits"
source: "https://arxiv.org/html/2611.05355v1"
author: "Teerawat Tongloy, Jiraporn Pongsopa, Rangsan Jomtarak"
published: "2026-11-03"
created: 2026-11-05
description: "When a language model answers, we can usually only estimate why. We build a transformer in which every step is a Born measurement - attention $|\langle q|k\rangle|^4$ normalised over each row, a measured product in place of the feed-forward nonlinearity, and a Born readout. With its denominators held at their values for the input, each class probability is a polynomial in the word amplitudes, so its integrated-gradi…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/transformer
  - keyword/language-model
  - keyword/nlp
  - keyword/machine-learning
---

# Reading Why: Born-Measured Attention with Exact Word Evidence on Light and Qubits

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.05355v1)
- published:: 2026-11-03
- updated:: 2026-11-03
- arxiv_id:: 2611.05355v1
- pdf:: https://arxiv.org/pdf/2611.05355v1
- categories:: quant-ph, cs.CL, cs.LG, physics.optics

## Abstract / Summary
When a language model answers, we can usually only estimate why. We build a transformer in which every step is a Born measurement - attention $|\langle q|k\rangle|^4$ normalised over each row, a measured product in place of the feed-forward nonlinearity, and a Born readout. With its denominators held at their values for the input, each class probability is a polynomial in the word amplitudes, so its integrated-gradient evidence is computed by a finite quadrature with no quadrature error: the words' contributions sum to the class probability above its no-information share, to $10^{-11}$ or better. On e-SNLI natural language inference, with about 98k parameters outside the embedding, the model reaches $76.98 \pm 0.17$% test accuracy, level with a softmax transformer of the same size ($76.62 \pm 0.36$%). Deleting the word its evidence ranks first changes the answer in 45% of test pairs, out of the 53% any single deletion can change, against 32% for the softmax model explained the same way and 40% by its attention x gradient. Attention can look more like the words annotators highlighted, yet accounts for the answer less well: deleting the word it ranks first changes the Born Transformer's answer in 32% of pairs. The same weights compile exactly to optoelectronic optics and to qubits, and a coherent attention layer becomes one circuit equal to the model (852 CNOTs on 23 qubits). On IBM's ibm_kingston, reading only the attention overlaps by Hadamard tests, the device gave the model's answers on two short test pairs and kept or changed them under deletion as the model does; the evidence itself did not yet survive the device, and we work out the shots and calibration that measuring it on hardware would need.

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.05355v1)
- [PDF](https://arxiv.org/pdf/2611.05355v1)
- [Seeing Why: Exact Evidence Maps for Quantum and Optical Image Classifiers](https://arxiv.org/abs/2611.01993) (2026, citations: 1)
- [Watching Quantum Models Think: Hilbert-Space Interpretability in Quantum Transformer Blocks](https://arxiv.org/abs/2609.23016) (2026, citations: 1)
- [A Quantum Roadmap for Softmax Attention: Exact Born-Rule Analogs for Softmax Attention on the Probability Simplex](https://arxiv.org/abs/2608.11173) (2026, citations: 2)
- [Photonic transformer chip: interference is all you need](https://photonix.springeropen.com/counter/pdf/10.1186/s43074-025-00182-7) (2025, citations: 11)
- [Quantum NLP models on Natural Language Inference](https://arxiv.org/abs/2510.15972) (2025, citations: 2)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/transformer #keyword/language-model #keyword/nlp #keyword/machine-learning
