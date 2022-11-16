# A connect4 game written in python
# Author : y5hn4v (https://github.com/y5hn4v)
# Version : 1.0.0
# -----------------------------------------
# Right now it is a command line game. But i will be adding a GUI and hopefully multiplayer in the future
# Reference : https://www.youtube.com/watch?v=XpYz-q1lxu8

# TODO - Use PyGame to build a GUI and also try to implement multiplayer. This project will help with understanding PyGame and also some networking with python
# Optional - Try to make the win() function more flexible and small

import numpy

# Right now the size of the board is fixed
ROWS = 6
COLUMNS = 7
# Initializing the board as a matrix using numpy
board = numpy.zeros((ROWS, COLUMNS))
# Function to accept the column to drop the piece
def user_input(turn):
    try:
        print(numpy.flip(board, 0))
        control = False
        while not control:
            user_input = int(input(f'Player {turn}, Pick the column between (0-6) : '))        
            if user_input >= 0 and user_input <= 6:
                control = True
                return user_input
            else:
                print("You did not enter a number between 0 and 6 . Please try again")
    # The main Exception that might occur will be 'invalid literal for int() with base 10:' if the user inputs anything other than an integer
    except Exception as e:
        print(f'Error occurred : {e}.Quitting')
        quit()
# Function to drop the piece on to the column inputted by the user
def drop_piece(column, piece):
    current_row = 0
    piece_dropped = False
    # Check if the piece is dropped
    while not piece_dropped:
            # Check if the column is full
            if current_row >= ROWS:
                print("That column is full . Please try again")
                return 0, 0 # Returning 0 to ask the user for input again
            # Check if there is a piece already present in that space
            if board[current_row][column] != 0:
                current_row += 1
            # If the column is not full AND if the space is empty , then drop the piece
            else:
                board[current_row][column] = piece
                piece_dropped = True
    return 1, current_row
# Function to check for a winner and returns the player number if the player wins
def win(column, row, player):
    return_value = 0
    # The below conditons will check for a winner by checking if there are 4 same pieces in a row or a column or in any one of the diagonals
    try:
        # Check to the left of the current piece
        if board[row][column] == player and board[row][column-1] == player and board[row][column-2] == player and board[row][column-3] == player:
            return_value = player
            pass
        # Check to the right of the current piece
        if board[row][column] == player and board[row][column+1] == player and board[row][column+2] == player and board[row][column+3] == player:
            return_value = player
            pass
        # Check to the top of the current piece
        if board[row][column] == player and board[row-1][column] == player and board[row-2][column] == player and board[row-3][column] == player:
            return_value = player
            pass
        # Check to the bottom of the current piece
        if board[row][column] == player and board[row+1][column] == player and board[row+2][column] == player and board[row+3][column] == player:
            return_value = player
            pass
        # Check the top right diagonal of the piece
        if board[row][column] == player and board[row+1][column+1] == player and board[row+2][column+2] == player and board[row+3][column+3] == player:
            return_value = player
            pass
        # Check the bottom left diagonal of the piece
        if board[row][column] == player and board[row-1][column-1] == player and board[row-2][column-2] == player and board[row-3][column-3] == player:
            return_value = player
            pass 
        # Check the bottom right diagonal of the piece
        if board[row][column] == player and board[row-1][column+1] == player and board[row-2][column+2] == player and board[row-3][column+3] == player:
            return_value = player
            pass 
        # Check the top left diagonal of the piece
        if board[row][column] == player and board[row+1][column-1] == player and board[row+2][column-2] == player and board[row+3][column-3] == player:
            return_value = player
            pass 
    # A try except block is used to avoid the "OUT OF BOUNDS" error
    except Exception:
        pass
    return return_value
# The function which calls the other functions at the correct time
def main():
    game_over = False
    turn = 1
    while not game_over:
        userinput = user_input(turn)
        drop_piece_return, current_row = drop_piece(userinput, turn)
        # If the column is full drop_piece() will return 0
        if drop_piece_return == 0:
            continue   
        winner = win(userinput, current_row, turn)
        # Check for winner
        if winner == turn:
            print(f'Player {winner} wins')
            game_over = True
        # Test if the board is full. all() function returns True is the matrix doesnt have a zero   
        if numpy.all(board):
            print("The board is full . GAME OVER")
            game_over = True
        #The below statements are done to keep the player numbers 1 and 2 only.
        if turn == 2:
            turn = 1
        else:
            turn += 1
        

if __name__ == '__main__':
    main()

