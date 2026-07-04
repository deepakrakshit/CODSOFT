def display_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_win(board, player):
    """Checks all 8 possible winning combinations for the given player."""
    win_paths = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for path in win_paths:
        if board[path[0]] == player and board[path[1]] == player and board[path[2]] == player:
            return True
    return False

def check_draw(board):
    """Returns True if there are no empty spaces left."""
    return ' ' not in board

def main():
    board = [' '] * 9
    current_player = 'X'
    
    print("Welcome to Tic-Tac-Toe! (Human vs Human)")
    print("Use numbers 1-9 to make a move (1 is top-left, 9 is bottom-right).")
    
    while True:
        display_board(board)
        
        # Get input and validate
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move, try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        # Apply move
        board[move] = current_player
        
        # Check game over conditions
        if check_win(board, current_player):
            display_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            break
            
        # Switch turns
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

if __name__ == "__main__":
    main()