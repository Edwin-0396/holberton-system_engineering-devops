#!/usr/bin/python3
"""script to export data in the JSON format."""

if __name__ == "__main__":
	import json

	import requests
	import sys

	USER_ID = sys.argv[1]

	todos = requests.get(f'https://jsonplaceholder.typicode.com/todos')
	users = requests.get(f'https://jsonplaceholder.typicode.com/users/{USER_ID}')
	

	USERNAME = users_Json['username']
	# Data to be written
	json_list = []
	json_dict = {}

	
	for items in todos_Json:
		Uid = items['userId']
		if (Uid == int(USER_ID)):
				TASK_COMPLETED_STATUS = items['completed']
				TASK_TITLE = items['title']
				dictionary = { "task": TASK_TITLE, "completed": TASK_COMPLETED_STATUS,"username": USERNAME,}
				json_list.append(dictionary)
				json_dict[f'{USER_ID}'] = json_list
	with open('json_data.json', 'w') as outfile:
		json.dump(json_dict, outfile)
	



	
		
