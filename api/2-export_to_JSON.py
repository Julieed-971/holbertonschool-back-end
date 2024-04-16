#!/usr/bin/python3
"""Export data from employees information to CSV file"""

import json
import requests
from sys import argv

if __name__ == "__main__":

    # Get user name related to id
    user_api_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        argv[1])
    user = requests.get(user_api_url)
    employee_name = user.json().get('username')

    # Get tasks from user
    tasks_url = "https://jsonplaceholder.typicode.com/users/{}/todos/".format(
        argv[1])
    todos = requests.get(tasks_url)
    todos_tasks = todos.json()

    # Create the list of dict with values to export to json
    todos_list = []
    for item in todos_tasks:
        todos_list.append({
            "task": item["title"],
            "completed": item["completed"],
            "username": employee_name
        })
    todos_dict = {argv[1]: todos_list}

    # Export data to a csv file
    json_file = "{}.json".format(argv[1])
    with open(json_file, "w") as f:
        json.dump(todos_dict, f)
