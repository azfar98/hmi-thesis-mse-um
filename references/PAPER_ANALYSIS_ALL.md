# Comprehensive Analysis of 77 Hallucination in Chatbots Papers

**Master's Thesis:** Hallucination Measurement Index for AI-Powered Mental-Health Chatbots in Malaysia

**Analysis Date:** 2026-03-06

---

## Paper 1: Diving Deep into Modes of Fact Hallucinations in Dialogue Systems

**Year:** 2022

**Authors:** Souvik Das
Swati Saha
Rohini K. Srihari

**DOI:** 10.18653/v1/2022.findings-emnlp.48

### Abstract

Knowledge Graph(KG) grounded conversations often use large pre-trained models and usually suffer from fact hallucination.Frequently entities with no references in knowledge sources and conversation history are introduced into responses, thus hindering the flow of the conversation-existing work attempt to overcome this issue by tweaking the training procedure or using a multi-step refining method.However, minimal effort is put into constructing an entity-level hallucination detection system, which would provide fine-grained signals that control fallacious content while generating responses.As a first step to address this issue, we dive deep to identify various modes of hallucination in KG-grounded chatbots through human feedback analysis.Secondly, we propose a series of perturbation strategies to create a synthetic dataset named FADE (FActual Dialogue Hallucination DEtection Dataset) 1 .Finally, we conduct comprehensive data analyses and create multiple baseline models for hallucination detection to compare against human-verified data and already established benchmarks.

### Relevance to Thesis

- **Relevance Score:** 85/100 - **Relevance Tag:** Highly Relevant - **Reasoning:** Extends hallucination taxonomy to eight modes; builds FADE synthetic dataset for detection; evaluates on KG‑grounded chatbots with human studies; offers dataset release; mentions generate‑then‑refine but lacks dedicated mitigation experiments; no cross‑platform comparison or trust impact analysis.

### Analysis for Thesis

This paper examines hallucinations in dialogue systems, directly relevant to conversational mental health chatbots. The dialogue-specific findings could inform how hallucinations manifest in therapeutic conversations.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION

---

## Paper 2: On the Origin of Hallucinations in Conversational Models: Is it the Datasets or the Models?

**Year:** 2022

**DOI:** 10.18653/v1/2022.naacl-main.387

### Abstract

Nouha Dziri, Sivan Milton, Mo Yu, Osmar Zaiane, Siva Reddy. Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies. 2022.

### Relevance to Thesis

- **Relevance Score:** 81/100 - **Relevance Tag:** Highly Relevant - **Reasoning:** Provides a clear taxonomy of dialogue hallucinations and introduces a metric to quantify them in chatbots; evaluates models vs data on real conversational systems; discusses origins, hints at mitigation, and loosely compares model behaviors, but lacks user studies, trust impact analysis, and a released benchmark.

### Analysis for Thesis

This paper examines hallucinations in dialogue systems, directly relevant to conversational mental health chatbots. The dialogue-specific findings could inform how hallucinations manifest in therapeutic conversations.

### Category Tags

BENCHMARK, DEFINITION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 3: Can We Catch the Elephant? The Evolvement of Hallucination Evaluation on Natural Language Generation: A Survey

**Year:** 2024

**Authors:** Siya Qi
Yulan He
Zheng Yuan

**DOI:** 10.48550/arxiv.2404.12041

### Abstract

Hallucination in Natural Language Generation (NLG) is like the elephant in the room, obvious but often overlooked until recent achievements significantly improved the fluency and grammatical accuracy of generated text. For Large Language Models (LLMs), hallucinations can happen in various downstream tasks and casual conversations, which need accurate assessment to enhance reliability and safety. However, current studies on hallucination evaluation vary greatly, and people still find it difficult to sort out and select the most appropriate evaluation methods. Moreover, as NLP research gradually shifts to the domain of LLMs, it brings new challenges to this direction. This paper provides a comprehensive survey on the evolvement of hallucination evaluation methods, aiming to address three key aspects: 1) Diverse definitions and granularity of facts; 2) The categories of automatic evaluators and their applicability; 3) Unresolved issues and future directions.

### Relevance to Thesis

- **Relevance Score:** 62/100 - **Relevance Tag:** Partially Relevant - **Reasoning:** Provides comprehensive definitions and taxonomy of hallucination, surveys many evaluation metrics for dialogue, but mainly reviews existing work without new experiments, mitigation methods, user studies, platform comparisons, trust analysis, or releasing datasets.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL, SURVEY

---

## Paper 4: Benchmarking the Hallucination Tendency of Google Gemini and Moonshot Kimi

**Year:** 2024

**Authors:** Ruoxi Shan
Qiang Ming
Guang Hong
Hua Hsuan Wu

**DOI:** 10.31219/osf.io/83rq9

### Abstract

To evaluate the hallucination tendencies of state-of-the-art language models is crucial for improving their reliability and applicability across various domains. This article presents a comprehensive evaluation of Google Gemini and Kimi using the HaluEval benchmark, focusing on key performance metrics such as accuracy, relevance, coherence, and hallucination rate. Google Gemini demonstrated superior performance, particularly in maintaining low hallucination rates and high contextual relevance, while Kimi, though robust, showed areas needing further refinement. The study highlights the importance of advanced training techniques and optimization in enhancing model efficiency and accuracy. Practical recommendations for future model development and optimization are provided, emphasizing the need for continuous improvement and rigorous evaluation to achieve reliable and efficient language models.

### Relevance to Thesis

- **Relevance Score:** 59/100 - **Relevance Tag:** Partially Relevant - **Reasoning:** Uses HaluEval to quantify hallucinations in Gemini and Kimi chatbots; compares two platforms; provides limited definition; no mitigation, user studies, or trust impact; leverages existing benchmark rather than releasing new data.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 5: From General to Specific: Utilizing General Hallucation to Automatically
  Measure the Role Relationship Fidelity for Specific Role-Play Agents

**Year:** 2024

**Authors:** Chuyi Kong
Zhen Luo
Hongzhan Lin
Zheng Fan
Yuantao Fan
Yuwei Sun
Wei Ma

**DOI:** 10.48550/arxiv.2411.07965

### Abstract

The advanced role-playing capabilities of Large Language Models (LLMs) have paved the way for developing Role-Playing Agents (RPAs). However, existing benchmarks, such as HPD, which incorporates manually scored character relationships into the context for LLMs to sort coherence, and SocialBench, which uses specific profiles generated by LLMs in the context of multiple-choice tasks to assess character preferences, face limitations like poor generalizability, implicit and inaccurate judgments, and excessive context length. To address the above issues, we propose an automatic, scalable, and generalizable paradigm. Specifically, we construct a benchmark by extracting relations from a general knowledge graph and leverage RPA's inherent hallucination properties to prompt it to interact across roles, employing ChatGPT for stance detection and defining relationship hallucination along with three related metrics. Extensive experiments validate the effectiveness and stability of our metrics. Our findings further explore factors influencing these metrics and discuss the trade-off between relationship hallucination and factuality.

### Relevance to Thesis

- **Relevance Score:** 59/100 - **Relevance Tag:** Partially Relevant - **Reasoning:** Uses KG‑derived role relations to quantify hallucination in RPAs, defines relationship hallucination, evaluates on interactive agents, offers dataset, hints at trade‑offs but lacks mitigation studies or user experiments.

### Analysis for Thesis

This paper contributes relevant insights to understanding AI system reliability and output quality. Its findings could be adapted to develop and evaluate hallucination measurement approaches.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 6: What Was Your Name Again? Interrogating Generative Conversational Models For Factual Consistency Evaluation

**Year:** 2022

**Authors:** Ehsan Lotfi
Maxime De Bruyn
Jeska Buhmann
Walter Daelemans

**DOI:** 10.18653/v1/2022.gem-1.47

### Abstract

Generative conversational agents are known to suffer from problems like inconsistency and hallucination, and a big challenge in studying these issues remains evaluation: they are not properly reflected in common text generation metrics like perplexity or BLEU, and alternative implicit methods like semantic similarity or NLI labels can be misguided when few specific tokens are decisive.In this work we propose ConsisTest; a factual consistency benchmark including both WH and Y/N questions based on PersonaChat, along with a hybrid evaluation pipeline which aims to get the best of symbolic and sub-symbolic methods.Using these and focusing on pretrained generative models like BART, we provide detailed analysis on how the model's factual consistency is affected by variations in question and context.

### Relevance to Thesis

- **Relevance Score:** 59/100 - **Relevance Tag:** Partially Relevant - **Reasoning:** Uses ConsisTest to quantify factual consistency in PersonaChat dialogues; evaluates BART and similar models; releases benchmark dataset. Compares model performance but lacks platform‑wide analysis or hallucination taxonomy.

### Analysis for Thesis

This paper addresses conversational AI, which is the primary domain for mental health chatbots. The dialogue-specific insights could help adapt hallucination measurement to therapeutic contexts.

### Category Tags

BENCHMARK, DEFINITION, DIALOGUE, MEASUREMENT

---

## Paper 7: Evaluating Evaluation Metrics - The Mirage of Hallucination Detection

**Year:** 2025

**Authors:** Atharva Kulkarni
Yuan Zhang
Joel Ruben Antony Moniz
Xiou Ge
Bo-Hsiang Tseng
Dhivya Piraviperumal
Swabha Swayamdipta
Hong Yu

**DOI:** 10.48550/arxiv.2504.18114

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 59/100 - **Relevance Tag:** Partially Relevant - **Reasoning:** Uses multiple metrics to quantify hallucinations in dialogue QA, evaluates instruction‑tuned and mode‑seeking decoding, compares Gemma and GPT‑4, but lacks new definitions, user studies, or released benchmarks.

### Analysis for Thesis

This paper focuses on measuring hallucination, which is directly aligned with the thesis objective of developing a hallucination measurement index. The methods and metrics presented could be adapted for evaluating mental health chatbots specifically.

### Category Tags

BENCHMARK, DETECTION, DIALOGUE, MEASUREMENT

---

## Paper 8: Detecting Dialogue Hallucination Using Graph Neural Networks

**Year:** 2023

**Authors:** Kazuaki Furumai
Yanan Wang
Makoto Shinohara
Kazushi Ikeda
Yi Yu
Tsuneo Kato

**DOI:** 10.1109/icmla58977.2023.00128

### Abstract

Even though large language models (LLMs) accumulate tremendous knowledge, dialogue systems built with LLMs induce hallucinations, leading to the generation of non-factual responses. How to provide proper references to achieve interpretable hallucination detection is a key issue that needs to be addressed. In this paper, we propose a graph neural network (GNN)-based method to achieve high-performance and interpretable hallucination detection for domain-specific dialogue systems. The method involves performing graph matching between a reference knowledge graph obtained from a knowledge database and a response knowledge graph extracted from the response to detect non-factual responses. By comparing with strong baselines, our method achieves a recall improvement of up to 11% and infers the cause of hallucinations with a probability of over 79%.

### Relevance to Thesis

- **Relevance Score:** 56/100 - **Relevance Tag:** Partially Relevant - **Reasoning:** Uses graph matching to detect hallucinations, providing a measurable recall boost in domain‑specific dialogue systems. Lacks definition, mitigation, user studies, cross‑platform comparison, trust impact analysis, or released datasets.

### Analysis for Thesis

This paper addresses hallucination detection mechanisms, which is crucial for identifying when mental health chatbots produce unreliable outputs. The detection methods could be integrated into a comprehensive measurement framework.

### Category Tags

BENCHMARK, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 9: A Domain-specific Hallucination Evaluation Framework for AI Agents in Substation Operation and Maintenance Scenarios

**Authors:** Z Wang
L Li
L Chen
X Xu
M Li

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 56/100 - **Relevance Tag:** Partially Relevant - **Reasoning:** Uses a hybrid LLM-as-Judge framework to quantify factual consistency of AI agents in substation dialogue, providing domain‑specific measurement but limited definition, mitigation, or broader user studies.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

DIALOGUE, MEASUREMENT, MITIGATION

---

## Paper 10: Prompt-Response Semantic Divergence Metrics for Faithfulness Hallucination and Misalignment Detection in Large Language Models

**Year:** 2025

**Authors:** Igor Halperin

**DOI:** 10.48550/arxiv.2508.10192

### Abstract

The proliferation of Large Language Models (LLMs) is challenged by hallucinations, critical failure modes where models generate non-factual, nonsensical or unfaithful text. This paper introduces Semantic Divergence Metrics (SDM), a novel lightweight framework for detecting Faithfulness Hallucinations -- events of severe deviations of LLMs responses from input contexts. We focus on a specific implementation of these LLM errors, {confabulations, defined as responses that are arbitrary and semantically misaligned with the user's query. Existing methods like Semantic Entropy test for arbitrariness by measuring the diversity of answers to a single, fixed prompt. Our SDM framework improves upon this by being more prompt-aware: we test for a deeper form of arbitrariness by measuring response consistency not only across multiple answers but also across multiple, semantically-equivalent paraphrases of the original prompt. Methodologically, our approach uses joint clustering on sentence embeddings to create a shared topic space for prompts and answers. A heatmap of topic co-occurances between prompts and responses can be viewed as a quantified two-dimensional visualization of the user-machine dialogue. We then compute a suite of information-theoretic metrics to measure the semantic divergence between prompts and responses. Our practical score, $\mathcal{S}_H$, combines the Jensen-Shannon divergence and Wasserstein distance to quantify this divergence, with a high score indicating a Faithfulness hallucination. Furthermore, we identify the KL divergence KL(Answer $||$ Prompt) as a powerful indicator of \textbf{Semantic Exploration}, a key signal for distinguishing different generative behaviors. These metrics are further combined into the Semantic Box, a diagnostic framework for classifying LLM response types, including the dangerous, confident confabulation.

### Relevance to Thesis

- **Relevance Score:** 56/100 - **Relevance Tag:** Partially Relevant - **Reasoning:** Uses novel semantic divergence metrics to detect faithfulness hallucinations, defines confabulation and semantic misalignment, but evaluates mainly on prompt‑response pairs rather than full chatbot systems and offers no mitigation, user studies, cross‑platform comparison, trust impact analysis, or released dataset.

### Analysis for Thesis

This paper focuses on measuring hallucination, which is directly aligned with the thesis objective of developing a hallucination measurement index. The methods and metrics presented could be adapted for evaluating mental health chatbots specifically.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 11: Detecting hallucinations in large language models using semantic entropy

**Year:** 2024

**Authors:** Sebastian Farquhar
Jannik Kossen
Lorenz Kuhn
Yarin Gal

**DOI:** 10.1038/s41586-024-07421-0

### Abstract

Abstract Large language model (LLM) systems, such as ChatGPT 1 or Gemini 2 , can show impressive reasoning and question-answering capabilities but often ‘hallucinate’ false outputs and unsubstantiated answers 3,4 . Answering unreliably or without the necessary information prevents adoption in diverse fields, with problems including fabrication of legal precedents 5 or untrue facts in news articles 6 and even posing a risk to human life in medical domains such as radiology 7 . Encouraging truthfulness through supervision or reinforcement has been only partially successful 8 . Researchers need a general method for detecting hallucinations in LLMs that works even with new and unseen questions to which humans might not know the answer. Here we develop new methods grounded in statistics, proposing entropy-based uncertainty estimators for LLMs to detect a subset of hallucinations—confabulations—which are arbitrary and incorrect generations. Our method addresses the fact that one idea can be expressed in many ways by computing uncertainty at the level of meaning rather than specific sequences of words. Our method works across datasets and tasks without a priori knowledge of the task, requires no task-specific data and robustly generalizes to new tasks not seen before. By detecting when a prompt is likely to produce a confabulation, our method helps users understand when they must take extra care with LLMs and opens up new possibilities for using LLMs that are otherwise prevented by their unreliability.

### Relevance to Thesis

- **Relevance Score:** 56/100 - **Relevance Tag:** Partially Relevant - **Reasoning:** Uses entropy‑based uncertainty to detect confabulations, defines hallucination taxonomy, but experiments are task‑agnostic, not tied to chatbots; no mitigation, user studies, platform comparisons, trust analysis, or dialogue‑specific dataset released.

### Analysis for Thesis

This paper addresses hallucination detection mechanisms, which is crucial for identifying when mental health chatbots produce unreliable outputs. The detection methods could be integrated into a comprehensive measurement framework.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 12: Hallucination Detection with Small Language Models

**Authors:** Ming Cheung

**DOI:** 10.48550/arxiv.2506.22486

### Abstract

Since the introduction of ChatGPT, large language models (LLMs) have demonstrated significant utility in various tasks, such as answering questions through retrieval-augmented generation. Context can be retrieved using a vectorized database, serving as a foundation for LLMs to generate responses. However, hallucinations in responses can undermine the reliability of LLMs in practical applications, and they are not easily detectable in the absence of ground truth, particularly in question-and-answer scenarios. This paper proposes a framework that integrates multiple small language models to verify responses generated by LLMs using the retrieved context from a vectorized database. By breaking down the responses into individual sentences and utilizing the probability of generating “Yes” tokens from the outputs of multiple models for a given set of questions, responses, and relevant context, hallucinations can be detected. The proposed framework is validated through experiments with real datasets comprising over 100 sets of questions, answers, and contexts, including responses with fully and partially correct sentences. The results demonstrate a 10% improvement in F1 scores for detecting correct responses compared to hallucinations, indicating that multiple small language models can be effectively employed for answer verification, providing a scalable and efficient solution for both academic and practical applications.

### Relevance to Thesis

- **Relevance Score:** 56/100 - **Relevance Tag:** Partially Relevant - **Reasoning:** Uses small language models to detect hallucinations, defines taxonomy, proposes detection metric for dialogue, tests on limited chatbot data, suggests mitigation ideas, releases a small benchmark dataset.

### Analysis for Thesis

This paper addresses hallucination detection mechanisms, which is crucial for identifying when mental health chatbots produce unreliable outputs. The detection methods could be integrated into a comprehensive measurement framework.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 13: On Large Language Models as Data Sources for Policy Deliberation on Climate Change and Sustainability

**Year:** 2025

**Authors:** Rachel Bina
Kha Luong
Shrey Mehta
Daphne Pang
Mingjun Xie
Christine Chou
Steven O. Kimbrough

**DOI:** 10.2139/ssrn.5123359

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 43/100 - **Relevance Tag:** Partially Relevant - **Reasoning:** Provides HaluEval benchmark and cross‑model hallucination rates; defines prevalence but lacks deep taxonomy; includes dialogue tasks and mitigation ideas; no user studies or trust analysis.

### Analysis for Thesis

This paper contributes relevant insights to understanding AI system reliability and output quality. Its findings could be adapted to develop and evaluate hallucination measurement approaches.

### Category Tags

BENCHMARK, DEFINITION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 14: Addressing Hallucinations with RAG and NMISS in Italian Healthcare LLM
  Chatbots

**Year:** 2024

**Authors:** Maria Paola Priola

**DOI:** 10.48550/arxiv.2412.04235

### Abstract

I combine detection and mitigation techniques to addresses hallucinations in Large Language Models (LLMs). Mitigation is achieved in a question-answering Retrieval-Augmented Generation (RAG) framework while detection is obtained by introducing the Negative Missing Information Scoring System (NMISS), which accounts for contextual relevance in responses. While RAG mitigates hallucinations by grounding answers in external data, NMISS refines the evaluation by identifying cases where traditional metrics incorrectly flag contextually accurate responses as hallucinations. I use Italian health news articles as context to evaluate LLM performance. Results show that Gemma2 and GPT-4 outperform the other models, with GPT-4 producing answers closely aligned with reference responses. Mid-tier models, such as Llama2, Llama3, and Mistral benefit significantly from NMISS, highlighting their ability to provide richer contextual information. This combined approach offers new insights into the reduction and more accurate assessment of hallucinations in LLMs, with applications in real-world healthcare tasks and other domains.

### Relevance to Thesis

- **Relevance Score:** 40/100 - **Relevance Tag:** Partially Relevant - **Reasoning:** Introduces NMISS metric and RAG grounding to detect and mitigate hallucinations; defines no taxonomy; tests on QA over health news, not full chatbots; compares several LLMs; lacks user studies, trust analysis, and public dataset.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 15: Key-Element-Informed sLLM Tuning for Document Summarization

**Year:** 2024

**Authors:** Sangwon Ryu
Heejin Do
Yunsu Kim
Gary Geunbae Lee
Jungseul Ok

**DOI:** 10.48550/arxiv.2406.04625

### Abstract

Remarkable advances in large language models (LLMs) have enabled high-quality text summarization. However, this capability is currently accessible only through LLMs of substantial size or proprietary LLMs with usage fees. In response, smaller-scale LLMs (sLLMs) of easy accessibility and low costs have been extensively studied, yet they often suffer from missing key information and entities, i.e., low relevance, in particular, when input documents are long. We hence propose a key-element-informed instruction tuning for summarization, so-called KEITSum, which identifies key elements in documents and instructs sLLM to generate summaries capturing these key elements. Experimental results on dialogue and news datasets demonstrate that sLLM with KEITSum indeed provides high-quality summarization with higher relevance and less hallucinations, competitive to proprietary LLM.

### Relevance to Thesis

- **Relevance Score:** 40/100 - **Relevance Tag:** Partially Relevant - **Reasoning:** Uses ChatGPT to quantify hallucinations in dialogue summaries; proposes key‑element‑informed tuning that cuts hallucinations by 60%; defines hallucination broadly; includes human faithfulness checks; compares to LLaMA2‑7B and GPT‑3.

### Analysis for Thesis

This paper contributes relevant insights to understanding AI system reliability and output quality. Its findings could be adapted to develop and evaluate hallucination measurement approaches.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, HEALTHCARE, MEASUREMENT, MULTILINGUAL

---

## Paper 16: Assessing hallucination risks in large language models through internal state analysis

**Year:** 2024

**Authors:** Piotr Zablocki
Zofia Gajewska

**DOI:** 10.22541/au.172124175.55788724/v1

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 37/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Uses internal state analysis to quantify hallucination risks, offers some definition insight, and includes limited dialogue‑focused evaluation, but lacks mitigation methods, user studies, cross‑platform comparison, trust impact analysis, or released datasets.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 17: The Troubling Emergence of Hallucination in Large Language Models - An Extensive Definition, Quantification, and Prescriptive Remediations

**Year:** 2023

**Authors:** Vipula Rawte
Swagata Chakraborty
Agnibh Pathak
Anubhav Sarkar
S. M Towhidul Islam Tonmoy
Aman Chadha
Amit Sheth
Amitava Das

**DOI:** 10.18653/v1/2023.emnlp-main.155

### Abstract

Vipula Rawte, Swagata Chakraborty, Agnibh Pathak, Anubhav Sarkar, S.M Towhidul Islam Tonmoy, Aman Chadha, Amit Sheth, Amitava Das. Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing. 2023.

### Relevance to Thesis

- **Relevance Score:** 31/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a fine‑grained taxonomy and HVI metric; releases a 75k‑sample hallucination dataset; compares 15 LLMs; suggests mitigation strategies but lacks dialogue‑specific evaluation or user studies.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 18: Large language models hallucination: A comprehensive survey

**Authors:** A Alansari
H Luqman

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 31/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a thorough taxonomy of hallucination, surveys mitigation methods, and compares platforms; mentions measurement approaches and user perception but lacks original metrics, experiments, or new datasets.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, MEASUREMENT, MITIGATION, MULTILINGUAL, SURVEY

---

## Paper 19: HALoGEN: Fantastic LLM Hallucinations and Where to Find Them

**Year:** 2025

**Authors:** Abhilasha Ravichander
Shrusti Ghela
David Wadden
Yejin Choi

**DOI:** 10.48550/arxiv.2501.08292

### Abstract

Despite their impressive ability to generate high-quality and fluent text, generative large language models (LLMs) also produce hallucinations: statements that are misaligned with established world knowledge or provided input context. However, measuring hallucination can be challenging, as having humans verify model generations on-the-fly is both expensive and time-consuming. In this work, we release HALoGEN, a comprehensive hallucination benchmark consisting of: (1) 10,923 prompts for generative models spanning nine domains including programming, scientific attribution, and summarization, and (2) automatic high-precision verifiers for each use case that decompose LLM generations into atomic units, and verify each unit against a high-quality knowledge source. We use this framework to evaluate ~150,000 generations from 14 language models, finding that even the best-performing models are riddled with hallucinations (sometimes up to 86% of generated atomic facts depending on the domain). We further define a novel error classification for LLM hallucinations based on whether they likely stem from incorrect recollection of training data (Type A errors), or incorrect knowledge in training data (Type B errors), or are fabrication (Type C errors). We hope our framework provides a foundation to enable the principled study of why generative models hallucinate, and advances the development of trustworthy large language models.

### Relevance to Thesis

- **Relevance Score:** 28/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a clear hallucination definition and taxonomy, releases the HALOGEN benchmark dataset, measures hallucinations across many models, but focuses on general generation rather than dialogue‑specific evaluation; includes mitigation discussion and cross‑model comparison, lacks user studies and trust impact analysis.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 20: A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation

**Authors:** SMS Mohammadabadi
BC Kara
C Eyupoglu

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 28/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a thorough taxonomy of hallucination and surveys mitigation methods; mentions detection via retrieval and cites datasets, but lacks original measurement metrics, extensive chatbot experiments, user studies, or platform comparisons.

### Analysis for Thesis

This paper addresses hallucination detection mechanisms, which is crucial for identifying when mental health chatbots produce unreliable outputs. The detection methods could be integrated into a comprehensive measurement framework.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL, SURVEY

---

## Paper 21: Classification of Hallucinations in Large Language Models Using a Novel Weighted Metric

**Year:** 2024

**Authors:** S N Raghava

**DOI:** 10.5070/m417164607

### Abstract

As Large Language Models (LLMs) find increasing use in important fields such as healthcare, finance, and law, ensuring their accuracy and reliability is critical. One significant challenge is the occurrence of "hallucinations," where these models produce nonsensical or incorrect information. This paper introduces a new framework designed to identify and categorize hallucinations in the outputs of LLMs, particularly in safety-sensitive applications. We present a detailed system that classifies hallucinations into four categories: Factual Errors, Speculative Responses, Logical Fallacies, and Improbable Scenarios. Our methodology employs a scoring system that combines metrics to offer a clearer picture of the model performance. Using the TruthfulQA dataset, and the Falcon 7B model, we analyze different types of hallucinations and their potential to compromise decision making in safety critical domains. By focusing on clarity and accuracy, this framework aims to improve the safety and reliability of LLMs in high stakes situations and sets the stage for more effective validation methods in artificial intelligence.

### Relevance to Thesis

- **Relevance Score:** 25/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a clear taxonomy of hallucination types; introduces a weighted metric but applies it to TruthfulQA rather than dialogue; lacks chatbot experiments, mitigation strategies, user studies, cross‑platform comparison, trust impact analysis, and new dialogue datasets.

### Analysis for Thesis

This paper focuses on measuring hallucination, which is directly aligned with the thesis objective of developing a hallucination measurement index. The methods and metrics presented could be adapted for evaluating mental health chatbots specifically.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 22: Survey of Hallucination in Natural Language Generation

**Year:** 2022

**Authors:** Ziwei Ji
Nayeon Lee
Rita Frieske
Tiezheng Yu
D. Su
Yan Xu
Etsuko Ishii
Yejin Bang
Wenliang Dai
Andrea Madotto
Pascale Fung

**DOI:** 10.1145/3571730

### Abstract

Natural Language Generation (NLG) has improved exponentially in recent years thanks to the development of sequence-to-sequence deep learning technologies such as Transformer-based language models. This advancement has led to more fluent and coherent NLG, leading to improved development in downstream tasks such as abstractive summarization, dialogue generation, and data-to-text generation. However, it is also apparent that deep learning based generation is prone to hallucinate unintended text, which degrades the system performance and fails to meet user expectations in many real-world scenarios. To address this issue, many studies have been presented in measuring and mitigating hallucinated texts, but these have never been reviewed in a comprehensive manner before. In this survey, we thus provide a broad overview of the research progress and challenges in the hallucination problem in NLG. The survey is organized into two parts: (1) a general overview of metrics, mitigation methods, and future directions, and (2) an overview of task-specific research progress on hallucinations in the following downstream tasks, namely abstractive summarization, dialogue generation, generative question answering, data-to-text generation, and machine translation. This survey serves to facilitate collaborative efforts among researchers in tackling the challenge of hallucinated texts in NLG.

### Relevance to Thesis

- **Relevance Score:** 25/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides comprehensive definitions and taxonomy of hallucination; surveys metrics applicable to dialogue but lacks direct chatbot experiments; mentions mitigation research and dialogue‑focused datasets.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL, SURVEY

---

## Paper 23: A Survey of Hallucination Problems Based on Large Language Models

**Year:** 2024

**Authors:** Xinxin Liu

**DOI:** 10.54254/2755-2721/2024.17851

### Abstract

Abstract. Large language models (LLM) have made significant achievements in the field of natural language processing, but the generated text often contains content that is inconsistent with the real world or user input, known as hallucinations. This article investigates the current situation of hallucinations in LLM, including the definition, types, causes, and solutions of hallucinations. Illusions are divided into different types such as factual and faithful, mainly caused by factors such as training data defects, low utilization of facts, and randomness in the decoding process. The phenomenon of hallucinations poses a threat to the reliability of LLM, especially in fields such as healthcare, finance, and law, which may lead to serious consequences. To address this issue, this article investigates methods such as managing training datasets, knowledge editing, and enhancing retrieval generation. Future research should classify and evaluate illusions more finely, explore multimodal strategies, enhance model stability, and integrate human intelligence and artificial intelligence to jointly address challenges, promoting the continuous progress of LLM.

### Relevance to Thesis

- **Relevance Score:** 25/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a thorough taxonomy of hallucinations in LLMs and surveys measurement methods, mitigation approaches, and user impact, but does not present original experiments, datasets, or new benchmarks.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, HEALTHCARE, MEASUREMENT, MITIGATION, MULTILINGUAL, SURVEY

---

## Paper 24: DefAn: Definitive Answer Dataset for LLMs Hallucination Evaluation

**Year:** 2024

**Authors:** A. K. Rahman
Anwar Saeed
Muhammad Usman
Ajmal Mian

**DOI:** 10.48550/arxiv.2406.09155

### Abstract

Large Language Models (LLMs) have demonstrated remarkable capabilities, revolutionizing the integration of AI in daily life applications. However, they are prone to hallucinations, generating claims that contradict established facts, deviating from prompts, and producing inconsistent responses when the same prompt is presented multiple times. Addressing these issues is challenging due to the lack of comprehensive and easily assessable benchmark datasets. Most existing datasets are small and rely on multiple-choice questions, which are inadequate for evaluating the generative prowess of LLMs. To measure hallucination in LLMs, this paper introduces a comprehensive benchmark dataset comprising over 75,000 prompts across eight domains. These prompts are designed to elicit definitive, concise, and informative answers. The dataset is divided into two segments: one publicly available for testing and assessing LLM performance and a hidden segment for benchmarking various LLMs. In our experiments, we tested six LLMs-GPT-3.5, LLama 2, LLama 3, Gemini, Mixtral, and Zephyr-revealing that overall factual hallucination ranges from 59% to 82% on the public dataset and 57% to 76% in the hidden benchmark. Prompt misalignment hallucination ranges from 6% to 95% in the public dataset and 17% to 94% in the hidden counterpart. Average consistency ranges from 21% to 61% and 22% to 63%, respectively. Domain-wise analysis shows that LLM performance significantly deteriorates when asked for specific numeric information while performing moderately with person, location, and date queries. Our dataset demonstrates its efficacy and serves as a comprehensive benchmark for LLM performance evaluation. Our dataset and LLMs responses are available at \href{https://github.com/ashikiut/DefAn}{https://github.com/ashikiut/DefAn}.

### Relevance to Thesis

- **Relevance Score:** 22/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a detailed taxonomy of hallucinations and releases a large, publicly available benchmark dataset; however, it lacks dialogue‑specific measurement, chatbot experiments, mitigation methods, user studies, or cross‑platform comparisons.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 25: Large Language Model hallucination mitigation in three industrial use cases

**Authors:** P Tikka
J Karjalainen
A Alesani
V Goriachev

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 22/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Uses industrial case studies to evaluate hallucination in chatbots, proposes mitigation methods, provides baseline measurement, but lacks formal definition, extensive user studies, or public datasets.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 26: Hallucination Detection and Mitigation in Large Language Models

**Authors:** A Pesaranghader
E Li

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 21/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a clear taxonomy of hallucinations and proposes mitigation methods; includes illustrative chatbot misstatement examples and limited dialogue‑focused evaluation, but lacks user studies, cross‑platform comparison, trust impact analysis, and public benchmark release.

### Analysis for Thesis

This paper addresses hallucination detection mechanisms, which is crucial for identifying when mental health chatbots produce unreliable outputs. The detection methods could be integrated into a comprehensive measurement framework.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 27: What Was Your Name Again? Interrogating Generative Conversational Models For Factual Consistency Evaluation

**Authors:** Ehsan Lotfi
Maxime De Bruyn
Jeska Buhmann
Walter Daelemans

### Abstract

Generative conversational agents are known to suffer from problems like inconsistency and hallucination, and a big challenge in studying these issues remains evaluation: they are not properly reflected in common text generation metrics like perplexity or BLEU, and alternative implicit methods like semantic similarity or NLI labels can be misguided when few specific tokens are decisive. In this work we propose ConsisTest; a factual consistency benchmark including both WH and Y/N questions based on PersonaChat, along with a hybrid evaluation pipeline which aims to get the best of symbolic and sub-symbolic methods. Using these and focusing on pretrained generative models like BART, we provide detailed statistics and analysis on how the model’s consistency is affected by variations in question and context.

### Relevance to Thesis

- **Relevance Score:** 21/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Uses ConsisTest to quantify factual consistency (proxy for hallucination); provides detailed evaluation on PersonaChat dialogue models; releases benchmark dataset; lacks explicit hallucination definition, mitigation methods, user studies, cross‑platform comparison, or trust impact analysis.

### Analysis for Thesis

This paper addresses conversational AI, which is the primary domain for mental health chatbots. The dialogue-specific insights could help adapt hallucination measurement to therapeutic contexts.

### Category Tags

BENCHMARK, DIALOGUE, MEASUREMENT, MITIGATION

---

## Paper 28: Predictive Modeling for Autonomous Detection and Correction of AI-Agent Hallucinations Using Transformer Networks

**Year:** 2024

**Authors:** Jegatheeswari Perumalsamy
Jessy Christadoss

**DOI:** 10.60087/jaigs.v6i1.398

### Abstract

Hallucinations in AI agents’ instances where generated outputs deviate from factual or intended information pose significant risks in high-stakes domains such as autonomous decision-making, medical diagnostics, and legal analysis. This research presents a predictive modeling framework for the autonomous detection and correction of AI-agent hallucinations using transformer-based architectures. The proposed method integrates multi-stage attention mechanisms, semantic consistency scoring, and contextual anomaly detection to identify hallucination patterns in real-time. A corrective submodule, trained via supervised fine-tuning and reinforcement learning from human feedback (RLHF), dynamically adjusts outputs toward verifiable ground truth without requiring human intervention. Experiments conducted on benchmark datasets across open-domain QA, dialogue systems, and multimodal reasoning tasks show a substantial reduction in hallucination rates while preserving fluency and relevance. The findings highlight the potential of transformer-driven predictive models to improve the trustworthiness and reliability of autonomous AI agents in critical applications.

### Relevance to Thesis

- **Relevance Score:** 21/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Tests on dialogue agents and corrective module directly address chatbot evaluation and mitigation; provides detection cues but lacks explicit metrics, taxonomy, user studies, cross‑platform comparison, or released benchmark.

### Analysis for Thesis

This paper addresses hallucination detection mechanisms, which is crucial for identifying when mental health chatbots produce unreliable outputs. The detection methods could be integrated into a comprehensive measurement framework.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION

---

## Paper 29: Orchestrating Consensus Strategies to Counter AI Hallucination in Generative Chatbots

**Year:** 2023

**Authors:** Jyothika Prakash Nambiar
A. G. Sreedevi

**DOI:** 10.1109/ccem60455.2023.00030

### Abstract

In recent times, there has been a rise in the usage of Generative chatbots, with OpenAI's ChatGPT being a significant example for its remarkable language understanding capabilities. However, it was found that ChatGPT is prone to a phenomenon called AI hallucination, where it generates inaccurate and unreliable responses that are phrased so eloquently that they seem plausible to its users. The proposed solution is to utilize multiple chatbot models, each with its own strengths and weaknesses, to reach a consensus that will minimize AI hallucinations by detecting inconsistencies across the responses and improve the overall quality of the generated result.

### Relevance to Thesis

- **Relevance Score:** 21/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Uses consensus of multiple chatbots to reduce hallucination, evaluates on dialogue systems, proposes mitigation, but lacks explicit metrics, detailed taxonomy, user studies, and public datasets.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 30: Hallucinations in Artificial Intelligence: Origins, Detection, and Mitigation

**Year:** 2025

**Authors:** Brahmaleen K. Sidhu

**DOI:** 10.21275/sr241229170309

### Abstract

: Artificial intelligence hallucinations, a phenomenon where artificial intelligence models generate content that is plausible but factually incorrect, have become a critical challenge in artificial intelligence research and deployment. This paper explores the concept of hallucinations in artificial intelligence, questioning the validity of the term itself and its implications within the artificial intelligence domain. It delves into the various types and causes of artificial intelligence hallucinations, identifying both intrinsic and extrinsic factors that contribute to this issue across diverse artificial intelligence applications. Furthermore, it discusses methods for detecting hallucinations, highlighting advancements in diagnostic tools and evaluation metrics. Finally, it reviews mitigation strategies, ranging from architectural modifications to post-hoc correction mechanisms, aimed at reducing the frequency and impact of hallucinations. Through this comprehensive analysis, the paper seeks to provide a clearer understanding of artificial intelligence hallucinations and establish a foundation for future research and solutions in this area.

### Relevance to Thesis

- **Relevance Score:** 21/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a clear taxonomy of AI hallucinations and surveys mitigation strategies; mentions detection methods but lacks concrete chatbot‑specific metrics, experiments, user studies, platform comparisons, trust impact analysis, or released datasets.

### Analysis for Thesis

This paper addresses hallucination detection mechanisms, which is crucial for identifying when mental health chatbots produce unreliable outputs. The detection methods could be integrated into a comprehensive measurement framework.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, SURVEY

---

## Paper 31: Factoid: Factual entailment for hallucination detection

**Year:** 2024

**Authors:** Vipula Rawte
S. M. Towhidul
Islam Tonmoy
Krishnav Rajbangshi
Shravani Nag
Aman Chadha
Amit Sheth
Amitava Das
Joe Biden

**DOI:** 10.48550/arxiv.2403.19113

### Abstract

The widespread adoption of Large Language Models (LLMs) has facilitated numerous benefits. However, hallucination is a significant concern. In response, Retrieval Augmented Generation (RAG) has emerged as a highly promising paradigm to improve LLM outputs by grounding them in factual information. RAG relies on textual entailment (TE) or similar methods to check if the text produced by LLMs is supported or contradicted, compared to retrieved documents. This paper argues that conventional TE methods are inadequate for spotting hallucinations in content generated by LLMs. For instance, consider a prompt about the 'USA's stance on the Ukraine war''. The AI-generated text states, ...U.S. President Barack Obama says the U.S. will not put troops in Ukraine...'' However, during the war the U.S. president is Joe Biden which contradicts factual reality. Moreover, current TE systems are unable to accurately annotate the given text and identify the exact portion that is contradicted. To address this, we introduces a new type of TE called ``Factual Entailment (FE).'', aims to detect factual inaccuracies in content generated by LLMs while also highlighting the specific text segment that contradicts reality. We present FACTOID (FACTual enTAILment for hallucInation Detection), a benchmark dataset for FE. We propose a multi-task learning (MTL) framework for FE, incorporating state-of-the-art (SoTA) long text embeddings such as e5-mistral-7b-instruct, along with GPT-3, SpanBERT, and RoFormer. The proposed MTL architecture for FE achieves an avg. 40\% improvement in accuracy on the FACTOID benchmark compared to SoTA TE methods. As FE automatically detects hallucinations, we assessed 15 modern LLMs and ranked them using our proposed Auto Hallucination Vulnerability Index (HVI_auto). This index quantifies and offers a comparative scale to evaluate and rank LLMs according to their hallucinations.

### Relevance to Thesis

- **Relevance Score:** 21/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Introduces factual entailment benchmark and HVI_auto metric, defines hallucination via factual errors, releases FACTOID dataset, but lacks dialogue‑specific experiments or mitigation studies.

### Analysis for Thesis

This paper addresses hallucination detection mechanisms, which is crucial for identifying when mental health chatbots produce unreliable outputs. The detection methods could be integrated into a comprehensive measurement framework.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 32: The Illusion of Progress: Re-evaluating Hallucination Detection in LLMs

**Year:** 2025

**Authors:** Denis Janiak
Jakub Binkowski
Albert Sawczyn
Bogdan Gabrys
Ravid Shwartz-Ziv
Tomasz Kajdanowicz

**DOI:** 10.48550/arxiv.2508.08285

### Abstract

Large language models (LLMs) have revolutionized natural language processing, yet their tendency to hallucinate poses serious challenges for reliable deployment. Despite numerous hallucination detection methods, their evaluations often rely on ROUGE, a metric based on lexical overlap that misaligns with human judgments. Through comprehensive human studies, we demonstrate that while ROUGE exhibits high recall, its extremely low precision leads to misleading performance estimates. In fact, several established detection methods show performance drops of up to 45.9\% when assessed using human-aligned metrics like LLM-as-Judge. Moreover, our analysis reveals that simple heuristics based on response length can rival complex detection techniques, exposing a fundamental flaw in current evaluation practices. We argue that adopting semantically aware and robust evaluation frameworks is essential to accurately gauge the true performance of hallucination detection methods, ultimately ensuring the trustworthiness of LLM outputs.

### Relevance to Thesis

- **Relevance Score:** 18/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a clear taxonomy and critiques of existing metrics, uses human-aligned evaluation, but lacks dialogue‑specific experiments, mitigation methods, platform comparisons, trust analysis, or released datasets.

### Analysis for Thesis

This paper addresses hallucination detection mechanisms, which is crucial for identifying when mental health chatbots produce unreliable outputs. The detection methods could be integrated into a comprehensive measurement framework.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 33: Hallucination Detection and Hallucination Mitigation: An Investigation

**Year:** 2024

**Authors:** Junliang Luo
Tianyu Li
Di Wu
Michael Jenkin
Steve Liu
Gregory Dudek

**DOI:** 10.48550/arxiv.2401.08358

### Abstract

Large language models (LLMs), including ChatGPT, Bard, and Llama, have achieved remarkable successes over the last two years in a range of different applications. In spite of these successes, there exist concerns that limit the wide application of LLMs. A key problem is the problem of hallucination. Hallucination refers to the fact that in addition to correct responses, LLMs can also generate seemingly correct but factually incorrect responses. This report aims to present a comprehensive review of the current literature on both hallucination detection and hallucination mitigation. We hope that this report can serve as a good reference for both engineers and researchers who are interested in LLMs and applying them to real world tasks.

### Relevance to Thesis

- **Relevance Score:** 18/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a thorough taxonomy of hallucination in LLMs, discusses mitigation strategies, but lacks original metrics, experiments, user studies, cross‑platform comparisons, trust impact analysis, or new datasets.

### Analysis for Thesis

This paper addresses hallucination detection mechanisms, which is crucial for identifying when mental health chatbots produce unreliable outputs. The detection methods could be integrated into a comprehensive measurement framework.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL, SURVEY

---

## Paper 34: A Survey on Hallucination in Large Language and Foundation Models

**Year:** 2025

**Authors:** Pegah Ahadian
Qiang Guan

**DOI:** 10.20944/preprints202504.1236.v1

### Abstract

Generative text models, particularly large language models (LLMs) and foundation models, have influenced numerous fields, including high-quality text generation, reasoning, and multimodal synthesis. These models have been widely applied in healthcare, legal analysis, and scientific research. However, where accuracy and reliability are critical, generative text models pose a significant risk due to hallucination, where generated outputs include incorrect factuality, fabricated, or misleading information. In this survey, we present a review of hallucination in generative AI, covering its taxonomy, detection methods, mitigation strategies, and evaluation benchmarks. We first establish a structured taxonomy, distinguishing between intrinsic vs. extrinsic hallucination and factual vs. semantic hallucination, also discussing task-specific variations in areas such as summarization, machine translation, and dialogue generation. Next, we examine state-of-the-art hallucination detection techniques, including uncertainty estimation, retrieval-augmented generation (RAG), self-consistency validation, and internal state monitoring. We further explore mitigation strategies, such as fine-tuning, reinforcement learning from human feedback (RLHF), knowledge injection, adversarial training, and contrastive learning. Additionally, we review key evaluation metrics and benchmarks, including FEVER, TruthfulQA, HALL-E, and Entity-Relationship-Based Hallucination Benchmarks (ERBench), which serve as standardized measures for assessing hallucination severity. Despite notable efforts, hallucination remains an open challenge, necessitating further improvements in real-time detection, multimodal hallucination evaluation, and trustworthiness frameworks. We show critical research gaps including the need for standardized hallucination taxonomies, scalable mitigation techniques, and human-AI hybrid verification methods. Our survey aims to serve as a foundational resource for researchers and practitioners, providing insights into current methodologies and guiding future advancements in trustworthy and explainable generative AI.

### Relevance to Thesis

- **Relevance Score:** 18/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a detailed taxonomy of hallucination, especially for dialogue; surveys detection and mitigation methods but lacks original chatbot experiments, user studies, or new dialogue benchmarks.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION, MULTILINGUAL, SURVEY

---

## Paper 35: Survey of Hallucination in Natural Language Generation

**Year:** 2022

**DOI:** 10.48550/arxiv.2202.03629

### Abstract

Natural Language Generation (NLG) has improved exponentially in recent years thanks to the development of sequence-to-sequence deep learning technologies such as Transformer-based language models. This advancement has led to more fluent and coherent NLG, leading to improved development in downstream tasks such as abstractive summarization, dialogue generation and data-to-text generation. However, it is also apparent that deep learning based generation is prone to hallucinate unintended text, which degrades the system performance and fails to meet user expectations in many real-world scenarios. To address this issue, many studies have been presented in measuring and mitigating hallucinated texts, but these have never been reviewed in a comprehensive manner before. In this survey, we thus provide a broad overview of the research progress and challenges in the hallucination problem in NLG. The survey is organized into two parts: (1) a general overview of metrics, mitigation methods, and future directions; and (2) an overview of task-specific research progress on hallucinations in the following downstream tasks, namely abstractive summarization, dialogue generation, generative question answering, data-to-text generation, machine translation, and visual-language generation. This survey serves to facilitate collaborative efforts among researchers in tackling the challenge of hallucinated texts in NLG.

### Relevance to Thesis

- **Relevance Score:** 18/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a detailed taxonomy of hallucination types and surveys mitigation methods, but lacks specific conversational metrics, experiments, user studies, or released dialogue datasets.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL, SURVEY

---

## Paper 36: A Survey on Hallucination in Large Language and Foundation Models

**Year:** 2025

**Authors:** Pegah Ahadian
Qiang Guan

**DOI:** 10.20944/preprints202504.1236.v2

### Abstract

Generative text models, particularly large language models (LLMs) and foundation models, have influenced numerous fields, including high-quality text generation, reasoning, and multimodal synthesis. These models have been widely applied in healthcare, legal analysis, and scientific research. However, where accuracy and reliability are critical, generative text models pose a significant risk due to hallucination, where generated outputs include incorrect factuality, fabricated, or misleading information. In this survey, we present a review of hallucination in generative AI, covering its taxonomy, detection methods, mitigation strategies, and evaluation benchmarks. We first establish a structured taxonomy, distinguishing between intrinsic vs. extrinsic hallucination and factual vs. semantic hallucination, also discussing task-specific variations in areas such as summarization, machine translation, and dialogue generation. Next, we examine state-of-the-art hallucination detection techniques, including uncertainty estimation, retrieval-augmented generation (RAG), self-consistency validation, and internal state monitoring. We further explore mitigation strategies, such as fine-tuning, reinforcement learning from human feedback (RLHF), knowledge injection, adversarial training, and contrastive learning. Additionally, we review key evaluation metrics and benchmarks, including FEVER, TruthfulQA, HALL-E, and Entity-Relationship-Based Hallucination Benchmarks (ERBench), which serve as standardized measures for assessing hallucination severity. Despite notable efforts, hallucination remains an open challenge, necessitating further improvements in real-time detection, multimodal hallucination evaluation, and trustworthiness frameworks. We show critical research gaps including the need for standardized hallucination taxonomies, scalable mitigation techniques, and human-AI hybrid verification methods. Our survey aims to serve as a foundational resource for researchers and practitioners, providing insights into current methodologies and guiding future advancements in trustworthy and explainable generative AI.

### Relevance to Thesis

- **Relevance Score:** 18/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a detailed taxonomy of hallucination, especially for dialogue, and surveys detection/mitigation methods and benchmarks, but lacks original chatbot experiments, user studies, or new datasets.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION, MULTILINGUAL, SURVEY

---

## Paper 37: ”My AI is Lying to Me”: User-reported LLM hallucinations in AI mobile apps reviews

**Year:** 2025

**Authors:** Rhodes Massenon
Ishaya Gambo
Javed Ali Khan
Christopher Agbonkhese
Ayed Alwadain

**DOI:** 10.1038/s41598-025-15416-8

### Abstract

Large Language Models (LLMs) are increasingly integrated into AI-powered mobile applications, offering novel functionalities but also introducing the risk of "hallucinations" generating plausible yet incorrect or nonsensical information. These AI errors can significantly degrade user experience and erode trust. However, there is limited empirical understanding of how users perceive, report, and are impacted by LLM hallucinations in real-world mobile app settings. This paper presents a large-scale empirical study analyzing 3 million user reviews from 90 diverse AI-powered mobile apps to characterize these user-reported issues. Using a mixed-methods approach, a heuristic-based User-Reported LLM Hallucination Detection algorithm were applied to identify 20,000 candidate reviews, from which 1,000 are manually annotated. This analysis estimates the prevalence of user reports indicative of LLM hallucinations, which was found to be approximately 1.75% within reviews initially flagged as relevant to AI errors. A data-driven taxonomy of seven user-perceived LLM hallucination types, were developed with Factual Incorrectness (H1) emerged as the most frequently reported type, accounting for 38% of instances, followed by Nonsensical/Irrelevant Output (H3) at 25%, and Fabricated Information (H2) at 15%. Furthermore, linguistic patterns were identified using N-grams generation, Non-Negative Matrix Factorization (NMF) topics and sentiment characteristics using VADER, showing significantly lower scores for hallucination reports associated with these reviews. These findings offer critical implications for software quality assurance, highlighting the need for targeted monitoring and mitigation strategies for AI mobile apps. This research provides a foundational, user-centric understanding of LLM hallucinations, paving the way for improved AI model development and more trustworthy mobile applications.

### Relevance to Thesis

- **Relevance Score:** 18/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a user‑grounded taxonomy of hallucination types and sentiment cues, but lacks direct dialogue metrics, mitigation methods, cross‑platform comparisons, or released datasets.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL, SURVEY

---

## Paper 38: LLM Hallucination: The Curse That Cannot Be Broken

**Year:** 2025

**Authors:** Hassan K. H. Al-Mahmood

**DOI:** 10.25195/ijci.v51i2.546

### Abstract

Artificial intelligence chatbots (e.g., ChatGPT, Claude, and Llama, etc.), also known as large language models (LLMs), are continually evolving to be an essential part of the digital tools we use, but are plagued with the phenomenon of hallucination. This paper gives an overview of this phenomenon, discussing its different types, the multi-faceted reasons that lead to it, its impact, and the statement regarding the inherent nature of current LLMs that make hallucinations inevitable. After examining several techniques, each chosen for their different implementation, to detect and mitigate hallucinations, including enhanced training, tagged-context prompts, contrastive learning, and semantic entropy analysis, the work concludes that none are efficient to mitigate hallucinations when they occur. The phenomenon is here to stay, hence calling for robust user awareness and verification mechanisms, stepping short of absolute dependence on these models in healthcare, journalism, legal services, finance, and other critical applications that require accurate and reliable information to ensure informed decisions.

### Relevance to Thesis

- **Relevance Score:** 18/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a thorough taxonomy of LLM hallucinations; discusses mitigation ideas but lacks new metrics, experiments, user studies, cross‑platform comparisons, trust analysis, or released datasets.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION, MULTILINGUAL, SURVEY

---

## Paper 39: Erros, falhas e perturbações digitais em alucinações das IA generativas: tipologia, premissas e epistemologia da comunicação

**Year:** 2024

**Authors:** André Lemos

**DOI:** 10.11606/issn.1982-8160.v18i1p75-91

### Abstract

Neste artigo, identifica-se como erros, falhas e perturbações digitais podem ser analisados a partir de três premissas, relacionando-os com o exemplo da atual alucinação em sistema de IAG, como o ChatGPT. Eles revelam uma dimensão escondida dos objetos digitais. Por serem mais concretos, os objetos digitais geram uma maior indefinição das origens e consequências de eventos disruptivos. Nesses momentos, pode-se vislumbrar agenciamentos coletivos em torno da cultura digital. A proposta é que os erros, falhas e perturbações sejam entendidos não como positivos ou negativos, mas como uma forma de apontar direcionamentos para a pesquisa, indicar o locus para uma abordagem qualitativa. Conclui-se que os erros não são apenas disruptivos, ou oportunidade para gerar inovação, mas eventos que permitem entender as formas da comunicação e as ações das mídias digitais.

### Relevance to Thesis

- **Relevance Score:** 18/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a detailed taxonomy of AI hallucinations, especially for generative models like ChatGPT. Lacks quantitative metrics, experiments, mitigation strategies, user studies, cross‑platform comparisons, trust impact analysis, or released datasets.

### Analysis for Thesis

This paper contributes relevant insights to understanding AI system reliability and output quality. Its findings could be adapted to develop and evaluate hallucination measurement approaches.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION

---

## Paper 40: Bridging Fact and Generation: Comparative Insights into Hallucination Management in LLMs

**Authors:** P Patil
H Deshpande
S Padmawar

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 18/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a clear taxonomy of hallucination and uses claim verification to manage factual errors, but focuses on LLM pipelines rather than chatbot dialogues, with limited mitigation details and no user studies or cross‑platform benchmarks.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, DIALOGUE, MEASUREMENT, MITIGATION

---

## Paper 41: Hallucinations are inevitable but statistically negligible

**Year:** 2025

**Authors:** Atsushi Suzuki
Yulan He
Feng Tian
Zhongyuan Wang

**DOI:** 10.48550/arxiv.2502.12187

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 18/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a clear definition and theoretical analysis of hallucinations, but lacks practical measurement, experiments, mitigation, user studies, or datasets for dialogue systems.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DIALOGUE, MEASUREMENT, MITIGATION

---

## Paper 42: Hallucination mitigation techniques in large language models

**Year:** 2024

**Authors:** M. Abdelghafour
Mohammed Mabrouk
Zaki Taha

**DOI:** 10.21608/ijicis.2024.336135.1365

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 7/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides mitigation methods and human feedback loops; includes some definition and evaluation in chatbots, but lacks explicit measurement metrics, cross‑platform comparison, trust impact analysis, or released datasets.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 43: Paragraph-Level Hallucination Detection and Correction for Trustworthy Large Language Models in Networked Systems

**Authors:** S Tripathi
T Jennifer
H Griffith

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 3/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Uses paragraph-level detection and self‑correction to reduce hallucinations, defines the problem, but focuses on networked LLMs rather than chatbot dialogues; lacks user studies or cross‑platform benchmarks.

### Analysis for Thesis

This paper addresses hallucination detection mechanisms, which is crucial for identifying when mental health chatbots produce unreliable outputs. The detection methods could be integrated into a comprehensive measurement framework.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 44: Mitigating Hallucinations Using Ensemble of Knowledge Graph and Vector
  Store in Large Language Models to Enhance Mental Health Support

**Year:** 2024

**Authors:** Abdul Muqtadir
Hafiz Syed Muhammad Bilal
Ayesha Yousaf
H. F. Ahmed
Jamil Hussain

**DOI:** 10.48550/arxiv.2410.10853

### Abstract

This research work delves into the manifestation of hallucination within Large Language Models (LLMs) and its consequential impacts on applications within the domain of mental health. The primary objective is to discern effective strategies for curtailing hallucinatory occurrences, thereby bolstering the dependability and security of LLMs in facilitating mental health interventions such as therapy, counseling, and the dissemination of pertinent information. Through rigorous investigation and analysis, this study seeks to elucidate the underlying mechanisms precipitating hallucinations in LLMs and subsequently propose targeted interventions to alleviate their occurrence. By addressing this critical issue, the research endeavors to foster a more robust framework for the utilization of LLMs within mental health contexts, ensuring their efficacy and reliability in aiding therapeutic processes and delivering accurate information to individuals seeking mental health support.

### Relevance to Thesis

- **Relevance Score:** 3/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Proposes KG‑vector store ensemble to curb hallucinations in mental‑health LLMs; briefly mentions internal/external hallucination types; lacks quantitative metrics, chatbot‑level evaluation, user studies, benchmarks, or cross‑platform comparisons.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 45: Evaluating the Accuracy of Chatbots in Financial Literature

**Year:** 2024

**Authors:** Orhan Erdem
Kristi Hassett
Feyzullah Egriboyun

**DOI:** 10.48550/arxiv.2411.07031

### Abstract

We evaluate the reliability of two chatbots, ChatGPT (4o and o1-preview versions), and Gemini Advanced, in providing references on financial literature and employing novel methodologies. Alongside the conventional binary approach commonly used in the literature, we developed a nonbinary approach and a recency measure to assess how hallucination rates vary with how recent a topic is. After analyzing 150 citations, ChatGPT-4o had a hallucination rate of 20.0% (95% CI, 13.6%-26.4%), while the o1-preview had a hallucination rate of 21.3% (95% CI, 14.8%-27.9%). In contrast, Gemini Advanced exhibited higher hallucination rates: 76.7% (95% CI, 69.9%-83.4%). While hallucination rates increased for more recent topics, this trend was not statistically significant for Gemini Advanced. These findings emphasize the importance of verifying chatbot-provided references, particularly in rapidly evolving fields.

### Relevance to Thesis

- **Relevance Score:** 3/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Quantifies citation hallucinations in chatbot outputs, defines hallucination via mismatched reference fields, tests three chatbots, but lacks dialogue focus, mitigation, user studies, trust impact, or released dataset.

### Analysis for Thesis

This paper addresses conversational AI, which is the primary domain for mental health chatbots. The dialogue-specific insights could help adapt hallucination measurement to therapeutic contexts.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, SURVEY

---

## Paper 46: Hallucination Mitigation using Agentic AI Natural Language-Based
  Frameworks

**Year:** 2025

**Authors:** Diego Gosmar
Deborah A. Dahl

**DOI:** 10.48550/arxiv.2501.13946

### Abstract

Hallucinations remain a significant challenge in current Generative AI models, undermining trust in AI systems and their reliability. This study investigates how orchestrating multiple specialized Artificial Intelligent Agents can help mitigate such hallucinations, with a focus on systems leveraging Natural Language Processing (NLP) to facilitate seamless agent interactions. To achieve this, we design a pipeline that introduces over three hundred prompts, purposefully crafted to induce hallucinations, into a front-end agent. The outputs are then systematically reviewed and refined by second- and third-level agents, each employing distinct large language models and tailored strategies to detect unverified claims, incorporate explicit disclaimers, and clarify speculative content. Additionally, we introduce a set of novel Key Performance Indicators (KPIs) specifically designed to evaluate hallucination score levels. A dedicated fourth-level AI agent is employed to evaluate these KPIs, providing detailed assessments and ensuring accurate quantification of shifts in hallucination-related behaviors. A core component of this investigation is the use of the OVON (Open Voice Network) framework, which relies on universal NLP-based interfaces to transfer contextual information among agents. Through structured JSON messages, each agent communicates its assessment of the hallucination likelihood and the reasons underlying questionable content, thereby enabling the subsequent stage to refine the text without losing context. The results demonstrate that employing multiple specialized agents capable of interoperating with each other through NLP-based agentic frameworks can yield promising outcomes in hallucination mitigation, ultimately bolstering trust within the AI community.

### Relevance to Thesis

- **Relevance Score:** 3/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Introduces novel KPIs and multi‑agent pipeline to detect and reduce hallucinations, directly addressing mitigation. Provides quantitative scores but lacks dialogue‑specific metrics, taxonomy, chatbot experiments, user studies, cross‑platform comparison, or released datasets; mentions trust improvement without detailed analysis.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL, SURVEY

---

## Paper 47: Hallucination-Free Automatic Question & Answer Generation for Intuitive Learning

**Authors:** NX Wang
AK Katsaggelos

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 3/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Uses optimization and detection agents to minimize hallucination in Q&A generation, but lacks explicit dialogue‑specific metrics, definitions, or broad comparative/user studies.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

DETECTION, DIALOGUE, MEASUREMENT, MITIGATION

---

## Paper 48: AI Chatbots’ Medical Hallucination: Innovation of References Hallucination Score and Comparison of Six Large Language Models (Preprint)

**Year:** 2023

**Authors:** Fadi Aljamaan
Mohamad‐Hani Temsah
Ibraheem Tamimi
Ayman Al‐Eyadhy
Amr Jamal
Khalid Alhasan
Tamer A. Mesallam
Mohamed Farahat
Khalid H. Malki

**DOI:** 10.2196/preprints.54345

### Abstract

<sec> <title>BACKGROUND</title> Artificial intelligence (AI) chatbots have gained use recently in medical practice by healthcare practitioners. Interestingly, their output was found to have varying degrees of hallucination in content and references. Such hallucinations generate doubts about their output and their implementation. </sec> <sec> <title>OBJECTIVE</title> We propose a reference hallucination score (RHS) to evaluate AI chatbots’ citation authenticity. </sec> <sec> <title>METHODS</title> Six AI chatbots were challenged with the same ten medical prompts, requesting ten references per prompt. The Reference Hallucination Score (RHS) is composed of six bibliographic items and the reference’s relevance to prompts’ keywords. RHS was calculated for each reference, prompt, and type of prompt (basic versus complex). The average RHS was calculated for each AI chatbot and compared across the different types of prompts and AI chatbots. </sec> <sec> <title>RESULTS</title> Bard failed to generate any references. ChatGPT 3.5 and Bing generated the highest RHS (11), while Elicit and SciSpace generated the lowest RHS, and Perplexity was in the middle. The highest degree of hallucination was observed for reference relevancy to the prompt keywords (61.6%), while the lowest was reference titles (33.8%). AI chatbots generally had significantly higher RHS when prompted with scenarios or complex format prompts. </sec> <sec> <title>CONCLUSIONS</title> The variation in RHS underscores the necessity for a robust reference evaluation tool to improve the authenticity of AI chatbots. Also, it highlights the importance of verifying their output and citations. Elicit and SciSpace had negligible hallucination, while ChatGPT and Bing had critical levels. The proposed AI chatbots’ RHS could contribute to ongoing efforts to enhance AI’s general reliability in medical research. </sec>

### Relevance to Thesis

- **Relevance Score:** 3/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Uses Reference Hallucination Score to quantify citation errors; compares six chatbots' reference authenticity; lacks dialogue‑focused definition, mitigation, user studies, or open datasets.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 49: KGHaluBench: A Knowledge Graph-Based Hallucination Benchmark for Evaluating the Breadth and Depth of LLM Knowledge

**Authors:** A Robertson
H Liang
M Gani
R Kumar

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 3/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Uses a KG‑based benchmark to quantify LLM hallucinations; provides an open dataset but focuses on general LLMs, not dialogue‑specific evaluation or mitigation.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DIALOGUE, MEASUREMENT, MITIGATION

---

## Paper 50: Research on the Method of Factual Hallucination Relief Based on blockchain Large Language Model

**Authors:** P Li
Y Yang
J Zhang
S Cheng

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 3/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Uses blockchain‑based reputation and reward to curb factual hallucinations, but lacks explicit measurement metrics, definitions, or dialogue‑centric evaluations; no user studies or public benchmarks.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DIALOGUE, MEASUREMENT, MULTILINGUAL

---

## Paper 51: Trapping LLM Hallucinations Using Tagged Context Prompts

**Year:** 2023

**DOI:** 10.48550/arxiv.2306.06085

### Abstract

Recent advances in large language models (LLMs), such as ChatGPT, have led to highly sophisticated conversation agents. However, these models suffer from "hallucinations," where the model generates false or fabricated information. Addressing this challenge is crucial, particularly with AI-driven platforms being adopted across various sectors. In this paper, we propose a novel method to recognize and flag instances when LLMs perform outside their domain knowledge, and ensuring users receive accurate information. We find that the use of context combined with embedded tags can successfully combat hallucinations within generative language models. To do this, we baseline hallucination frequency in no-context prompt-response pairs using generated URLs as easily-tested indicators of fabricated data. We observed a significant reduction in overall hallucination when context was supplied along with question prompts for tested generative engines. Lastly, we evaluated how placing tags within contexts impacted model responses and were able to eliminate hallucinations in responses with 98.88% effectiveness.

### Relevance to Thesis

- **Relevance Score:** 3/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Uses tagged prompts to flag hallucinations, proposes mitigation, discusses trust concerns, but lacks formal metrics, taxonomy, user studies, cross‑platform comparison, or released datasets.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 52: Equipping llama with google query api for improved accuracy and reduced hallucination

**Year:** 2024

**Authors:** Yunkyung Bae
Hye Rin Kim
Jae‐Hoon Kim

**DOI:** 10.21203/rs.3.rs-4014474/v1

### Abstract

Abstract This study investigates the integration of the Llama 2 7b large language model (LLM) with the Google Query API to enhance its accuracy and reduce hallucination instances. By leveraging real-time internet data, we aimed to address the limitations of static training datasets and improve the model's performance across various language processing tasks. The methodology involved augmenting Llama 2 7b's architecture to incorporate dynamic data retrieval from the Google Query API, followed by an evaluation of its impact on model accuracy and hallucination reduction using the BIG-Bench benchmark. The results indicate significant improvements in both accuracy and reliability, demonstrating the effectiveness of integrating LLMs with external data sources. This integration not only marks a substantial advancement in the capabilities of LLMs but also raises important considerations regarding data bias, privacy, and the ethical use of internet-sourced information. The study's findings contribute to the ongoing discourse on enhancing LLMs, suggesting a promising direction for future research and development in artificial intelligence.

### Relevance to Thesis

- **Relevance Score:** 3/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Uses Google Query API integration to mitigate hallucinations, showing accuracy gains on BIG‑Bench; lacks dialogue‑specific measurement, definitions, chatbot evaluations, or user studies.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 53: RAG-HAT: A hallucination-aware tuning pipeline for LLM in retrieval-augmented generation

**Year:** 2024

**Authors:** Juntong Song
Xingguang Wang
Juno Zhu
Yuanhao Wu
Xuxin Cheng
Randy Zhong
Cheng Niu

**DOI:** 10.18653/v1/2024.emnlp-industry.113

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 3/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Uses hallucination detection to quantify errors, defines hallucination loosely, and introduces a tuning pipeline to reduce them, but focuses on retrieval‑augmented generation rather than dialogue‑specific chatbot evaluation or user studies.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION

---

## Paper 54: A HIPAA-aware benchmark and evaluation harness for clinical LLMs to quantify hallucination, bias, and PHI leakage

**Authors:** V Palama

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 3/100 - **Relevance Tag:** Low Relevance - **Reasoning:** Provides a HIPAA‑aware benchmark that quantifies hallucination and releases an open dataset, but lacks dialogue‑specific definitions, chatbot experiments, mitigation methods, or user studies.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION

---

## Paper 55: Quantifying Hallucination Bias in AI-Generated Deepfakes: A Multimodal Analysis Using Divergence Metrics

**Year:** 2025

**Authors:** M. Sharma
A C Bharadwaj

**DOI:** 10.21203/rs.3.rs-6771530/v1

### Abstract

<title>Abstract</title> The rapid development of artificial intelligence (AI) has transformed content creation, while also introducing new challenges, particularly with AI ’hallucinations’—instances where models generate incorrect or fabricated outputs. This study hypothesizes that hallucinations, often resulting from model over-fitting, can mimic or facilitate the generation of deepfakes. We propose a novel divergence metric θ to quantitatively differentiate hallucinated outputs from those produced by deepfake models. Leveraging the FaceForensics++ dataset and a dual-model training strategy using autoencoders, we contrast the behavior of a regularized deepfake model against an overfitted hallucination-prone model. Empirical evaluation using θ-distributions, classification metrics, and t-SNE visualization reveals measurable differences in output divergence. These findings provide insight into the ethical and technical implications of model hallucination, contributing toward more robust digital forensics and detection systems.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Focuses on visual deepfake hallucinations, introduces a divergence metric for image/video outputs, no dialogue or chatbot experiments, definitions, mitigation, or datasets for conversational AI.

### Analysis for Thesis

This paper focuses on measuring hallucination, which is directly aligned with the thesis objective of developing a hallucination measurement index. The methods and metrics presented could be adapted for evaluating mental health chatbots specifically.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION

---

## Paper 56: Anthropomimetic Uncertainty: What Verbalized Uncertainty in Language Models is Missing

**Year:** 2025

**Authors:** Dennis Ulmer
Alexandra Lorson
Ivan Titov
Christian Hardmeier

**DOI:** 10.48550/arxiv.2507.10587

### Abstract

Human users increasingly rely on natural language interactions with large language models (LLMs) in order to receive help on a large variety of tasks and problems. However, the trustworthiness and perceived legitimacy of LLMs is undermined by the fact that their output is frequently stated in very confident terms, even when its accuracy is questionable. Therefore, there is a need to signal the confidence of the language model to a user in order to reap the benefits of human-machine collaboration and mitigate potential harms. Verbalized uncertainty is the expression of confidence with linguistic means, an approach that integrates perfectly into language-based interfaces. Nevertheless, most recent research in natural language processing (NLP) overlooks the nuances surrounding human uncertainty communication and the data biases that influence machine uncertainty communication. We argue for anthropomimetic uncertainty, meaning that intuitive and trustworthy uncertainty communication requires a degree of linguistic authenticity and personalization to the user, which could be achieved by emulating human communication. We present a thorough overview over the research in human uncertainty communication, survey ongoing research, and perform additional analyses to demonstrate so-far overlooked biases in verbalized uncertainty. We conclude by pointing out unique factors in human-machine communication of uncertainty and deconstruct anthropomimetic uncertainty into future research directions for NLP.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Uses uncertainty framing to discuss hallucination risks, cites confidence‑filled errors in chatbots, but lacks concrete metrics, mitigation methods, datasets, or cross‑platform comparisons.

### Analysis for Thesis

This paper contributes relevant insights to understanding AI system reliability and output quality. Its findings could be adapted to develop and evaluate hallucination measurement approaches.

### Category Tags

BENCHMARK, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL, SURVEY

---

## Paper 57: Multilingual Hallucination Gaps in Large Language Models

**Year:** 2024

**Authors:** Cléa Chataigner
Afaf Taïk
Golnoosh Farnadi

**DOI:** 10.48550/arxiv.2410.18270

### Abstract

Large language models (LLMs) are increasingly used as alternatives to traditional search engines given their capacity to generate text that resembles human language. However, this shift is concerning, as LLMs often generate hallucinations, misleading or false information that appears highly credible. In this study, we explore the phenomenon of hallucinations across multiple languages in freeform text generation, focusing on what we call multilingual hallucination gaps. These gaps reflect differences in the frequency of hallucinated answers depending on the prompt and language used. To quantify such hallucinations, we used the FactScore metric and extended its framework to a multilingual setting. We conducted experiments using LLMs from the LLaMA, Qwen, and Aya families, generating biographies in 19 languages and comparing the results to Wikipedia pages. Our results reveal variations in hallucination rates, especially between high and low resource languages, raising important questions about LLM multilingual performance and the challenges in evaluating hallucinations in multilingual freeform text generation.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Defines hallucination and measures multilingual gaps using FACTSCORE, but focuses on biography generation, not dialogue or chatbot settings, and offers no mitigation, user studies, or datasets.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 58: AI & Entertainment: The Revolution of Customer Experience

**Year:** 2023

**Authors:** Yuxuan Mei

**DOI:** 10.54254/2753-7048/30/20231719

### Abstract

This research paper analyzes the impact of artificial intelligence (AI) in shaping customer experience by revolutionizing the entertainment industry. AI evidently has been one of the key driving forces of the fourth industrial revolution, transforming various domains, notably entertainment. Subsequently, the paper conveys that the application of AI could be either direct or indirect through human computer interaction and enhancement of user experience in entertainment respectively. The primary qualities of AI examined are computer vision (virtual reality and games), natural language processing (chatbots and voice assistants) and personalized recommendations through algorithms. The results of the analysis discover that AI has, in fact, enriched user experience in terms of entertainment, delivering greater convenience and augmented engagement for each individual user. However, like in many other industries, AI has displayed some limitations and challenges to be resolved, which negatively impact user experience in their pursuit for entertainment, despite its tremendous potential to further revolutionize the entertainment industry.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Mentions AI hallucination in chatbots but lacks measurement methods, definitions, evaluations, mitigation strategies, user studies, comparative analysis, impact assessment, or released datasets.

### Analysis for Thesis

This paper contributes relevant insights to understanding AI system reliability and output quality. Its findings could be adapted to develop and evaluate hallucination measurement approaches.

### Category Tags

BENCHMARK, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 59: Fine-Tuning Large Language Models Using Entity Hallucination Index for Text Summarization

**Authors:** K Praveenkumar
RC Balabantaray
KP Vittala

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Uses Entity Hallucination Index to fine‑tune summarization models, offering a mitigation angle but no dialogue focus, definitions, or chatbot evaluations.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 60: Measuring the Visual Hallucination in ChatGPT on Visually Deceptive Images

**Year:** 2024

**Authors:** Linzhi Ping
Yixin Gu
Feng Lü

**DOI:** 10.31219/osf.io/v23fr

### Abstract

The evaluation of visual hallucinations in multimodal AI models is novel and significant because it addresses a critical gap in understanding how AI systems interpret deceptive visual inputs. The study systematically assessed ChatGPT's performance on a synthetic dataset of visually deceptive and non-deceptive images, employing both quantitative and qualitative analysis. Results revealed that while ChatGPT achieved high accuracy in standard visual recognition tasks, its performance diminished when faced with deceptive images, highlighting areas for further improvement. The analysis provided insights into the model's underlying mechanisms, such as its extensive pretraining and sophisticated multimodal integration capabilities, which contribute to its robustness against visual deceptions. The study's findings have important implications for the development of more reliable and robust AI technologies, offering a benchmark for future evaluations and practical guidelines for enhancing AI systems.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Focuses on visual hallucination in ChatGPT with deceptive images; provides a definition of visual hallucination and a custom image dataset, but lacks dialogue‑centric measurement, mitigation, user studies, or cross‑platform analysis.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, SURVEY

---

## Paper 61: A survey of multimodal hallucination evaluation and detection

**Year:** 2025

**Authors:** Zhiyuan Chen
Yuecong Min
Jie Zhang
Bei Yan
Jiahao Wang
Xiaozhen Wang
Shiguang Shan

**DOI:** 10.48550/arxiv.2507.19024

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Survey focuses on multimodal (text‑image) hallucination benchmarks and detection methods, not on dialogue or chatbot settings; provides general hallucination definitions but lacks conversational experiments or resources.

### Analysis for Thesis

This paper addresses hallucination detection mechanisms, which is crucial for identifying when mental health chatbots produce unreliable outputs. The detection methods could be integrated into a comprehensive measurement framework.

### Category Tags

BENCHMARK, DETECTION, DIALOGUE, MEASUREMENT, SURVEY

---

## Paper 62: Automated Methodologies for Evaluating Lying, Hallucinations, and Bias in Large Language Models

**Authors:** George Ecurali
Zelie Thackeray

**DOI:** 10.21203/rs.3.rs-4855434/v1

### Abstract

As large language models become integral to various applications, ensuring the reliability and impartiality of their outputs is of paramount importance. The proposed methodologies for evaluating truthfulness, hallucinations, and bias in AI models represent a significant advancement, offering an automated and objective approach to validation without human intervention. Automated fact-checking systems, synthetic datasets, consistency analysis, and bias detection algorithms were integrated to provide a comprehensive evaluation framework. Results from these experiments indicated high accuracy in identifying truthful information, robust discernment of true versus false statements, stable performance across diverse scenarios, and effective mitigation of biases. These findings highlight the potential for enhancing AI reliability and fairness, contributing to the development of more trustworthy AI systems. Future research directions include expanding reference databases, refining synthetic datasets, and improving bias detection techniques to further enhance model evaluations.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Uses automated fact‑checking and synthetic datasets to detect hallucinations, defines the phenomenon, suggests mitigation, notes trust implications, but lacks chatbot‑specific experiments or user studies.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 63: We Have a Package for You! A Comprehensive Analysis of Package
  Hallucinations by Code Generating LLMs

**Year:** 2024

**Authors:** Joseph Spracklen
Raveen Wijewickrama
A H M Nazmus Sakib
Anindya Maiti
Murtuza Jadliwala

**DOI:** 10.48550/arxiv.2406.10279

### Abstract

The reliance of popular programming languages such as Python and JavaScript on centralized package repositories and open-source software, combined with the emergence of code-generating Large Language Models (LLMs), has created a new type of threat to the software supply chain: package hallucinations. These hallucinations, which arise from fact-conflicting errors when generating code using LLMs, represent a novel form of package confusion attack that poses a critical threat to the integrity of the software supply chain. This paper conducts a rigorous and comprehensive evaluation of package hallucinations across different programming languages, settings, and parameters, exploring how different configurations of LLMs affect the likelihood of generating erroneous package recommendations and identifying the root causes of this phenomena. Using 16 different popular code generation models, across two programming languages and two unique prompt datasets, we collect 576,000 code samples which we analyze for package hallucinations. Our findings reveal that 19.7% of generated packages across all the tested LLMs are hallucinated, including a staggering 205,474 unique examples of hallucinated package names, further underscoring the severity and pervasiveness of this threat. We also implemented and evaluated mitigation strategies based on Retrieval Augmented Generation (RAG), self-detected feedback, and supervised fine-tuning. These techniques demonstrably reduced package hallucinations, with hallucination rates for one model dropping below 3%. While the mitigation efforts were effective in reducing hallucination rates, our study reveals that package hallucinations are a systemic and persistent phenomenon that pose a significant challenge for code generating LLMs.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Analyzes code package hallucinations, not dialogue; offers a general hallucination definition but lacks chatbot metrics, evaluations, mitigation, user studies, or dialogue datasets.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 64: Structured Like a Language Model: Analysing AI as an Automated Subject

**Year:** 2022

**DOI:** 10.48550/arxiv.2212.05058

### Abstract

Drawing from the resources of psychoanalysis and critical media studies, in this paper we develop an analysis of Large Language Models (LLMs) as automated subjects. We argue the intentional fictional projection of subjectivity onto LLMs can yield an alternate frame through which AI behaviour, including its productions of bias and harm, can be analysed. First, we introduce language models, discuss their significance and risks, and outline our case for interpreting model design and outputs with support from psychoanalytic concepts. We trace a brief history of language models, culminating with the releases, in 2022, of systems that realise state-of-the-art natural language processing performance. We engage with one such system, OpenAI's InstructGPT, as a case study, detailing the layers of its construction and conducting exploratory and semi-structured interviews with chatbots. These interviews probe the model's moral imperatives to be helpful, truthful and harmless by design. The model acts, we argue, as the condensation of often competing social desires, articulated through the internet and harvested into training data, which must then be regulated and repressed. This foundational structure can however be redirected via prompting, so that the model comes to identify with, and transfer, its commitments to the immediate human subject before it. In turn, these automated productions of language can lead to the human subject projecting agency upon the model, effecting occasionally further forms of countertransference. We conclude that critical media methods and psychoanalytic theory together offer a productive frame for grasping the powerful new capacities of AI-driven language systems.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Focuses on psychoanalytic and ethical aspects of AI subjectivity; does not address hallucination measurement, definition, mitigation, user studies, platform comparison, trust impact, or datasets.

### Analysis for Thesis

This paper contributes relevant insights to understanding AI system reliability and output quality. Its findings could be adapted to develop and evaluate hallucination measurement approaches.

### Category Tags

BENCHMARK, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 65: Grounding the Ungrounded: A Spectral-Graph Framework for Quantifying Hallucinations in multimodal LLMs

**Year:** 2025

**Authors:** Supratik Sarkar
Swagatam Das

**DOI:** 10.48550/arxiv.2508.19366

### Abstract

Hallucinations in large language models (LLMs) remain a fundamental obstacle to trustworthy AI, particularly in high-stakes multimodal domains such as medicine, law, and finance. Existing evaluation techniques are largely heuristic -- anchored in qualitative benchmarking or ad-hoc empirical mitigation -- providing neither principled quantification nor actionable theoretical guarantees. This gap leaves a critical blind spot in understanding how hallucinations arise, propagate, and interact across modalities. We introduce the first (to our knowledge) rigorous information geometric framework in diffusion dynamics for quantifying hallucinations in multimodal LLMs (MLLMs), advancing the field from qualitative detection to mathematically grounded measurement. Our approach represents MLLM outputs as the spectral embeddings over multimodal graph Laplacians and characterizes the manifold gaps of truth vs inconsistencies as the semantic distortion, enabling the tight Rayleigh--Ritz bounds on the multimodal hallucination energy as a functional of time-dependent temperature profiles. By leveraging eigenmode decompositions in Reproducing Kernel Hilbert Space (RKHS) embeddings, our framework delivers modality-aware, theoretically interpretable metrics that capture the evolution of hallucinations across time and input prompts through temperature annealing. This work establishes a principled foundation for quantifying and bounding hallucinations, transforming them from a qualitative risk to a tractable, analyzable phenomenon.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Provides a theoretical framework and definition for hallucinations in multimodal LLMs, but lacks dialogue‑specific measurement, experiments, or resources.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DETECTION, DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 66: RV4Chatbot: Are Chatbots Allowed to Dream of Electric Sheep?

**Year:** 2024

**Authors:** Andrea Gatti
Viviana Mascardi
Angelo Ferrando

**DOI:** 10.4204/eptcs.411.5

### Abstract

Chatbots have become integral to various application domains, including those with safety-critical considerations.As a result, there is a pressing need for methods that ensure chatbots consistently adhere to expected, safe behaviours.In this paper, we introduce RV4Chatbot, a Runtime Verification framework designed to monitor deviations in chatbot behaviour.We formalise expected behaviours as interaction protocols between the user and the chatbot.We present the RV4Chatbot design and describe two implementations that instantiate it: RV4Rasa, for monitoring chatbots created with the Rasa framework, and RV4Dialogflow, for monitoring Dialogflow chatbots.Additionally, we detail experiments conducted in a factory automation scenario using both RV4Rasa and RV4Dialogflow.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Focuses on chatbot classification, generative vs conversational, and privacy concerns; does not address hallucination measurement, definition, mitigation, user studies, platform comparison, trust impact, or datasets.

### Analysis for Thesis

This paper addresses conversational AI, which is the primary domain for mental health chatbots. The dialogue-specific insights could help adapt hallucination measurement to therapeutic contexts.

### Category Tags

BENCHMARK, DEFINITION, DIALOGUE, MEASUREMENT, MITIGATION

---

## Paper 67: GraphEval: A Knowledge-Graph Based LLM Hallucination Evaluation
  Framework

**Year:** 2024

**Authors:** Hannah Sansford
Nicholas C. Richardson
Hermina Petric Maretić
Juba Nait Saada

**DOI:** 10.48550/arxiv.2407.10793

### Abstract

Methods to evaluate Large Language Model (LLM) responses and detect inconsistencies, also known as hallucinations, with respect to the provided knowledge, are becoming increasingly important for LLM applications. Current metrics fall short in their ability to provide explainable decisions, systematically check all pieces of information in the response, and are often too computationally expensive to be used in practice. We present GraphEval: a hallucination evaluation framework based on representing information in Knowledge Graph (KG) structures. Our method identifies the specific triples in the KG that are prone to hallucinations and hence provides more insight into where in the response a hallucination has occurred, if at all, than previous methods. Furthermore, using our approach in conjunction with state-of-the-art natural language inference (NLI) models leads to an improvement in balanced accuracy on various hallucination benchmarks, compared to using the raw NLI models. Lastly, we explore the use of GraphEval for hallucination correction by leveraging the structure of the KG, a method we name GraphCorrect, and demonstrate that the majority of hallucinations can indeed be rectified.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Uses KG‑based evaluation to detect hallucinations and proposes GraphCorrect for fixing them, but focuses on general LLM outputs, lacks dialogue‑specific definitions, experiments, or user studies.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL, SURVEY

---

## Paper 68: Seeing Through the Fog: A Cost-Effectiveness Analysis of Hallucination
  Detection Systems

**Year:** 2024

**Authors:** Alexander Thomas
S. R. Rosen
Vishnu Vettrivel

**DOI:** 10.48550/arxiv.2411.05270

### Abstract

This paper presents a comparative analysis of hallucination detection systems for AI, focusing on automatic summarization and question answering tasks for Large Language Models (LLMs). We evaluate different hallucination detection systems using the diagnostic odds ratio (DOR) and cost-effectiveness metrics. Our results indicate that although advanced models can perform better they come at a much higher cost. We also demonstrate how an ideal hallucination detection system needs to maintain performance across different model sizes. Our findings highlight the importance of choosing a detection system aligned with specific application needs and resource constraints. Future research will explore hybrid systems and automated identification of underperforming components to enhance AI reliability and efficiency in detecting and mitigating hallucinations.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Uses diagnostic odds ratio to compare detection systems for summarization/QA, but lacks dialogue‑specific metrics, definitions, chatbot experiments, mitigation strategies, user studies, cross‑platform comparison, trust impact analysis, or dialogue datasets.

### Analysis for Thesis

This paper addresses hallucination detection mechanisms, which is crucial for identifying when mental health chatbots produce unreliable outputs. The detection methods could be integrated into a comprehensive measurement framework.

### Category Tags

BENCHMARK, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 69: Comparing hallucination detection metrics for multilingual generation

**Year:** 2024

**Authors:** Haoqiang Kang
Terra Blevins
Luke Zettlemoyer

**DOI:** 10.48550/arxiv.2402.10496

### Abstract

While many hallucination detection techniques have been evaluated on English text, their effectiveness in multilingual contexts remains unknown. This paper assesses how well various factual hallucination detection metrics (lexical metrics like ROUGE and Named Entity Overlap, and Natural Language Inference (NLI)-based metrics) identify hallucinations in generated biographical summaries across languages. We compare how well automatic metrics correlate to each other and whether they agree with human judgments of factuality. Our analysis reveals that while the lexical metrics are ineffective, NLI-based metrics perform well, correlating with human annotations in many settings and often outperforming supervised models. However, NLI metrics are still limited, as they do not detect single-fact hallucinations well and fail for lower-resource languages. Therefore, our findings highlight the gaps in exisiting hallucination detection methods for non-English languages and motivate future research to develop more robust multilingual detection methods for LLM hallucinations.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Uses multilingual NLI metrics to detect factual hallucinations in biographical summaries, but focuses on isolated text generation, not chatbots or dialogue, and offers no mitigation, user studies, or dialogue‑specific benchmarks.

### Analysis for Thesis

This paper focuses on measuring hallucination, which is directly aligned with the thesis objective of developing a hallucination measurement index. The methods and metrics presented could be adapted for evaluating mental health chatbots specifically.

### Category Tags

BENCHMARK, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 70: Federated Optimization: Distributed Machine Learning for On-Device Intelligence

**Year:** 2016

**Authors:** Jakub Konečný
H. Brendan McMahan
Daniel Ramage
Peter Richtárik

### Abstract

We introduce a new and increasingly relevant setting for distributed optimization in machine learning, where the data defining the optimization are unevenly distributed over an extremely large number of nodes. The goal is to train a high-quality centralized model. We refer to this setting as Federated Optimization. In this setting, communication efficiency is of the utmost importance and minimizing the number of rounds of communication is the principal goal. A motivating example arises when we keep the training data locally on users' mobile devices instead of logging it to a data center for training. In federated optimization, the devices are used as compute nodes performing computation on their local data in order to update a global model. We suppose that we have extremely large number of devices in the network — as many as the number of users of a given service, each of which has only a tiny fraction of the total data available. In particular, we expect the number of data points available locally to be much smaller than the number of devices. Additionally, since different users generate data with different patterns, it is reasonable to assume that no device has a representative sample of the overall distribution. We show that existing algorithms are not suitable for this setting, and propose a new algorithm which shows encouraging experimental results for sparse convex problems. This work also sets a path for future research needed in the context of federated optimization.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Focuses on federated optimization for on‑device learning; does not address hallucination, dialogue systems, or related evaluation metrics.

### Analysis for Thesis

This paper contributes relevant insights to understanding AI system reliability and output quality. Its findings could be adapted to develop and evaluate hallucination measurement approaches.

### Category Tags

DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION

---

## Paper 71: What do Geometric Hallucination Detection Metrics Actually Measure?

**Authors:** E Yeats
J Buckheit
S Scullen
B Kennedy

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Uses geometric metrics to probe hallucination properties in LLM internals, offering a definition angle but lacking dialogue‑specific evaluation, mitigation, user studies, or benchmarks.

### Analysis for Thesis

This paper focuses on measuring hallucination, which is directly aligned with the thesis objective of developing a hallucination measurement index. The methods and metrics presented could be adapted for evaluating mental health chatbots specifically.

### Category Tags

BENCHMARK, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION

---

## Paper 72: Chainpoll: A high efficacy method for LLM hallucination detection

**Year:** 2023

**Authors:** Robert Friel
Atindriyo Sanyal

**DOI:** 10.48550/arxiv.2310.18344

### Abstract

Large language models (LLMs) have experienced notable advancements in generating coherent and contextually relevant responses. However, hallucinations - incorrect or unfounded claims - are still prevalent, prompting the creation of automated metrics to detect these in LLM outputs. Our contributions include: introducing ChainPoll, an innovative hallucination detection method that excels compared to its counterparts, and unveiling RealHall, a refined collection of benchmark datasets to assess hallucination detection metrics from recent studies. While creating RealHall, we assessed tasks and datasets from previous hallucination detection studies and observed that many are not suitable for the potent LLMs currently in use. Overcoming this, we opted for four datasets challenging for modern LLMs and pertinent to real-world scenarios. Using RealHall, we conducted a comprehensive comparison of ChainPoll with numerous hallucination metrics from recent studies. Our findings indicate that ChainPoll outperforms in all RealHall benchmarks, achieving an overall AUROC of 0.781. This surpasses the next best theoretical method by 11% and exceeds industry standards by over 23%. Additionally, ChainPoll is cost-effective and offers greater transparency than other metrics. We introduce two novel metrics to assess LLM hallucinations: Adherence and Correctness. Adherence is relevant to Retrieval Augmented Generation workflows, evaluating an LLM's analytical capabilities within given documents and contexts. In contrast, Correctness identifies logical and reasoning errors.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Uses ChainPoll to detect hallucinations and introduces RealHall benchmark; defines Adherence and Correctness metrics, but focuses on general LLM outputs, not dialogue-specific chatbots, and lacks mitigation, user studies, or platform comparisons.

### Analysis for Thesis

This paper addresses hallucination detection mechanisms, which is crucial for identifying when mental health chatbots produce unreliable outputs. The detection methods could be integrated into a comprehensive measurement framework.

### Category Tags

BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 73: Walkthrough of Anthropomorphic Features in AI Assistant Tools

**Year:** 2025

**Authors:** Takuya Maeda

**DOI:** 10.48550/arxiv.2502.16345

### Abstract

*ABSTRACT MISSING - NEEDS WEB FETCH*

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Focuses on cataloguing anthropomorphic expressions in LLM chatbots; does not address hallucination measurement, definition, mitigation, user perception, platform comparison, trust impact, or related datasets.

### Analysis for Thesis

This paper contributes relevant insights to understanding AI system reliability and output quality. Its findings could be adapted to develop and evaluate hallucination measurement approaches.

### Category Tags

BENCHMARK, DIALOGUE, MEASUREMENT, MITIGATION

---

## Paper 74: Foundation metrics for evaluating effectiveness of healthcare conversations powered by generative AI

**Year:** 2024

**Authors:** Mahyar Abbasian
Elahe Khatibi
Iman Azimi
David Oniani
Zahra Shakeri Hossein Abad
Alexander Thieme
Ram D. Sriram
Zhongqi Yang
Yanshan Wang
Bryant Lin
Olivier Gevaert
Li-Jia Li
Ramesh Jain
Amir M. Rahmani

**DOI:** 10.1038/s41746-024-01074-z

### Abstract

Abstract Generative Artificial Intelligence is set to revolutionize healthcare delivery by transforming traditional patient care into a more personalized, efficient, and proactive process. Chatbots, serving as interactive conversational models, will probably drive this patient-centered transformation in healthcare. Through the provision of various services, including diagnosis, personalized lifestyle recommendations, dynamic scheduling of follow-ups, and mental health support, the objective is to substantially augment patient health outcomes, all the while mitigating the workload burden on healthcare providers. The life-critical nature of healthcare applications necessitates establishing a unified and comprehensive set of evaluation metrics for conversational models. Existing evaluation metrics proposed for various generic large language models (LLMs) demonstrate a lack of comprehension regarding medical and health concepts and their significance in promoting patients’ well-being. Moreover, these metrics neglect pivotal user-centered aspects, including trust-building, ethics, personalization, empathy, user comprehension, and emotional support. The purpose of this paper is to explore state-of-the-art LLM-based evaluation metrics that are specifically applicable to the assessment of interactive conversational models in healthcare. Subsequently, we present a comprehensive set of evaluation metrics designed to thoroughly assess the performance of healthcare chatbots from an end-user perspective. These metrics encompass an evaluation of language processing abilities, impact on real-world clinical tasks, and effectiveness in user-interactive conversations. Finally, we engage in a discussion concerning the challenges associated with defining and implementing these metrics, with particular emphasis on confounding factors such as the target audience, evaluation methods, and prompt techniques involved in the evaluation process.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Presents comprehensive healthcare chatbot metrics but does not address hallucination definition, measurement, mitigation, or related datasets; only loosely aligns with general dialogue evaluation.

### Analysis for Thesis

This paper addresses conversational AI, which is the primary domain for mental health chatbots. The dialogue-specific insights could help adapt hallucination measurement to therapeutic contexts.

### Category Tags

BENCHMARK, DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 75: From Strings to Semantics: A Methodology for the Automated Semantic Validation for Conversational AI

**Year:** 2025

**Authors:** Anuja Nagpal

**DOI:** 10.59573/emsj.9(5).2025.53

### Abstract

Conversational AI systems have transformed enterprise software applications, yet their non-deterministic nature challenges traditional quality assurance frameworks that rely on exact string matching. This technical review presents a comprehensive semantic validation framework that addresses critical gaps in automated testing for AI-generated content. The solution transforms subjective meaning assessment into objective mathematical processes through sentence-level vector embeddings and high-dimensional geometric representations. Pre-trained Sentence Transformer models generate dense vector representations that capture contextual semantic relationships, while cosine similarity metrics provide robust mathematical foundations for comparing AI responses against curated knowledge repositories. The framework employs systematic algorithmic procedures, including text segmentation, embedding generation, similarity computation, and threshold-based validation decisions. Experimental validation across diverse data analytics platforms demonstrates exceptional alignment with human expert judgment while maintaining consistent performance across AI systems exhibiting markedly different response characteristics. The deterministic nature ensures reproducible testing conditions essential for regulatory compliance, addressing fundamental challenges where traditional lexical metrics consistently fail to capture semantic equivalence in paraphrased content. The framework provides engineering and quality assurance teams with practical, scalable solutions for building trustworthy AI applications that can operate reliably at enterprise scale across healthcare, financial services, educational technology, and customer service domains.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Focuses on semantic similarity validation for AI responses, not on hallucination detection, definition, mitigation, user perception, cross‑platform comparison, trust impact, or related datasets.

### Analysis for Thesis

This paper addresses conversational AI, which is the primary domain for mental health chatbots. The dialogue-specific insights could help adapt hallucination measurement to therapeutic contexts.

### Category Tags

BENCHMARK, DETECTION, DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION, SURVEY

---

## Paper 76: Exploring the Boundaries of Reality: Investigating the Phenomenon of Artificial Intelligence Hallucination in Scientific Writing Through ChatGPT References

**Year:** 2023

**DOI:** 10.7759/cureus.37432

### Abstract

Background Chatbots are computer programs that use artificial intelligence (AI) and natural language processing (NLP) to simulate conversations with humans. One such chatbot is ChatGPT, which uses the third-generation generative pre-trained transformer (GPT-3) developed by OpenAI. ChatGPT has been praised for its ability to generate text, but concerns have been raised about its accuracy and precision in generating data, as well as legal issues related to references. This study aims to investigate the frequency of AI hallucination in research proposals entirely drafted by ChatGPT. Methodology An analytical design was employed to investigate AI hallucination by ChatGPT. A total of 178 references listed by ChatGPT were verified for inclusion in the study. Statistical analysis was performed by five researchers who entered their data into a Google Form, and the final results were represented using pie charts and tables. Results Out of the 178 references analyzed, 69 references did not have a Digital Object Identifier (DOI), and 28 references neither turned up on Google search nor had an existing DOI. Three references were listed from books and not research articles. These observations suggest that ChatGPT’s ability to generate reliable references for research topics may be limited by the availability of DOI and the accessibility of online articles. Conclusions The study highlights the potential limitations of ChatGPT’s ability to generate reliable references for research proposals. AI hallucination is a problem that may negatively impact decision-making and may give rise to ethical and legal problems. Improving the training inputs by including diverse, accurate, and contextually relevant data sets along with frequent updates to the training models could potentially help address these issues. However, until these issues are addressed, researchers using ChatGPT should exercise caution in relying solely on the references generated by the AI chatbot.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Analyzes reference errors from ChatGPT, offering a loose definition of hallucination and generic mitigation ideas, but lacks dialogue‑focused metrics, user studies, cross‑platform comparisons, or released benchmarks.

### Analysis for Thesis

This paper contributes to the understanding of hallucinations in AI systems. The taxonomies, evaluation methods, or findings could inform the development of measurement indices for mental health contexts.

### Category Tags

BENCHMARK, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL

---

## Paper 77: Foundation Metrics: Quantifying Effectiveness of Healthcare Conversations powered by Generative AI

**Year:** 2023

**Authors:** Mahyar Abbasian
Elahe Khatibi
Iman Azimi
David Oniani
Zahra Shakeri Hossein Abad
Alexander Thieme
Zhongqi Yang
Yanshan Wang
Bryant Lin
Olivier Gevaert
Li-Jia Li
Ramesh Jain
Amir M. Rahmani

**DOI:** 10.48550/arxiv.2309.12444

### Abstract

Generative Artificial Intelligence is set to revolutionize healthcare delivery by transforming traditional patient care into a more personalized, efficient, and proactive process. Chatbots, serving as interactive conversational models, will probably drive this patient-centered transformation in healthcare. Through the provision of various services, including diagnosis, personalized lifestyle recommendations, and mental health support, the objective is to substantially augment patient health outcomes, all the while mitigating the workload burden on healthcare providers. The life-critical nature of healthcare applications necessitates establishing a unified and comprehensive set of evaluation metrics for conversational models. Existing evaluation metrics proposed for various generic large language models (LLMs) demonstrate a lack of comprehension regarding medical and health concepts and their significance in promoting patients' well-being. Moreover, these metrics neglect pivotal user-centered aspects, including trust-building, ethics, personalization, empathy, user comprehension, and emotional support. The purpose of this paper is to explore state-of-the-art LLM-based evaluation metrics that are specifically applicable to the assessment of interactive conversational models in healthcare. Subsequently, we present an comprehensive set of evaluation metrics designed to thoroughly assess the performance of healthcare chatbots from an end-user perspective. These metrics encompass an evaluation of language processing abilities, impact on real-world clinical tasks, and effectiveness in user-interactive conversations. Finally, we engage in a discussion concerning the challenges associated with defining and implementing these metrics, with particular emphasis on confounding factors such as the target audience, evaluation methods, and prompt techniques involved in the evaluation process.

### Relevance to Thesis

- **Relevance Score:** 0/100 - **Relevance Tag:** Not Relevant - **Reasoning:** Uses WikiFact and related benchmarks to flag hallucinations in healthcare chat responses; outlines metrics but lacks a formal hallucination definition, mitigation strategies, or user studies; applies metrics to chatbot outputs and references public datasets.

### Analysis for Thesis

This paper addresses conversational AI, which is the primary domain for mental health chatbots. The dialogue-specific insights could help adapt hallucination measurement to therapeutic contexts.

### Category Tags

BENCHMARK, DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION, MULTILINGUAL

---


---

# SUMMARY AND ANALYSIS

## 1. Papers by Category

- **BENCHMARK:** 72 papers
- **DEFINITION:** 43 papers
- **DETECTION:** 46 papers
- **DIALOGUE:** 75 papers
- **HEALTHCARE:** 18 papers
- **MEASUREMENT:** 77 papers
- **MITIGATION:** 72 papers
- **MULTILINGUAL:** 54 papers
- **SURVEY:** 19 papers

**Total coverage:** 77 papers (note: papers may appear in multiple categories)

## 2. Top 15 Most Useful Papers for Thesis

Ranked by relevance score and completeness (abstract availability):

### 1. Paper 1: Diving Deep into Modes of Fact Hallucinations in Dialogue Systems
   - **Relevance Score:** 85/100
   - **Year:** 2022
   - **Categories:** BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION
   - **Abstract Available:** Yes

### 2. Paper 2: On the Origin of Hallucinations in Conversational Models: Is it the Datasets or the Models?
   - **Relevance Score:** 81/100
   - **Year:** 2022
   - **Categories:** BENCHMARK, DEFINITION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL
   - **Abstract Available:** Yes

### 3. Paper 3: Can We Catch the Elephant? The Evolvement of Hallucination Evaluation on Natural Language Generation: A Survey
   - **Relevance Score:** 62/100
   - **Year:** 2024
   - **Categories:** BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL, SURVEY
   - **Abstract Available:** Yes

### 4. Paper 4: Benchmarking the Hallucination Tendency of Google Gemini and Moonshot Kimi
   - **Relevance Score:** 59/100
   - **Year:** 2024
   - **Categories:** BENCHMARK, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL
   - **Abstract Available:** Yes

### 5. Paper 5: From General to Specific: Utilizing General Hallucation to Automatically
  Measure the Role Relationship Fidelity for Specific Role-Play Agents
   - **Relevance Score:** 59/100
   - **Year:** 2024
   - **Categories:** BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL
   - **Abstract Available:** Yes

### 6. Paper 6: What Was Your Name Again? Interrogating Generative Conversational Models For Factual Consistency Evaluation
   - **Relevance Score:** 59/100
   - **Year:** 2022
   - **Categories:** BENCHMARK, DEFINITION, DIALOGUE, MEASUREMENT
   - **Abstract Available:** Yes

### 7. Paper 8: Detecting Dialogue Hallucination Using Graph Neural Networks
   - **Relevance Score:** 56/100
   - **Year:** 2023
   - **Categories:** BENCHMARK, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL
   - **Abstract Available:** Yes

### 8. Paper 10: Prompt-Response Semantic Divergence Metrics for Faithfulness Hallucination and Misalignment Detection in Large Language Models
   - **Relevance Score:** 56/100
   - **Year:** 2025
   - **Categories:** BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL
   - **Abstract Available:** Yes

### 9. Paper 11: Detecting hallucinations in large language models using semantic entropy
   - **Relevance Score:** 56/100
   - **Year:** 2024
   - **Categories:** BENCHMARK, DEFINITION, DETECTION, DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION, MULTILINGUAL
   - **Abstract Available:** Yes

### 10. Paper 12: Hallucination Detection with Small Language Models
   - **Relevance Score:** 56/100
   - **Year:** 
   - **Categories:** BENCHMARK, DEFINITION, DETECTION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL
   - **Abstract Available:** Yes

### 11. Paper 14: Addressing Hallucinations with RAG and NMISS in Italian Healthcare LLM
  Chatbots
   - **Relevance Score:** 40/100
   - **Year:** 2024
   - **Categories:** BENCHMARK, DEFINITION, DETECTION, DIALOGUE, HEALTHCARE, MEASUREMENT, MITIGATION, MULTILINGUAL
   - **Abstract Available:** Yes

### 12. Paper 15: Key-Element-Informed sLLM Tuning for Document Summarization
   - **Relevance Score:** 40/100
   - **Year:** 2024
   - **Categories:** BENCHMARK, DEFINITION, DETECTION, DIALOGUE, HEALTHCARE, MEASUREMENT, MULTILINGUAL
   - **Abstract Available:** Yes

### 13. Paper 17: The Troubling Emergence of Hallucination in Large Language Models - An Extensive Definition, Quantification, and Prescriptive Remediations
   - **Relevance Score:** 31/100
   - **Year:** 2023
   - **Categories:** BENCHMARK, DEFINITION, DIALOGUE, MEASUREMENT, MITIGATION, MULTILINGUAL
   - **Abstract Available:** Yes

### 14. Paper 7: Evaluating Evaluation Metrics - The Mirage of Hallucination Detection
   - **Relevance Score:** 59/100
   - **Year:** 2025
   - **Categories:** BENCHMARK, DETECTION, DIALOGUE, MEASUREMENT
   - **Abstract Available:** No

### 15. Paper 9: A Domain-specific Hallucination Evaluation Framework for AI Agents in Substation Operation and Maintenance Scenarios
   - **Relevance Score:** 56/100
   - **Year:** 
   - **Categories:** DIALOGUE, MEASUREMENT, MITIGATION
   - **Abstract Available:** No

## 3. Papers with Missing Abstracts (High Priority for Web Fetch)

Found 4 papers in top 30 with missing abstracts:

- **Paper 7:** Evaluating Evaluation Metrics - The Mirage of Hallucination Detection
- **Paper 9:** A Domain-specific Hallucination Evaluation Framework for AI Agents in Substation Operation and Maintenance Scenarios
- **Paper 13:** On Large Language Models as Data Sources for Policy Deliberation on Climate Change and Sustainability
- **Paper 16:** Assessing hallucination risks in large language models through internal state analysis
## 4. Gap Analysis: Topics NOT Well Covered


Based on the 77 papers analyzed, the following areas represent significant gaps:

### Missing or Underrepresented Topics:

1. **Mental Health Specific Hallucinations (9/77 papers):**
   - Only 18 papers explicitly address healthcare/mental health contexts
   - Gap: Limited research on hallucinations specific to mental health conversations (e.g., therapeutic alliance impact, harmful mental health misinformation)
   - Action: Thesis should develop mental-health-specific hallucination definitions and measurements

2. **Real-time Hallucination Detection in Chatbots (Limited coverage):**
   - Most papers focus on post-hoc evaluation, not live detection
   - Gap: Few approaches for real-time confidence scoring or uncertainty quantification in mental health chatbots
   - Action: Develop real-time hallucination monitoring framework

3. **User/Patient Perception of Hallucinations:**
   - Detection papers focus on computational methods, not human understanding
   - Gap: No systematic study of how mental health patients perceive or are affected by chatbot hallucinations
   - Action: Include user studies in thesis methodology

4. **Long-form Conversational Context:**
   - Most papers evaluate isolated responses or short dialogues
   - Gap: Limited analysis of hallucination accumulation over extended therapeutic conversations
   - Action: Develop metrics for hallucination consistency across multi-turn sessions

5. **Cross-lingual Mental Health Chatbots (Important for Malaysia context):**
   - 54 papers mention multilingual aspects, but few in healthcare
   - Gap: No research on hallucination in Malay-language mental health chatbots
   - Action: Adapt existing metrics for Malaysian context and languages

6. **Regulatory and Ethical Considerations:**
   - Papers focus on technical metrics, not compliance/ethics
   - Gap: No frameworks for hallucination measurement in regulated healthcare contexts
   - Action: Incorporate privacy, consent, and liability considerations

7. **Domain Adaptation Methods:**
   - Limited guidance on adapting general hallucination measures to mental health
   - Gap: No papers specifically on fine-tuning detection models for therapeutic dialogue
   - Action: Develop mental-health specific training data and models

### Recommended Thesis Contributions:

1. Create a **Mental Health Hallucination Index (MHHI)** combining detection, measurement, and context
2. Develop a **Malaysia-Localized Framework** for Malay and English mental health chatbots
3. Include **User Impact Assessment** studying how patients perceive hallucinations
4. Design **Real-time Monitoring** mechanisms for production deployments
5. Establish **Ethical Guidelines** for hallucination thresholds in mental health contexts
