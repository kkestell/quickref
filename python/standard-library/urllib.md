```python
import urllib.request
import urllib.parse

# Sending GET requests
url = 'https://www.example.com'
response = urllib.request.urlopen(url)
html = response.read()  # Returns the HTML content of the page

# Sending POST requests
url = 'https://www.example.com/post'
data = {'name': 'John', 'age': 30}
data = urllib.parse.urlencode(data)
data = data.encode('utf-8')  # Encodes the data as a UTF-8 byte string
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)

# Handling HTTP errors
try:
    response = urllib.request.urlopen('https://www.example.com/nonexistent')
except urllib.error.HTTPError as e:
    print(f'Error code: {e.code}, Error message: {e.reason}')

# Using headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)


```
