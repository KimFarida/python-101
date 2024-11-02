#INHERITANCE
#POLYMORPHISM
#ENCAPSULATION
#ABSTRACTION

# class Person:
#     def __str__(self):
#         return f'I just created a new_person'
#
# p = Person()
# print(p)

# class Robot:
#     """
#     This is a class method for creating Android Robots
#     """
#     __population = 0
#     def __init__(self, name):
#         self.name = name
#         print(f"Initializing {self.name}")
#         Robot.__population +=1
#
#     def die(self):
#         """
#         This is a method that kill a robot and reduces the class attribute population by 1
#         :return:
#         """
#         print(f"{self.name} is being destroyed")
#
#         Robot.__population -= 1
#
#         if Robot.__population == 0:
#             print(f"{self.name} was the last one")
#         else:
#             print(f"There are still {Robot.__population} ROBOTS working")
#
#     def say_hi(self):
#         print(f"Greetings, my masters call me {self.name}")
#
#     @classmethod
#     def how_many(cls):
#         print(f"We have {cls.__population}")
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# Robot.how_many()
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# droid2.__class__.how_many()
#
# print("\nRobots can do some work here.\n")
#
# print("Robots have finished their work. So let's destroy them.")
# droid1.die()
# droid2.die()
#
# Robot.how_many()
#
# print(Robot.__doc__)
# print(Robot.die.__doc__)


#INHERITANCE | ENCAPSULATION | POLYMORPHISM
#BASE CLASS
class SchoolMember:
    """
    Represents any school member
    """
    __population = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        SchoolMember.__population += 1
        print(f"Initialized SchoolMember : {self.name}")

    def tell(self):
        print(f"Name: {self.name}| Age: {self.age}")

    @classmethod
    def show_population(cls):
        print(f"We have {cls.__population} School Members")


class Teacher(SchoolMember):
    __population = 0
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        Teacher.__population += 1
        print(f"Initialized Teacher : {self.name}")

    def tell(self):
        super().tell()
        print(f"Salary: {self.salary}")

    @classmethod
    def show_population(cls):
        super().show_population()
        print(f"We have {cls.__population} Teachers")

class Student(SchoolMember):
    __population = 0
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
        Student.__population +=1
        print(f"Initialized Student : {self.name}")

    def tell(self):
        super().tell()
        print(f"Marks:{self.marks}")

    @classmethod
    def show_population(cls):
        super().show_population()
        print(f"We have {cls.__population} Students")

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
a =  Student('Aisha', 17, 85)
m =  Student('Mahmud', 17, 95)

# prints a blank line
print()

members = [t, s, a, m]
for member in members:
    # Works for both Teachers and Students
    member.tell()

t.__class__.show_population()
s.__class__.show_population()

#ASSIGNMENT - MODEL A HOSPITAL with 4 CLASSES
#MAKE SURE ALL THE CONCEPTS WE SPOKE ON ARE REFLECTED
