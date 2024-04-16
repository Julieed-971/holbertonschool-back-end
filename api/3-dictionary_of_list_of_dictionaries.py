#!/usr/bin/python3
"""Export data from employees information to CSV file"""

import json
import requests

if __name__ == "__main__":

    # Get user name related to id
    user_api_url = "https://jsonplaceholder.typicode.com/users/"
    users = requests.get(user_api_url)
    # employee_name = user.json().get('username')
    users_list = users.json()

    # Get tasks from user
    tasks_url = "https://jsonplaceholder.typicode.com/todos/"
    todos = requests.get(tasks_url)
    todos_tasks = todos.json()

    # Create the list of dict with values to export to json
    all_users_tasks_dict = {
        user["id"]: [
            {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in todos_tasks
            if task["userId"] == user["id"]
        ]
        for user in users_list
    }

    # Export data to a csv file
    with open("todo_all_employees.json", "w") as f:
        json.dump(all_users_tasks_dict, f)
