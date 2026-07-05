import random

def display_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_win(board, player):
    win_paths = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for path in win_paths:
        if board[path[0]] == player and board[path[1]] == player and board[path[2]] == player:
            return True
    return False

def check_draw(board):
    return ' ' not in board

def get_random_ai_move(board):
    """Finds all empty spaces and selects one randomly."""
    empty_spaces = []
    for i in range(9):
        if board[i] == ' ':
            empty_spaces.append(i)
    return random.choice(empty_spaces)

def main():
    board = [' '] * 9
    human = 'X'
    ai = 'O'
    
    print("Welcome to Tic-Tac-Toe! (Human vs Basic AI)")
    print("You are X.")
    print("The AI is O.")
    
    while True:
        display_board(board)
        
        # --- Human Turn ---
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        board[move] = human
        
        if check_win(board, human):
            display_board(board)
            print("You won!")
            break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            break
            
        # --- AI Turn ---
        print("AI is making a move...")
        ai_move = get_random_ai_move(board)
        board[ai_move] = ai
        
        if check_win(board, ai):
            display_board(board)
            print("AI wins!")
            break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()