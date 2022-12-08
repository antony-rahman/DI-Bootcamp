import random
# i couldn't finish all the features for the game: for some reason it asks twice for the user input, but on the sec time it workd
# I couldn't find a way to save the results for each new game
# the menu for new game or quit is displayed but it just start a new game, no matter what is the user input.
#Global variables
moves = ['p', 's', 'r']
tie = []
win = []
loose = []
results = {}

class Game:
    def __init__(self):
        self.user = self.get_user_item()
        self.comp= self.get_computer_item()
    def get_user_item(self)-> str:
        '''asks for user move, validate it and return the user_item'''
        user_item = input('Choose your move:(r = rock)(p=paper)(s=scissors)')
        while user_item not in moves:
            user_item = input('Please pic a valid option:(r = rock)(p=paper)(s=scissors)')
            return user_item
        else:
            return user_item

    def get_computer_item(self)-> str:
        '''create a random choice for the computer_item and returns it'''
        computer_item = random.choice(moves)
        return computer_item

    def get_game_result(self):
        '''compares the user and computer items and returns a winner or a tie'''
        global tie
        global win
        global loose
        while True:            
            if self.user == self.comp:
                tie =+ +1
                return 'tie'
            elif self.user =='p':
                if self.comp == 's':
                    winner = 'computer'
                    loose =+ 1
                    return 'loose'
                else:
                    winner = 'user'
                    win =+ 1
                    return 'win'
            elif self.user =='s':
                if self.comp == 'r':
                    winner = 'computer'
                    loose =+ 1
                    return 'loose'
                else:
                    winner = 'user'
                    win =+ 1
                    return 'win'
            elif self.user =='r':
                if self.comp == 'p':
                    winner = 'computer'
                    loose =+ 1
                    return 'loose'
                else:
                    winner = 'user'
                    win =+ 1
                    return 'win'
        

    def play(self):
        # self.get_game_result()
        if self.get_game_result() == 'win':
            print(f'computer choose: {self.comp} you choose, {self.user}. You won.')
        elif self.get_game_result() == 'loose':
            print(f'computer choose: {self.comp} you choose, {self.user}. You loose.')
        elif self.get_game_result() == 'tie':
            print(f'computer choose: {self.comp} you choose, {self.user}. It`s a tie.')
        print(tie)
        print(win)
        print(loose)

