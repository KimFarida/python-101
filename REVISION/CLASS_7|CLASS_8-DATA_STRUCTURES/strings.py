text = "Python Programming"

# Advanced slicing
reversed_text = text[::-1]
every_second = text[::2]
last_three = text[-3:]

# Multiple slices
middle = text[2:-2]

# Advanced string methods
text = "  Python Programming is Amazing!  "

# Cleanup methods
cleaned = text.strip()
titled = text.title()
swapped = text.swapcase()

# Search and replace
found = text.find('Programming')  # returns index
count = text.count('m')
replaced = text.replace('Python', 'Java')

# Advanced splits and joins
words = text.split()
csv = "1,2,3,4,5"
numbers = csv.split(',')
joined = '-'.join(words)

# Different formatting methods
name = "Alice"
age = 25

# f-strings with expressions
info = f"{name} is {age} years old"
calc = f"Age in months: {age * 12}"

# Format specification
pi = 3.14159
formatted = f"{pi:.2f}"

# Format method
template = "Hello, {name}! You are {age} years old."
filled = template.format(name=name, age=age)