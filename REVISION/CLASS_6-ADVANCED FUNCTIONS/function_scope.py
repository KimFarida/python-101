# global_var = "I'm global"
#
# def scope_demo():
#     local_var = "I'm local"
#     print(global_var)
#     print(local_var)
#
# def another_function():
#     #print(local_var)
#     print(global_var)
#
# another_function()

'''
The problem is the scope of the variable.
You can’t directly modify a variable from a high-level scope like global in a lower-level scope like local.
Internally, Python assumes that any name directly assigned within a function is local to that function.
'''

# counter = 0
#
# #You can read a global varible, but only reassignment lest you affect it when a lower namespace function is called
# def increment(arg):
#     # Fix this function to properly increment the global counter
#     print(counter)
#
#     arg = arg + 1
#
#     return arg
# counter = increment(counter)
# print(counter)

# number = 5
#
# def add():
#     total = 1 + 1
#     return total
#
# number = number +  add()
# print(number)

counter = 0

def increment():
    global counter
    counter = counter + 1

increment()
print(counter)



