```python
import argparse

# -----------------------------------------------
# Basic Usage
# -----------------------------------------------

parser = argparse.ArgumentParser(description='Description of your program')
parser.parse_args()

# -----------------------------------------------
# Positional Arguments
# -----------------------------------------------

# Define a required positional argument
parser.add_argument('foo', help='foo help')
# Define an optional positional argument with default value
parser.add_argument('bar', nargs='?', default='bar_default', help='bar help')

# Parse the arguments from command line
args = parser.parse_args()

print(args.foo)  # Access the value of foo
print(args.bar)  # Access the value of bar

# -----------------------------------------------
# Optional Arguments
# -----------------------------------------------

# Define an optional argument with a single value
parser.add_argument('-a', '--arg1', help='arg1 help')
# Define an optional argument with multiple values
parser.add_argument('-b', '--arg2', nargs='+', help='arg2 help')
# Define a mutually exclusive group of arguments
group = parser.add_mutually_exclusive_group()
group.add_argument('-c', '--option1', action='store_true', help='option1 help')
group.add_argument('-d', '--option2', type=int, help='option2 help')

# Parse the arguments from command line
args = parser.parse_args()

print(args.arg1)   # Access the value of arg1
print(args.arg2)   # Access the list of values of arg2
print(args.option1)# Access the value of option1
print(args.option2)# Access the value of option2

# -----------------------------------------------
# Advanced Usage
# -----------------------------------------------

# Define a parent parser
parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--parent_arg', help='parent_arg help')

# Define a subparser with a different set of arguments
subparsers = parser.add_subparsers(help='sub-command help')
sub_parser1 = subparsers.add_parser('sub1', parents=[parent_parser], help='sub1 help')
sub_parser1.add_argument('--sub_arg', help='sub_arg help')
sub_parser2 = subparsers.add_parser('sub2', help='sub2 help')

# Parse the arguments from command line
args = parser.parse_args()

print(args.parent_arg)  # Access the value of parent_arg
if hasattr(args, 'sub_arg'):
    print(args.sub_arg) # Access the value of sub_arg only if sub1 was called
```