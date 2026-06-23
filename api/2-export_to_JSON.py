#!/usr/bin/python3
"""
Exports an employee's TODO list data to a JSON file.
"""
import json
import sys

import requests


def export_to_json(employee_id):
    """Fetches user and todo details and writes records to a JSON file."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data to retrieve the username field
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch all tasks belonging to the employee
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Structure data to match requirements
    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data_to_export = {str(employee_id): tasks_list}
    filename = "{}.json".format(employee_id)

    # Write dictionary to JSON file
    with open(filename, mode='w') as json_file:
        json.dump(data_to_export, json_file)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            emp_id = int(sys.argv[1])
            export_to_json(emp_id)
        except ValueError:
            pass
