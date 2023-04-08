#!/usr/bin/python3
"""
    This module gathers some fake data from a REST API
"""
import requests
import sys
import csv

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
            taskList.append([
                empID, empUsr,
                str(tsk['completed']),
                tsk['title']
            ])

        with open("2.csv", "w", newline='') as f:
            writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerows(taskList)

    except SyntaxError:
        print("USAGE: ./1-export_to_CSV.py <employee ID>")
