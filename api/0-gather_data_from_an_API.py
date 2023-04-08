#!/usr/bin/python3
"""
    This module gathers some fake data from a REST API
"""
import requests
import sys

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise SyntaxError

        empID = sys.argv[1]
        empData = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{empID}")
        empName = empData.json()['name']

        tasks = requests.get(
            "https://jsonplaceholder.typicode.com"
            f"/todos/?userId={empID}").json()

        completedTasks = 0
        completedList = []
        for tsk in tasks:
            if tsk['completed']:
                completedTasks += 1
                completedList.append(tsk['title'])

        print(f"Employee {empName} is done with"
              f" tasks({completedTasks}/{len(tasks)}):")
        for tsk in completedList:
            print(f"\t{tsk}")

    except SyntaxError:
        print("USAGE: ./0-gather_data_from_an_API.py <employee ID>")
