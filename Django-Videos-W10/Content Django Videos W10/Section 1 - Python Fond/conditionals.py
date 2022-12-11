# If Else Statement --> TRUE or FALSE

x = 10
y = 6

# Comparisons operator, (==, !=, >, <, >=, <=) are used to compare
# simple IF

if x > y:
    print(f'{x} is greater {y}')
# use elif
elif x == y:
    print(f'{x} is equal {y}')
else:
    print(f'{x} is less {y}')


# Nested if
if x > 2:
    if x <= 10:
        print(x, 'is less than 2 and greater than 10')

# Logical and, is, not

# and, both have to be true
if x > 2 and x <= 10:
    print(x, 'is less than 2 and greater than 10')

# or, one of them --> logic
if x > 2 or x <= 10:
    print(x, 'is less than 2 and greater than 10')

# not
if not(x == y):
    print(x, 'is not equal', y)

# not in
numbers = [1, 2, 3, 4, 5, 6, 10]
if x not in numbers:
    print(x in numbers)

# is
if x is y:
    print(x is y)

# is not
if x is not y:
    print('Nope it isnt')
