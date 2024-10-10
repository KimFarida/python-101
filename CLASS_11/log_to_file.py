#Create a program that logs user input into a file.
from tkinter.tix import INTEGER
user_name = ''
user_age = ''

while True:
    user_name = input("What is your name?:")
    if not user_name or user_name.startswith(" "):
        print("INVALID USERNAME")
        continue

    try:
        user_age = int(input("What is your age?:"))
        break
    except ValueError:
        print("INVALID AGE, PLEASE PUT IN AN INTEGER")

if user_name and user_age:
    with open("user_logs.txt", "a+") as f:
        f.write(f"{user_name}: {user_age}\n")