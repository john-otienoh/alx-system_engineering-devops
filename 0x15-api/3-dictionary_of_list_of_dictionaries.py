#!/usr/bin/python3
"""Returns to-do list info for a given employee ID and converts to json"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + ' users').json()
    data = []
    for i in users:
        td = requests.get(url + "todos", params={"userId": i.get('id')}).json()
        for t in td:
            data[i.get('id')].append({
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": i.get('username'),
            })
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
