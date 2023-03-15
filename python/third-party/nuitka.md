To use Nuitka to compile a Python application to a native executable, follow these steps:

Install Nuitka using pip:

```
pip install nuitka
```

Write your Python application code.

Create a Python entry point file for your application that imports and runs your application code.

Compile your application using Nuitka with the following command:

```console
$ python -m nuitka --standalone entry_point.py
```

This will generate a standalone executable for your application.

Here's an example:

Suppose you have a Python file myapp.py that contains your application code:

```python
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
```

Create a new file `entry_point.py` that imports and runs your `main()` function:

```python
from myapp import main

if __name__ == "__main__":
    main()
```

Compile your application using Nuitka with the following command:

```console
$ python -m nuitka --standalone entry_point.py
```

This will generate a standalone executable for your application that can be run on any system with the same architecture as your development machine.