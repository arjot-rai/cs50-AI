"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0
    count_empty = 0

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == X:
                count_x += 1
            elif board[i][j] == O:
                count_o += 1
            else:
                count_empty += 1
    if count_empty == 0:
        return X
    elif count_x == count_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allowed_moves = set()

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                allowed_moves.add((i, j))

    return allowed_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    allowed_actions = actions(board)

    if action not in allowed_actions:
        raise Exception

    p = player(board)

    new_board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]

    for i in range(0, 3):
        for j in range(0, 3):
            if (i, j) == action:
                new_board[i][j] = p
            else:
                new_board[i][j] = board[i][j]

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(0, 3):
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] is not EMPTY:
            return board[i][0]
        if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] is not EMPTY:
            return board[0][i]
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] is not None:
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]) and board[2][0] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    w = winner(board)
    if w == X or w == O:
        return True
    if len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)

    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        p = player(board)
        moves = actions(board)
        best_move = -1
        if p == X:
            best_val = -math.inf
            for move in moves:
                new_board = result(board, move)
                if winner(board) == X:
                    return move
                new_val = helperMinimax(new_board, -math.inf, math.inf)
                if best_val < new_val:
                    best_move = move
                    best_val = new_val
            return best_move
        else:
            best_val = math.inf
            for move in moves:
                new_board = result(board, move)
                if winner(board) == O:
                    return O
                new_val = helperMinimax(new_board, -math.inf, math.inf)
                if best_val > new_val:
                    best_move = move
                    best_val = new_val
            return best_move

def helperMinimax(board, alpha, beta):
    if terminal(board):
        return utility(board)

    p = player(board)

    if p == X:
        max_val = -math.inf
        moves = actions(board)
        for move in moves:
            new_board = result(board, move)
            value = helperMinimax(new_board, alpha, beta)
            max_val = max(max_val, value)
            alpha = max(alpha, max_val)
            if beta <= alpha:
                break
        return max_val
    else:
        min_val = math.inf
        moves = actions(board)
        for move in moves:
            new_board = result(board, move)
            value = helperMinimax(new_board, alpha, beta)
            min_val = min(min_val, value)
            beta = min(beta, min_val)
            if beta <= alpha:
                break
        return min_val


