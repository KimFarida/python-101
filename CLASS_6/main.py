#creating docstrings
import random


from CLASS_5.main import number, print_text


def greeting(name):
    """
    Greets the person given the name.
    Parameters:
        name (str) : Name of the person.
    Returns:
        str: greeting message
    """
    return f"Hello {name}"

def add_list(*list):
    """
    Adds a running sum as a we iterate through list as the items in a new list
    Parameters:
    *args: A variable length argument list

    Returns:
        list : Prefix sum list
    """
    sum_num = 0
    new_list = []

    for num in list:
        sum_num += num
        new_list.append(sum_num)

    return new_list
# print(random.randint.__doc__)
# print(random.randint(1, 5))
# print(add_list(1,2,3,4,5))
# print(add_list.__doc__)

x = 300
def print_x(x):
    x = 400
    return x

x = 10

def change_value():
    number = 5
    print(number)

    global x
    print(x)

    x = 7
    print(f"Inside function:{x}")

# change_value()

# print(f"Outside function:{x}")
# print(number)

def main():
    a = 5
    def square():
        nonlocal a
        print(f"Square: {a * a}")

        a = 3

    square()
    print(a)

# main()

#LAMDA
add = lambda x,y : x + y
# print(add(2,3))

#LAMBDA FUNCTION TO SQUARE A NUMBER
square_num = lambda a: a * a

num_list = [1,2,3,4,5]
#
# number_square = list(map(square_num, num_list))
#
# print(num_list)
# print(number_square)

# RECURSION
def pickAisha(i = 0):
    #Base Case
    if i == 12:
        print(f"HURRAYYY ITS HOLIDAYS. WE DONT HAVE TO PICK AISHA TIKL NEXT SESSION")
        return
    print(f"WEEK {i + 1} We have picked Aisha for School ")
    pickAisha(i+1)

# pickAisha()

def count(i = 1):
    #Base Case
    if i > 5:
        return

# count()
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        print(n)
        return n * factorial(n-1)

# factorial(5)
from functools import reduce
#Does not return an object like map
multiply = lambda x, y: x * y
product = reduce(multiply, num_list)
# print(product)

#ASSIGNMENT - WRITE THE FACTORIAL FUNCTION USING FOR/WHILE LOOPS
even_numbers = list(filter(lambda x : x % 2 == 0, num_list))
# print(even_numbers)

def example(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

example(1, 2, 3, name="Alice", age=25)
