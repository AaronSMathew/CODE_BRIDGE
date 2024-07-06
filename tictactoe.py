import random


# Initialize the board
def init_board():
    return [" " for _ in range(9)]


# Print the board
def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i : i + 3]))
        if i < 6:
            print("---------")


# Check if a player has won
def check_win(board, player):
    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],  # Rows
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  # Columns
        [0, 4, 8],
        [2, 4, 6],  # Diagonals
    ]
    return any(
        all(board[i] == player for i in condition) for condition in win_conditions
    )


# Check if the board is full
def is_full(board):
    return " " not in board


# Get available moves
def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == " "]


# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_win(board, "O"):
        return 1
    if check_win(board, "X"):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for move in get_available_moves(board):
            board[move] = "O"
            score = minimax(board, depth + 1, False)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for move in get_available_moves(board):
            board[move] = "X"
            score = minimax(board, depth + 1, True)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score


# Get best move for AI
def get_best_move(board):
    best_score = float("-inf")
    best_move = None
    for move in get_available_moves(board):
        board[move] = "O"
        score = minimax(board, 0, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


# Main game loop
def play_game():
    board = init_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, and the AI is O.")
    print_board(board)

    while True:
        # Human player's turn
        while True:
            try:
                move = int(input("Enter your move (0-8): "))
                if move not in get_available_moves(board):
                    raise ValueError
                break
            except ValueError:
                print("Invalid move. Try again.")

        board[move] = "X"
        print_board(board)

        if check_win(board, "X"):
            print("You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        # AI's turn
        print("AI is thinking...")
        ai_move = get_best_move(board)
        board[ai_move] = "O"
        print(f"AI chose position {ai_move}")
        print_board(board)

        if check_win(board, "O"):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break


if __name__ == "__main__":
    play_game()
