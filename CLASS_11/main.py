# cl3
#
# with open("text.txt", 'r+') as f:
#     for line in f.readlines():
#         print(line)
#
#     f.seek(5)
#     location = f.tell()
#     print(f.readline())
#     print(location)
#     f.seek(0)
#     print(f.read())

#/Users/kimfarida/PycharmProjects/pythonProject/CLASS_11/log_to_file.py

with open("text.txt", 'w+') as f:
    f.write("SEYI IS A GIRL\n")
    # f.seek(0)
    #print(f.read())

with open("text.txt" ,"a+") as f:
    f.write("AISHA IS A GIRL\n")

    lines = ["MAHMUD IS A BOY\n", "OLAMIDE IS A BOY\n", "MUSTARPHA IS A BOY\n"]
    f.writelines(lines)
    f.seek(0)
    print(f.read())

# INITIAL METHOD OF FILE HANDLING
file = open('text.txt', 'r')
#print(file.read())
file.close()


#ABSOLUTE PATH
#/Users/kimfarida/PycharmProjects/pythonProject/python.txt

#REALATIVE PATH

# with open("../python.txt", 'r') as f:
    #using read()
    #data = f.read()
    # print(data)
    # f.seek(0)
    #using f.readline()
    # line = f.readline()
    # print(line)
    # line = f.readline()
    #print(line)
    #using readlines()

    # #Readlines return a list that you can iterate through
    # lines = f.readlines()
    # for line in lines:
    #     print(line)

try:
    f = open("myfile.txt", "x")
except FileExistsError:
    print("THIS FILE ALREADY EXISTS!")

