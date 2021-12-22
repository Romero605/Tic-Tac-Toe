import csv
# ------- Global Variables -----------

board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

#If the game is still going
game_still_going = True

#Who won? or tie?
winner = None

#Who's turn is it
current_player = "X"
#This is the intro of the game
def intro():
    print("Welcome to my virtual player vs player tic tac toe game!")
    print("In this game of tic tac toe you will be playing agaisnt a buddy of yours.")
    print("The goal of this game is for the player to get three in a row, either in diagonal, row, or column.")
    print("Good luck! May the best win!")
    input("Press enter to play Tic Tac Toe:")
intro()
#Plays the game of Tic Tac Toe
def play_game():
    #This displays the initial board
     display_board()
     # While the game is still going
     while game_still_going:
        #handle a single turn of a random player
        handle_turn(current_player)

        #This checks if the game has ended
        check_if_game_over()

        #Flips to the other player
        flip_player()
        
     data = load()
     
     xwins = int(data[1][0])
     owins = int(data[1][1])
     draws = int(data[1][2])
     
        #the game has finished
     if winner == "X":
         print(winner + " has won!")
         xwins += 1
     elif winner == "O":
            print(winner + " has won!")
            owins += 1
     elif winner == None:
            print("It is a draw!")
            draws += 1
     
     print("\n")
     print("X total wins: "+str(xwins))
     print("O total wins: "+str(owins))
     print("Total draws: "+str(draws))
     export(data, str(xwins), str(owins), str(draws))
#This displays the game board and the positions of each slot     
def display_board():
    print("\n")
    print(board[0] + "|" + board[1] + "|" + board[2] + "    1 | 2 | 3")
    print(board[3] + "|" + board[4] + "|" + board[5] + "    4 | 5 | 6")
    print(board[6] + "|" + board[7] + "|" + board[8] + "    7 | 8 | 9")
    print("\n")



#Handle a single turn of a random player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9:")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid Input, Choose a position from 1-9:")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant enter a value here. Go again.")

    board[position] = player

    display_board()


#checks who won either X or O
def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    #Set up important variable
    global winner
    #check the rows
    row_winner = check_rows()
    #check the columns
    column_winner = check_columns()
    #check the diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
       winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
#Checks if anyone has won in the fashion of a row
def check_rows():
    #Set up global variables
    global game_still_going
    #Check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #if any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    #Return the winner either X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

#Checks if anyone has won in the fashion of a column
def check_columns():
    #Set up global variables
    global game_still_going
    #Check if any of the rows have all the same values (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    #If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    #Return the winner either X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None
#Checks if anyone has won in the fashion of a diagonal
def check_diagonals():
    #Set up global variables
    global game_still_going
    #Check if any of the rows have all the same values (and is not empty)
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"
    #If any diagonal does have a match, flag that there is a win
    if diagonals_1 or diagonals_2:
        game_still_going = False
    #Return the winner either X or O
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    else:
        return None

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False


def flip_player():
    #We need a global variable
    global current_player
    # If the current player was X, then change to O
    if current_player == "X":
        current_player = "O"
        #If the current player was O, then change to X
    elif current_player == "O":
        current_player = "X"

def load():
    data = []
    with open('data.csv', 'r',newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data
    
#leader is winner
def export(Data,x,o,d):
    
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(["X-wins", "O-wins","Draws"])
        writer.writerow([x,o,d])
        
    
play_game()


