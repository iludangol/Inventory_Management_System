# Mini Retail POS System with Total Products and Buy Confirmation

# Inventory (Category -> Subcategory -> Product: [stock, price])
inventory = {
    "Electronics": {
        "Mobiles": {"iPhone 13": [5, 1200], "Samsung S22": [3, 1000]},
        "Laptops": {"Dell XPS": [4, 1500], "MacBook Air": [2, 2000]}
    },
    "Clothing": {
        "Men": {"Shirt": [10, 20], "Jeans": [5, 40]},
        "Women": {"Dress": [7, 50], "Top": [8, 25]}
    },
    "Groceries": {
        "Fruits": {
            "Apple": [20, 2],
            "Banana": [30, 1],
            "Orange": [25, 1.5]
        },
        "Vegetables": {
            "Potato": [50, 0.5],
            "Tomato": [40, 0.8],
            "Onion": [35, 0.6]
        },
        "Beverages": {
            "Milk": [25, 1.2],
            "Juice": [15, 2],
            "Coffee": [10, 5]
        }
    }
}

# Function to calculate total products in a category
def total_products(category):
    count = 0
    for sub in inventory[category]:
        count += len(inventory[category][sub])
    return count

# Function to show categories
def show_categories():
    print("\nCategories and Total Products:")
    for i, cat in enumerate(inventory.keys(), 1):
        print(f"{i}. {cat} ({total_products(cat)} products)")
    choice = int(input("Choose category: "))
    return list(inventory.keys())[choice-1]

# Function to show subcategories
def show_subcategories(category):
    print(f"\nSubcategories in {category}:")
    subcats = inventory[category]
    for i, sub in enumerate(subcats.keys(), 1):
        print(f"{i}. {sub} ({len(subcats[sub])} products)")
    choice = int(input("Choose subcategory: "))
    return list(subcats.keys())[choice-1]

# Function to show products
def show_products(category, subcategory):
    print(f"\nProducts in {subcategory}:")
    products = inventory[category][subcategory]
    for i, (name, details) in enumerate(products.items(), 1):
        print(f"{i}. {name} - Stock: {details[0]}, Price: Rs.{details[1]}")
    choice = int(input("Choose product: "))
    return list(products.keys())[choice-1]

def show_categories_table():
    print("\n--- Categories and Subcategories ---")
    print(f"{'Category':<15} | {'Subcategories':<30} | {'#Products'}")
    print("-"*60)
    
    for category, subcats in inventory.items():
        # Join all subcategory names separated by comma
        subcat_names = ", ".join(subcats.keys())
        # Count total products in this category
        total_products = sum(len(subcats[sub]) for sub in subcats)
        print(f"{category:<15} | {subcat_names:<30} | {total_products}")


# Function to buy a product
def buy_product(category, subcategory, product):
    stock, price = inventory[category][subcategory][product]
    print(f"\nSelected Product: {product} - Stock: {stock}, Price: Rs.{price}")
    confirm = input("Do you want to buy this? (Y/N): ").upper()
    if confirm == "Y":
        qty = int(input(f"Enter quantity (Available: {stock}): "))
        if qty <= stock:
            inventory[category][subcategory][product][0] -= qty
            total = qty * price
            print(f"✅ Purchased {qty} x {product} for ${total}")
            if inventory[category][subcategory][product][0] == 0:
                print(f"⚠️ {product} is now OUT OF STOCK!")
        else:
            print("❌ Not enough stock available!")
    else:
        print("Purchase cancelled.")

# Main Function
def pos_system():
    while True:
        print("-----------------------------")
        print("       Retail Store POS      ")
        print("-----------------------------")
        print("1. Buy Product")
        print("2. Show Categories")
        print("3. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            category = show_categories()
            subcategory = show_subcategories(category)
            product = show_products(category, subcategory)
            buy_product(category, subcategory, product)
        
        elif choice ==2:
            show_categories_table()  
            break 

        elif choice == 3:
            print("Exiting POS System...")
            break
        else:
            print("Invalid choice! Try again.")
            

# Run Program
pos_system()
