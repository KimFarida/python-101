# File modes demonstration
"""
'r' - Read (default)
'w' - Write (overwrites)
'a' - Append
'x' - Exclusive creation
'b' - Binary mode
't' - Text mode (default)
'+'- Read and write
"""

# Basic file operations
file = open('sample.txt', 'r')
content = file.read()
file.close()

# Better way using context manager
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)