from game import *
game_goes_on = True
options = ['g','x','q']


def print_results(results):
    from game import results 
    print(f' Game Results:\n {results}\n Thank you for playing!')   
    
def get_user_menu_choice():
    user_choose = input('Play a new game = g \n Show scores = x\n Quit = q\n')
    while user_choose not in options:
        user_choose = input('Please enter a valid option:\n Play a new game = g\n Show scores = x\n Quit = q\n')
    else: return user_choose

def main():      
    global game_goes_on
    while game_goes_on:
        if get_user_menu_choice() == 'g': 
            game = Game()
            game.play() 
            game.get_game_result()
            get_user_menu_choice()               
        if get_user_menu_choice() == 'x':
            print_results(game)
            get_user_menu_choice()  
    else:
        game_goes_on == False
        
main()