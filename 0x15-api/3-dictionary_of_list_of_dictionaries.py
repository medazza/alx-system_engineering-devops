#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import json
import requests


def fetch_all_employee_data():
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(f"{base_url}users").json()

    all_employee_data = {
        user["id"]: [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user["username"],
            }
            for todo in requests.get(
                f"{base_url}todos", params={"userId": user["id"]}
            ).json()
        ]
        for user in users
    }

    return all_employee_data


if __name__ == "__main__":
    all_employee_data = fetch_all_employee_data()
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_employee_data, jsonfile)
