#!/usr/bin/python3
""" Write a Python script that, using this REST API, for a given employee ID
    returns information about his/her TODO list progress."""
import csv
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
    USER_ID = USER_DATA.get('id')
    TOTAL_TASKS = len(TODO_DATA)
    DONE_TASKS = [task for task in TODO_DATA if task.get('completed') is True]

    # Exporting to CSV
    CSV_FILE_NAME = f"{USER_ID}.csv"
    with open(CSV_FILE_NAME, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                      'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # Writing CSV header
        writer.writeheader()
        # Writing CSV rows
        for task in TODO_DATA:
            writer.writerow({
                'USER_ID': USER_ID,
                'USERNAME': EMPLOYEE_NAME,
                'TASK_COMPLETED_STATUS': task.get('completed'),
                'TASK_TITLE': task.get('title')
            })

    print(f"\nData exported to {CSV_FILE_NAME}")


if __name__ == "__main__":
    # Check if the script is provided with an employee ID
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    EMPLOYEE_ID = int(sys.argv[1])
    fetch_employee_todo_progress(EMPLOYEE_ID)
