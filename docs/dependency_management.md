# Dependency Management

## Purpose

This project separates runtime and development dependencies to keep the environment clean and reproducible.

## Structure

requirements/

    base.txt
    dev.txt
    prod.txt

## Installation

Development:

```bash
python -m pip install -r requirements/dev.txt
```

Production:

```bash
python -m pip install -r requirements/prod.txt
```

## Rules

- Never install packages globally.
- Use `python -m pip`.
- Only direct dependencies are listed.
- Keep dependency files minimal.