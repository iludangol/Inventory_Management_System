# Inventory_Management_System
This is my first project on python.
Mini Retail POS System

A simple Retail Point of Sale (POS) system built with Python.
This project demonstrates basic inventory management with categories, subcategories, and products, along with the ability to buy items, update stock, and view available products.

Features
Inventory stored as a nested dictionary (Category → Subcategory → Product).
View categories, subcategories, and products with stock and price.
Buy products with stock validation and auto-update.
Shows categories in a table with subcategories and product counts.
User-friendly CLI menu system.

Inventory Structure
Category → Subcategory → Product: [Stock, Price]


Example:

"Electronics": {
    "Mobiles": {"iPhone 13": [5, 1200], "Samsung S22": [3, 1000]},
    "Laptops": {"Dell XPS": [4, 1500], "MacBook Air": [2, 2000]}
}


How to Run

Clone the repository:

git clone https://github.com/yourusername/mini-retail-pos.git
cd mini-retail-pos


1) Run the program:

2) python pos_system.py

Menu Options
Buy Product → Select a category, subcategory, and product to purchase.
Show Categories → Displays a table of categories, subcategories, and product counts.
Exit → Quit the system.


Example Output
-----------------------------
       Retail Store POS      
-----------------------------
1. Buy Product
2. Show Categories
3. Exit
Enter choice: 2

--- Categories and Subcategories ---
Category        | Subcategories                  | #Products
------------------------------------------------------------
Electronics     | Mobiles, Laptops              | 4
Clothing        | Men, Women                    | 4
Groceries       | Fruits, Vegetables, Beverages | 9

Developed by [Ilu Dangol]