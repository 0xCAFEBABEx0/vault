---
title: "Shape-Aware Three-Way Merge for RDF Knowledge Graphs: The schema defines the conflict: an implementation and evaluation"
source: "https://arxiv.org/html/2611.34870v1"
author: "Steve Brown"
published: "2026-11-25"
created: 2026-11-28
description: "Merging RDF serializations creates ordering conflicts and misses semantic ones. We describe and evaluate a three-way merge in which the schema defines a conflict: set algebra combines canonical triples, and a slot is contended only where a SHACL shape bounds its cardinality and both sides' changes cannot stand within that bound. Unbounded predicates union; contended slots go to a person. The same shapes graph valida…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/arxiv
  - keyword/nlp
  - keyword/evaluation
  - keyword/agents
---

# Shape-Aware Three-Way Merge for RDF Knowledge Graphs: The schema defines the conflict: an implementation and evaluation

## Source Metadata
- type:: paper
- source:: [arXiv](https://arxiv.org/html/2611.34870v1)
- published:: 2026-11-25
- updated:: 2026-11-25
- arxiv_id:: 2611.34870v1
- pdf:: https://arxiv.org/pdf/2611.34870v1
- categories:: cs.DB, cs.AI, cs.SE

## Abstract / Summary
Merging RDF serializations creates ordering conflicts and misses semantic ones. We describe and evaluate a three-way merge in which the schema defines a conflict: set algebra combines canonical triples, and a slot is contended only where a SHACL shape bounds its cardinality and both sides' changes cannot stand within that bound. Unbounded predicates union; contended slots go to a person. The same shapes graph validates the result. We do not claim the first three-way merge for RDF. Our contribution is an implementation in a production multi-agent store and an evaluation against a reimplementation of Quit Store's Context Merge overlap rule, which it extends rather than replaces, and six other strategies. Across five synthetic seeds, the shape-aware operator raised 33 conflicts, all true positives as judged by the same shapes that define them, with no triples lost or fabricated and no SHACL violations admitted. The context-overlap baseline, counted per slot, detected the same 33 conflicts but asked 845 questions. A replay built from recorded production incidents covers 105 human alias repairs (93 after excluding 12 chained pairs) and 939 duplicate-value incidents. It reproduces a triple-level limit: different names for one entity remain invisible (0 of 93 alias repairs detected, matching 0 of 21 synthetic cases). In a study of evolving shape contracts, merging shape declarations first handles the tested cardinality changes, while datatype evolution exposes a detector blind spot caught by post-merge validation. An oracle that reads no shapes agrees with the shipped operator on the facts and history of all 23 reachable single-slot cases. Under wrong shapes, a missing bound loses data silently and a spurious one only adds questions. The supported claim is fewer human decisio…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [arXiv abstract](https://arxiv.org/abs/2611.34870v1)
- [PDF](https://arxiv.org/pdf/2611.34870v1)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/arxiv #keyword/nlp #keyword/evaluation #keyword/agents
