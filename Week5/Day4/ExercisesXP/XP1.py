#EX1 - I couldn't do it, but th EX2 is done
import datetime
from random import randint

words_collection = []
def get_words_from_file()->list:    
    '''read the file`s content and return the words as a collection'''
    with open('words.txt', mode='r') as f:
        f.readlines()
        for word in f:
            words_collection.append(word)
    return words_collection 

def get_random_sentence(lenght:int)->str:
    '''creates a random phrase wich its lenght is the given parameter(lenght)'''
    random_words = []
    with open('words.txt', mode='r') as f:
        f.read()
        for word in words_collection:
            random_words.append(word)
    return random_words  

def main():
    print(get_words_from_file.__dict__())
    user_input = input("enter today`s date: ")
    current_date = datetime.datetime.now()
    if user_input == current_date:
        user_num = input(int('how long you want the sentence to be?(choose a number between 2 and 20): '))
        while user_num != range(2-20):
            input(int('Sorry, it really has to be a number between 2 and 20: '))
        else:
            print(get_random_sentence(user_num))
    else:
        user_input = input("That's not right, please enter today`s date correctly: ")

print(get_words_from_file())
print(get_random_sentence(5))


# # ex 2 
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
# sampleJason = eval(sampleJson)
# #1
# print(sampleJason['company']['employee']['payable'])
# #2
# sampleJason['company']['employee']['birth_date'] = '24/07.2000'
# print(sampleJason)
# #3
# with open("XP1.json", "w") as out_file:
#     json.dump(sampleJason, out_file)