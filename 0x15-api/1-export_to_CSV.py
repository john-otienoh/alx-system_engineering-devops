#!/usr/bin/python3
"""Returns to-do list info for a given employee ID and converts to csv"""
import csv
import requests
import sys

if __name__ == "__main__":
    i_d = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(i_d)).json()
    todos = requests.get(url + "todos", params={"userId": i_d}).json()

    completed = [i.get("title") for i in todos if i.get("completed") is True]
    with open(f"{i_d}.csv", "w", newline="") as csvfile:
        mywriter = csv.writer(csvfile)
        info = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        mywriter.writerow(info)
        for i in todos:
            n = user.get('username')
            mywriter.writerow([i_d, n, i["completed"], i["title"]])
