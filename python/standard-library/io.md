```python
import io

# Creating an in-memory buffer
buf = io.BytesIO()

# Writing to an in-memory buffer
buf.write(b'Hello world!')
print(buf.getvalue())  # b'Hello world!'

# Creating a text buffer
text_buf = io.StringIO()

# Writing to a text buffer
text_buf.write('Hello world!')
print(text_buf.getvalue())  # 'Hello world!'

# Reading from a file
with open('example.txt', 'r') as f:
    print(f.read())

# Reading from an in-memory buffer
buf = io.BytesIO(b'Hello world!')
print(buf.read())  # b'Hello world!'

# Reading from a text buffer
text_buf = io.StringIO('Hello world!')
print(text_buf.read())  # 'Hello world!'

# Redirecting stdout to a file
with open('output.txt', 'w') as f:
    with io.redirect_stdout(f):
        print('Hello world!')

# Using a custom stream for input
class MyStream(io.RawIOBase):
    def read(self, size=-1):
        return b'Hello world!'

with io.TextIOWrapper(MyStream()) as f:
    print(f.read())

# Reading lines from a file
with open('example.txt', 'r') as f:
    for line in f:
        print(line)

# Reading lines from a text buffer
text_buf = io.StringIO('Hello\nworld\n')
for line in text_buf:
    print(line.strip())

# Reading CSV data from a file
import csv

with open('example.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Writing CSV data to a file
with open('example.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['John', '25'])
    writer.writerow(['Jane', '30'])
```
