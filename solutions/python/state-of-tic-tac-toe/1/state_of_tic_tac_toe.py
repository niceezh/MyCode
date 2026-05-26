def win_x(board, x):
    if x * 3 in board:
        return True
    if board[0][0] == board[1][1] == board[2][2] == x:
        return True
    if board[0][2] == board[1][1] == board[2][0] == x:
        return True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == x:
            return True
    return False

def count_x(board, x):
    return board[0].count(x) + board[1].count(x) + board[2].count(x)

def gamestate(board):
    if count_x(board, "O") > count_x(board, "X"):
        raise ValueError("Wrong turn order: O started")
    if count_x(board, "X") - count_x(board, "O") > 1:
        raise ValueError("Wrong turn order: X went twice")
    if win_x(board, "X") and win_x(board, "O"):
        raise ValueError("Impossible board: game should have ended after the game was won")
    if win_x(board, "X") or win_x(board, "O"):
        return "win"
    if count_x(board, "X") + count_x(board, "O") == 9:
        return "draw"
    return "ongoing"

if __name__ == '__main__':
    print(gamestate(["OOX", "   ", "   "]))
