import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read an INI file
config.read('config.ini')

# Get all section names
sections = config.sections()
print(f"All section names: {sections}")

# Get all options in a section
section_name = 'section_name'
options = config.options(section_name)
print(f"All options in {section_name}: {options}")

# Get a value in a section
option_name = 'option_name'
value = config.get(section_name, option_name)
print(f"Value of {option_name} in {section_name}: {value}")

# Get an int value in a section
option_name = 'int_option'
int_value = config.getint(section_name, option_name)
print(f"Int value of {option_name} in {section_name}: {int_value}")

# Get a float value in a section
option_name = 'float_option'
float_value = config.getfloat(section_name, option_name)
print(f"Float value of {option_name} in {section_name}: {float_value}")

# Get a boolean value in a section
option_name = 'bool_option'
bool_value = config.getboolean(section_name, option_name)
print(f"Boolean value of {option_name} in {section_name}: {bool_value}")

# Set a value in a section
option_name = 'option_name'
new_value = 'new_value'
config.set(section_name, option_name, new_value)

# Write changes to the file
with open('config.ini', 'w') as configfile:
    config.write(configfile)

# Notes:
# - The `ConfigParser` object is used to read and write configuration files in the INI format.
# - The `read()` method reads the contents of an INI file into the `ConfigParser` object.
# - The `sections()` method returns a list of all section names in the file.
# - The `options(section)` method returns a list of all options in the specified section.
# - The `get(section, option)` method returns the value of the specified option in the specified section.
# - The `getint(section, option)` and `getfloat(section, option)` methods return integer and float values, respectively.
# - The `getboolean(section, option)` method returns a boolean value. The value of the option is interpreted as a boolean using standard Python boolean rules (e.g. "yes", "true", and "on" are interpreted as True, while "no", "false", and "off" are interpreted as False).
# - The `set(section, option, value)` method sets the value of the specified option in the specified section.
# - The `write(file)` method writes the current state of the `ConfigParser` object to the specified file.
