# 2) Inventory Reorder Alert System
print("# Inventory Reorder Alert System")
def check_inventory(products):
    for product, stock in products.items():
        if stock < 15:
            print(f"{product}: Reorder Alert | Stock Available: {stock}")
        else:
            print(f"{product}: Stock OK | Stock Available: {stock}")


# Sample dictionary
inventory = {
    "Laptop": 20,
    "Mouse": 10,
    "Keyboard": 8,
    "Monitor": 25
}

check_inventory(inventory)