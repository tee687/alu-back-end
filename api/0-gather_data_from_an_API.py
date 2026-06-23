#!/usr/bin/python3
"""
Fetches and displays an employee's TODO list progress using a REST API.
"""
import sys

import requests


def get_todo_progress(employee_id):
    """Fetches user and todo data from API and prints progress."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list for the employee
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate task metrics
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(completed_tasks)

    # Print the first line summary
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    # Print the titles of completed tasks with 1 tab and 1 space
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            emp_id = int(sys.argv[1])
            get_todo_progress(emp_id)
        except ValueError:
            pass
