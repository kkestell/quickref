```python
import pathlib

# Path objects can be created with strings
path = pathlib.Path('/etc/hosts')

# You can join path segments with / or with the / operator
path = pathlib.Path('/etc') / 'hosts'
path = pathlib.Path('/etc').joinpath('hosts')

# You can also create a Path object from a relative path
path = pathlib.Path('file.txt')

# Path objects are very flexible, they can represent files or directories
path = pathlib.Path('/etc')
path = pathlib.Path('/etc/passwd')
path = pathlib.Path('~/Documents/myfile.txt')

# Path objects have many attributes
path = pathlib.Path('/etc/hosts')
path.name  # 'hosts'
path.parent  # '/etc'
path.suffix  # '.txt'
path.suffixes  # [] because this is not a file with an extension
path.stem  # 'hosts'

# You can check if a path exists
path = pathlib.Path('/etc/hosts')
path.exists()  # True

# Check if a path is a file or a directory
path.is_file()  # True
path.is_dir()  # False

# List all the files and directories in a directory
path = pathlib.Path('/etc')
list(path.iterdir())

# Recursive directory listing
list(pathlib.Path('/etc').glob('**/*.conf'))

# You can check if two paths are equivalent
path1 = pathlib.Path('/etc')
path2 = pathlib.Path('/private/etc')
path1.samefile(path2)  # False

# Get the absolute path
path = pathlib.Path('~/Documents/myfile.txt')
path.absolute()

# Create a new directory
pathlib.Path('/tmp/newdir').mkdir()

# Create a new file and write some text to it
with open('myfile.txt', 'w') as f:
    f.write('Hello world!')
pathlib.Path('myfile.txt').touch()

# Read the contents of a file
path = pathlib.Path('myfile.txt')
with path.open() as f:
    contents = f.read()
print(contents)

# Rename a file
path = pathlib.Path('myfile.txt')
path.rename('newfile.txt')

# Delete a file or a directory
pathlib.Path('newfile.txt').unlink()
pathlib.Path('/tmp/newdir').rmdir()

# Copy a file
pathlib.Path('source.txt').copy2('destination.txt')

# Move a file or a directory
pathlib.Path('source.txt').replace('destination.txt')

# Globbing
list(pathlib.Path('/etc').glob('*.conf'))
list(pathlib.Path('/etc').rglob('*.conf'))
```
