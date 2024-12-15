class SchoolBag:
    def __init__(self, color):
        self.color = color
        self.items = []
        self.is_open = False

    def open_bag(self):
        self.is_open = True
        print(f"The {self.color} bag is now open!")

    def close_bag(self):
        if not self.is_open:
            print('School Bag is already close')
        else:
            self.is_open = False
            print(f"The {self.color} bag is now closed!")

    def add_item(self, item):
        if self.is_open:
            self.items.append(item)
            print(f"Added {item} to the {self.color} bag")
        else:
            print("Open the bag first!")

    def list_items(self):
        print(f"Items in {self.color} bag:", ', '.join(self.items))


# Each student has their own bag
alice_bag = SchoolBag("blue")
bob_bag = SchoolBag("red")

alice_bag.open_bag()
alice_bag.add_item("textbook")
alice_bag.add_item("lunch")
alice_bag.close_bag()
alice_bag.add_item("pencil")
alice_bag.open_bag()
alice_bag.add_item('pencil')
alice_bag.list_items()