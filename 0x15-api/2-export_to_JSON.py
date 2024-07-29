#!/usr/bin/python3
""" Gather data from an API """


import json
import requests
import sys


if __name__ == '__main__':

    emp_id = sys.argv[1]
    employee = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(emp_id))

    name = employee.json().get('username')

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    f_name = "{}.json".format(emp_id)
    user_dict = {}
    tasks = []
    with open(f_name, 'w') as f:
        for task in todos.json():
            if (task.get('userId') == int(emp_id)):
                task_dict = {
                        "task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": name
                        }
                tasks.append(task_dict)

        user_dict[emp_id] = tasks
        json.dump(user_dict, f)
