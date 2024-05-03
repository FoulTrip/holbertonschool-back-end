#!/usr/bin/python3
""""
Using what you did in the task #0, extend your Python script to export data in the JSON format.
"""
import json
import requests


if __name__ == "__main__":

    link = "https://jsonplaceholder.typicode.com"
    users_url = f"{link}/users"
    response = requests.get(users_url)

    user_data = response.json()

    allurl = f"{link}/todos"
    todo_response = requests.get(allurl)

    todos = todo_response.json()

    all_employees_data = {}

    for user in user_data:
        datas_exported = []
        user_id = user.get("id")
        user_name = user.get("username")
        for task in todos:
            if task["userId"] == user_id:
                data_to_export = {
                    "username": user_name,
                    "task": task["title"],
                    "completed": task["completed"],
                }
                datas_exported.append(data_to_export)

        all_employees_data[user_id] = datas_exported

    filename = "todo_all_employees.json"
    with open(filename, mode="w") as file:
        json.dump(all_employees_data, file)
