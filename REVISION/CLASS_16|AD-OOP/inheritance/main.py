class Parent:
    hair_color = 'brown'
    _password = 'password'

    def __init__(self):
        self.languages = ['English', 'Yoruba']

    def __str__(self):
        return 'I am a human being'



class Child(Parent):
    def __init__(self, languqges):
        super().__init__()
        self.languages.extend(languqges)

# new_child = Child(['French'])
# new_child2 = Child(['German', 'Spanish'])
#
# print(new_child.languages)
# print(new_child2.languages)
# print(new_child)

class Dog:
    species = 'Canis familaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} barks: {sound}'

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

class GoldenRetriever(Dog):
    def speak(self, sound='Bark'):
        return super().speak(sound)

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
henry = GoldenRetriever('Henry', 7)

#check type of object
print(type(miles))

#check if an object is an instance or inherits from a class -n Takes two arguements (obj and class)
print(isinstance(miles, Dog))
print(miles.speak())
print(jim.speak('Woof'))
print(henry.speak())