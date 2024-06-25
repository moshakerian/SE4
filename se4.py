#Mozhdeh shakerian
#40025028
#SE4

import csv

class Product:
    def __init__(self, product_id, name, product_type, price, is_available, rate):
        self.product_id = int(product_id)
        self.name = name
        self.product_type = product_type
        self.price = float(price)
        self.is_available = is_available.lower() == 'true'
        self.rate = float(rate)

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        if not isinstance(product.product_id, int):
            raise ValueError("Product ID must be a number!")
        if not product.is_available:
            raise ValueError(f"{product.name} is not available at the moment!")
        self.items.append(product)
        print(f"Added to cart: {product.name} - {product.price}")

    def total_price(self):
        return sum(item.price for item in self.items)

    def clear(self):
        self.items = []

class User:
    def __init__(self, username, wallet=0.0):
        self.username = username
        self.wallet = float(wallet)
        self.cart = Cart()

    def checkout(self):
        total = self.cart.total_price()
        if total > self.wallet:
            raise ValueError("Not enough money in your wallet!")
        self.wallet -= total
        self.print_receipt()
        self.cart.clear()

    def print_receipt(self):
        print("Payment successful!")
        for item in self.cart.items:
            print(f"{item.name} - {item.price}")
        print(f"Remaining wallet balance: {self.wallet:.2f}")

def read_products(file_path):
    products = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product = Product(row['ID'], row['Name'], row['Type'], row['Price'], row['Is_available'], row['Rate'])
            products[product.product_id] = product
    return products

products = read_products(r"C:\Users\shake\OneDrive\Desktop\products.csv")

def add_product_to_cart(user):
    try:
        product_id = input("Enter product ID: ")
        if not product_id.isdigit():
            raise ValueError("Product ID must be a number!")
        product_id = int(product_id)
        if product_id not in products:
            raise ValueError("No product found with the given ID!")
        product = products[product_id]
        user.cart.add_product(product)
    except ValueError as e:
        print(e)

def checkout(user):
    try:
        user.checkout()
    except ValueError as e:
        print(e)

user = User(username="testuser", wallet=100.0)

add_product_to_cart(user)

checkout(user)