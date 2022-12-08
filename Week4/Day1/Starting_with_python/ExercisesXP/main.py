# Exercise 1 : Hello World
# Instructions
# Print the following output in one line of code:

# Hello world
# Hello world
# Hello world
# Hello world


from distutils.log import info


print("Hello world\n  Hello world\n  Hello world\n  Hello world\n  Hello world\n")
 
 
# Exercise 2 : Some Math
# Instructions
# Write code that calculates the result of: (99^3) * 8 (99 to the power of 3 times 8)

calc = (99^3) * 8
print(calc)



# Exercise 3 : What Is The Output ?
# Instructions
# Predict the output of the following code snippets:

# # >>> 5 < 3

# False

# # >>> 3 == 3

# True

# # >>> 3 == "3"

# False

# # >>> "3" > 3

# > Not supported between str and int

# # >>> "Hello" == "hello"

# False

# 🌟 Exercise 4 : Your Computer Brand
# Instructions
# Create a variable called computer_brand which value is
# the brand name of your computer.
# Using the computer_brand variable print a sentence
# that states the following: "I have a <computer_brand> computer".

computer_brand = "Lenovo"
sentence = f"I have a {computer_brand} computer"
print(sentence)

# Exercise 5 : Your Information
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself.
# The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

name = "Anton"

age = "32"

shoe_size = 46

info = f"My name is {name}, I'm {age} years old, and you know I'm packing because my shoe size is {shoe_size}"

print(info)

