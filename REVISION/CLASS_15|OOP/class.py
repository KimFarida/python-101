# The simplest possible class
class Dog:
    species = 'Canis familaris'

    def __init__(self, name, age):
        self.name = name
        self.age  =  age

    def __str__(self):
        return f'Name:{self.name}, Age: {self.age}'

    def speak(self, sound):
        print(f"{self.name}: {sound}!")


# Step-by-step creation
my_dog = Dog("Buddy", 4)  # Create a dog named Buddy


my_other_dog = Dog("Bingo", 3)

my_dog.__class__.species = 'Felis silverstris'
# print(my_dog.__dict__)
# print(my_other_dog.__dict__)
# # print(my_other_dog.species)
# # print(my_dog.__class__.species)
# print(my_other_dog.species)
my_dog.speak('How do you do?')
my_other_dog.speak('I am very well, and you?')
my_dog.speak('I\'m also fine, What will you be doing today?')
my_other_dog.speak('Nothing much Just playing with my friends')

print(my_dog)