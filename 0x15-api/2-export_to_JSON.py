#!/usr/bin/python3
"""Python script that uses a REST API
"""
import json
import requests
from sys import argv


def get_usr_tojson(uid):
    """GET user todos at given id"""
    url = "https://jsonplaceholder.typicode.com/"
    endpoint_a = "users/"
    endpoint_b = "todos?userId="

    """Employee Name"""
    query_employee = url + endpoint_a + uid
    employee = requests.get(query_employee).json()
    """Employee Tasks"""
    query_tasks = url + endpoint_b + uid
    tasks = requests.get(query_tasks).json()
    """Concatenate two responses"""
    data = {"employee": employee, "tasks": tasks}
    out = []
    employee_id = data.get("employee").get("id")
    for tsk in data.get("tasks"):
        o = {}
        o["task"] = tsk.get("title")
        o["completed"] = tsk.get("completed")
        o["username"] = data.get("employee").get("username")
        out.append(o)
    with open('{}.json'.format(uid), 'w') as json_file:
        json.dump({employee_id: out}, json_file)

if __name__ == '__main__':
    """Excecute it"""
    get_usr_tojson(argv[1])
