import json

with open('people.json') as json_data:
    details = json.load(json_data)
user_data = details['State']['Resident']
print(user_data[0])