#!/usr/bin/python3
"""Export data from employees information to CSV file"""

import csv
import requests
from sys import argv

if __name__ == "__main__":

    # Get user name related to id
    user_api_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        argv[1])
    user = requests.get(user_api_url)
    employee_name = user.json().get('username')
    id = user.json().get('id')

    # Get tasks from user
    tasks_url = "https://jsonplaceholder.typicode.com/users/{}/todos/".format(
        argv[1])
    todos = requests.get(tasks_url)
    todos_tasks = todos.json()

    # Export data to a csv file
    csv_file = "{}.csv".format(argv[1])
    with open(csv_file, "w") as csv_obj:
        csv_writer = csv.writer(csv_obj, delimiter=",", quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for item in todos_tasks:
            csv_writer.writerow([argv[1], employee_name,
                                item.get('completed'), item.get('title')])
    csv_obj.close()
