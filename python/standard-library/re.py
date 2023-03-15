import re

# Basic pattern matching
match = re.match(r'hello', 'hello world')
search = re.search(r'world', 'hello world')
find_all = re.findall(r'l', 'hello world')
replace = re.sub(r'world', 'Python', 'hello world')

# Character classes
match_letters = re.match(r'[a-zA-Z]', 'Hello')
match_digits = re.match(r'[0-9]', '123')
match_word_chars = re.match(r'\w', 'Hello_123')
match_non_word_chars = re.match(r'\W', '#!@')

# Quantifiers
match_zero_or_more = re.match(r'a*', 'aaa')
match_one_or_more = re.match(r'a+', 'aaa')
match_zero_or_one = re.match(r'a?', 'aaa')
match_specific = re.match(r'a{3}', 'aaa')
match_range = re.match(r'a{1,3}', 'aaa')

# Grouping
match_groups = re.match(r'(hello) (world)', 'hello world')
group = match_groups.group()
group_one = match_groups.group(1)
group_two = match_groups.group(2)

# Regular expressions
match_email = re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'example@example.com')
match_phone = re.match(r'^\+?[0-9]{1,3}\s?[0-9]{10}$', '+1 1234567890')

# Flags
match_case_insensitive = re.match(r'hello', 'Hello', re.IGNORECASE)
match_multiple_lines = re.match(r'^hello', 'hello\nworld', re.MULTILINE)
