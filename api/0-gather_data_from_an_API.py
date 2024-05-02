#!/usr/bin/python3

"""
script that,
using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""


if __name__ == "__main__":

    import requests
    from sys import argv

    if len(argv) < 2:
        exit()
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}&completed=true"
    )
    name = requests.get(
        f"https://jsonplaceholder.typicode.com/users?id={argv[1]}"
    )
    name = name.json()
    name = name[0]["name"]
    todo = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}"
    )
    todo = todo.json()
    todo = len(todo)
    todos = todos.json()
    todo_list = []

    for x in todos:
        todo_list.append("\t {}".format(x["title"]))
    print(
        f"Employee {name} is done with tasks({len(todos)}/{ todo}):"
    )
    for y in todo_list:
        print(y)
