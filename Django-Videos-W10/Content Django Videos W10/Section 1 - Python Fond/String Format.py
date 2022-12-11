# Strings and formatting
# String are surrounded by single or Double - Quote

name = "Daniel"
x = 26

# Concatenate
# print('Hello I am ' + x)

# + != space


# String formating

# Argument Position format
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{}, {x}, {name}'.format('a', x, name))
# 3.6+ python
print(f'My name is {name}')


s = "hello i am happy"

# Capitalize, don't forget to call the function
print(s.capitalize())

# Make all uppercase
print(s.upper())
print(s.swapcase())

# Make lower case
print(s.lower())

# Get length
print(len(s))

# Replace
print(s.replace('happy', 'cool'))

# Count the number of "h"
sub = "h"
print(s.count('h'))

# Starts with
print(s.startswith('hello'))
# End with
print(s.endswith('d'))

# Ends with
print(s.split())

# find the position
print(s.find('r'))
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())

# check all the others
# s.
