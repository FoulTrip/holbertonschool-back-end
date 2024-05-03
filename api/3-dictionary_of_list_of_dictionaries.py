#!/usr/bin/python3
"""
Script to export data in the JSON format.
"""


if __name__ == "__main__":

    import requests
    from sys import argv
    import json
    import os

    link = "https://jsonplaceholder.typicode.com"

    if len(argv) < 2:
        exit()
    user_id = argv[1]
    todos = requests.get(f"{link}/todos?userId={user_id}")
    user_info = requests.get(f"{link}/users?id={user_id}")
    name = user_info.json()[0]["username"]
    todos = todos.json()
    result = {}
    result[user_id] = []
    for todo in todos:
        result[user_id].append(
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": name,
            }
        )

    currentDirectory = os.path.dirname(os.path.realpath(__file__))

    json_file_path = os.path.join(currentDirectory, "todo_all_employees.json")

    with open(json_file_path, "w") as result_file:
        json.dump(result, result_file)

    with open(json_file_path, "r") as f:
        data = f.read()
