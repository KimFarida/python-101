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
from CLASS_5.main import print_text

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

l1 = [1, 2, 3]
l2 = [4, 5, 6]
t = (*l1, *l2)
print(t)
