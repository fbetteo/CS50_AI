"""
Tic Tac Toe Player
"""
import copy
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
    x_count = 0
    o_count = 0
    for i in range(3):
       for j in board[i]:
           if j == "X":
               x_count += 1
           elif j == "O":
               o_count += 1
           else:
               None
    if x_count == o_count:
        return "X"
    else:
        return "O"
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available = set()
    for i, row in enumerate(board):
       for j in range(3):
        if board[i][j] == EMPTY:
            available.add((i,j))
    return available

   

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if new_board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = player(board)
        return new_board
    else:
        raise Exception("Invalid move")



def transpose(board):
    new_board = copy.deepcopy(board)
    new_board = zip(*new_board)
    return new_board

def check_diagonal_winner(board, mark):
    off_diag = [board[i][i] for i in range(3)]
    main_diag = [board[i][2-i] for i in range(3)]
    return all(itm == mark for itm in off_diag) or all(itm == mark for itm in main_diag)

def winner_check(board, mark):
    return any(all(itm == mark for itm in row) for row in board)

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    transposed_board = transpose(board)
    if winner_check(board, X) or winner_check(transposed_board, X) or check_diagonal_winner(board, X):
        return X
    if winner_check(board, O) or winner_check(transposed_board, O) or check_diagonal_winner(board, O):
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) or all(all(itm != EMPTY for itm in row) for row in board)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    p = winner(board)
    if p == X:
        return 1
    elif p == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
