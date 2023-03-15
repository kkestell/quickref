import pickle

# Pickle an object
data = {"name": "Alice", "age": 30, "scores": [70, 80, 90]}
with open("data.pickle", "wb") as f:
    pickle.dump(data, f)

# Unpickle an object
with open("data.pickle", "rb") as f:
    data = pickle.load(f)
print(data)  # => {'name': 'Alice', 'age': 30, 'scores': [70, 80, 90]}

# Pickle multiple objects to the same file
data1 = {"name": "Bob", "age": 25}
data2 = {"name": "Charlie", "age": 35}
with open("data.pickle", "wb") as f:
    pickle.dump(data1, f)
    pickle.dump(data2, f)

# Unpickle multiple objects from the same file
with open("data.pickle", "rb") as f:
    data1 = pickle.load(f)
    data2 = pickle.load(f)
print(data1)  # => {'name': 'Bob', 'age': 25}
print(data2)  # => {'name': 'Charlie', 'age': 35}

# Pickle and unpickle a class instance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} ({self.age})"
        
person = Person("David", 40)

# Pickle the object
with open("person.pickle", "wb") as f:
    pickle.dump(person, f)

# Unpickle the object
with open("person.pickle", "rb") as f:
    person = pickle.load(f)
print(person)  # => David (40)

# Handle errors when unpickling
try:
    with open("data.pickle", "rb") as f:
        data = pickle.load(f)
except (EOFError, pickle.UnpicklingError):
    print("Error: Could not unpickle the object")