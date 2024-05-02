#!/usr/bin/python3
"""
Script to export data in the JSON format.
"""


if __name__ == "__main__":

    import requests
    from sys import argv
    import json

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
    with open(f"{user_id}.json", "w") as result_file:
        json.dump(result, result_file)
