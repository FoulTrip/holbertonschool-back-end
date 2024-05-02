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
    todos = requests.get(f"{link}/todos?userId={argv[1]}")
    name = requests.get(f"{link}/users?id={argv[1]}")
    name = name.json()
    name = name[0]["username"]
    todos = todos.json()
    result = {}
    result[argv[1]] = []
    for todo in todos:
        result[argv[1]].append(
            {
                "task": todo["title"], 
                "completed": todo["completed"], 
                "username": name
            }
        )
    with open("{}.json".format(argv[1]), "w") as result_file:
        json.dump(result, result_file)
