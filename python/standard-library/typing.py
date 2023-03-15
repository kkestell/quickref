from typing import List, Tuple, Dict, Any, Union

# Define types for function arguments and return values
def greeting(name: str) -> str:
    return "Hello, " + name + "!"

print(greeting("Alice"))    # Output: Hello, Alice!

# Define types for lists
def sum_values(values: List[int]) -> int:
    return sum(values)

print(sum_values([1, 2, 3]))    # Output: 6

# Define types for tuples
def get_name_and_age() -> Tuple[str, int]:
    return ("Alice", 30)

name, age = get_name_and_age()
print(name)     # Output: Alice
print(age)      # Output: 30

# Define types for dictionaries
def get_person() -> Dict[str, Any]:
    return {"name": "Alice", "age": 30}

person = get_person()
print(person["name"])   # Output: Alice
print(person["age"])    # Output: 30

# Define types for union types
def multiply_values(value1: Union[int, float], value2: Union[int, float]) -> Union[int, float]:
    return value1 * value2

print(multiply_values(2, 3))        # Output: 6
print(multiply_values(2.5, 3.5))    # Output: 8.75
print(multiply_values(2, 3.5))      # Output: 7.0

