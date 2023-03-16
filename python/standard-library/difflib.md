```python
import difflib

# Create a Differ object
differ = difflib.Differ()

# Compare two lists of strings
list1 = ['apple', 'banana', 'cherry']
list2 = ['apple', 'orange', 'cherry']
result = differ.compare(list1, list2)
print('\n'.join(result))

# Output:
#   apple
# - banana
# + orange
#   cherry


# Compare two strings
str1 = 'hello world'
str2 = 'hello python'
result = differ.compare(str1, str2)
print('\n'.join(result))

# Output:
#   h e l l o   w o r l d
# -       p      y      t
# +       y      h      o
#   ...             +++


# Compare two files
with open('file1.txt') as f1, open('file2.txt') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

result = differ.compare(lines1, lines2)
print('\n'.join(result))

# Output:
#   line 1
# - line 2 in file1
# + line 2 in file2
#   line 3 in file1
#   line 4 in file1
# - line 5 in file1
# + line 5 in file2
#   line 6


# Get unified diff between two lists
list1 = ['apple', 'banana', 'cherry']
list2 = ['apple', 'orange', 'cherry']
result = difflib.unified_diff(list1, list2, fromfile='file1.txt', tofile='file2.txt')
print('\n'.join(result))

# Output:
# --- file1.txt
# +++ file2.txt
# @@ -1,3 +1,3 @@
#  apple
# -banana
# +orange
#  cherry


# Get context diff between two strings
str1 = 'hello world'
str2 = 'hello python'
result = difflib.context_diff(str1, str2, fromfile='file1.txt', tofile='file2.txt')
print('\n'.join(result))

# Output:
# *** file1.txt
# --- file2.txt
# ***************
# *** 1,2 ****
#   hello world
# ! hello python
# --- 1,2 ----
#   hello world
# ! hello python
#   ***************
# ```


# Get a list of matched blocks between two strings
str1 = 'hello world'
str2 = 'hello python'
matcher = difflib.SequenceMatcher(None, str1, str2)
for match in matcher.get_matching_blocks():
    print(f'match: {match}')
    
# Output:
# match: Match(a=0, b=0, size=6)
# match: Match(a=8, b=7, size=3)
# match: Match(a=11, b=13, size=0)
    

# Get the longest contiguous matching subsequence between two strings
str1 = 'hello world'
str2 = 'hello python'
matcher = difflib.SequenceMatcher(None, str1, str2)
match = matcher.find_longest_match(0, len(str1), 0, len(str2))
print(f'match: {match}')

# Output:
# match: Match(a=0, b=0, size=6)

```
