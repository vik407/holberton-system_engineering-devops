#!/usr/bin/python3
"""Python script that uses a REST API
"""
import csv
import requests
from sys import argv


def get_usr_tocsv(uid):
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

    with open("{}.csv".format(uid), mode="w") as res:
        out = csv.writer(res, quoting=csv.QUOTE_ALL)
        employee_id = data.get("employee").get("id")
        employee_usr = data.get("employee").get("username")
        for o in data.get("tasks"):
            out.writerow([
                employee_id, employee_usr, o.get("completed"), o.get("title")
            ])

if __name__ == '__main__':
    """Excecute it"""
    get_usr_tocsv(argv[1])
