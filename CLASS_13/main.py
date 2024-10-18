# >>> "one" + 1
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str
# >>> [1,2,3] + 5
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate list (not "int") to list
# >>> [1,2,3] + [5]
# [1, 2, 3, 5]
# >>>
from lib2to3.fixes.fix_asserts import NAMES


# >>> print(name)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'name' is not defined

# >>> numbers = [1, 2, 3, 4, 5]
# >>> numbers[5]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range

# >>> student = {"name":"Seyi", "university":"CU", "address":"Ota"}
# >>> student["course"]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'course'


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name:{self.name}| Age:{self.age}"


# new_person =  Person("Seyi", 19)
# print(new_person.name)
# print(new_person.age)
# print(new_person.location)
# Traceback (most recent call last):
#   File "/Users/kimfarida/PycharmProjects/pythonProject/CLASS_13/main.py", line 16, in <module>
#     print(new_person.location)
# AttributeError: 'Person' object has no attribute 'location'

# >>> int("one")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: 'one'

# >>> 3 / 0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero

# >>> die = [1, 2, 3, 4, 5, 6]
# >>> choice(die)
# 2
# >>> from random import choi
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: cannot import name 'choi' from 'random' (/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/random.py)
#
#

#TRY-EXCEPT
# >>> try:
# ...     print ("Second element = %d" %(a[1]))
# ...     print ("Fourth element = %d" %(a[3]))
# ... except:
# ...     print ("An error occurred")
# ...
# Second element = 2
# An error occurred

# #HANDLING SPECIFIC EXCEPTIONS
# food = {"name": "Egusi and Pounded Yam", "tribe": "Yoruba", "calories": 1056}
# serving = ["breakfast", "lunch", "dinner"]
# try:
#     print(serving[3])
#     print(food["serving"])
# except KeyError:
#     print("This key does not exist")
# except IndexError:
#     print("The index is out of range")


#EXCEPTION WITH ELSE CLAUSE
# def divide(a, b):
#     try:
#         c = a / b
#     except ZeroDivisionError:
#         print(f"The division of {a}/{b} is 0")
#     else:
#         print(c)
#     finally:
#         print("We divided!")
#
# divide(3,0)
# divide(6, 2)

# try:
#     raise NameError("Hi there")
# except NameError as e:
#     print("An exception")
#     raise


#HANDLING MULTIPLE EXCEPTIONS AT ONCE
# try:
#     print(int("one"))
# except Exception as e:
#     print(e)

# number = 10
# if number > 5:
#     raise Exception(f"The number should not exceed 5. ({number=})")
# print(number)

# number = 1
# if number > 5:
#     raise Exception(f"The number should not exceed 5. ({number=})")
# print(number)

def linux_interaction():
    import sys
    if "darwin" not in sys.platform:
        raise RuntimeError("Function can only run on Linux systems.")
    print("Doing darwin things.")

linux_interaction()