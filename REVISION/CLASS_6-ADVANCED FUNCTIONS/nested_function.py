def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(3)
print(result)

#assignment
# def create_multiplier(factor):
#     # Create a nested function that multiplies its input by factor
#     pass



def greeting():
    greeting = "hi"

    def say_hi():
        print(greeting)

    say_hi()

greeting()

def build_house(cement, wood, sand, alum):
    def make_blocks(cement, sand):
        print(f"Making {cement} Cement")
    def make_roofing(alum):
        print(f"Roofing Done with {alum} sheets!")
    def make_furniture(wood):
        print(f"Making Chairs and Tables from {wood} logs")

    make_blocks(cement, sand)
    make_roofing(alum)
    make_furniture(wood)

    print("WELCOME TO YOUR NEW HOUSE")

#build_house(20, 300, 2, 59)

#USING NON LOCAL
def main():
    x = 1
    y = 6
    def add():
        nonlocal x

        x = 4
        nonlocal y
        y = 5

    add()
    print(x)
    print(y)

#main()
# PASSING DOWN AND REASSIGNING
def main():
    x = 1
    y = 6
    def add(x , y):

        x = 4
        y = 5

        return x, y

    x , y = add(x, y)

    print(x)
    print(y)

#main()