#!/usr/bin/python3
"""
for a given employee ID, returns JSON
about his/her TODO list progress.
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    USER_ID = sys.argv[1]

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID))
    users_Json = users.json()
    todos_Json = todos.json()

    USERNAME = users_Json['username']
    json_list = []
    json_dict = {}

    for items in todos_Json:
        Uid = items['userId']
        if (Uid == int(USER_ID)):
            TASK_COMPLETED_STATUS = items['completed']
            TASK_TITLE = items['title']
            dictionary = {"task": TASK_TITLE,
                          "completed": TASK_COMPLETED_STATUS,
                          "username": USERNAME}
            json_list.append(dictionary)
            json_dict['{}'.format(USER_ID)] = json_list
    with open('{}.json'.format(USER_ID), 'w') as outfile:
        json.dump(json_dict, outfile)
