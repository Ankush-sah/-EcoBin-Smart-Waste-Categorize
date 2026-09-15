"""Command-line waste categorizer for EcoBin."""

from pathlib import Path

CATEGORIES = {
    "Recyclable": ("plastic", "bottle", "can", "paper", "cardboard", "glass", "tin"),
    "Compostable": ("banana", "peel", "food", "vegetable", "fruit", "leaves", "egg", "tea", "coffee"),
    "Electronic Waste": ("battery", "phone", "laptop", "cable", "charger", "remote", "lightbulb"),
}

LOG_FILE = Path(__file__).resolve().parents[2] / "waste_log.txt"


def categorize_waste(item: str) -> str:
    """Return the disposal category for a waste item.

    Matching is case-insensitive and uses simple keyword rules.
    """
    normalized = item.strip().lower()

    for category, keywords in CATEGORIES.items():
        if any(keyword in normalized for keyword in keywords):
            return category

    return "Landfill"


def log_to_file(item: str, category: str, log_file: Path = LOG_FILE) -> None:
    """Append a classification result to the configured log file."""
    log_file.parent.mkdir(parents=True, exist_ok=True)
    with log_file.open("a", encoding="utf-8") as file:
        file.write(f"{item.strip()} -> {category}\n")


def main() -> None:
    """Run the interactive EcoBin command-line application."""
    print("EcoBin - Smart Waste Categorizer")
    print("Type 'exit' to quit.\n")

    while True:
        item = input("Enter a waste item: ").strip()

        if item.lower() == "exit":
            print("Thank you for using EcoBin.")
            return

        if not item:
            print("Please enter a waste item.\n")
            continue

        category = categorize_waste(item)
        print(f"Category: {category}\n")
        log_to_file(item, category)


if __name__ == "__main__":
    main()
