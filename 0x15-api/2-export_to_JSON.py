#!/usr/bin/python3
""" Write a Python script that, using this REST API, for a given employee ID
    returns information about his/her TODO list progress."""
import json
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
    task_data = [
        {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": USER_DATA["username"],
        }
        for todo in TODO_DATA
    ]
    with open(f"{u_id}.json", "w") as jsonfile:
        json.dump({u_id: task_data}, jsonfile)


if __name__ == "__main__":
    # Check if the script is provided with an employee ID
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)
    EMPLOYEE_ID = sys.argv[1]
    fetch_employee_todo_progress(EMPLOYEE_ID)
