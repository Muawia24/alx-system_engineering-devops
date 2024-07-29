#!/usr/bin/python3
""" Gather data from an API """


import json
import requests


if __name__ == '__main__':

    users = requests.get(
            "https://jsonplaceholder.typicode.com/users")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_dict = {}

    for user in users.json():

        tasks = []
        userId = user.get('id')

        for task in todos.json():
            if (task.get('userId') == userId):
                task_dict = {
                        "username": task.get('username'),
                        "task": task.get('title'),
                        "completed": task.get('completed')
                        }
                tasks.append(task_dict)

        user_dict[userId] = tasks

    with open("todo_all_employees.json", 'w') as f:
        json.dump(user_dict, f)
