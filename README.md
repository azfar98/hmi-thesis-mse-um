# Hallucination Measurement Index (HMI) Framework for Bilingual Malay-English Mental Health Chatbots

Master of Software Engineering thesis — Universiti Malaya
**Author:** Azfar Rahman bin Fazul Rahman (Matric 23057185)
**Supervisor:** Dr. Hema A/P Subramaniam

This repository holds the final thesis, the HMI scoring engine source code, the scored dataset, statistical results, defence screenshots, and the literature references used in the study.

---

## Repository structure

| Folder | Contents |
|---|---|
| [`thesis/`](thesis/) | Final signed thesis PDF + English and Bahasa Malaysia abstracts, as submitted to Dr. Hema via MAYA |
| [`source_code/`](source_code/) | HMI scoring engine (`hmi_core.py`), Streamlit dashboard (`app.py`), and the data-collection script used to gather chatbot responses |
| [`dataset/`](dataset/) | MH-Hallu-MY scenario bank (305 prompts, EN+BM, 12 clinical categories) and the registry of 12 verified external datasets used |
| [`results/`](results/) | Full 2,745-response scored dataset (`hmi_results.csv`) plus the research matrices and statistical analysis workbooks |
| [`screenshots/`](screenshots/) | Dashboard screenshots (single-response, batch, cross-chatbot comparison modes) used in the thesis defence |
| [`references/`](references/) | Analysis of the source papers cited in the literature review (title, authors, DOI, abstract, relevance) |

---

## The HMI framework

HMI is a composite 0–100 hallucination score for AI mental-health chatbot responses, combining five weighted sub-metrics:

| Dimension | Weight | Tool |
|---|---|---|
| Factual Consistency (FC) | 0.30 | SelfCheckGPT |
| Response Groundedness (RG) | 0.25 | DeBERTa-large-MNLI (NLI) |
| Safety Compliance (SC) | 0.25 | Detoxify + custom rubric |
| Semantic Coherence (SH) | 0.10 | BERTScore + VADER |
| Cultural Appropriateness (CA) | 0.10 | Custom Malaysian-context rules |

```
HMI = (0.30·FC + 0.25·RG + 0.25·SC + 0.10·SH + 0.10·CA) × 100
```

Severity bands: MINIMAL (0–10) · LOW (11–30) · MODERATE (31–50) · HIGH (51–75) · CRITICAL (76–100)

## Dataset

**MH-Hallu-MY**: 305 prompts (155 English + 150 Bahasa Malaysia) across 12 ICD-11/DSM-5 clinical categories, tested against 3 platforms (ChatGPT/GPT-4, Gemini Pro, Microsoft Copilot) × 3 repeats = **2,745 scored responses**.

## Running the prototype

See [`source_code/README.md`](source_code/README.md) for setup and demo instructions. API keys for the data-collection script are **not included** — copy [`source_code/data_collection/config.py.example`](source_code/data_collection/config.py.example) to `config.py` and fill in your own keys (this file is gitignored).

## Note on literature references

`references/PAPER_ANALYSIS_ALL.md` contains bibliographic analysis (title, authors, DOI, abstract, relevance) of the papers cited in the thesis, not the source PDFs themselves — most are copyrighted publisher content and are not redistributed here. Use the DOIs to retrieve the original papers.

---

*Private repository — not for public distribution without the author's and supervisor's permission.*
