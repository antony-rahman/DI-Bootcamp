# Tuples is ordered and unchangeable.
fruit_tuple = ('Apple', 'Mango', 'Strawberries')

# get a value
print(fruit_tuple[0])

# Can not change value
# fruit_tuple[1] = 'Grape'  # Error

# Tuples with one value have a trailing commas
fruit_tuple2 = ('apples',)  # must have a commas to be Tuples

# get the length
print(len(fruit_tuple))

del fruit_tuple


# Set is UNordered and unindexed. No Duplicate.

fruit_set = {'Apple', 'Orange', 'Mango'}


# check if in set
print('Apple' in fruit_set)  # True or False

# add to set
fruit_set.add('Grape')

# Delete or Remove
fruit_set.remove('Grape')
fruit_set.clear()
del fruit_set
