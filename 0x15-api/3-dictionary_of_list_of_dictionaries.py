#!/usr/bin/python3
""" script to get the details of an employee task completion status """
import json
import requests


def all_employee_todo_status_to_json():
    """ gets the todo progress for all and export details to json"""
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/").json()

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump({user.get("id"): [{
            "username": user.get('username'),
            "task": t.get("title"),
            "completed": t.get("completed")
            } for t in requests.get(url + "todos",
                                    params={"userId": user.get("id")}).json()]
            for user in users}, jsonfile)


if __name__ == "__main__":
    all_employee_todo_status_to_json()
