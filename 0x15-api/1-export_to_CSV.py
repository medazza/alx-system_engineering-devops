#!/usr/bin/python3
""" Write a Python script that, using this REST API, for a given employee ID
    returns information about his/her TODO list progress."""
import csv
import requests
import sys


def fetch_employee_todo_progress(u_id):
    if u_id == 0:
        sys.exit(1)
    # base url
    b_url = "https://jsonplaceholder.typicode.com/"
    # API endpoint for fetching user data
    USER_DATA = requests.get(f"{b_url}users/{u_id}").json()
    # API endpoint for fetching TODO data
    TODO_DATA = requests.get(f"{b_url}todos", params={"userId": u_id}).json()

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
    EMPLOYEE_ID = sys.argv[1]
    fetch_employee_todo_progress(EMPLOYEE_ID)
