# Traditional vs Lambda
def double(x):
    return x * 2

double_lambda = lambda x: x * 2

print(double_lambda(2))

number = [1, 2, 3, 4]
double_number = map(double_lambda, number)

print(list(double_number))

# Using with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))

'''
Create a lambda function to filter out odd numbers from a list.
'''