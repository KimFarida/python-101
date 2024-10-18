#Create a program that logs user input into a file.
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
        user_data = f"{user_name}: {user_age}\n"
        f.write(user_data)
        print(f"Sucessfully added new user : {user_data}")

        f.seek(0)
        users = f.readlines()

        print("CURRENT USERS | AGE")

        for user in users:
            print(user)