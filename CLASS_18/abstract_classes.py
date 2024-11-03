from abc import ABC, abstractmethod

class Aircraft(ABC):

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def land(self):
        print("All checks completed")

class Jet(Aircraft):

    def fly(self):
        print("My jet is flying")

    def land(self):
        super().land()
        print("My jet has landed")

'''
An Abstract class is a class that contains one or more abstract methods.
Abstract classes cannot be instantiated.

Abstract classes can only be used via inheritance and their concrete child classes have to provide an implementation 
for all the abstract methods.

A class that inherits an abstract class and implements all its abstract methods is called a concrete class

A child class of an abstract class can be instantiated only if it overrides all the abstract methods in the parent class.

The term override in Python inheritance indicates that a child class implements a method with the same name as a method implemented in its parent class. This is a basic concept in object-oriented programming.


'''


#ABSTRACT PROPERTIES
class Aircraft(ABC):

    def __int__(self, speed):
        self.__speed = speed

    @property
    @abstractmethod
    def speed(self):
        pass

    @speed.setter
    @abstractmethod
    def speed(self, value):
        pass

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def land(self):
        print("All checks completed")

'''
Note: it’s important to specify the @abstractmethod decorator after the @property and @speed.setter decorators
'''

class Jet(Aircraft):

    def __int__(self, speed):
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    def fly(self):
        print("My jet is flying")

    def land(self):
        super().land()
        print("My jet has landed")


# jet1 = Jet(900)
# print(jet1.speed)
# jet1.speed = 950
# print(jet1.speed)

'''
ABCMeta is a metaclass that allows to define abstract base classes.
A metaclass is a class that allows to create other classes
'''

class Account:
    def __init__(self):
        self._username = None
        self.__password = None

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError("Password length less than 8")
        self.__password = value

    def __str__(self):
        return "This is an account object"

seyi = Account()
# seyi.username = "seyi123"
# seyi.password = "admin"
#
# print(seyi.username)
# print(seyi.password)
print(seyi)