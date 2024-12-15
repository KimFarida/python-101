class MenuItem:
    def __init__(self, name, price, cuisine):
        self.name = name
        self.price = price
        self.cuisine = cuisine
        self.is_available = True

    def order(self, quantity=1):
        if self.is_available:
            total = self.price * quantity
            return f"Ordered {quantity} {self.name}(s). Total: ${total}"
        return f"Sorry, {self.name} is not available"

    def mark_unavailable(self):
        self.is_available = False
        print(f"{self.name} is now unavailable")


# Creating menu items
pizza = MenuItem("Margherita Pizza", 12.99, "Italian")
burger = MenuItem("Cheese Burger", 8.99, "American")
print(burger.order(4))
burger.mark_unavailable()
print(burger.order(4))
swallow = MenuItem('Eba and Egusi Soup', 14.99, 'Nigerian')
print(swallow.order(4))
