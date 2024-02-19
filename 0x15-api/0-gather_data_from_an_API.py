#!/usr/bin/python3
""" Write a Python script that, using this REST API, for a given employee ID
    returns information about his/her TODO list progress."""
import requests
import sys


def fetch_employee_todo_progress(empId):
    if empId == 0:
        sys.exit(1)
    # API endpoint for fetching user data
    user_url = f'https://jsonplaceholder.typicode.com/users/{empId}'
    # API endpoint for fetching TODO data
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={empId}'

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch TODO data
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Extract relevant information
    employee_name = user_data['name']
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task['completed']]

    # Display the progress
    print(f"Employee {employee_name} is done with "
          f"tasks({len(completed_tasks)}/{total_tasks}):")

    # Display titles of completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    # Check if the script is provided with an employee ID
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
