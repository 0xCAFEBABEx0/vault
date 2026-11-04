---
title: "Dharma Field Extractor: Any Document In, Structured Fields in JSON Out"
source: "https://huggingface.co/blog/Dharma-AI/dharma-field-extractor"
author: "Hugging Face Blog"
published: "2026-11-04"
created: 2026-11-05
description: "In April, we released DharmaOCR-LITE , a model specialized for OCR across a wide range of documents, from contracts and court filings to invoices, IDs and forms. The paper behind it made a narrow, well-measured case for domain specialization: a smaller model trained closer to its task beating general-purpose frontier APIs on that task. OCR gives you the text on a page, faithful to the original formatting. That's exa…"
tags:
  - type/literature
  - theme/research
  - theme/learning
  - source/huggingface
  - keyword/nlp
---

# Dharma Field Extractor: Any Document In, Structured Fields in JSON Out

## Source Metadata
- type:: blog
- source:: [Hugging Face Blog](https://huggingface.co/blog/Dharma-AI/dharma-field-extractor)
- published:: 2026-11-04

## Abstract / Summary
In April, we released DharmaOCR-LITE , a model specialized for OCR across a wide range of documents, from contracts and court filings to invoices, IDs and forms. The paper behind it made a narrow, well-measured case for domain specialization: a smaller model trained closer to its task beating general-purpose frontier APIs on that task. OCR gives you the text on a page, faithful to the original formatting. That's exactly what you want when the job is the whole document, like a contract you'll read end to end or a manuscript you're digitizing. However, there's a different use case: you don't want the page, you want specific fields out of it, in a shape a system downstream can consume. Every line item on an invoice, as a list. The patient name, exam type and date from a medical requisition, ready to schedule. The fields off an ID, mapped to the columns of an employee record. Run that document through OCR and you get back everything printed on it, line by line, with no indication of which string is the exam type, which is the date or which number is the total. Someone still has to write the code that maps each value to the right field before it reaches the database. A general-purpose…

## Why it matters for GenAI tracking
- Captured automatically as part of the nightly generative-AI research and technical-blog watchlist.
- Review manually before promoting any idea to `3_Permanent` notes.

## Related Materials
- [Hugging Face Blog](https://huggingface.co/blog)

## Follow-up Questions
- question:: Should this be converted into a permanent insight note?
- question:: Are there implementation details, benchmarks, or released code worth tracking separately?

---
Tags: #type/literature #theme/research #theme/learning #source/huggingface #keyword/nlp
