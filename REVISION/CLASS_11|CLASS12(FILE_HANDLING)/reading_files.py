# Different reading methods
# with open('sample.txt', 'r') as file:
#     # Read entire file
#     content = file.read()
#
#     file.seek(0)
#     # Read line by line
#     line = file.readline()
#     print(line)
#     print(file.tell)
#     #
#     # # Read all lines into list
#     # lines = file.readlines()
#     # print(lines)
#     #
#     # # Iterate over lines
#     # for line in file:
#     #     print(line.strip())
try:
     file = open('example.txt', 'r')
except:
    print("FILE DOES NOT EXIST")