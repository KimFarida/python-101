class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.inventory = []

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage! Health: {self.health}")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} healed {amount} points! Health: {self.health}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up {item}")


# Creating and interacting with characters
player1 = Character("Hero")
player2 = Character("Warrior")

player1.take_damage(20)
player2.heal(10)
player1.add_item("Sword")