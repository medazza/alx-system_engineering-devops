#!/usr/bin/python3
""" Write a Python script that, using this REST API, for a given employee ID
    returns information about his/her TODO list progress."""
import requests
import sys


def fetchemployeetodoprogress(empId):
    if empId == 0:
        sys.exit(1)
    # API endpoint for fetching user data
    userurl = f'https://jsonplaceholder.typicode.com/users/%7BempId%7D'
    # API endpoint for fetching TODO data
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={empId}'

    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Unable to fetch user data")
        sys.exit(1)
    user_data = user_response.json()

    # Fetch TODO data
    todo_response = requests.get(todo_url)
    if todo_response.status_code != 200:
        print("Error: Unable to fetch todos data")
        sys.exit(1)
    todo_data = todo_response.json()

    # Extract relevant information
    employee_name = user_data.get('name')
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task.get('completed') is True]

    # Display the progress
    print(f"Employee {employee_name} is done with "
          f"tasks({len(completed_tasks)}/{total_tasks}):")

    # Display titles of completed tasks
    for task in completed_tasks:
        print(f"\t{task.get('title')}")


if __name == "__main":
    # Check if the script is provided with an employee ID
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
    fetch_employee_todo_progress(employee_id)
