#!/usr/bin/python3
"""
    This module gathers some fake data from a REST API
"""
import requests
import sys
import json

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise SyntaxError

        empID = sys.argv[1]
        empData = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{empID}")
        empUsr = empData.json()['username']

        tasks = requests.get(
            "https://jsonplaceholder.typicode.com"
            f"/todos/?userId={empID}").json()

        taskList = []
        for tsk in tasks:
            taskList.append(
                {"task": tsk['title'],
                 "completed": tsk['completed'],
                 "username": empUsr}
                )

        dictionary = {str(empID): taskList}

        with open("2.json", "w", encoding="utf-8") as f:
            json.dump(dictionary, f)

    except SyntaxError:
        print("USAGE: ./2-export_to_JSON.py <employee ID>")
