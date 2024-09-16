#SIMPLE FUNCTION DEFINITION
from CLASS_4.main import prime_numbers


def greet():
    print("Hello there! Good morning")
#calling the function
#greet()


# Python function that prints a text
def print_text(string):
    print(string)

text_1 = "Today is a lovely day. I love Mondays"
# print_text(text_1)
text_2 = "Aisha came late to class!"
# print_text(text_2)

#Using a function with a list.
list_animals = ["dog", "chicken", "cow", "elephant", "cat"]
# for animal in list_animals:
#     print_text(animal)

# Python function that accepts two numbers as arguments and returns the sum
def sum_numbers(a,b):
    add_numbers = a + b #3 + 2 = 5
    return add_numbers # 5

numbers_add = sum_numbers(50, 20)
# print(numbers_add)

#KEYWORD ARGUMENTS
def minus_numbers(a,b):
    sub_numbers = a - b
    return sub_numbers

number = minus_numbers(b = 20, a = 50)
# print(number)

#DEFAULT ARGUMENTS
def person(name="Aisha", surname="Aisha"):
    return f"{name} {surname}"

student_1 = person()
student_2 = person("Oluwaseyi", "Oyadokun")
#
# print(student_1)
# print(student_2)

#VARIABLE LENGTH
def calculator(*args):
    total = 0
    for arg in args:
        total+=arg

    return total

# print(calculator(2,3,5,7,9,10,12,5,9,12,34,56,78,102))

# Python function that accepts different values as parameters and returns a list
def make_list(*items):
    items_list = []
    for item in items:
        items_list.append(item)
    return items_list

# student_list = make_list("Oluwaseyi", "Aisha", "Mahmud","Abdulsalam", "OLamide", "Umar", "Adebayo")
# print(student_list)
# #
# Python Program to Find LCM
# def LCM(*numbers):
#     #After all LCM is lowest common multiple
#     #Goal is to divide through each number till we get to 0
#     numbers_list = [num for num in numbers]
#     LCM_num = 1
#     smallest_number = min(numbers_list)
#
#     while sum(numbers_list) != 0:
#         smallest_number = min(numbers_list)
#
#         for i in range(len(numbers_list)):
#                 if numbers_list[i] % smallest_number == 0:
#                     numbers_list[i] = numbers_list[i] // smallest_number
#                     LCM_num *= smallest_number
#                 else:
#                     numbers_list[i] = numbers_list[i] // smallest_number
#     return LCM_num
# print(LCM(2,6))

# Python Program to Find HCF

# Python Program to Convert Decimal to Binary, Octal and Hexadecimal -ASSIGNMENT
#Hint google the int methods

# Python Program To Find ASCII value of a character -
#chr - converts from ascii to character
#ord - converts from  character to ASCII
#ASSIGNMENT - CONVERT FULL STRINGS TO ASCII E.G "Aisha" - return as a string.
#HINT - Use a for loop
def convert_to_ascii(character):
    return ord(character)
print(convert_to_ascii("A"))




