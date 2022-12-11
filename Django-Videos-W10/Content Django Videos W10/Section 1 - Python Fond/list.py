
# List in Python

numbers = [1, 2, 3, 4]
print(numbers)

# using a constructor
numbers = list((1, 2, 3, 4))
fruits = ['Apples', 'Oranges', 'Grapes']

# Get Value
print(fruits[1])  # 0

# get len
print(len(fruits))

# append
fruits.append('Mangos')

# remove
fruits.remove('Grapes')

# insert into position
fruits.insert(0, 'Straweberries')

# remove from position
fruits.pop()

# reverse
fruits.reverse()

# sort or reverse sort
fruits.sort()
fruits.sort(reverse=True)


print(fruits)
