#!/usr/bin/python3
"""script to export data in the JSON format."""

if __name__ == "__main__":
    import json
    import requests

    json_list = []
    json_dict = {}

    users = requests.get('https://jsonplaceholder.typicode.com/users')
    users_Json = users.json()
    todos = requests.get(f'https://jsonplaceholder.typicode.com/todos')
    todos_Json = todos.json()
    for items_users in users_Json:
        ID = int(items_users['id'])

        for items_todos in todos_Json:
            USER_ID = items_todos['userId']
            if (ID == int(USER_ID)):
                USERNAME = items_users['username']
                TASK_TITLE = items_todos['title']
                TASK_COMPLETED_STATUS = items_todos['completed']
                dictionary = {"username": USERNAME, "task": TASK_TITLE,
                              "completed": TASK_COMPLETED_STATUS}
                json_list.append(dictionary)
        json_dict[ID] = json_list
        json_list = []
    with open('json_data.json', 'w') as outfile:
        json.dump(json_dict, outfile)
