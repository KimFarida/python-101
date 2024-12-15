class Student:
    def __init__(self, name):
        self.name = name  # Attribute
        self.grades = []  # Attribute (list)
        self.subjects = set()  # Attribute (set)

    def add_grade(self, grade, subject):
        self.grades.append(grade)
        self.subjects.add(subject)

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def show_report(self):
        print(f"Student: {self.name}")
        print(f"Subjects: {', '.join(self.subjects)}")
        print(f"Average Grade: {self.get_average():.2f}")


# Usage demonstration
alice = Student("Alice")
alice.add_grade(85, "Math")
alice.add_grade(92, "Science")
alice.show_report()