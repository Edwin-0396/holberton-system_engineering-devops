#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress."""

if __name__ == "__main__":
    """Module to export to CSV"""
    import csv
    import requests
    import sys

    USER_ID = sys.argv[1]

    todos = requests.get(f'https://jsonplaceholder.typicode.com/todos')
    users = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{USER_ID}')
    todos_Json = todos.json()
    users_Json = users.json()

    USERNAME = users_Json['username']

    with open(f'{USER_ID}.csv', 'w', newline='') as csvfile:
        for items in todos_Json:
            Uid = items['userId']
            if (Uid == int(USER_ID)):
                TASK_COMPLETED_STATUS = items['completed']
                TASK_TITLE = items['title']
                spamwriter = csv.writer(
                    csvfile, delimiter=',', quotechar='|',
                    quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(
                    [f'"{USER_ID}"', f'"{USERNAME}"',
                     f'"{TASK_COMPLETED_STATUS}"', f'"{TASK_TITLE}"'])
