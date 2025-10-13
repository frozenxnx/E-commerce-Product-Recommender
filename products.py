import pandas as pd
import random

categories = {
    "Electronics": ["Wireless Mouse", "Bluetooth Speaker", "Smartwatch", "Gaming Keyboard", "Power Bank", "Laptop Sleeve", "Earbuds", "Phone Case", "USB Cable", "Webcam"],
    "Fashion": ["T-shirt", "Jeans", "Sneakers", "Jacket", "Watch", "Sunglasses", "Handbag", "Cap", "Belt", "Shoes"],
    "Home": ["Vacuum Cleaner", "Table Lamp", "Wall Clock", "Cushion Cover", "Curtains", "Coffee Mug", "Dinner Set", "Air Purifier", "Toaster", "Kettle"],
    "Sports": ["Yoga Mat", "Dumbbells", "Skipping Rope", "Cricket Bat", "Football", "Tennis Racket", "Running Shoes", "Water Bottle", "Gym Gloves", "Cycling Helmet"],
    "Beauty": ["Face Wash", "Shampoo", "Conditioner", "Lipstick", "Moisturizer", "Perfume", "Hair Oil", "Body Lotion", "Nail Polish", "Sunscreen"],
    "Books": ["Novel", "Notebook", "Comics", "Cookbook", "Self-help Book", "Biography", "Magazine", "Travel Guide", "Thriller Book", "Children’s Story Book"],
    "Groceries": ["Rice Bag", "Wheat Flour", "Olive Oil", "Honey", "Almonds", "Oats", "Coffee Powder", "Green Tea", "Cookies", "Cereal"]
}

products = []
id_counter = 1

for category, items in categories.items():
    for item in items:
        price = round(random.uniform(5, 100), 2)
        tags = ",".join(random.sample(["eco", "premium", "new", "bestseller", "discount", "trending", "value"], 3))
        products.append([id_counter, item, category, tags, price])
        id_counter += 1

df = pd.DataFrame(products, columns=["id", "title", "category", "tags", "price"])
df.to_csv("data/products.csv", index=False)
print("✅ products.csv created with", len(df), "rows")
