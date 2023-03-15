import json

# Encoding and decoding JSON
data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_str = json.dumps(data)  # Converts a Python dictionary to a JSON string
data_dict = json.loads(json_str)  # Converts a JSON string to a Python dictionary

# Writing and reading JSON files
with open('data.json', 'w') as f:
    json.dump(data, f)  # Writes a Python dictionary to a JSON file

with open('data.json', 'r') as f:
    data_dict = json.load(f)  # Reads a JSON file and returns a Python dictionary

# Handling JSON errors
try:
    data_dict = json.loads('{"name": "John", "age": 30,}')  # Raises a ValueError because of the trailing comma
except ValueError as e:
    print(f'Error decoding JSON: {e}')
