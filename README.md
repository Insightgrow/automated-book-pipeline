# AI-Powered Automated Book Publication Workflow 

A next-generation AI-powered pipeline that transforms raw online book chapters into enhanced, human-refined, and reward-assessed literary outputs — **automatically**.

> It has been built using advanced LLMs, real-time scraping, human-in-the-loop editing, reward modeling, and voice input which makes the system redefine modern digital publishing.

---

## Key Features

### 1. **Web Scraping via Playwright**
It fetches book chapters live from platforms like Wikisource using robust headless browser automation.  
**Why it's valuable**: It supports dynamic websites, captures high-quality screenshots, and ensures content freshness — far superior to static scraping methods.

---

### 2. **AI Rewriting (HuggingFace Transformers)**
It utilizes **Flan-T5** models to rewrite raw chapters with improved coherence and tone.  
**Why it's valuable**: It applies advanced NLP techniques for stylistic enhancements without sacrificing core meaning.

---

### 3. **AI Reviewing with LLM Feedback Loop**
It automatically critiques and improves the AI’s initial output using a second LLM pass.  
**Why it's valuable**: It introduces self-reviewing capabilities for better contextual alignment, tone correction, and polishing.

---

### 4. **Human-in-the-Loop Editing**
It prompts the user to manually review and optionally edit AI-enhanced text.  
**Why it's valuable**: It ensures final output quality with human creativity and critical judgment, addressing edge cases AI may miss.

---

### 5. **Reward Evaluation System**
It implements a scoring mechanism that compares:
- AI vs. Human Final outputs based on:
  - Cosine similarity
  - Readability 

**Why it's valuable**: It introduces a gamified and feedback-rich evaluation method inspired by **Reinforcement Learning from Human Feedback (RLHF)**.

---

### 6. **Batch Chapter Support**
It upload chapters via a CSV file and process multiple in one go.  
**Why it's valuable**: It scales the system for full book automation — one command to process a whole novel.

---

### 7. **Voice Input for Human Editing**
The users can dictate edits via speech input (microphone), powered by `speech_recognition`.  
**Why it's valuable**: It increases accessibility and speed, especially useful for content creators and editors who prefer dictation.

---

### 8. **Dynamic Markdown Dashboard**
It generates a `dashboard.md` with a **tabular view** of chapter-by-chapter metrics:
- Chapter ID
- URL
- Similarity (AI & Final)
- Readability (AI & Final)
- Reward Decision

**Why it's valuable**: It tracks progress, performance, and quality over time in a structured and shareable format.

---

## Tech Stack

| Layer              | Technology Used                               |
|-------------------|------------------------------------------------|
| Scraping Engine    | `Playwright` (Python)                         |
| AI Rewrite Model   | `google/flan-t5-base` via HuggingFace         |
| Speech Interface   | `speech_recognition`, `pyaudio`               |
| Evaluation Logic   | `textstat`, `scikit-learn` (TF-IDF + Cosine) |
| File I/O & Parsing | `nltk`, `csv`, `os`, `tabulate`               |
| Dashboard Format   | GitHub-Flavored Markdown                      |

---

## How It Works

1. **Load `chapters.csv`** → Contains URLs of chapters.
2. **Run `main.py`** → Initiates the full pipeline.
3. **Each chapter** goes through:
   - Scraping
   - AI rewriting
   - AI reviewing
   - Manual editing (text or voice)
   - Reward scoring
4. **Results** are logged and exported to:
   - `.txt` files (for each version)
   - `dashboard.md` (summary)

---

## Why This Project Stands Out

1. It combines **LLMs + RLHF concepts** for real-world content automation
2. It uses **open-source HuggingFace models**, making it fully offline-ready  
3. It **includes voice input**, which is rare in editorial automation pipelines  
4. It produces a **review dashboard** to evaluate and audit AI quality  
5. It enables **batch processing**, aligning with scalable content pipelines  
6. It is esigned to be **user-friendly** yet **technically robust**
