class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
class Flying:
    def fly(self):
        print("Flying high!")


class Swimming:
    def swim(self):
        print("Swimming deep!")

class Crawling:
    def crawl(self):
        print("Crawling slowly")



class Duck(Animal, Flying, Swimming):
    def __init__(self, name):
        super().__init__(name, species="Duck")

    def make_sound(self):
        print("Quack!")

class Crocodile(Animal, Swimming, Crawling):
    def __init__(self, name):
        super().__init__(name, species="Crocodile")

    def bite(self):
        print("Bites Antelope")
# Usage
donald = Duck("Donald")
donald.fly()  # From Flying class
donald.swim()  # From Swimming class
donald.make_sound()  # Duck's own method

manny = Crocodile("Manny")
manny.swim()
manny.crawl()
manny.bite()