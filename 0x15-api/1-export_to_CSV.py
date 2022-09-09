#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID, returns
information
"""
import csv
import requests
import sys


if __name__ == "__main__":
    USER_ID = sys.argv[1]

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID))
    todos_Json = todos.json()
    users_Json = users.json()

    USERNAME = users_Json['username']

    with open('{}.csv'.format(USER_ID), 'w', newline='') as csvfile:
        for items in todos_Json:
            Uid = items['userId']
            if (Uid == int(USER_ID)):
                TASK_COMPLETED_STATUS = items['completed']
                TASK_TITLE = items['title']
                spamwriter = csv.writer(
                    csvfile, delimiter=',', quotechar='|',
                    quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(
                    ['"{}"'.format(USER_ID), '"{}"'.format(USERNAME),
                     '"{}"'.format(TASK_COMPLETED_STATUS),
                     '"{}"'.format(TASK_TITLE)])
