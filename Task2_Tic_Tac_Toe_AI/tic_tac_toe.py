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

def get_empty_spaces(board):
    """Returns a list of indices that are currently empty."""
    empty_spaces = []
    for i in range(9):
        if board[i] == ' ':
            empty_spaces.append(i)
    return empty_spaces

def minimax(board, depth, is_maximizing, ai_player, human_player):
    """Recursive algorithm to find the optimal move."""
    # Terminal states (Base cases)
    if check_win(board, ai_player):
        return 10 - depth # Favor faster wins
    if check_win(board, human_player):
        return depth - 10 # Favor slower losses
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -1000
        for move in get_empty_spaces(board):
            board[move] = ai_player
            score = minimax(board, depth + 1, False, ai_player, human_player)
            board[move] = ' ' # Undo move
            if score > best_score:
                best_score = score
        return best_score
    else:
        best_score = 1000
        for move in get_empty_spaces(board):
            board[move] = human_player
            score = minimax(board, depth + 1, True, ai_player, human_player)
            board[move] = ' ' # Undo move
            if score < best_score:
                best_score = score
        return best_score

def get_best_move(board, ai_player, human_player):
    """Evaluates all possible moves and returns the optimal one."""
    best_score = -1000
    best_move = 0
    
    for move in get_empty_spaces(board):
        board[move] = ai_player
        score = minimax(board, 0, False, ai_player, human_player)
        board[move] = ' ' # Undo move
        
        if score > best_score:
            best_score = score
            best_move = move
            
    return best_move

def main():
    board = [' '] * 9
    human = 'X'
    ai = 'O'
    
    print("Welcome to Tic-Tac-Toe!")
    print("You are X.")
    print("The computer is O.")
    
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
            print("Congratulations! You win!")
            break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            break
            
        # --- AI Turn ---
        print("AI is calculating the optimal move...")
        ai_move = get_best_move(board, ai, human)
        board[ai_move] = ai
        
        if check_win(board, ai):
            display_board(board)
            print("AI wins! Better luck next time.")
            break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()