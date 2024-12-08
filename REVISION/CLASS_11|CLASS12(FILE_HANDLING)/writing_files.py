# Writing to files
with open('output.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.writelines(['Line 1\n', 'Line 2\n'])

# Appending to files
with open('output.txt', 'a') as file:
    file.write('Appended line\n')