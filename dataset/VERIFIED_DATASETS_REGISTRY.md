# VERIFIED DATASETS REGISTRY FOR HMI THESIS

**Last Updated:** 7 March 2026
**Status:** All datasets verified as publicly accessible with confirmed URLs

---

## CATEGORY A: Mental Health Conversation Datasets (for Scenario Bank & Groundedness)

### 1. MentalChat16K
- **Source:** HuggingFace — [ShenLab/MentalChat16K](https://huggingface.co/datasets/ShenLab/MentalChat16K)
- **Size:** 16,000+ synthetic counseling conversations (9,775 synthetic + real data)
- **License:** MIT
- **Format:** CSV
- **Paper:** arXiv:2503.13509
- **Downloads:** 1,400+
- **Use in HMI:** Ground truth knowledge base for Response Groundedness (RG) dimension; source of realistic mental health prompts for scenario bank design
- **Verified:** YES — publicly accessible on HuggingFace

### 2. ESConv (Emotional Support Conversation)
- **Source:** HuggingFace — [thu-coai/esconv](https://huggingface.co/datasets/thu-coai/esconv)
- **GitHub:** [thu-coai/Emotional-Support-Conversation](https://github.com/thu-coai/Emotional-Support-Conversation)
- **Size:** 1,300 conversations, 31,410 utterances
- **License:** CC-BY-NC-4.0
- **Format:** JSON
- **Paper:** Liu et al. (2021), "Towards Emotional Support Dialog Systems," ACL 2021. arXiv:2106.01144
- **Downloads:** 13,100+
- **Use in HMI:** Informs scenario bank design — provides templates for emotional support conversation structures and 8 support strategies; validates clinical realism of MH-Hallu-MY prompts
- **Verified:** YES — publicly accessible on HuggingFace

### 3. Counsel Chat
- **Source:** HuggingFace — [nbertagnolli/counsel-chat](https://huggingface.co/datasets/nbertagnolli/counsel-chat)
- **Size:** 1,000+ real counseling Q&A pairs
- **License:** Open
- **Format:** CSV
- **Paper:** Bertagnolli (2020), "Counsel Chat: Bootstrapping High-Quality Therapy Data"
- **Downloads:** 703
- **Use in HMI:** Secondary ground truth for Response Groundedness (RG) dimension; real counselor responses for evaluating chatbot alignment with professional advice
- **Verified:** YES — publicly accessible on HuggingFace

### 4. Mental Health Counseling Conversations
- **Source:** HuggingFace — [Amod/mental_health_counseling_conversations](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations)
- **Size:** 1K-10K real counseling conversations
- **License:** Other (open)
- **Format:** JSON
- **DOI:** 10.57967/hf/1581
- **Downloads:** 2,000+
- **Use in HMI:** Additional ground truth for clinical response validation; supplements MentalChat16K for RG knowledge base
- **Verified:** YES — publicly accessible on HuggingFace

### 5. Mental Health Conversational Data (Kaggle)
- **Source:** Kaggle — [elvis23/mental-health-conversational-data](https://www.kaggle.com/datasets/elvis23/mental-health-conversational-data)
- **Use in HMI:** Supplementary conversation patterns for scenario bank design
- **Verified:** YES — publicly accessible on Kaggle

### 6. Mental Health FAQ for Chatbot (Kaggle)
- **Source:** Kaggle — [narendrageek/mental-health-faq-for-chatbot](https://www.kaggle.com/datasets/narendrageek/mental-health-faq-for-chatbot)
- **Size:** 98 FAQs (QuestionID, Questions, Answers)
- **Use in HMI:** FAQ-style prompts for factual accuracy testing in scenario bank
- **Verified:** YES — publicly accessible on Kaggle

---

## CATEGORY B: Hallucination Benchmarks (for HMI Validation)

### 7. HaluEval
- **Source:** HuggingFace — [pminervini/HaluEval](https://huggingface.co/datasets/pminervini/HaluEval)
- **GitHub:** [RUCAIBox/HaluEval](https://github.com/RUCAIBox/HaluEval)
- **Size:** 35,000 samples (5,000 general + 30,000 task-specific)
- **License:** Apache 2.0
- **Paper:** Li et al. (2023), "HaluEval: A Large-Scale Hallucination Evaluation Benchmark," EMNLP 2023. arXiv:2305.11747
- **Downloads:** 5,200+
- **Use in HMI:** Validation benchmark — HMI scores on HaluEval dialogue subset compared against established hallucination labels; validates Factual Consistency (FC) dimension
- **Verified:** YES — publicly accessible on HuggingFace

### 8. TruthfulQA
- **Source:** HuggingFace — [truthfulqa/truthful_qa](https://huggingface.co/datasets/truthfulqa/truthful_qa)
- **Size:** 817 questions across 38 categories (including health)
- **License:** Apache 2.0
- **Paper:** Lin et al. (2022), "TruthfulQA: Measuring How Models Mimic Human Falsehoods," ACL 2022. arXiv:2109.07958
- **Downloads:** 62,600+
- **Use in HMI:** Validation benchmark — HMI FC scores on health-related TruthfulQA questions compared against truthfulness labels; cross-validates composite HMI against established truthfulness measure
- **Verified:** YES — publicly accessible on HuggingFace

### 9. MedHallu
- **Source:** HuggingFace — [UTAustin-AIHealth/MedHallu](https://huggingface.co/datasets/UTAustin-AIHealth/MedHallu)
- **Size:** 10K-100K medical hallucination samples
- **Paper:** arXiv:2502.14302 (2025)
- **Downloads:** 1,000+
- **Use in HMI:** Domain-specific validation — HMI evaluated on medical hallucination cases to validate clinical sensitivity; most directly relevant benchmark for healthcare hallucination
- **Verified:** YES — publicly accessible on HuggingFace

### 10. SelfCheckGPT WikiBio Dataset
- **Source:** HuggingFace — [potsawee/wiki_bio_gpt3_hallucination](https://huggingface.co/datasets/potsawee/wiki_bio_gpt3_hallucination)
- **Size:** <1,000 samples with human annotations
- **License:** CC-BY-SA-3.0
- **Paper:** Manakul et al. (2023), "SelfCheckGPT," EMNLP 2023. arXiv:2303.08896
- **Downloads:** 29,500+
- **Use in HMI:** Reference implementation and calibration dataset for Factual Consistency (FC) dimension; used to validate SelfCheckGPT scoring pipeline
- **Verified:** YES — publicly accessible on HuggingFace

### 11. Hallucinations Leaderboard Results
- **Source:** HuggingFace — [hallucinations-leaderboard/results](https://huggingface.co/datasets/hallucinations-leaderboard/results)
- **Size:** Comprehensive multi-model benchmark results
- **License:** Apache 2.0
- **Downloads:** 58,400+
- **Use in HMI:** Cross-referencing HMI chatbot rankings against leaderboard rankings for external validity
- **Verified:** YES — publicly accessible on HuggingFace

---

## CATEGORY C: Safety & Toxicity Datasets (for Safety Compliance Dimension)

### 12. Ethical Reasoning in Mental Health (EthicsMH)
- **Source:** HuggingFace — [UVSKKR/Ethical-Reasoning-in-Mental-Health-v1](https://huggingface.co/datasets/UVSKKR/Ethical-Reasoning-in-Mental-Health-v1)
- **Size:** <1K ethical reasoning samples
- **Paper:** arXiv:2509.11648
- **Downloads:** 1,600+
- **Use in HMI:** Informs Safety Compliance (SC) rubric design — provides ethical reasoning benchmarks specific to mental health AI
- **Verified:** YES — publicly accessible on HuggingFace (gated)

---

## DATASET-TO-HMI-DIMENSION MAPPING

| HMI Dimension | Primary Dataset | Validation Dataset | Tool |
|---|---|---|---|
| Factual Consistency (FC) | SelfCheckGPT WikiBio (#10) | HaluEval (#7), TruthfulQA (#8) | SelfCheckGPT |
| Response Groundedness (RG) | MentalChat16K (#1), Counsel Chat (#3) | MedHallu (#9) | DeBERTa NLI |
| Safety Compliance (SC) | EthicsMH (#12) | Do-Not-Answer* | Detoxify + rubric |
| Semantic Coherence (SH) | ESConv (#2) | HaluEval dialogue (#7) | BERTScore + VADER |
| Cultural Appropriateness (CA) | Custom MH-Hallu-MY | — | Custom rules + NER |

*Do-Not-Answer: Wang et al. (2023) — available at https://github.com/Libr-AI/do-not-answer

---

## HOW EACH DATASET IS USED (Research Justification)

### For Scenario Bank Design (MH-Hallu-MY):
- **MentalChat16K** → Extract clinical topic categories and conversation patterns
- **ESConv** → Adopt emotional support strategy framework (8 strategies)
- **Counsel Chat** → Derive real counselor question types
- **Kaggle MH FAQ** → Include FAQ-style factual queries

### For HMI Ground Truth / Knowledge Base:
- **MentalChat16K + Counsel Chat + Amod conversations** → Combined as reference knowledge base for NLI-based groundedness checking

### For HMI Validation:
- **HaluEval** → Run HMI pipeline on known-hallucinated vs non-hallucinated dialogue samples; compute accuracy/F1
- **TruthfulQA (health subset)** → Run HMI on health questions; compare FC scores against truthfulness labels
- **MedHallu** → Run HMI on medical hallucination cases; validate clinical sensitivity
- **SelfCheckGPT WikiBio** → Calibrate FC dimension scoring thresholds

### For Safety Rubric:
- **EthicsMH** → Derive ethical violations categories for SC dimension
- **Do-Not-Answer** → Identify unsafe response patterns for SC binary flags

---

## TOTAL VERIFIED DATASETS: 12
## ALL PUBLICLY ACCESSIBLE: YES
## ALL WITH CONFIRMED URLs: YES
