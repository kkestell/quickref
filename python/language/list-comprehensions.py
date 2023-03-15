# Basic list comprehension
my_list = [x for x in range(10)]
print(my_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# List comprehension with condition
my_list = [x for x in range(10) if x % 2 == 0]
print(my_list)  # [0, 2, 4, 6, 8]

# List comprehension with expression
my_list = [x * 2 for x in range(10)]
print(my_list)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Nested list comprehension
my_list = [[x + y for x in range(3)] for y in range(3)]
print(my_list)  # [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# List comprehension with if-else statement
my_list = ['even' if x % 2 == 0 else 'odd' for x in range(10)]
print(my_list)  # ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

