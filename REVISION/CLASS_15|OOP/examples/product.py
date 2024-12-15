class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.stock = 0
        self.reviews = []

    def add_stock(self, quantity):
        self.stock += quantity
        print(f"Added {quantity} {self.name}(s). New stock: {self.stock}")

    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return f"Sold {quantity} {self.name}(s)"
        return "Not enough stock"

    def add_review(self, review, rating):
        self.reviews.append({"review": review, "rating": rating})
        print(f"Added review for {self.name}")

    def see_reviews(self):
        print(f'''
        Reviews
        {self.reviews}
''')


# Using the product system
laptop = Product("Gaming Laptop", 999.99, "Electronics")
laptop.add_stock(5)
laptop.sell(2)
laptop.add_review("Great product!", 5)
laptop.add_review("Very Durable", 4.5)
laptop.see_reviews()