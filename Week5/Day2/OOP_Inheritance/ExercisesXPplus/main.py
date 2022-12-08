# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]
# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ first name.

class Family():
    def __init__(self, last_name: str, members:list) -> object:
        self.last_name = last_name
        self.members = members

    def born(self, **child) -> None:
        ''' adds a new member to the class Family'''
        self.members.append(child)        
        print(f"Congratulations for the new family member {child['name']}!")

    def get_member(self):
        '''checking if the member exists in self.members'''
        for member in self.members:
            if name == member['name']:
                return member
        else:
            raise ValueError("No such member in this family")

    def is_18(self, member_name: str) -> bool:
        '''check if a member is above 18 years old'''
        member = self.get_member()
        if member['age'] >= 18:
             return True
        else:
            return False
    def family_presentation(self):
        '''prints a presentation with the last_name and all the f_names of the members'''
        print(f'Welcome to the {self.last_name} Family!')
        for member in self.members:
            print(f"{member['name']} lives here!")

schmidt = Family('schmidt',[{'name':'Michael','age':35,'gender':'Male','is_child':False},
                        {'name':'Sarah','age':32,'gender':'Female','is_child':False}] )
print(schmidt.members)
schmidt.born(name = 'Moshe', age = 0, gender = 'Male', is_child = True)
print (schmidt.is_18(schmidt.members[0]['name']))
schmidt.family_presentation()
        


# Exercise 2 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:

# This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]


# 2.Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


# 3. Add a method called incredible_presentation which : * prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method) * prints all the members’ incredible name and power.


# 4. Call the incredible_presentation method.
# 5. Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# 6. Call the incredible_presentation method again.

class TheIncredibles(Family):
    def use_power(self, name:str)-> None:
            member = self.get_member(name)
            if self.is_18(name):
                print(f'{member[name]} is using power: {member[power]}')
            else: 
                raise ValueError("Member is under 18!")

    def family_presentation(self):
        '''adds new elelments in the family_presentation method'''
        super().family_presentation()
        power_stack = '|'.join([member['power'] for member in self.members])
        print(f'power stack:{power_stack}')
       
data2 = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]

incredible_fam = TheIncredibles('Incredible', data2)
incredible_fam.use_power('Sarah')