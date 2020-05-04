#!/usr/bin/python3
"""Python script that uses a REST API
"""
import requests
from sys import argv


def get_usr_todos(uid):
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
    total_tasks = len(data.get("tasks"))
    search_completed = [tsk for tsk in data.get("tasks")
                        if tsk.get("completed")]
    total_completed = len(search_completed)
    """Return global info"""
    print('Employee {} is done with tasks({}/{}):'
          .format(data.get('employee').get('name'),
                  total_completed, total_tasks))
    """Return each task"""
    for tasks in search_completed:
        print('\t {}'.format(tasks.get('title')))

if __name__ == '__main__':
    """Excecute it"""
    get_usr_todos(argv[1])
