# Advanced list operations
numbers = [1, 2, 3, 4, 5]

# Less common but powerful methods
numbers.extend([6, 7]) #adds multiple elements to a list at once [1, 2, 3, 4, 5, 6, 7]
numbers.insert(0, 0) #inserts at a specific index [0, 1, 2, 3, 4, 5, 6, 7]
numbers.pop() # removes the last el  and returns it [0, 1, 2, 3, 4, 5, 6]
numbers.index(3) #  return the index of a particular element -  #3


# numbers - [0, 1, 2, 3, 4, 5, 6]
# numbers[:3] -> [0, 1, 2]
# numbers[::2] -> [0, 2, 4, 6]
# numbers[::-1] -> [6, 5, 4, 3, 2, 1, 0]
# numbers[2:] -> [2, 3, 4, 5, 6]

reversed = [numbers[i] for i in range(len(numbers) -1, -1, -1)]

pairs = []

for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x !=y :
            pairs.append((x, y))

vec = [[1,2,3], [4,5,6], [7,8,9]]

new_list = []
for elem in vec:
    for num in elem:
        new_list.append(num)

#LIST  COMPREHENSION
# Multiple list operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [ el for sublist in matrix for el in sublist]

def rotate_list(lst, k):
    """
    Rotate a list k positions to the right
    Example: rotate_list([1,2,3,4,5], 2) → [4,5,1,2,3]
    """

    start = lst[-k:]
    end = lst[:-k]
    start.extend(end)
    return start


print(rotate_list([1,2,3,4,5], 2))

# Basic to advanced list comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Single condition
evens = [x for x in numbers if x % 2 == 0]

# Multiple conditions
filtered = [x for x in numbers if x % 2 == 0 and x > 5]

# Nested list comprehension
matrix = [[i+j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

'''
Create a list comprehension that generates a list of tuples containing numbers and their squares,
but only for even numbers between 1 and 10.
'''
