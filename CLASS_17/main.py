'''
4 PRINCIPLES OF OOP
- INHERITANCE
- POLYMORPHISM
- ABSTRACTION
- ENCAPSULATION
'''
#ABSTRACTION

#METHOD OVERRIDING

from abc import ABC, abstractmethod

#
# class Animal(ABC):
#     def __int__(self, name):
#         self.name = name
#
#     #@abstractmethod
#     def make_sounds(self):
#         print('I am an Animal')
#
# class Dog(Animal):
#     def __int__(self, name):
#         super().__init__(name)
#
#
#     def make_sounds(self):
#         print("Woof")
#
#
# animal = Animal()
# animal.make_sounds()
#
# dog = Dog()
# dog.make_sounds()

#BLUEPRINT
class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass

    def identity(self):
        print("My Parent Class is a Polygon")

class Triangle(Polygon):

    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    def noofsides(self):
        print("I have 6 sides")

#
# triangle = Triangle()
# triangle.noofsides()
#
# pentagon = Pentagon()
# pentagon.noofsides()
#
# hexagon = Hexagon()
# hexagon.noofsides()


class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Lion(Animal):
    def move(self):
        print("I can roar")

# seyi = Human()
# seyi.move()
#
# snake = Snake()
# snake.move()
#
# lion = Lion()
# lion.move()

#IMPLEMENTATION OF ABSRACT THROUGH SUBCLASSES
'''
Concrete Methods in Abstract Base Classes
Concrete classes contain only concrete (normal) methods whereas abstract classes may contain both concrete methods and abstract methods.
'''

from abc import ABC

class R(ABC):
    def rk(self):
        print("Abstract Base Class")

class K(R):
    def rk(self):
        super().rk()
        print("subclass")

# r = K()
# r.rk()

# Abstract Properties in Python
import abc
from abc import ABC, abstractmethod

class parent(ABC):
    @abstractmethod
    def geeks(self):
        return 'parent class'

class child(parent):

    @property
    def geeks(self):
        return 'child class'


# try:
#     r = parent()
#     print(r.geeks)
# except Exception as seyi:
#     print(seyi)
#
# r = child()
# print(r.geeks)

'''
ABSTRACT CLASS INSTANTIATION
So, we use an abstract class as a template and according to the need,
 we extend it and build on it before we can use it. Due to the fact, 
 an abstract class is not a concrete class, it cannot be instantiated.
When we create an object for the abstract class it raises an error. 
'''

class Shape(ABC):
    def print_shape(self):
        print("I AM A SHAPE")

    @abstractmethod
    def area(self):
        print("Found the area")
