#!/usr/bin/python3
"""Return information about employee TO DO list progress"""


import requests
from sys import argv

if __name__ == "__main__":

    # Get user name related to id
    user_api_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    user = requests.get(user_api_url)
    employee_name = user.json().get('name')

    # Get tasks from user
    tasks_api_url = "https://jsonplaceholder.typicode.com/users/{}/todos/".format(
        argv[1])
    todos = requests.get(tasks_api_url)
    todos_tasks = todos.json()
    total_tasks = len(todos_tasks)

    # Get and append task title for done task in todos_tasks
    titles = [item.get('title') for item in todos_tasks if
            item.get("completed") is True]
    done_tasks = len(titles)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))
    for _ in titles:
        print("\t {}".format(_))
