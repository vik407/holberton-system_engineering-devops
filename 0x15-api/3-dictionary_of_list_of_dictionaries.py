#!/usr/bin/python3
"""Python script that uses a REST API
"""
import json
import requests


def get_dump():
    """GET user todos at given id"""
    url = "https://jsonplaceholder.typicode.com/"
    endpoint_a = requests.get(url + "users/").json()
    endpoint_b = requests.get(url + "todos/").json()
    the_dict = {}

    for users in endpoint_a:
        the_users = []
        for tasks in endpoint_b:
            if users.get("id") == tasks.get("userId"):
                o = {}
                o["task"] = tasks.get("title")
                o["completed"] = tasks.get("completed")
                o["username"] = users.get("username")
                the_users.append(o)
        the_dict[users.get("id")] = the_users
    """Dump!"""
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(the_dict, json_file)

if __name__ == '__main__':
    """Excecute it"""
    get_dump()
