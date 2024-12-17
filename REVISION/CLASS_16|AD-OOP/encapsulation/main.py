
#Protected
# class Student:
#     _school_name = 'Corona High School'
#     def __init__(self, name):
#         self._name =  name
#
#     @property #Getter
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value
#
#
#
# new_student = Student("Amina")
#
# print(new_student.name)
# new_student.name = "Aisha"
# print(new_student.name)

# refrain
# from accessing and modifying
# instance
# variables
# prefixed
# with _ from outside its class.

class Employee:
    __company = 'MTN'

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def __display(self):
        print("This is a private method")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

new_employee = Employee('Mamhud', 500_000)

#can access private attributes like this - BUT DO NOT USEEE
#print(new_employee._Employee__name)
# new_employee._Employee__display()

print(new_employee.name)
