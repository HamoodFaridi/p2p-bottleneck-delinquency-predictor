# Architecture Decision Records (ADR)

This document records important architectural decisions made during the project.

---

## ADR-001

### Title

Use a Production-Oriented Project Structure

### Status

Accepted

### Context

The project aims to demonstrate production-grade machine learning engineering rather than a notebook-only data science workflow.

### Decision

Use a layered project structure separating:

- source code
- notebooks
- data
- documentation
- tests
- deployment

### Consequences

Pros

- Easier maintenance
- Better scalability
- Easier testing

Cons

- Slightly more initial setup




========DATED 09/22/2026=========================
                    ┌──────────────────────┐
                    │   Raw Dataset (CSV)  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Production Entry   │
                    │      Point / Main     │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼──────────────────┐
             ▼                 ▼                  ▼
       load_data()       clean_data()       build_targets()
       loader.py          cleaner.py        target_builder.py
             │                 │                  │
             └─────────────────┴──────────────────┘
                               │
                               ▼
                    Feature Engineering
                               │
                               ▼
                    Train / Validation
                               │
                               ▼
                         ML Model
                               │
                               ▼
                         Predictions
                               │
                               ▼
                       API / Dashboard