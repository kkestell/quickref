# Comments start with a hash symbol

# Variables can be assigned using =
x = 5
y = "Hello, world!"

# Basic data types include numbers, strings, and booleans
num = 10
string = "This is a string"
boolean = True

# Arithmetic operators include +, -, *, /, and %
result = 10 + 5     # 15
result = 10 - 5     # 5
result = 10 * 5     # 50
result = 10 / 5     # 2.0
result = 10 % 3     # 1

# Comparison operators include ==, !=, >, >=, <, and <=
result = 10 == 5    # False
result = 10 != 5    # True
result = 10 > 5     # True
result = 10 >= 5    # True
result = 10 < 5     # False
result = 10 <= 5    # False

# Logical operators include and, or, and not
result = True and False  # False
result = True or False   # True
result = not True        # False

# if-elif-else statements
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")

# for loops
for i in range(5):
    print(i)

# while loops
i = 0
while i < 5:
    print(i)
    i += 1

# Lists can be created with []
my_list = [1, 2, 3]

# Dictionaries can be created with {}
my_dict = {'name': 'Alice', 'age': 30}

# Accessing elements of lists and dictionaries
print(my_list[0])          # 1
print(my_dict['name'])     # 'Alice'

# Adding elements to lists and dictionaries
my_list.append(4)
my_dict['city'] = 'New York'

# Functions can be defined with def
def my_function(param1, param2):
    return param1 + param2

# Functions can have default arguments
def my_function(param1, param2=10):
    return param1 + param2

# Classes can be defined with class
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
