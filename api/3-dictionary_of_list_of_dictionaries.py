#!/usr/bin/python3
"""
Script to export data in the JSON format.
"""


if __name__ == "__main__":
    import requests
    import json
    
    link = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{link}/users")
    users = users.json()
    result = {}
    for user in users:
        todos = requests.get(
            f"{link}/todos?userId={user["id"]}"
        )
        todos = todos.json()
        result[user["id"]] = []
        for todo in todos:
            result[user["id"]].append(
                {
                    "username": user["username"],
                    "task": todo["title"],
                    "completed": todo["completed"],
                }
            )
    with open("todo_all_employees.json", "w") as result_file:
        json.dump(result, result_file)
