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