# EcoBin: Smart Waste Categorizer

A lightweight Python command-line application that classifies household waste into **Recyclable, Compostable, Electronic Waste, or Landfill** and records each classification in a log file.

## Features

- Keyword-based waste classification
- Interactive command-line interface
- Persistent logging to `waste_log.txt`
- Simple, readable Python implementation
- Easy to extend with new waste categories and keywords

## How It Works

1. The user enters a waste item such as `plastic bottle` or `banana peel`.
2. EcoBin normalizes the input and checks it against predefined keyword groups.
3. The item is assigned a disposal category.
4. The result is appended to the waste log.

## Project Structure

```text
.
├── EcoBin/
│   ├── main.py
│   └── waste_log.txt
└── README.md
```

## Run Locally

Make sure Python 3 is installed, then run:

```bash
python EcoBin/main.py
```

Type `exit` to close the application.

## Example

```text
Enter a waste item (or type 'exit' to quit): plastic bottle
Category: Recyclable
```

## Technical Notes

The current implementation uses keyword matching rather than a machine-learning model. This keeps the project intentionally simple and makes the classification logic easy to understand and modify.

## Future Improvements

- Replace keyword rules with a trained ML classifier
- Add a larger and more structured waste dataset
- Add unit tests
- Improve ambiguous-item handling
- Add a web or REST API interface
- Add analytics for waste-category statistics

## Author

**Ankush Sah**

Aspiring AI/ML Engineer focused on Python, machine learning, and practical AI projects.
