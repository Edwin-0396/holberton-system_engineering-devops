#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

if __name__ == "__main__":
    import requests
    import sys

    ID = sys.argv[1]
    user_Id = ID
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    Title = []

    todos = requests.get(f'https://jsonplaceholder.typicode.com/todos')
    users = requests.get(f'https://jsonplaceholder.typicode.com/users/{ID}')
    todos_Json = todos.json()
    users_Json = users.json()

    EMPLOYEE_NAME = users_Json['name']

    for items in todos_Json:
        Uid = items['userId']
        if (Uid == int(user_Id)):
            if (items['completed']):
                Title.append(items['title'])
                NUMBER_OF_DONE_TASKS += 1
            if (items['completed'] or items['completed'] is False):
                TOTAL_NUMBER_OF_TASKS += 1

    print(
        f"Employee {EMPLOYEE_NAME} is done with tasks(\
{NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}): ")
    for title in Title:
        print(f"\t{title}")
