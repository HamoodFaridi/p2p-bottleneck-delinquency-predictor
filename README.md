# Procure-to-Pay Bottleneck & Delinquency Predictor

An end-to-end Machine Learning project for predicting invoice payment behavior in Procure-to-Pay (P2P) processes.

The solution uses historical invoice data to identify invoices that are likely to be paid late and estimate when an invoice is expected to be paid.

## Project Objective

The objective is to build an end-to-end ML solution that can:

1. Predict whether an invoice is likely to be paid after its due date.
2. Estimate the expected number of days until the invoice is paid.
3. Convert the predicted payment duration into an expected payment date.
4. Provide business users with actionable visibility into payment risk and expected payment timing.

The project demonstrates the complete ML lifecycle, from data understanding and feature engineering through model development, API development, dashboarding, testing, and deployment.

---

## ML Prediction Objectives

The project contains two complementary prediction problems.

### 1. Payment Delinquency Classification

**Business question:**

> Will this invoice be paid late?

Target variable:

```text
is_delayed
```

Definition:

```text
days_late = clear_date - due_in_date

is_delayed = 1 when days_late > 0
is_delayed = 0 when days_late <= 0
```

The classification model will produce:

* Predicted class: Delayed / Not Delayed
* Probability of delayed payment

Example:

```text
Invoice: INV-001
Late payment probability: 82%
Prediction: Delayed
```

### 2. Payment Time Prediction

**Business question:**

> How long will it take for this invoice to be paid?

Rather than directly modeling a calendar date, the regression model will predict:

```text
days_to_payment
```

This represents the number of days between the prediction point and the eventual payment date.

The predicted duration can then be converted into:

```text
expected_payment_date
```

and compared with the invoice due date to estimate expected delinquency.

Example:

```text
Prediction date:          2026-09-08
Expected days to payment: 42
Expected payment date:    2026-10-20
Due date:                 2026-10-08
Expected delay:           12 days
```

---

## Data Population

The current dataset contains 50,000 invoice records.

### Historical / Closed Invoices

Approximately 40,000 invoices have a populated `clear_date`.

These invoices provide the observed payment outcome and will be used to:

* Create supervised learning targets
* Train ML models
* Validate model performance
* Evaluate final model performance

The closed population will be divided into training, validation, and test datasets using a time-aware approach.

### Open Invoices

Approximately 10,000 invoices do not have a `clear_date`.

These invoices do not have an observed payment outcome and therefore will not be used for model accuracy evaluation.

After the models are finalized, the open invoices will be used as the prediction population.

---

## Prediction Point

The prediction point represents the point in the invoice lifecycle at which the model is expected to make its prediction.

The current design is to make the prediction using information available at or before invoice creation/posting.

The exact business event representing the prediction point will be finalized during Phase 3.

This is critical to prevent data leakage.

---

## Data Leakage Prevention

The models must only use information that would have been available at the prediction point.

The following fields will not be used as model features:

* `clear_date`
* `days_late`
* `is_delayed`
* `isOpen`
* Any other information generated after the prediction point

Historical payment outcomes are used only to create supervised learning targets.

---

## Project Architecture

```text
Raw Invoice Data
       │
       ▼
Data Understanding
       │
       ▼
Data Cleaning
       │
       ▼
Target Definition
       │
       ▼
Feature Engineering
       │
       ▼
ML Pipeline
       │
       ├───────────────┐
       ▼               ▼
Classification      Regression
       │               │
       ▼               ▼
is_delayed       days_to_payment
       │               │
       └───────┬───────┘
               ▼
       Model Evaluation
               │
               ▼
       Prediction Pipeline
               │
               ▼
          Backend API
               │
               ▼
          Dashboard
               │
               ▼
           Deployment
```

---

## Project Roadmap

| Phase | Description                   | Status         |
| ----- | ----------------------------- | -------------- |
| 1     | Data Understanding            | ✅ Complete     |
| 2     | Data Cleaning                 | ✅ Complete     |
| 3     | Target Definition             | 🔵 In Progress |
| 4     | Feature Engineering           | ⏳ Planned      |
| 5     | ML Pipeline                   | ⏳ Planned      |
| 6     | Classification Model          | ⏳ Planned      |
| 7     | Regression Model              | ⏳ Planned      |
| 8     | Evaluation & Business Metrics | ⏳ Planned      |
| 9     | Prediction Pipeline           | ⏳ Planned      |
| 10    | Backend / API                 | ⏳ Planned      |
| 11    | Front-End / Dashboard         | ⏳ Planned      |
| 12    | Testing                       | ⏳ Planned      |
| 13    | Documentation                 | ⏳ Planned      |
| 14    | Deployment                    | ⏳ Planned      |
| 15    | GitHub / Portfolio Polish     | ⏳ Planned      |

---

## Current Dataset

The current dataset contains:

* 50,000 invoice records
* Historical and open invoices
* Customer information
* Invoice amounts
* Payment terms
* Invoice dates
* Due dates
* Payment clearing dates

After data-cleaning activities, exact duplicate records and redundant/unusable columns are removed while expected missing values, such as `clear_date` for open invoices, are preserved.

---

## Technology Stack

### Data & ML

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost / other open-source ML libraries where appropriate

### Backend

* FastAPI

### Dashboard

* Streamlit

### Development

* Visual Studio Code
* Git
* GitHub
* Python virtual environment

### Deployment

* Docker
* Open-source / free-tier compatible deployment options

---

## Repository Structure

```text
p2p-bottleneck-delinquency-predictor
├─ docs
│  ├─ adr.md
│  ├─ dependency_management.md
│  └─ engineering_journal.md
├─ models
├─ notebooks
│  └─ 01_dataset_understanding.ipynb
├─ README.md
├─ requirements
│  ├─ base.txt
│  ├─ dev.txt
│  └─ prod.txt
├─ src
│  ├─ constants.py
│  ├─ data
│  │  ├─ cleaner.py
│  │  ├─ dataset_catalog.py
│  │  ├─ external
│  │  ├─ interim
│  │  ├─ processed
│  │  ├─ raw
│  │  │  └─ customer_invoices
│  │  │     └─ dataset.csv
│  │  └─ loader.py
│  └─ evaluation
│     └─ dataset_evaluator.py
└─ tests
   └─ test_data_pipeline.py
```

---

## Project Status

🚧 **Phase 3 — Target Definition**

The initial data understanding and data cleaning phases are complete.

The next objective is to finalize the prediction point and implement the two supervised learning targets:

1. `is_delayed` — classification
2. `days_to_payment` — regression

Once target definitions are finalized, the project will proceed to feature engineering.
