# DICTIONARY

# CREATING
"""
>>> char_num = {'a': 1, 'b': 2, 'c': 3}
>>> char_num
{'a': 1, 'b': 2, 'c': 3}
>>> name_age = dict([('Seyi', 18), ('Mahmud', 16)])
"""

#ACCESSING
"""
>>> char_num['a']
 1
>>> char_num['c']
 3
char_num = {'a': 1, 'b': 2, 'c': 3, 'a': 4}
>>> char_num['a']
 4
"""

#UPDATING
"""
>>> student = {'name': 'John', 'age': 20, 'major': 'Computer Science'}
>>> student['name']
'John'

>>> student['age']
20 

>>> student['major']
'Computer Science'

>>> student['major'] = "English"
>>> student['major']
'English'

>>> student
{'name': 'John', 'age': 20, 'major': 'English'}

>>> student['name'] = "Emmanuel"
>>> student
{'name': 'Emmanuel', 'age': 20, 'major': 'English'}

>>> student['university'] = "Covenant Univeristy"
>>> student['hobby'] = ["Singing", "Playing Football", "Drumming"]
>>> student
{'name': 'Emmanuel', 'age': 20, 'major': 'English', 'university': 'Covenant Univeristy',
'hobby': ['Singing', 'Playing Football', 'Drumming']}
"""

#DELETING
"""
>>> del student['age']
>>> student
{'name': 'Emmanuel', 'major': 'English', 'university': 'Covenant Univeristy',
'hobby': ['Singing', 'Playing Football', 'Drumming']}
"""


"""
>>> name_age = dict([('Seyi', 18), ('Mahmud', 16)])
>>> name_age
{'Seyi': 18, 'Mahmud': 16}

>>> name_age.keys()
dict_keys(['Seyi', 'Mahmud'])

>>> name_age.values()
dict_values([18, 16])

>>> name_age.items()
dict_items([('Seyi', 18), ('Mahmud', 16)])

>>> name_age.get("Seyi")
18

>>>name_age.get("Aisha")

>>> name_age.get("Aisha", "Not in dictionary")
'Not in dictionary'

>>> name_age.get("Olamide", "Not in dictionary")
'Not in dictionary'

>>> name_age.get("Aisha", "Not in dictionary")
'Not in dictionary'
"""


#LOOPING
"""
>>> for name, age in name_age.items():
    ...print(f"My name is {name}, I am {age} years old")

My name is Seyi, I am 18 years old
My name is Mahmud, I am 16 years old
"""

#REMOVE ALL ITEMS
"""
>>> name_age.clear()
>>> name_age
{}
"""

#REMOVE SPECIFIC ITEM AND RETURN IT
"""
>>> student
{'name': 'Emmanuel', 'major': 'English', 'university': 'Covenant Univeristy',
 'hobby': ['Singing', 'Playing Football', 'Drumming']}
>>> student.pop('university')
'Covenant Univeristy'
"""

"""
>>> student
{'name': 'Emmanuel', 'major': 'English', 'hobby': ['Singing', 'Playing Football', 'Drumming']}

>>> my_dict = {'Sophia': 32, 'William': 23, 'Emma': 27}
>>> max_key = max(my_dict, key=my_dict.get)
>>> max_key
'Sophia'

>>> my_dict = {'name': 'Sophia', 'age': 32, 'contact': {'phone': '123-456-7890', 'email': 'sophia@example.com'}}
>>> my_dict['contact']['email']
'sophia@example.com'

>>> name_age = dict(zip(["Seyi"], [16]))
>>> name_age
{'Seyi': 16}

>>> my_dict.popitem()
('contact', {'phone': '123-456-7890', 'email': 'sophia@example.com'})
>>> dict.fromkeys(['a', 'b'], 1)
{'a': 1, 'b': 1}

>>> colors = ["red", "green", "blue"]
>>> colors_dict = {color[0]: color for color in colors}
>>> colors_dict
{'r': 'red', 'g': 'green', 'b': 'blue'}
"""
