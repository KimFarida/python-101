# Writing CSV
import csv
data = [
    ['Name', 'Age', 'City'],
    ['John', '25', 'New York'],
    ['Alice', '30', 'London']
]

with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

# Using DictWriter
fieldnames = ['Name', 'Age', 'City']
data = [
    {'Name': 'John', 'Age': '25', 'City': 'New York'},
    {'Name': 'Alice', 'Age': '30', 'City': 'London'},
    {'Name': 'Seyi', 'City': 'Lagos', 'Gender':'F'}

]

with open('output.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames, restval=15,extrasaction='ignore')
    writer.writeheader()
    writer.writerows(data)