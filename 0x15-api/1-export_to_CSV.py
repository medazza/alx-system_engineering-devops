#!/usr/bin/python3
"""Python script to export data in the CSV format."""
import csv
import requests
import sys


def export_to_csv(user_id):
    b_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{b_url}users/{user_id}").json()
    todoData = requests.get(f"{b_url}todos", params={"userId": user_id}).json()

    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todoData:
            writer.writerow(
                [user_id, user["username"], todo["completed"], todo["title"]]
            )


if __name__ == "__main__":
    user_id = sys.argv[1]
    export_to_csv(user_id)
