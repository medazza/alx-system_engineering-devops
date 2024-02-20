#!/usr/bin/python3
'''
    Python script that returns information using REST API
'''
import requests
import sys


def FETCH_EMPLOYEE_TODO_PROGRESS(empId):
    if empId == 0:
        sys.exit(1)
    # API endpoint for fetching user data
    USER_URL = f'https://jsonplaceholder.typicode.com/users/{empId}'
    # API endpoint for fetching TODO data
    TODO_URL = f'https://jsonplaceholder.typicode.com/todos?userId={empId}'

    # Fetching user data
    USER_RESPONSE = requests.get(USER_URL)
    USER_DATA = USER_RESPONSE.json()

    # Fetching TODO data
    TODO_RESPONSE = requests.get(TODO_URL)
    TODO_DATA = TODO_RESPONSE.json()

    # Extracting relevant information
    EMPLOYEE_NAME = USER_DATA['name']
    TOTAL_TASKS = len(TODO_DATA)
    COMPLETED_TASKS = [task for task in TODO_DATA if task['completed']]

    # Displaying the progress
    print(f"Employee {EMPLOYEE_NAME} is done with "
          f"tasks({len(COMPLETED_TASKS)}/{TOTAL_TASKS}):")

    # Displaying titles of completed tasks
    for task in COMPLETED_TASKS:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    # Check if the script is provided with an employee ID
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    EMPLOYEE_ID = int(sys.argv[1])
    FETCH_EMPLOYEE_TODO_PROGRESS(EMPLOYEE_ID)
