import sqlite3

# Create a connection to a SQLite database
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE users
                  (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# Insert data into the table
cursor.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Charlie', 'charlie@example.com')")

# Commit changes to the database
conn.commit()

# Select data from the table
cursor.execute("SELECT * FROM users")

# Fetch one row at a time
row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()

# Fetch all rows at once
rows = cursor.fetchall()
for row in rows:
    print(row)

# Update data in the table
cursor.execute("UPDATE users SET email='newemail@example.com' WHERE name='Bob'")

# Delete data from the table
cursor.execute("DELETE FROM users WHERE name='Charlie'")

# Close the cursor and connection
cursor.close()
conn.close()
