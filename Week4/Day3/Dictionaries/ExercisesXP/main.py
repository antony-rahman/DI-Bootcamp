# Exercise 1 : Convert Lists Into Dictionaries

# Convert the two following lists, into dictionaries.
# Zip the lists together using zip(list_1, list_2).
# Create a dictionary from the list of tuples using the constructor dict() on the result.
# In other words, call dict(zip(list_1, list_2)) to convert two lists into a dictionary.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


dictionary = dict(zip(keys, values))
print(dictionary)


# Exercise 2 : Cinema

# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.


cinema = {}

for i in range(4):
    name = input("Enter your name: ")
    age = input("Enter your age: ")

cinema[name]=age

print(cinema)


price_list = cinema.values()


if cinema[age] < 3:
        print("Your ticket is free")
elif cinema[age] < 12:
        print("Your ticket is $10") 
else:
        print("Your ticket is $15")
print(cinema)


total_cost = sum()



# Exercise 3: Zara

# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US. 
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:

# creation_date: 1975 
# number_stores: 10 000


# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ?

brand = {
    "name":"zara",
    "creation_date":1975,
    "creator_name":"Amancio Ortega Gaona",
    "type_of_clothes":"men, women, children, home",
    "international_competitors":"Gap, H&M, Benetton",
    "number_stores":7000,
    "major_color":{ 
            "france":"blue",
            "spain":"red",
            "us":"pink, green"
         }
}
brand["number_stores"] = 2
print(brand["number_stores"])

print(brand)

brand["country_creation"] = "spain"
print(brand["country_creation"])

del brand["creation_date"]

print(brand["major_color"]["us"])

print(len(brand))

print(brand.keys())

more_on_zara = {
    "creation_date": "1975",
    "number_stores": "10 000"
}
print(more_on_zara)

brand.update(more_on_zara)

print(brand["number_stores"])




# Exercise 4 : Disney Characters

# Use this list :

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :

# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.


users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

users_dict = dict.fromkeys(users, "")
print(users)
 
for x in range(5):
    for user in users:
       users_dict[user]= x

print(users_dict)

r = sorted(users_dict.keys())
print(r)