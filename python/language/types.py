# Determine the type of an object
x = 5
print(type(x))      # Output: <class 'int'>

# Convert between types
x = "5"
y = int(x)
print(y)            # Output: 5

x = 3.14
y = int(x)
print(y)            # Output: 3

x = "3.14"
y = float(x)
print(y)            # Output: 3.14

# Check if an object is an instance of a certain type
x = 5
print(isinstance(x, int))   # Output: True
print(isinstance(x, float)) # Output: False

# Check if an object is of a certain type
x = 5
print(type(x) == int)   # Output: True
print(type(x) == float) # Output: False

# Check if an object is a subclass of a certain type
class A:
    pass

class B(A):
    pass

b = B()
print(issubclass(B, A))  # Output: True
print(issubclass(A, B))  # Output: False

# Create a custom type
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(person.name)  # Output: Alice
print(person.age)   # Output: 30

