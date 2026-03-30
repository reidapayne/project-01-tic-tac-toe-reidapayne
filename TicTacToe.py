"""
Author:         Reid Payne
Date:           3/16/2026
Assignment:     Project 1
Course:         CPSC1050
Lab Section:    001

CODE DESCRIPTION: This program will give a brief introduction to its usage, then ask two players, player X and player O, to 
play Tic-Tac-Toe against each other. The players will be prompted to input row and column numbers to place their X or O marker on 
the Tic-Tac-Toe board, which will update accordingly. When the board is filled (a tie) or a player has gotten three of their 
markers in a row (horizontally, vertically, or diagonally) the game will announce the results and ask if you would like to play again.

"""


def create_empty_board():
    """
    Creates and returns a 3x3 Tic-Tac-Toe board, each cell starts as a blank space " "

    Returns: A 3x3 list of lists filled with a blank space
    """
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]    
    return board



def print_board(board):
    """
    Prints the Tic-Tac_Toe board to the screen. Empty spaces are shown as underscores.

    Arguments: a board (3x3 list)
    """
    for row in range(3):
        line = ""
        for col in range(3):
            cell = board[row][col]
            if cell == " ":
                cell = "_"
            line += "| " + cell + " "
        line += "|"
        print(line)


def read_row_col():
    """
    Reads and validates user input for row and column. Ensures values are digits between 1 and 3. 
    
    Returns: A row and col, two integers.
    """
    valid = False

    while valid == False:
        pieces = input().split()

        # Checks that there are two peices and both are valid numbers
        if len(pieces) == 2 and pieces[0] in ["1","2","3"] and pieces[1] in ["1", "2", "3"]:
            row = int(pieces[0])
            col = int(pieces[1])


            if row >= 1 and row <= 3 and col >=1 and col <= 3:
                valid = True
            else:
                print("Please enter valid row and col numbers from 1 to 3:")
        else:
            print("Please enter valid row and col numbers from 1 to 3:")

    return row - 1, col - 1 # Convert to zero based index



def winner_found(board, player):
    """
    Checks whether the given player (X or O) has won.

    Arguments: board (3x3) list with player either "X" or "O"

    Returns: True, if a winning condition is met.
    """
    # Checks all three row
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True

    # Checks all three columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board [2][col] == player:
            return True
    
    # Checks top left to bottom right diagonal
    if board[0][0] == player and board[1][1] == player and board [2][2] == player:
        return True

    # Checks top right to bottom left diagonal
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False
    

def tie_found(board):
    """
    Checks whether the game has ended in a tie, a tie occurs when no empty spaces remain and no one
    has won.

    Arguments: board (3x3) list

    Returns: True if no empty spaces remain
    """
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False
    return True
    


def swap_player(player):
    """
    Switches the current player, X becomes O and O becomes X

    Arguments: player - either "X" or "O"

    Returns: "O" if the player was "X" and "X" if the player was "O"
    """
    if player == "X":
        return "O"
    else:
        return "X"


def play():
    """
    Runs a single game of Tic-Tac-Toe, alternating players until someone wins

    Returns: None

    Arguments: None
    """

    print("Let's play Tic-Tac-Toe!")
    print("When prompted, enter desired row and column numbers")
    print("Example: 1 3")
    print("| _ | _ | X |")
    print("| _ | _ | _ |")
    print("| _ | _ | _ |")
    print("Let's play!")
    print("Player X starts!")

    board = create_empty_board()
    current = "X" # X always goes first
    game_over = False
        
    while game_over == False:
        print_board(board)
        print("Enter row and column for player " + current)
        row, col  = read_row_col()

        # Keeps asking if the spot is already taken
        while board[row][col] != " ":
            print("That spot is full!")
            print("Please enter valid row and col numbers from 1 to 3:")
            row, col  = read_row_col()

        board[row][col] = current # Place the players "X" or "O"

        if winner_found(board, current):
            print_board(board)
            print("Player " + current + " WINS!")
            game_over = True

        elif tie_found(board):
            print_board(board)
            print("It's a TIE!")
            game_over = True
            
        else:
            current = swap_player(current) # Switch to the other player
            


def play_again():
    """
    Asks the user if they want to play another game, returns True if yes and False otherwise

    Arguments: None

    Returns: True if user enters Y, False if user enters N
    """
    print("Do you want to play again? Y or N")
    answer = input().strip()

    while answer != "Y" and answer != "y" and answer != "N" and answer != "n":
        print("Please enter valid input: Y or N")
        print("Do you want to play again? Y or N")
        answer = input().strip()

    return answer == "Y" or answer == "y"


        
def main():
    """
    Controls overall game flow and continues playing until the user chooses not to.

    Arguments: None

    Returns: None
    """
    keep_playing = True

    while keep_playing != False:
        play()
        keep_playing = play_again()
        
    print("Thanks for playing!")

if __name__ == "__main__":
    main()