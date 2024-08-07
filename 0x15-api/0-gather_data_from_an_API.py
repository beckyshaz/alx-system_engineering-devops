#!/usr/bin/python3
"""using requests module to retrive data using api"""

import requests as req
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    resp = req.get(url).json()
    name = resp.get("name")

    url_do = "https://jsonplaceholder.typicode.com/users/{}/todos"\
        .format(user_id)
    todos = req.get(url_do).json()

    total = len(todos)

    count = 0

    for todo in todos:
        if todo.get("completed") is True:
            count += 1
    print(f"Employee {name} is done with tasks({count}/{total}):")

    for todo in todos:
        if todo.get("completed") is True:
            print(f"\t {todo.get('title')}")
