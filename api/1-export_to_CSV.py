#!/usr/bin/python3
"""
Script to export data in the CSV format.
"""


if __name__ == "__main__":

    import csv
    import requests
    from sys import argv

    link = "https://jsonplaceholder.typicode.com"

    if len(argv) < 2:
        exit()
    todos = requests.get(f"{link}/todos?userId={argv[1]}")
    name = requests.get(f"{link}/users?id={argv[1]}")
    name = name.json()
    name = name[0]["username"]
    todos = todos.json()
    file_name = "{}.csv".format(argv[1])
    with open(file_name, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([argv[1], name, todo["completed"], todo["title"]])
