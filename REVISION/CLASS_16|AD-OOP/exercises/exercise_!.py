"""
Create a vehicle hierarchy:
1. Base Vehicle class with common attributes
2. Specific vehicle types (Car, Motorcycle, Truck)
3. Each with unique methods and attributes
4. Include proper encapsulation
"""


class Vehicle:
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year
        self.__mileage = 0

    @property
    def mileage(self):
        return self.__mileage


    def drive(self, distance):
        self.__mileage += distance

# implement Car, Motorcycle, and Truck classes