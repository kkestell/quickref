```python
import os

# Get the current working directory
cwd = os.getcwd()
print(cwd)

# Change the current working directory
os.chdir('/path/to/new/dir')

# List the files and directories in a directory
dir_contents = os.listdir('/path/to/dir')
print(dir_contents)

# Create a directory
os.mkdir('/path/to/new/dir')

# Create a directory and any missing parent directories
os.makedirs('/path/to/new/dir')

# Remove a file
os.remove('/path/to/file')

# Rename a file
os.rename('/path/to/old/file', '/path/to/new/file')

# Check if a file or directory exists
if os.path.exists('/path/to/file/or/dir'):
    print('Exists')

# Check if a path is a file
if os.path.isfile('/path/to/file'):
    print('Is a file')

# Check if a path is a directory
if os.path.isdir('/path/to/dir'):
    print('Is a directory')

# Get the size of a file
file_size = os.path.getsize('/path/to/file')
print(file_size)

# Get the last modified time of a file
last_modified = os.path.getmtime('/path/to/file')
print(last_modified)

# Check the permissions of a file or directory
permissions = os.stat('/path/to/file/or/dir').st_mode
print(permissions)

# Set the permissions of a file or directory
os.chmod('/path/to/file/or/dir', 0o755)

# Execute a command in the shell
os.system('ls -l')

```
