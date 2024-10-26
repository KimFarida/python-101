# PERSON, CLASS ATTRIBUTES, INSTANCE ATTRIBUTES, METHODS

class Person:
    population = 0
    def __init__(self, name, age, height, gender):
        try:
            if gender not in ("M", "F"):
                raise NameError
            if age < 0 or age > 100:
                raise ValueError

        except NameError:
            print("You put in a wrong gender")
        except ValueError:
            print("You put in an invalid age")

        self.name = name
        self.height = height
        self.age = age
        self.gender = gender
        Person.population += 1

    def introduce_yourself(self):
        return f"""
        My name is {self.name}.
        I am {self.age} years old.
        I am {self.height}cm tall.
        I am a {self.gender + "emale" if self.gender == "F" else self.gender + "ale"}
"""
    @classmethod
    def no_of_persons(cls):
        return cls.population




new_girl = Person("Aisha", 17, 160, "F")
print(new_girl.introduce_yourself())
new_boy = Person("Mahmud", 17, 180, "M")
print(new_boy.introduce_yourself())

print(Person.no_of_persons())

