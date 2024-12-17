class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic sound")

    def get_info(self):
        return f"{self.name} is a {self.species}"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball!")


# Usage
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.make_sound()  # Calls Dog's version
print(my_dog.get_info())  # Uses Animal's version
my_dog.fetch()  # Dog-specific method