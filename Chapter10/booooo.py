import json

text = 'user_info.json'

with open(text, 'r') as file:
    name = json.load(file)
print(name)