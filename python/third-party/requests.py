import requests

# Sending a GET request
response = requests.get('http://example.com')
print(response.status_code)     # Output: 200
print(response.text)            # Output: HTML content of the page

# Sending a POST request with data
data = {'name': 'Alice', 'age': 30}
response = requests.post('http://example.com', data=data)
print(response.status_code)     # Output: 200
print(response.text)            # Output: HTML content of the page

# Sending a POST request with JSON data
import json

data = {'name': 'Alice', 'age': 30}
json_data = json.dumps(data)
response = requests.post('http://example.com', data=json_data, headers={'Content-Type': 'application/json'})
print(response.status_code)     # Output: 200
print(response.text)            # Output: HTML content of the page

# Sending a GET request with query parameters
params = {'q': 'Python', 'page': 2}
response = requests.get('http://example.com/search', params=params)
print(response.url)             # Output: http://example.com/search?q=Python&page=2

# Sending a request with headers
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get('http://example.com', headers=headers)
print(response.status_code)     # Output: 200

# Sending a request with authentication
auth = ('username', 'password')
response = requests.get('http://example.com', auth=auth)
print(response.status_code)     # Output: 200

