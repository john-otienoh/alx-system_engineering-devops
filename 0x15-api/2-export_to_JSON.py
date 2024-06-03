#!/usr/bin/python3
"""Returns to-do list info for a given employee ID and converts to json"""
import json
import requests
import sys

if __name__ == "__main__":
    i_d = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(i_d)).json()
    todos = requests.get(url + "todos", params={"userId": i_d}).json()
    n = user.get('username')

    completed = [i.get("title") for i in todos if i.get("completed") is True]
    data = {i_d: []}
    for i in todos:
        data[i_d].append({
            "task": i["title"],
            "completed": i["completed"],
            "username": n
        })
    with open(f"{i_d}.json", "w") as jsonfile:
        json.dump(data, jsonfile)
