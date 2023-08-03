#!/usr/bin/python3
""" script to get the details of an employee task completion status """
import json
import requests
import sys


def export_employee_todo_status_to_json(userId):
    """ gets the todo progress and export details to json"""
    url = "https://jsonplaceholder.typicode.com/"
    todos = requests.get(url + "todos", params={"userId": userId}).json()
    user = requests.get(url + f"users/{userId}").json()
    name = user.get("username")

    with open(f'{userId}.json', 'w') as jsonfile:
        json.dump({userId: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": name} for t in todos]}, jsonfile)


if __name__ == "__main__":
    userId = sys.argv[1]
    export_employee_todo_status_to_json(userId)
