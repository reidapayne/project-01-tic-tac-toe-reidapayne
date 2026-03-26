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

"""
Creates and return a 3x3 Tic-Tac-Toe board, each cell starts as a blank space " "
"""
def create_empty_board():
    board = []
    for _ in range(3): # Create 3 rows
        row = []
        for _ in range(3): # Create 3 columns per row
            row.append(" ") # Empty cell
        board.append(row)
    return board


"""
Prints the Tic-Tac_Toe board to the screen. Empty spaces are shown as underscores.
"""
def print_board(board):
    for row in range(3):
        line = ""
        for col in range(3):
            cell = board[row][col]
            if cell == " ":
                cell = "_"
            line += "| " + cell + " "
        line += "|"
        print(line)

"""
Reads and validates user input for row and column.

Ensures values are digits between 1 and 3. Returns zero-based indices.
"""
def read_row_col():
    valid = False

    while not valid:
        text = input()
        pieces = text.split()

        if len(pieces) == 2 and pieces[0].isdigit() and pieces[1].isdigit():
            row = int(pieces[0])
            col = int(pieces[1])

            if row >= 1 and row <= 3 and col >=1 and col <= 3:
                valid = True
            else:
                print("Please enter valid row and col numbers from 1 to 3:")
        else:
            print("Please enter valid row and col numbers from 1 to 3:")

    return row - 1, col - 1


"""
Checks whether the given player (X or O) has won.

Returns True if a winning condition is met.
"""
def winner_found(board, player):
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True

    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board [2][col] == player:
            return True
        
    if board[0][0] == player and board[1][1] == player and board [2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False
    

"""
Checks whether the game has ended in a tie, a tie occurs when no empty spaces remain and no one
has won.
"""
def tie_found(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False
    return True
    

"""
Switches the current player, X becomes O and O becomes X
"""
def swap_player(player):
    if player == "X":
        return "O"
    else:
        return "X"


"""
Runs a single game of Tic-Tac-Toe.
"""
def play():
    print("Let's play Tic-Tac-Toe!")
    print("When prompted, enter desired row and column numbers")
    print("Example: 1 3")
    print("| _ | _ | X |")
    print("| _ | _ | _ |")
    print("| _ | _ | _ |")
    print("Let's play!")
    print("Player X starts!")

    board = create_empty_board()
    current = "X"
    game_over = False
        
    while not game_over:
        print_board(board)
        print("Enter row and column for player " + current)
        row, col  = read_row_col()

        while board[row][col] != " ":
            print("That spot is full!")
            print("Please enter valid row and col numbers from 1 to 3:")
            row, col  = read_row_col()

        board[row][col] = current

        if winner_found(board, current):
            print_board(board)
            print("Player " + current + " WINS!")
            game_over = True

        elif tie_found(board):
            print_board(board)
            print("It's a TIE!")
            game_over = True
            
        else:
            current = swap_player(current)
            

"""
Asks the user if they want to play another game, returns True if yes and False otherwise
"""
def play_again():
    print("Do you want to play again? Y or N")
    answer = input().strip()

    while answer != "Y" and answer != "y" and answer != "N" and answer != "n":
        print("Please enter valid input: Y or N")
        print("Do you want to play again? Y or N")
        answer = input().strip()

    return answer == "Y" or answer == "y"

    #answer = input().strip()

    #if answer == "Y" or answer == "y":
    #    return True
    #elif answer == "N" or answer == "n":
    #    return False
    #else:
    #    print("Invalid input. Enter Y or N.")

              
"""
Controls overall game flow and continues playing until the user chooses not to.
"""
def main():
    keep_playing = True

    while keep_playing:
        play()
        keep_playing = play_again()
        
    print("Thanks for playing!")

if __name__ == "__main__":
    main()