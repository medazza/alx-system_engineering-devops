#!/usr/bin/python3
""" Write a Python script that, using this REST API, for a given employee ID
    export data in the CSV format."""
import csv
import requests
import sys


def fetch_employee_todo_progress(empId):
    if empId == 0:
        sys.exit(1)
    base_url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(f"{base_url}users/{empId}").json()
    todo_data = requests.get(f"{base_url}todos", params={"userId": empId}).json()

    # Extract relevant information
    employee_name = user_data.get('name')

    # Exporting to CSV FILE
    with open(f"{empId}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todo_data:
            writer.writerow(
                [empId, employee_name, todo["completed"], todo["title"]]
            )


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
