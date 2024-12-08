"""
Create a simple logging system that:
1. Takes user input repeatedly
2. Writes each input to a log file with timestamp
3. Allows viewing of last N log entries
4. Handles file operations safely
"""
from urllib3.filepost import writer

prompt = '''
Hi and welcome to our Log System. Would you Like to write something?
'''

print(prompt)
while True:
    user_input = input("Start Writing: ")

    with open('log.txt', 'a+') as f:
        f.write(user_input + '\n')

    write_again= ''
    while True:

        write_again = input("Would you like to write something else?Input YES or NO").strip().lower()

        if write_again in ['yes', 'no']:
            break

        print('PLEASE INPUT YES OR NO')

    if write_again == 'no':
        break




