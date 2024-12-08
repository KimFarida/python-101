"""
Create a CSV processor that:
1. Reads a grades.csv file containing student records
2. Calculates average grade for each student
3. Adds a new column with pass/fail status
4. Writes results to a new CSV file
"""
import csv

from numpy.ma.extras import average


class CSV_processor():
    file_name = 'grade.csv'

    #Reads a grades.csv file containing student records
    @classmethod
    def read_grades(cls):
        #open file
        grades = []
        with open(cls.file_name, 'r') as f:
            grade_reader = csv.DictReader(f)

            for row in  grade_reader:
                grades.append(row)

        return grades

    @classmethod
    def calculate_average(cls):
        with open(cls.file_name, 'r') as f:
            grade_reader = cls.read_grades()

            average_grade = []
            for row in  grade_reader:
                ave_grade =  (int(row['chem']) + int(row['phy']) + int(row['bio']) + int(row['maths'])) / 4
                average_grade.append(ave_grade)

        return average_grade

    @classmethod
    def add_pass_status(cls):
        average = cls.calculate_average()

        grades = cls.read_grades()

        for average,grade in zip(average, grades):

            if average > 50:
                grade['status'] = 'P'
            else:
                grade['status'] = 'F'

        with open(cls.file_name, 'w', newline='') as f:
            field_names=['first_name','last_name','chem','phy','bio','maths', 'status']
            dict_writer = csv.DictWriter(f, fieldnames=field_names)
            dict_writer.writeheader()
            dict_writer.writerows(grades)

        return grades

    @classmethod
    def write_results(cls):
        grades = cls.add_pass_status()
        average = cls.calculate_average()
        for av, g in zip(average, grades):
            g['average_score'] = av



        with open('results.csv', 'w') as f:
            field_names = ['first_name', 'last_name', 'average_score']
            writer = csv.DictWriter(f, fieldnames=field_names, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(grades)




grade_book= CSV_processor()

# print(grade_book.read_grades())
# grade_book.calculate_average()
grade_book.write_results()