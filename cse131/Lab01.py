# 1. Name:
#      Nathan Schmidt
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was figuring out how to
#      implement the already given code into the program to
#      create around. That was the most difficult part for me;
#      however, I still got it done. I really didn't feel too
#      well prepared for the assignment either, I am not sure
#      if it was because there really was no guidance or what.
# 5. How long did it take for you to complete the assignment?
#      The program took me about 2 hours.

import json
import os.path

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    # Put file reading code here.

    with open(filename) as file:
        board = json.load(file)

    return board

def save_board(filename, board):
    '''Save the current game to a file.'''
    # Put file writing code here.

    with open(filename, "w") as file_save:
        json.dump(board, file_save)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    # Put display code here.

    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def is_x_turn(board):
    '''Determine whose turn it is.'''
    # Put code here determining if it is X's turn.

    x_turn = 0
    o_turn = 0

    i = 0
    while i < len(board):
        if board[i] == "X":
            x_turn += 1
        elif board[i] == "O":
            o_turn += 1
        i += 1

    if x_turn <= o_turn:
        return True

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    # Put game play code here. Return False when the user has indicated they are done.

    # Defines variables.
    turn = ""
    player_turn = ""
    
    display_board(board)
    while turn != "q" and game_done(board, True) == False:
        if is_x_turn(board) == True:
            player_turn = "X"
        else:
            player_turn = "O"
        
        turn = input(f"{player_turn}: ")

        if turn.lower() != "q":
            post_turn = int(turn) - 1

        false_move = "That place is already taken! Try again.\n"

        if board[post_turn] != "X":
            if board[post_turn] != "O":
                board[post_turn] = player_turn

            elif board[post_turn] == "O":
                print(false_move)
        elif board[post_turn] == "X":
            print(false_move)

        display_board(board)

    if turn.lower() == "q":
        save_board("board_saved.json", board)

    existing_file = os.path.exists("board_saved.json")
    if existing_file:
        if game_done(board, True) == True and turn.lower() != "q":
            os.remove("board_saved.json")

    return False

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True

    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# The file read code, game loop code, and file close code goes here.
existing_file = os.path.exists("board_saved.json")
if existing_file:
    board = read_board("board_saved.json")
else:
    board = blank_board["board"]

play_game(board)

print("\nThe game is over.")