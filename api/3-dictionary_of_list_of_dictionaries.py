#!/usr/bin/python3
"""
Exports TODO list data of all employees to a single JSON file.
"""
import json

import requests


def export_all_to_json():
    """Fetches all users and their tasks, exporting them into a JSON file."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all users to map user IDs to usernames
    users_response = requests.get("{}/users".format(base_url))
    users_data = users_response.json()

    # Fetch all todo tasks across the platform
    todos_response = requests.get("{}/todos".format(base_url))
    todos_data = todos_response.json()

    # Create a quick dictionary lookup mapping userId -> username
    user_map = {user.get("id"): user.get("username") for user in users_data}

    # Structure data to match: { "USER_ID": [ {"username":..., "task":..., "completed":...}, ... ] }
    all_employees_data = {str(user_id): [] for user_id in user_map.keys()}

    for task in todos_data:
        user_id = task.get("userId")
        if user_id in user_map:
            all_employees_data[str(user_id)].append({
                "username": user_map[user_id],
                "task": task.get("title"),
                "completed": task.get("completed")
            })

    # Save dictionary to the target output json file
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as json_file:
        json.dump(all_employees_data, json_file)


if __name__ == "__main__":
    export_all_to_json()
