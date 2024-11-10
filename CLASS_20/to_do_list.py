# Simple To-Do List Manager (Using os and datetime Modules)
# Description: This console-based to-do list app helps users add, view, and delete tasks. Tasks can be timestamped, and users will store tasks in a text file.
# Learning Goals:
# Use os for file operations and datetime for managing timestamps.
# Understand module functionality and practice modular programming.
# How It Works: Users can add tasks, view all tasks with their creation dates, and delete tasks. Each task will be saved in a text file, so the data persists even if the program is restarted.

# CREATE A TEXT FILE FOR EACH TO DO LIST PER DAY
# VIEW TASKS REGISTERED TO BE DONE FOR THAT DAY
# ONCE A TASK IS COMPLETED- ADDED DONE TO THE BEGINNING OF THE LINE
# ONCE ASKED FOR TASK FOR THE DAY, SHOW WHAT DONE AND WHAT TO DO
# IF COMPLETED FOR THE DAY, DELETE ALL


# WE SHOULD HAVE A PROMPT
# - ADD TASKS
# - VIEWS TASKS
# - EDIT TASKS ONCE DONE
# - WHEN ALL DONE DELETE TASKS

import os
from datetime import datetime

from CLASS_11.main import lines

#Make a tasks Directory:
cwd = os.getcwd()

try:
    path = os.path.join(cwd, 'TASKS')
    os.mkdir(path)
except FileExistsError:
    print("Task Directory Already Created")



#lETS CREATE THE PROMPT
prompt = """
Hello and welcome to our to-do list.
#1 - Add Task
#2 - View Tasks
#3 - Mark a Task As Done
"""

#Ask user for input
def ask_option():
    while True:
        try:
            user_input = int(input("Enter a valid option between 1 - 3: ").strip())
            if 1 <= user_input <= 3:
                return user_input
        except ValueError:
            print("Invalid Input. Please make sure its a number.")


def ask_input():
    user_input = ''

    while not user_input or all(c == ' ' for c in user_input):
        user_input = input("Enter new task: ")
    return user_input

def save_task(task, task_date, task_time):
    file_path = f'TASKS/{task_date}.txt'

    if os.path.exists(file_path):
        print("Oh you already have Tasks for this Day")
    else:
        print("This is your first Task")

    with open(file_path, 'a+') as f:
        added_task = f'{task_time} - {task}\n'
        f.write(added_task)
        print(f'TASK ADDED:{added_task}')

def view_task(task_date):
    file_path = f'TASKS/{task_date}.txt'

    if not os.path.exists(file_path):
        print("You do not have any Tasks for this Date")
    else:
        with open(file_path, 'r') as f:
            lines = f.readlines()

            for line in lines:
                print(line)



#ADD A TASK
def add_task(task_date, task_time):
    # ask the user for the task they want to add.
    task = ask_input()

    #save the task
    save_task(task, task_date, task_time)

def main():
    date_time = str(datetime.now()).split(' ')

    task_date = date_time[0]
    task_time = date_time[1].split('.')[0]

    while True:
        print(prompt)
        option = ask_option()

        if option == 1:
            add_task(task_date, task_time)

        elif option == 2:
            view_task(task_date)
            pass
        else:
            #mark a task a done.
            pass



main()
