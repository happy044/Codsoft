import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == "O":
        return 10 - depth
    elif winner == "X":
        return depth - 10
    elif is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        return max_eval
        return max_eval
    else:
        min_eval = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        return min_eval
        return min_eval

def best_move(board):
    best_val = -math.inf
    move = (-1, -1)
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[row][col] = " "
                if move_val > best_val:
                    best_val = move_val
                    move = (row, col)
    return move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are X, and AI is O.")

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        # Human player's turn
        while True:
            try:
                human_move = input("Enter your move (row and column: 0 0 for top-left): ")
                row, col = map(int, human_move.split())
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell is already occupied. Choose another.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column as numbers between 0 and 2.")

        # Check for winner after human move
        winner = check_winner(board)
        if winner or is_full(board):
            print_board(board)
            if winner:
                print(f"{winner} wins!")
            else:
                print("It's a draw!")
            break

        # AI's turn
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"

if __name__ == "__main__":
    main()
