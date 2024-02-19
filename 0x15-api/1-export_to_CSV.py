#!/usr/bin/python3
""" Write a Python script that, using this REST API, for a given employee ID
    export data in the CSV format."""
import csv
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
    user_id = user_data.get('id')
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task.get('completed') is True]

    # Exporting to CSV
    CSV_FILE_NAME = f"{user_id}.csv"
    with open(CSV_FILE_NAME, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                      'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Writing CSV header
        writer.writeheader()

        # Writing CSV rows
        for task in todo_data:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': 'TRUE' if task['completed']
                else 'FALSE',
                'TASK_TITLE': task['title']
            })

    print(f"\nData exported to {CSV_FILE_NAME}")


if __name__ == "__main__":
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
