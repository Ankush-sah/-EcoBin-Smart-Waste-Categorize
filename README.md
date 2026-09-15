# EcoBin: Smart Waste Categorizer

A lightweight Python command-line application that classifies household waste into **Recyclable, Compostable, Electronic Waste, or Landfill** and records classifications in a local log.

## Features

- Case-insensitive keyword-based classification
- Interactive command-line interface
- Input validation for empty entries
- Persistent UTF-8 logging
- Modular package structure
- Automated tests with `pytest`

## How It Works

1. The user enters a waste item.
2. EcoBin normalizes the input and checks predefined keyword groups.
3. The first matching category is returned.
4. The classification is appended to `waste_log.txt`.

## Project Structure

```text
.
├── src/
│   └── ecobin/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_main.py
├── .gitignore
└── README.md
```

## Requirements

- Python 3.9+
- `pytest` for running tests

## Run the Application

From the repository root:

```bash
python -m src.ecobin.main
```

Example:

```text
EcoBin - Smart Waste Categorizer
Type 'exit' to quit.

Enter a waste item: plastic bottle
Category: Recyclable
```

## Run Tests

```bash
python -m pytest
```

## Technical Notes

The current classifier is **rule-based**, not machine learning. It is deliberately simple so the classification logic is transparent and easy to extend. An item that matches multiple categories currently uses the first matching category defined in `CATEGORIES`.

## Roadmap

- [x] Refactor into a package structure
- [x] Add automated tests
- [x] Add input validation
- [ ] Add a larger labeled waste dataset
- [ ] Build an ML-based classifier
- [ ] Add confidence scores
- [ ] Add a REST API
- [ ] Add a web interface
- [ ] Add waste analytics and visualizations

## Author

**Ankush Sah**

Aspiring AI/ML Engineer building practical Python and machine-learning projects.
