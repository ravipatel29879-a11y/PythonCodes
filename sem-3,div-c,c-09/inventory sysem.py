stock = {}

def add_product(product_name, quantity):
    stock[product_name] = stock.get(product_name, 0) + quantity

def remove_product(product_name):
    if product_name in stock:
        del stock[product_name]
    else:
        print(f"Product '{product_name}' not found.")

def update_quantity(product_name, quantity):
    if product_name in stock:
        stock[product_name] = quantity
    else:
        print(f"Product '{product_name}' does not exist.")

def show_stock():
    print(f"\n{'Product':<15} | {'Quantity':<10}")
    print("-" * 28)
    for product_name, quantity in stock.items():
        print(f"{product_name:<15} | {quantity:<10}")

def check_low_stock():
    low_stock_items = {product_name: quantity for product_name, quantity in stock.items() if quantity < 6}
    print(f"\nLow Stock Items (<6): {low_stock_items if low_stock_items else 'None'}")


# Simulation
add_product("Books", 20)
add_product("Pencils", 4)
add_product("Rulers", 3)
add_product("Colors", 12)

show_stock()
check_low_stock()

update_quantity("Pencils", 14)
remove_product("Rulers")

print("\n--- After Modifications ---")
show_stock()
