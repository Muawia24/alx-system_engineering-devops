#!/usr/bin/python3
""" Gather data from an API """


import requests
import sys


if __name__ == '__main__':

    tot_tasks = 0
    done_tasks = 0

    emp_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos/{}".format(emp_id)
    employee = requests.get(url)

    name = employee.json().get('name')

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    for task in todos.json():
        if (task.get('userId') == int(emp_id)):
            tot_tasks += 1
            if (task.get('completed')):
                done_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
        name, done_tasks, tot_tasks))

    for task in todos.json():
        if (task.get('userId') == int(emp_id)):
            if (task.get('completed')):
                print(task.get('title'))
