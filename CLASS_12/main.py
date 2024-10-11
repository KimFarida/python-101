import csv


# Writing a dictionary to a CSV file

# Storing emails from customers-100.csv into a new CSV file -

# Reading a CSV file
with open("customers-100.csv", "r") as f:
    to_csv_obj = csv.reader(f)
    fields = next(to_csv_obj)

    count = 0
    for row in to_csv_obj:
        for i in range(len(fields)):
            print(f"{fields[i]}:{row[i]}")
        print('\n')
        count+=1
        if count == 2:
            break

#ASSIGNMENT
# Reading CSV Files Into a Dictionary With csv
#Make a dictiionary of 10 customers-customers-100.csv

file = "animal.csv"

# Writing to a CSV file
fields = ['Name', 'Breed', 'Country', 'Lifespan', 'Sound']
rows = [
    ['Dog', 'German Sherpard', 'German', '6', 'Bark'],
    ['Cat', 'Persian', 'Siberia', '9', 'Meow'],
    ['Goat', 'Pygmy', 'Mountain', '8', 'Bleat']
]
with open(file, "w") as f:
    list_to_csv = csv.writer(f)

    list_to_csv.writerow(fields)
    list_to_csv.writerows(rows)



