import csv

# Reading CSV
# with open('data.csv', 'r') as file:
#     csv_reader = csv.reader(file)
#     headers = next(csv_reader)  # Skip header row
#     for row in csv_reader:
#         print(row)

# Using DictReader
with open('data.csv', 'r') as file:
    csv_dict_reader = csv.DictReader(file)
    for row in csv_dict_reader:
        print(row)
        #print(row['Name'],row['Breed'], row['Country'], row['Lifespan'], row['Sound'])