#FOR WHILE LOOPS
from setuptools.package_index import user_agent

# for x in range(2, 6):
#     print(x)
#
prime_numbers = [1, 3, 5, 7, 11]
#
# for prime in prime_numbers:
#     print(prime)

#A list of people on a queue
# queue = ["Jack", "Ann", "Sofie"]
#lenght of my queue
# length =  len(queue)
#
# for i in range(length):
#     name = queue[i]
#     print(f"Position: {i} - Name: {name}")
#
# queue[0] = "Aisha"
# queue[1] = "Oluwaseyi"
# queue[2] = "Mahmud"
# print(queue)

#LOOPING THRU A DICTIONARY
#A dictionary is an iterable of key, value pairs
# ages = {
#     'Jay-Z':52,
#     'Emma': 44,
#     'Oluwaseyi': 15,
#     'Mahmud': 16
# }
#
# for (key, value) in ages.items():
#     print(key, value)
#
# #Loop thru a string
# letters = "ABCDE"

#
# name = "Aisha"
# count = 0
#
# print(name)
# while name == "Aisha":
#     count +=1
#     print(count)
#     if count == 10:
#         name = "Oluwaseyi"
#
#
# print(name)

# i = 0
# while i <= 5:
#     print(i)
#     i += 1


# while True:
#     user_input = input('>>>')
#     print(f"The user said:{user_input}")
#
#     if user_input == 'quit':
#         break
#
# print("Quitting...")


#MINI EXERCISE - CALCULATOR
#Ask the user to keep entering numbers
#on each input convert  to a float()
#add to running total
#when user enters add stop this loop
sum_total = 0

# while True:
#     user_input = input("Please enter a number: ")
#     if user_input == "add":
#         break
#     else:
#         #Convert to float
#         num = float(user_input)
#         sum_total = sum_total + num
#         # T0-DO Print the number and the current total
#
# print(f"Your total is {sum_total}")


#ANOTHER WHILE LOOP EXAMPLE
# n = 1
#
# while n <= 10:
#     print(n)
#
#     if n == 5:
#         break
#
#     n += 1
# print("Loop Ended ")

# count = 0
#
# while count < 5:
#     count+=1
#     if count == 3:
#         continue
#     else:
#         print(count)

# cities = ["Berlin", "Sao Paulo", "Tokyo", "New York"]
# capitals = ["Berlin", "Tokyo"]
# city_capitals = 0
#
# for city in cities:
#     if city not in capitals:
#         continue
#     else:
#         print(f"{city} is a capital")
#         city_capitals +=1
#
# print(f"We have {city_capitals} cities that are capitals")

# cities = ["Berlin", "Sao Paulo", "Tokyo", "New York"]
#
# for city in cities:
#     if " " in city:
#         continue
#     else:
#         print(city)

# numbers = [[1,2,3], [4,5,6], [7,8,9]]
#
# for sublist in numbers:
#     print(f"This is sublist:{sublist}")
#
#     for num in sublist:
#         print(num)

#To do : PRINT A 3D LIST

# x = 1
# y = 1
#
# while x <=5 :
#     y = 1
#     while y <=x:
#         print(y, end ="")
#         y += 1
#     print()
#     x+=1

# artists = 'The Beatles', 'Elvis Presley', 'Michael Jackson', 'Madonna'
# sales = 600e6, 600e6, 350e6, 300e6
#
# for artist, sold in zip(artists, sales):
#     print(artist, sold)
#
# n = 3
# numbers_in_3D = [[[k for k in range(n)] for j in range(n)] for i in range(n)]
# print(numbers_in_3D)