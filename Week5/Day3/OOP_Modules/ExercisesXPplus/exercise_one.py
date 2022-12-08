from func import add
from random import randint

def random_num(user_num:int)->str:
    pc_number = randint(1,100)
    if pc_number == user_num:
        print(f'The pc number:{pc_number}, and your number matched!')
    else:
        print(f'The pc number was:{pc_number}. Try again')

random_num(25)