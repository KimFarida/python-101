# #CONDITIONAL STATEMENTS
# #A game that asks you maths questions
# import random
#
# # We need two variables to store our numbers
# num_1 = random.randint(1, 10)
# num_2 = random.randint(1, 10)
# answer = num_1 + num_2
#
# # we need a variable to take userinput and remove whitespace
#
# #we want to convert our input to an int so we can compare
# while True:
#     try:
#         user_input = int(input(f"What is {num_1} + {num_2}?:\n").strip(" "))
#
#         if answer == user_input:
#             print(f"Yes! The correct answer is {answer}")
#             break
#         else:
#             print(f"WRONG. PLEASE TRY AGAIN")
#     except ValueError as e:
#         print("You did not put in a valid integer. Please try again :(")

#conditional syntax
# if condition :
#     statements
# elif condition:
#     statements
# else:
#     statements

# z = 1000
# if z == 100:
#     print("z is 100")
# elif z == 200:
#     print("z is 200")
# elif z == 300:
#     print("z is 300")
# elif z == 1000:
#     print("z is 1000")
# else:
#     print("z is unknown")

# m = 22
# n = 25
# if m > n:
#     print("m is greater than n")
# elif m == n:
#     print("m is equals to n")
# else:
#     print("m is less than n")

# p = 10
# q = 30
#
# if (p < q) or (p == q):
#     print("Either p is less than q or p is equal to q")
# elif (p == 30) and (q == 30):
#     print("p and q are equal")
# elif p != q:
#     print("p is not equal to q")
# else:
#     print("p is greater than q")

# is_true = False
#
# if is_true == True:
#     print("Statement is True")
# else:
#     print("Statement is False")

# z = 3
#
# if z < 0:
#     if z == -1:
#         print("z is -1 ")
#
#     print("z is less than zero")
# else:
#     if z < 5:
#         print("z is less than 5")
#     else:
#         print("z is greater than 5")

# count = 350
# if count < 400:
#     print("The count is below 400")
#     if count < 300:
#         print("The count is less than 300")
#     else:
#         print("The count is less than 400 but greater than or equal to 300")

#in | no in
# name = "Aisha"
#
# if "i" in name:
#     print("Yes")
# else:
#     print('No')
#
# if "e" not in name:
#     print("No")

# x = 55
# y = 110
#
# print("X") if x > y else print("Y")
# name = "Aisha" if 'e' in "Aisha" else "Mahmud"
# print(name)
#
# s = 200
# r = 400
# print("s is not equal to r") if s!= r else print("s is equals to r")

# s = 3000
# t = 1000
# if s > t and t % 2 == 0:
#     print("Both conditions are true")

# x = 100
# y = 10
#
# if x > y:
#     pass

# print("Enter a number")
# number = int(input())
#
# if number < 20:
#     print("The number is less than 20")
# elif number == 20:
#     print("The number is equal to 20")
# else:
#     print("The number is greater than 20")
#
# print("Enter a number")
# number = int(input())
#
# if number % 5 == 0:
#     print("The number is divisble by 5")
# else:
#     print("The number is not divisible by 5")

#GUESSING GAME
#ASK A USER FOR INPUT
#AND KEEP ASKING TILL THEY GET THE CORRECT ANSWER
#BONUS, IF THE PERSON FAILS 3 TIMES GIVE A HINT
#IF THEY GET A CORRECT ANSWER PRINT THE ANSWER AND END THE PROGRAM

#ROCK PAPER SCISSORS
#TWO VARAIBLES , ONE FOR USER INPUT AND ONE FOR COMPUTER
#scissors - scissors - draw
# scissors - rock - rock wins
# scissors - paper - scissors wins
#paper - rock - paper wins
