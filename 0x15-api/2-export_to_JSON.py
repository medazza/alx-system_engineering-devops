#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import json
import requests
import sys


def export_to_json(user_id):
    b_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{b_url}users/{user_id}").json()
    todos = requests.get(f"{b_url}todos", params={"userId": user_id}).json()

    data_task = [
        {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": user["username"],
        }
        for todo in todos
    ]

    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump({user_id: data_task}, jsonfile)


if __name__ == "__main__":
    user_id = sys.argv[1]
    export_to_json(user_id)
