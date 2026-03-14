# Fraudulent Job Ad Detection

Exploratory analysis and classification model to detect fraudulent job postings, using the [Recruitment Scam dataset](https://www.kaggle.com/datasets/amruthjithrajvr/recruitment-scam) from Kaggle.

---

## Overview

Job scams are increasingly prevalent. This project analyses scraped job ad data and builds a machine learning pipeline to classify job postings as fraudulent or legitimate.

**Approach:**
- Data cleaning & exploratory analysis
- NLP feature engineering using zero-shot NLI classification
- Binary classification with Random Forest, XGBoost, and Logistic Regression
- Evaluation using Recall, F1-score, and AUC-ROC

---

## Project Structure

```
├── main.ipynb        # Main notebook — EDA, feature engineering, model training
├── functions.py      # Helper functions (compare_fradulent_vs_not)
├── DataSet.csv       # Original dataset from Kaggle
└── README.md
```

---

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <repo-folder>
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost \
            beautifulsoup4 transformers sentence-transformers \
            umap-learn torch
```

### 4. Download the dataset

Download `DataSet.csv` from [Kaggle](https://www.kaggle.com/datasets/amruthjithrajvr/recruitment-scam) and place it in the root directory.

### 5. Run the notebook

```bash
jupyter notebook main.ipynb
```

---

## Requirements

```
pandas
numpy
matplotlib
seaborn
scikit-learn
xgboost
beautifulsoup4
transformers
sentence-transformers
umap-learn
torch
jupyter
```

> **Note:** The NLP zero-shot classification step (`cross-encoder/nli-MiniLM2-L6-H768`) processes 12,000+ rows and may take 15–30 minutes on CPU. A GPU (`device=0`) will significantly speed this up.

---

## Key Results

| Model | Recall (Fraud) | F1 (Fraud) | AUC-ROC |
|---|---|---|---|
| Random Forest | 0.56 | 0.71 | 0.98 |
| **XGBoost** | **0.80** | **0.79** | **0.98** |
| Logistic Regression | 0.74 | 0.28 | 0.86 |

**Top fraud signals:** `country_US`, `company_profile_legitimacy_score`, `required_education_High School or equivalent`