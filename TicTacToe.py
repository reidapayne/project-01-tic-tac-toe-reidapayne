def play():
    
    def game_intro():
        print("Let's play Tic-Tac-Toe!")
        print("When prompted, enter desired row and column numbers")
        print("Example: 1 3")
        print()
    

    def create_empty_board():
        board = []
        for _ in range(3):
            row = []
            for _ in range(3):
                row.append(" ")
            board.append(row)
        return board
    return board


    def print_board(board):
        # Will look like:
        # | _ | _ | X |
        # | _ | _ | _ |
        # | _ | _ | _ |

        for row in range(3):
            for col in range(3):
                cell = board[row][col]
                if cell == " ":
                    cell_to_show = "_"
                else:
                    cell_to_show = cell
                line = line + "| " + cell_to_show + " "
            line = line + "|"
            print(line)
        print()


    def read_row_col():
        valid = False
        row = 0
        col = 0

        while not valid:
            text = input("Enter row and column (1 - 3), seperated by a space: ").strip()
            pieces = text.split()
            if len(pieces) == 2:
                a = pieces[0]
                b = pieces[1]
                if a.isdigit() and b.isdigit():
                    row = int(a)
                    col = int(b)
                    if row >= 1 and row is <= 3 and col >=1 and c <= 3:
                        return row - 1 , col - 1
            print("Invalid input. Examples 1 3 (rows ad columns are 1 to 3).")
    

    def winner_found(board, player):
        for row in range(3):
            if board[0][col] == player and board[row][1] == player and board[row][2] == player:
                return True
        for col in range(3):
            if board[0][col] == player and board[1][col] == player and board [2][col] == player:
                return True
        
        if board[0][0] == player and board[1][1] == player and board [2][2] == player:
            return True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True
        return False
    
    def tie_found():
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    return False
        return True
    
    def swap_player():
        if player == "X":
            return "0"
        else:
            return "X"
    def check_play():
        game_intro()
        board = create_empty_board()
        current = "X"
        game_over = False
        
        while not game_over:
            print_board(board)
            print("Player " + current + "'s turn.")
            row, col  = read_row_col

            if board[row][col] != " ":
                print("That spot is already taken. Try again.")
                continue
            
            board[row][col] = current

            if winner_found(board, current):
                print_board(board)
                print("Player " + current + "wins! Game Over.")
                game_over = True

            elif tie_found(board):
                print_board(board)
                print("It's a tie! Game Over.")
                game_over = True
            
            else:
                current_player = swap_player(current_player)
            
            
    def play_again():
        while True:
            answer = input("Play again? (Y/N)":).strip()
                if answer == "Y" or answer == "y":
                    return True
                elif answer ==  "N" or answer == "n":
                    return False
                else:
                    print("Invalid input. Please enter Y or N".)
                

    def main():
        keep_playing = True
        while keep_playing:
            play()
            keep_playing = play_again()
        
        print("Thanks for playing!")


if __name__ == "__main__":
    play()
