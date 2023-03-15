import argparse

# Basic usage
parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-f', '--foo', help='Description of foo argument')
parser.add_argument('-b', '--bar', type=int, help='Description of bar argument')
args = parser.parse_args()

# Positional arguments
parser.add_argument('arg1', help='Description of arg1')
parser.add_argument('arg2', type=int, help='Description of arg2')

# Required arguments
parser.add_argument('required_arg', help='Description of required_arg', required=True)

# Default values
parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')
parser.add_argument('-l', '--log', default='log.txt', help='Log file')

# Choices
parser.add_argument('-c', '--choice', choices=['A', 'B', 'C'], help='Choice argument')

# Sub-commands
subparsers = parser.add_subparsers(title='sub-commands', dest='subparser')
parser_a = subparsers.add_parser('command_a', help='Description of command A')
parser_a.add_argument('-a', '--arg', help='Description of argument for command A')
parser_b = subparsers.add_parser('command_b', help='Description of command B')
parser_b.add_argument('-b', '--arg', help='Description of argument for command B')

args = parser.parse_args()

if args.subparser == 'command_a':
    # Handle command A
elif args.subparser == 'command_b':
    # Handle command B

