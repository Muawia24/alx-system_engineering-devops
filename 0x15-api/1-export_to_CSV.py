#!/usr/bin/python3
""" Gather data from an API """


import requests
import sys
import csv

if __name__ == '__main__':

    emp_id = sys.argv[1]
    employee = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(emp_id))

    name = employee.json().get('username')

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    f_name = "{}.csv".format(emp_id)
    with open(f_name, 'w', newline='') as csvfile:
        writer = csv.writer(
                csvfile, delimiter=',', quotechar='"',
                quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            if (task.get('userId') == int(emp_id)):
                task_stat = task.get('completed')
                task_title = task.get('title')
                writer.writerow(
                        [emp_id, name, task_stat, task_title])
