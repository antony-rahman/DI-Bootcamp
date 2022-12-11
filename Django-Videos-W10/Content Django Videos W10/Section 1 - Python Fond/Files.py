# Python functions for CRUD files
# CRUD = Create, Read, Update, Delete

# Open a files
myFile = open('myfile.txt', 'w')

# get some infos
print('Name: ', myFile.name)
print('is closed ', myFile.closed)
print('Mode: ', myFile.mode)

# Write to a file
myFile.write('I love python')
myFile.write(' and JavaScript')
myFile.close()

# Append and not Write
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

# Read, 100 charchters
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
text = myFile.readline(100)
print(text)

# Nice link explained
# https://www.guru99.com/reading-and-writing-files-in-python.html#:~:text=Use%20the%20function%20open(%22filename,with%20read%20and%20write%20permissions.&text=Use%20the%20readlines%20function%20to,the%20file%20one%20by%20one.
