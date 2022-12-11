# Loops - For, while, range...

people = ['Daniel', 'Megane', 'Avner']

# For loop
for person in people:
    print(person, 'is in the list')

print('-----------------')
# Break out the loop
for person in people:
    print(person, 'is in the list')
    if person == 'Daniel':
        break
# position of break matter

print('-----------------')
# continue (also = skip)
for person in people:
    if person == 'Megane':
        continue
    print(person, 'is in the list')

print('-----------------')
# Range
for i in range(len(people)):
    print(people[i], 'is cool')

print('-----------------')
# 10 not included
for i in range(0, 10):
    print(i)

print('-----------------')
# While
count = 0
while count <= 10:
    print('Count :', count)
    count += 1
