def display_board(board):
    """Prints the current state of the board in a 3x3 grid."""
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def main():
    # Initialize an empty board with 9 spaces
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    
    print("Welcome to Tic-Tac-Toe!")
    print("Board successfully initialized:")
    display_board(board)

if __name__ == "__main__":
    main()