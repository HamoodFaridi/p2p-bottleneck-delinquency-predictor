# Procure-to-Pay Bottleneck & Delinquency Predictor

## Objective

Build an end-to-end machine learning solution that predicts procurement bottlenecks and invoice payment delinquency using publicly available procurement datasets.

## Planned Features

- Data ingestion
- Data preprocessing
- Feature engineering
- Exploratory Data Analysis
- Machine learning
- Explainable AI (SHAP)
- FastAPI inference service
- Streamlit dashboard
- Docker deployment
- CI/CD using GitHub Actions

## Status

🚧 Project setup in progress.
```
p2p-bottleneck-delinquency-predictor
├─ docs
│  ├─ adr.md
│  ├─ dependency_management.md
│  └─ engineering_journal.md
├─ models
├─ notebooks
│  └─ 01_dataset_understanding.ipynb
├─ project_tree.ps1
├─ README.md
├─ requirements
│  ├─ base.txt
│  ├─ dev.txt
│  └─ prod.txt
├─ requirements.txt
├─ src
│  ├─ constants.py
│  ├─ data
│  │  ├─ cleaner.py
│  │  ├─ dataset_catalog.py
│  │  ├─ dataset_evaluator.py
│  │  ├─ external
│  │  ├─ interim
│  │  ├─ loader.py
│  │  ├─ processed
│  │  ├─ raw
│  │  │  └─ customer_invoices
│  │  │     └─ dataset.csv
│  │  └─ __init__.py
│  └─ evaluation
│     ├─ dataset_evaluator.py
│     └─ __init__.py
└─ tests
   └─ test_data_pipeline.py

```