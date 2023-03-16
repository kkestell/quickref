```python
import csv

# Reading CSV files
with open('file.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        print(', '.join(row))

# Writing CSV files
with open('file.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"')
    writer.writerow(['Name', 'Age', 'Email'])
    writer.writerow(['Alice', '30', 'alice@example.com'])
    writer.writerow(['Bob', '35', 'bob@example.com'])

# Reading CSV files with a header row
with open('file.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'], row['Age'], row['Email'])

# Writing CSV files with a header row
with open('file.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'Alice', 'Age': '30', 'Email': 'alice@example.com'})
    writer.writerow({'Name': 'Bob', 'Age': '35', 'Email': 'bob@example.com'})


```
