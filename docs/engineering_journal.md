                 Historical Invoices
                         │
                         ▼
                 Feature Engineering
                         │
                         ▼
                  ML Model Training
                         │
                         ▼
              Predict Payment Delinquency
                         │
                         ▼
              ┌──────────────────────┐
              │ Current Open Invoices│
              └──────────────────────┘
                         │
                         ▼
                  Risk Prediction
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       Low Risk      Medium Risk      High Risk
          │              │              │
          ▼              ▼              ▼
       Normal         Monitor       Take Action


Invoice       Customer      Amount      Risk
------------------------------------------------
INV10001      Customer A    $2,400      🔴 High
INV10002      Customer B    $8,100      🟢 Low
INV10003      Customer C    $5,700      🟠 Medium


customer_historical_late_rate
customer_average_payment_delay
customer_invoice_count
customer_average_invoice_amount


Data Dictionary:

| Category            | Columns                                                                                                               |
| ------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Potential target    | `isOpen`                                                                                                              |
| Potential outcome   | `clear_date`                                                                                                          |
| Customer            | `cust_number`, `name_customer`                                                                                        |
| Dates               | `posting_date`, `document_create_date`, `document_create_date.1`, `due_in_date`, `baseline_create_date`, `clear_date` |
| Financial           | `total_open_amount`                                                                                                   |
| Payment behavior    | `cust_payment_terms`                                                                                                  |
| Business dimensions | `business_code`, `invoice_currency`, `document type`                                                                  |
| Likely identifiers  | `doc_id`, `invoice_id`                                                                                                |
| Constant / useless  | `posting_id`                                                                                                          |
| Completely missing  | `area_business`                                                                                                       |



Highly Predictive Features:

Customer
+
Payment terms
+
Invoice amount
+
Currency
+
Timing
+
Historical customer behavior



Current Porject Structure

P2P-Bottleneck-Predictor/

│

├── .git/
│   ├── many folders
│
├── .venv/
│   ├── many folders (untracked)
│
├── docs/
│   ├── adr.md
│   ├── dependency_management.md
│   ├── engineering_journal.md
│
├── models/
│
├── notebooks/
│   ├── dataset_understanding.ipynb
│
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   ├── prod.txt
│
├── src/
│   ├── data/
│   ├── evaluation/
├── data/
│   ├── raw/
│   ├── processed/
│   ├── external/

├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── visualization/
│   ├── api/
│
├── tests/
│
├── models/
│
├── dashboard/
│
├── configs/
│
├── docs/
│
├── .github/
│
├── requirements.txt
├── README.md
├── .gitignore
├── pyproject.toml




Step 5 — Target definition

Historical closed invoices
        │
        ▼
Calculate actual payment behavior
        │
        ▼
Create is_delayed target
        │
        ▼
Train model
        │
        ▼
Open invoices
        │
        ▼
Predict probability of delayed payment



Step 6 — Feature engineering

Invoice-level

invoice_amount
days_until_due
invoice_term_days
posting_day_of_week
posting_month
posting_year
posting_quarter

Customer-level

customer_average_payment_delay
customer_median_payment_delay
customer_late_payment_rate
customer_invoice_count
customer_average_invoice_amount
customer_previous_late_payments


Step 8 — Train/test strategy

Older invoices
       │
       ▼
Training data
       │
       │
       ▼
Later invoices
       │
       ▼
Validation/Test


roadmap

PHASE 2 — DATA CLEANING
│
├── ✅ Column name standardization
├── ✅ Remove unusable columns
├── 🔄 Date standardization        ← NOW
├── ⏭ Date quality validation
├── ⏭ Duplicate/key investigation
├── ⏭ Missing-value treatment
├── ⏭ Categorical-value validation
└── ⏭ Final cleaned dataset
        │
        ▼
PHASE 3 — TARGET CREATION
│
├── days_late
├── is_delayed
└── Historical vs open invoice separation
        │
        ▼
PHASE 4 — FEATURE ENGINEERING
│
├── Invoice features
├── Date features
├── Customer behavior
├── Payment-term features
└── Leakage prevention
        │
        ▼
PHASE 5 — MODELING
│
├── Baseline
├── Random Forest
├── Gradient Boosting
├── Hyperparameter tuning
└── Model selection
        │
        ▼
PHASE 6 — EVALUATION
│
├── Precision
├── Recall
├── F1
├── ROC-AUC
├── PR-AUC
└── Business impact
        │
        ▼
PHASE 7 — PRODUCTION PIPELINE
│
├── Saved model
├── Prediction pipeline
├── API
└── Application
        │
        ▼
PHASE 8 — DEPLOYMENT
│
├── Local production-style deployment
├── Docker
└── GitHub CI/CD



                 DATA CLEANING
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
    Structural      Quality        Modeling
     cleaning       checks         readiness
        │              │              │
   • columns       • missing      • leakage
   • names         • duplicates   • target
   • types         • dates        • IDs
   • datatypes     • ranges       • features
        │              │              │
        └──────────────┼──────────────┘
                       ↓
                 CLEAN DATASET
                       ↓
                 MODEL PIPELINE



