#!/usr/bin/python3
"""
    This module gathers some fake data from a REST API
"""
import json
import requests
import sys

if __name__ == "__main__":

    empData = requests.get(
        f"https://jsonplaceholder.typicode.com/users/")\
        .json()

    dictionary = {}

    for emp in empData:
        tasks = requests.get(
            "https://jsonplaceholder.typicode.com"
            f"/todos/?userId={emp['id']}").json()

        taskList = []
        for tsk in tasks:
            taskList.append(
                {"username": emp['username'],
                 "task": tsk['title'],
                 "completed": tsk['completed']}
            )

        dictionary.update({str(emp['id']): taskList})

    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        json.dump(dictionary, f)
