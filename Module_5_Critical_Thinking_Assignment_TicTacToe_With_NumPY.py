"""
Pseudocode:

Create a 3x3 board initialized with empty spaces
Set current player to X

Define function to display the board

Define function to check if a player has won
    Check rows, columns, and both diagonals

Define function to check for a draw
    Determine whether the board contains empty spaces

Start game loop
    Display the board
    Prompt current player for row and column
    If square is occupied, prompt again
    Place the player's mark on the board

    If the player has won
        Display board and announce winner
        End game

    If the board is full
        Display board and announce draw
        End game

    Switch players and continue loop
"""



"""Tic-Tac-Toe with NumPy

This program allows two players to play a 2-player tic-tac-toe game using
a 3x3 NumPy array as the game board. Players take turns entering the row
and column index where they would like to place their mark (X or O).

The program validates that moves are made only on empty squares and
updates the board after each turn. After every move, the program checks
whether a player has won by completing a row, column, or diagonal, or
if the game has ended in a draw."""


import numpy as np

# Create a 3x3 Tic-Tac-Toe board filled with empty spaces
board = np.full((3, 3), " ")

def print_board():
    """Display the current Tic Tac Toe board."""
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")

def check_winner(player):
    """Check whether the specified player has won the game."""
    for i in range(3):
        if np.all(board[i] == player):
            return True
        if np.all(board[:, i] == player):
            return True
        if np.all(np.diag(board) == player):
            return True
        if np.all(np.diag(np.fliplr(board)) == player):
            return True
        return False
    
def check_draw():
    """Check whether the game has ended in a draw."""
    if not np.any(board == " "):
        return True
    return False

current_player = "X"

while True:
    # Main game loop: display the board and prompt the current player for a move
    print_board()
    row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
    col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

    # Ensure the selected square is empty before allowing the move
    if board[row][col] != " ":
        print("That square is already taken. Try again.")
        continue

    board[row][col] = current_player

    # Check whether the move resulted in a win or a draw
    if check_winner(current_player):
        print_board()
        print(f"Player {current_player} wins!")
        break

    if check_draw():
        print_board()
        print("The game is a draw.")
        break
    
    # Switch turns between players X and O
    current_player = "O" if current_player == "X" else "X"
    print()