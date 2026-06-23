#!/usr/bin/python3
"""
Exports an employee's TODO list data to a CSV file.
"""
import csv
import sys

import requests


def export_to_csv(employee_id):
    """Fetches user and todo details and writes records to a CSV file."""
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

    # Generate file name dynamically based on employee ID
    filename = "{}.csv".format(employee_id)

    # Open CSV file with specific quotation rules matching the format requirements
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            emp_id = int(sys.argv[1])
            export_to_csv(emp_id)
        except ValueError:
            pass
