#!/usr/bin/python3
""" script to get the details of an employee task completion status
    and export to a csv file, using userId as the csv file name
"""
import csv
import requests
import sys


def export_employee_todo_status_to_csv(userId):
    """ gets the todo progress and export to csv """
    url = "https://jsonplaceholder.typicode.com/"
    todos = requests.get(url + "todos", params={"userId": userId}).json()
    user = requests.get(url + f"users/{userId}").json()
    name = user.get("name")

    with open(f'{userId}.csv', "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([userId, name, t.get("completed"), t.get("title")])


if __name__ == "__main__":
    userId = sys.argv[1]
    export_employee_todo_status_to_csv(userId)
