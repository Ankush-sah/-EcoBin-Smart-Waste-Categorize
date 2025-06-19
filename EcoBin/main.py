# EcoBin - Smart Waste Categorizer
# Author: Ankush
# Description: Categorizes household waste and logs it in a file.

def categorize_waste(item):
    """Categorize waste item into Recyclable, Compostable, E-Waste, or Landfill."""
    item = item.lower()

    recyclable_keywords = ['plastic', 'bottle', 'can', 'paper', 'cardboard', 'glass', 'tin']
    compostable_keywords = ['banana', 'peel', 'food', 'vegetable', 'fruit', 'leaves', 'egg', 'tea', 'coffee']
    ewaste_keywords = ['battery', 'phone', 'laptop', 'cable', 'charger', 'remote', 'lightbulb']
    
    if any(word in item for word in recyclable_keywords):
        return 'Recyclable'
    elif any(word in item for word in compostable_keywords):
        return 'Compostable'
    elif any(word in item for word in ewaste_keywords):
        return 'Electronic Waste'
    else:
        return 'Landfill'

def log_to_file(item, category):
    """Log categorized waste item to a text file."""
    with open("waste_log.txt", "a") as f:
        f.write(f"{item} -> {category}\n")

def main():
    print("♻️  Welcome to EcoBin - Smart Waste Categorizer ♻️\n")
    
    while True:
        item = input("Enter a waste item (or type 'exit' to quit): ").strip()
        
        if item.lower() == 'exit':
            print("✅ Thank you for using EcoBin. Check 'waste_log.txt' for your waste log.")
            break
        
        category = categorize_waste(item)
        print(f"🗂️  Category: {category}\n")
        
        log_to_file(item, category)

if __name__ == "__main__":
    main()
