#DEFINING A CLASS

#CREATING A DOG CLASS AS A LIST
["German Sheperd", 3, "Black", "M"]
["German Spitz", "White"]

class Dog:
    breed = "German Shepard"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} is barking"

#CREATING A NEW OBJECT
new_dog1 = Dog("Bingo", 5)
# print(new_dog1.name)
# print(new_dog1.age)
#
# new_dog1.color = "Black"
# print(new_dog1.color)
#
# print(new_dog1.__dict__)
# print(new_dog1.bark())

new_dog2 = Dog("Zeus", 3)
# print(new_dog1.breed)
# print(new_dog2.breed)

new_dog2.__class__.breed = "Japanese Spitz"
print(new_dog2.breed)
print(new_dog1.breed)
# print(new_dog2.__class__.breed)


# print(new_dog1.__dict__)
print(new_dog2.__dict__)

print(new_dog1.bark())
print(new_dog2.bark())

class Person:
    pass

#STATE - ATTRIBUTES
#BEAHVIOUR - METHODS
#IDENTITY - VARIABLE NAME