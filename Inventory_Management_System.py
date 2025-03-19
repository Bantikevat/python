# Sample Data Structure
inventory = [
    

]

# Function to add a new item to the inventory
def add_product(inventory):
    product_id = len(inventory) + 1  # Auto-Generate ID
    name = input("Product Name: ")
    price = float(input("Price: ₹"))
    quantity = int(input("Quantity: "))
    
    new_product = {
        "id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }
    inventory.append(new_product)
    print(f"{name} added successfully! ✅")
# add_product(inventory)
# print(inventory)
def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty! 😟")
        return
    
    print("\n{:<5} {:<20} {:<10} {:<10}".format("ID", "Name", "Price", "Quantity"))
    print("-" * 50)
    for product in inventory:
        print("{:<5} {:<20} ₹{:<8} {:<10}".format(
            product["id"], product["name"], product["price"], product["quantity"]
        ))



def update_quantity(inventory):
    product_id = int(input("Enter Product ID: "))
    for product in inventory:
        if product["id"] == product_id:
            new_qty = int(input("New Quantity: "))
            product["quantity"] = new_qty
            print("Quantity Updated! ✅")
            return
    print("Product not found! ❌")


def check_low_stock(inventory):
    low_stock = [product for product in inventory if product["quantity"] < 10]
    if low_stock:
        print("\nLow Stock Alert! 🚨")
        view_inventory(low_stock)
    else:
        print("No low stock items. 👍")


import json

def save_inventory(inventory, filename="inventory.json"):
    try:
        with open(filename, "w") as file:
            json.dump(inventory, file)
        print("Data saved successfully! 💾")
    except Exception as e:
        print(f"Error saving data: {e} ❌")

def load_inventory(filename="inventory.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No existing data. Starting fresh! 🌟")
        return []
    except Exception as e:
        print(f"Error loading data: {e} ❌")
        return []


def main():
    inventory = load_inventory()  # Start with saved data
    
    while True:
        print("\n===== Inventory Management =====")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Update Quantity")
        print("4. Check Low Stock")
        print("5. Save & Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            view_inventory(inventory)
        elif choice == "3":
            update_quantity(inventory)
        elif choice == "4":
            check_low_stock(inventory)
        elif choice == "5":
            save_inventory(inventory)
            print("Exiting... Goodbye! 👋")
            break
        else:
            print("Invalid choice! ❌")

if __name__ == "__main__":
    main()