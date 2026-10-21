tasks = []

def add_item(item_name, categories_set):
    item = {
        "item": item_name,
        "categories": set(categories_set)
    }
    tasks.append(item)

def show_all():
    print("\n--- All Tasks ---")
    for number, entry in enumerate(tasks, start=1):
        category_text = ", ".join(entry['categories'])
        print(f"{number}. Task: {entry['item']:<25} | Categories: [{category_text}]")

def search_by_category(search_category):
    print(f"\n--- Tasks tagged with '{search_category}' ---")
    found_items = [entry['item'] for entry in tasks if search_category in entry['categories']]
    if found_items:
        for item_name in found_items:
            print(f"  - {item_name}")
    else:
        print("  No tasks found for this category.")


# Demonstration
add_item("Complete Project", {"study", "important"})
add_item("Buy Vegetables", {"home", "shopping"})
add_item("Create Report", {"study", "office"})

show_all()
search_by_category("study")
search_by_category("shopping")
