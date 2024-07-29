#!/usr/bin/python3
""" Gather data from an API """


import json
import requests


if __name__ == '__main__':

    users = requests.get(
            "https://jsonplaceholder.typicode.com/users")

    user_dict = {}
    tasks = []
    for user in users.json():
        userId = user.get('id')

        todos = requests.get("https://jsonplaceholder.typicode.com/todos")

        for task in todos.json():
            if (task.get('userId') == int(userId)):
                task_dict = {
                        "username": task.get('username'),
                        "task": task.get('title'),
                        "completed": task.get('completed')
                        }
                tasks.append(task_dict)

        user_dict[userId] = tasks
    with open("todo_all_employees.json", 'w') as f:
        json.dump(user_dict, f)
