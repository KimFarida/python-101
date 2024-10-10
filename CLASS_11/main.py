#ABSOLUTE FILE PATH
#/Users/kimfarida/PycharmProjects/pythonProject/CLASS_11

#Opened a new File if exists else we created
file = open("text.txt", "w+")

#we wrote tom the file
file.write("This is a new file we just created and we are writing into it\n")
#We closed the file
file.close()

#READING FROM A FILE
# file = open("text.txt", "r")
# print(file.read())


file = open("text.txt", "a+")

file.write("This is the 2nd line\n")
file.write("This is the 3rd line\n")
file.write("This is the 4th line\n")
file.close()

# with open("text.txt", 'r') as f:
    # #This reads the entire file
    # data = f.read()
    # print(data)

    # #This reads a line in the file
    # data = f.readline()
    # print(data)
    #
    # #This returns a list of every line in the file
    # data = f.readlines()
    # print(data)

with open("text.txt", 'a+') as f:
    text_to_add = []

    for i in range(4, 8):
        text = f"This is the {i}th line\n"
        text_to_add.append(text)

    f.writelines(text_to_add)

with open("text.txt", 'r') as f:
    # for line in f.readlines():
    #     print(line)

    f.seek(5)
    location = f.tell()
    print(f.readline())
    print(location)