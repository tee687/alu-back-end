#!/usr/bin/python3
"""
Exports TODO list data of all employees to a single JSON file.
"""
import json

import requests


def export_all_to_json():
    """Fetches all users and tasks, then exports them to a JSON file."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users_response = requests.get("{}/users".format(base_url))
    users_data = users_response.json()

    # Fetch all tasks
    todos_response = requests.get("{}/todos".format(base_url))
    todos_data = todos_response.json()

    # Create a dictionary map of user_id to username
    user_map = {user.get("id"): user.get("username") for user in users_data}

    # Initialize the target storage dictionary format
    all_employees_data = {str(u_id): [] for u_id in user_map.keys()}

    # Populate tasks list inside the dictionary
    for task in todos_data:
        user_id = task.get("userId")
        if user_id in user_map:
            all_employees_data[str(user_id)].append({
                "username": user_map[user_id],
                "task": task.get("title"),
                "completed": task.get("completed")
            })

    # Save dictionary out to the required target file name
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as json_file:
        json.dump(all_employees_data, json_file)


if __name__ == "__main__":
    export_all_to_json()
