# my_list  = list()
# print(my_list)
#
# list_of_things = [1, True, "Aisha", [1,2,3]]
# print(list_of_things)
#
# duplicate_list = [1,1,2,3,3,4,4,5,6]
# print(duplicate_list)
#
# duplicate_list = set(duplicate_list)
# print(duplicate_list)
#
# #LIST
# my_list = []
# my_list = list()
#
# #SET
# my_set = set()
# print(type(my_set))
#
# #DICTIONARY
# my_dict = {}
# my_dict = dict()
#
# #TUPLE
# my_tuple = tuple()
# my_tuple = ()
# my_tuple = (3,) #for a tuple  with a single  element
# print(len(my_tuple))

# numbers  = [1, 2, 3, 4, 5, 6, 7]
# last_idx = len(numbers) - 1
# print(numbers[last_idx])
# print(numbers[-1])
# print(numbers["one"]) numbers[::-1]
# del numbers
# print(numbers)
# last_element = numbers.pop()
# print(numbers)
# print(last_element)
# numbers.clear()
# print(numbers)

# my_list = [10, 20, 'Jessie', 'Esther', 50]
# my_list[2:4] = [30, 40]
#
# print(my_list)
#
# print(my_list[::2])
# print(my_list.index(40))
#
# try:
#     print(my_list.index(150))
# except ValueError:
#     print("The value does not exist in the list")

list1 =  [1, 2, 3, 4]
# list2 = list1.copy()
#
# list2.append(5)
# print(list1)
# print(list2)

# list1.reverse()

# reverse_list1 = list1[::-1]
# print(list1, reverse_list1)
#
# print(max(list1))
# print(min(list1))

# print(all([True, True, 0]))
#
# l1 = [10, 20, 30, 40, 50]
# print(l1 * 5)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# t = (*l1, *l2)
# print(t)

# #TESTING OUT STRINGS
# name = 'Seyi' #Single quotes
# hobby = "Reading" #Double quotes
# fav_foods = """
# Yam and egg
# Akara and Pap
# Fried Rice and Chicken
# """
# # Triple Quotes
# print(name, hobby, fav_foods)

#ACESSING STRINGS
occupation = "Pythonista"
length = len(occupation) #Lenght is 10
print(length)



# occupation[9]
# 'a'
# occupation[:3]
# 'Pyt'
# occupation[:6]
# 'Python'
# occupation[3:6]
# 'hon'
# occupation[2:6]
# 'thon'
# occupation[-1]
# 'a'
# occupation[-2]
# 't'
# occupation[-5:]
# 'nista'
# name = "Harry Potter"
# name[0:4]
# 'Harr'
# name[0:5]
# 'Harry'
# name[6:]
# 'Potter'
# name[6:12]
# 'Potter'
# name[::-1]
# 'rettoP yrraH'
# reversed(name)
# < reversed
# object
# at
# 0x1045138e0 >
# "".join(reversed(name))
# 'rettoP yrraH'
# list(name)
# ['H', 'a', 'r', 'r', 'y', ' ', 'P', 'o', 't', 't', 'e', 'r']
# list(name)[::-1]
# ['r', 'e', 't', 't', 'o', 'P', ' ', 'y', 'r', 'r', 'a', 'H']
# ''.join(list(name)[::-1])
# 'rettoP yrraH'
# name = 'Seyi'
# name = 'Feyi'
# name
# 'Feyi'

#USINGG SINGLE QUOTES
'''
>>> sentence = 'Hi I\'m ABDULSALAM'
sentence
"Hi I'm ABDULSALAM"
'''

#USINGG DOUBLE  QUOTES
'''
>>> quotes = "Renes Descartes said, \"Cogito Ergo, sum\", which means I think so therefore I am"
>>> quotes
'Renes Descartes said, "Cogito Ergo, sum", which means I think so therefore I am'
'''

#USING PYTHON STRING METHODS EXAMPLES
'''
>>> name = "aisha"
>>> name.capitalize()
'Aisha'

>>> name
'aisha'

>>> capital_a = name.capitalize()

>>> name
'aisha'

>>> capital_a
'Aisha'

>>> name = capital_a

>>> name
'Aisha'

>>> name.count('a')
1

>>> name.lower().count('a')
2

>>> name.endswith("sha")
True

>>> name.find('a')
4

>>> name.find('A')
0
'''

#STRING FORMATTING
'''
# Default Order
>>> string1 = "{} {} {}".format('I', 'am a', 'boy')
>>> string1
'I am a boy'

# Positional Order
>>> mahmud = "Hello, my name is {}. I am {} years old. I am learning {}".format('Mahmud', '16', 'Python')
>>> mahmud
'Hello, my name is Mahmud. I am 16 years old. I am learning Python'

>>> mahmud = "Hello, my name is {2}. I am {0} years old. I am learning {1}".format('16', 'Python', 'Mahmud')
>>> mahmud
'Hello, my name is Mahmud. I am 16 years old. I am learning Python'

#keyword Order
>>> mahmud = "Hello, my name is {name}. I am {age} years old. I am learning {language}".format(age='16', language='Python',                                                                                        name='Mahmud')
>>> mahmud
'Hello, my name is Mahmud. I am 16 years old. I am learning Python'

>>> string = "{0:2f}".format(1 / 6)
>>> string
'0.166667'

>>> string = "{0:.2f}".format(1 / 6)
>>> string
'0.17'

>>> string = "{0:.1f}".format(1 / 6)
>>> string
'0.2'

>>> first_name = "John"
>>> last_name = "Doe"
>>> first_name + last_name
'JohnDoe'
'''

