# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.

check10 = input("type a string: ")

if len(check10) < 10 :
    print("string not long enough")
elif len(check10) > 10:
    print("string too thick")
else: print(check10)

# Then, print the first and last characters of the given text.

print(check10[0] + "" + check10[-1]) 

# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "Hello World"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# Hello World

letter=""

for i in check10:
    letter+=i
    print(letter)
    
# 4. Bonus: Swap some characters around then print the newly jumbled string 
# (hint: look into the shuffle method). For example:

# Hlrolelwod

import random

l = list(check10)
random.shuffle(l)
result = ''.join(l)

print(result)


    
    
   
    
