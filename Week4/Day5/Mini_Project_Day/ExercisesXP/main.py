board = ["-","-","-",
         "-","-","-",
         "-","-","-",
          "-","-","-",
           "*","*","*"]

game_on = True

current_player = "x"

def display_board():
    print("**" + board[12] + "***" + board[13] + "***"+ board[14] + "**" )
    print("* " + board[0] + " | " + board[1] + " | " + board[2] + " *" + "      " + "1|2|3")
    print("*-" + board[9] + "-|-" + board[10] + "-|-"+ board[11] + "-*" )
    print("* " + board[3] + " | " + board[4] + " | " + board[5] + " *" + "      " + "4|5|6")
    print("*-" + board[9] + "-|-" + board[10] + "-|-"+ board[11] + "-*" )
    print("* " + board[6] + " | " + board[7] + " | " + board[8] + " *" + "      " + "7|8|9")
    print("**" + board[12] + "***" + board[13] + "***"+ board[14] + "**" )

def players():
    print("Select Player - x or o")
    p1 = input("Player1: ")
    p2 = ""
    if p1 == "x":
        p2 = "o"
        print("Player2: " + p2)
    elif p1 == "o":
        p2 = "x"
        print("Player2: " + p2)
    elif p1 != "o" or p1 != "x":
        print("Sorry,invalid input. Type x or o")
        play_game()

def player_position():
    global current_player
    print("Current Player: " + current_player)
    position = input("Choose position from 1 - 9: ")
 
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
          position = input("Choose position from 1 - 9: ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Position already selected, choose another position!")
    board[position] = current_player
    display_board()

def play_game():
    print("My Tic Tac Toe Game")
    display_board()
    players()
    
    while game_on:
        player_position()
        
        def check_winner():
            global game_on
           
            if board[0] == board[1] == board[2] != "-":
                game_on = False
                print("Congratulations " + board[0]+" you WON!")
            elif board[3] == board[4] == board[5] != "-":
                game_on = False
                print("Congratulations " + board[3]+" you WON!")
            elif board[6] == board[7] == board[8] != "-":
                game_on = False
                print("Congratulations " + board[6]+" you WON!")
          
            elif board[0] == board[3] == board[6] != "-":
                game_on = False
                print("Congratulations " + board[0]+" you WON!")
            elif board[1] == board[4] == board[7] != "-":
                game_on = False
                print("Congratulations " + board[1]+" you WON!")
            elif board[2] == board[5] == board[8] != "-":
                game_on = False
                print("Congratulations " + board[2]+" you WON!")
             
            elif board[0] == board[4] == board[8] != "-":
                game_on = False
                print("Congratulations " + board[0]+" you WON!")
            elif board[2] == board[4] == board[6] != "-":
                game_on = False
                print("Congratulations "+ board[6]+" you WON!")
           
            elif "-" not in board:
                game_on = False
                print("It's a Tie")
                exit()

        def flip_player():
            global current_player
            if current_player == "x":
                current_player = "o"
            else:
                current_player = "x"
        flip_player()
        check_winner()

play_game()