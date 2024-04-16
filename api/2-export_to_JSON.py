#!/usr/bin/python3
"""Export data from employees information to CSV file"""

import json
import requests
from sys import argv

if __name__ == "__main__":

    # Get user name related to id
    user_api_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        argv[1])
    users = requests.get(user_api_url)
    users_list = users.json()

    # Get tasks from user
    tasks_url = "https://jsonplaceholder.typicode.com/users/{}/todos/".format(
        argv[1])
    todos = requests.get(tasks_url)
    todos_tasks = todos.json()

    # Create the list of dict with values to export to json
    user_all_tasks_dict = {
        argv[1]: [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": users_list.get("username")
            }
            for task in todos_tasks
        ]
    }

    # Export data to a json file
    json_file = "{}.json".format(argv[1])
    with open(json_file, "w") as f:
        json.dump(user_all_tasks_dict, f)
