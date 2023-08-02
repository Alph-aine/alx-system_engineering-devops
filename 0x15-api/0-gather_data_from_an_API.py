#!/usr/bin/python3
""" script to get the details of an employee task completion status """
import requests
import sys


def get_employee_todo_status(userId):
    """ gets the todo progress """
    url = "https://jsonplaceholder.typicode.com/"
    todos = requests.get(url + "todos", params={"userId": userId}).json()
    user = requests.get(url + f"users/{userId}").json()

    name = user.get("name")
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks ({}/{}):".format(
        name, len(completed), len(todos)))
    for c in completed:
        print("\t {}".format(c))


if __name__ == "__main__":
    userId = sys.argv[1]
    get_employee_todo_status(userId)
