class Animal():
    def __init__(self, name, noise):
        self.name = name
        self.noise = noise

    def __str__(self):
        return f"This is a {self.__class__.__name__} and its name is {self.name}"

    def noises(self):
        print(f"This {self.name} {self.noise}")


class Dog(Animal):
    def __init__(self, name, noise):
        super().__init__(name, noise)


class Cat(Animal):
    def __init__(self, name, noise):
        super().__init__(name, noise)

#Create a Dog and a Cat
bingo = Dog("bingo", "barks")
neko = Cat("neko", "meows")

print(bingo)
print(neko)
bingo.noises()
neko.noises()