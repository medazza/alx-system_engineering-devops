#!/usr/bin/python3
""" Write a Python script that, using this REST API, for a given employee ID
    returns information about his/her TODO list progress."""
import requests
import sys


def fetch_employee_todo_progress(empId):
    if empId == 0:
        sys.exit(1)
    # API endpoint for fetching user data
    USER_URL = f'https://jsonplaceholder.typicode.com/users/{empId}'
    # API endpoint for fetching TODO data
    TODO_URL = f'https://jsonplaceholder.typicode.com/todos?userId={empId}'

    # Fetching user data
    USER_RESPONSE = requests.get(USER_URL)
    if USER_RESPONSE.status_code != 200:
        print("Error: Unable to fetch user data")
        sys.exit(1)
    USER_DATA = USER_RESPONSE.json()
    # Fetching TODO data
    TODO_RESPONSE = requests.get(TODO_URL)
    if TODO_RESPONSE.status_code != 200:
        print("Error: Unable to fetch todos data")
        sys.exit(1)
    TODO_DATA = TODO_RESPONSE.json()
    # Extracting relevant information
    EMPLOYEE_NAME = USER_DATA.get('name')
    TOTAL_TASKS = len(TODO_DATA)
    DONE_TASKS = [task for task in TODO_DATA if task.get('completed') is True]

    # Displaying the progress
    print(f"Employee {EMPLOYEE_NAME} is done with "
          f"tasks({len(DONE_TASKS)}/{TOTAL_TASKS}):")

    # Displaying titles of completed tasks
    for task in DONE_TASKS:
        print(f"\t{task.get('title')}")


if __name__ == "__main__":
    # Check if the script is provided with an employee ID
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    EMPLOYEE_ID = int(sys.argv[1])
    fetch_employee_todo_progress(EMPLOYEE_ID)
