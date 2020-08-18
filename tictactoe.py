"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
import random

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
    playerX=0
    playerO=0

    for row in board:
        for col in row:
            if col == X:
                playerX += 1
            elif col == O:
                playerO += 1

    if playerX > playerO:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionsAvailable = set()
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] is EMPTY:
                actionsAvailable.add((row, column))
    return actionsAvailable


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    new_board = deepcopy(board)
    current_player = player(new_board)

    if new_board[i][j] is not EMPTY:
        raise Exception("Invalid action.")
    else:
        new_board[i][j] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for x in range(len(board)):
        if board[x][0] is not EMPTY and board[x][0] == board[x][1] == board[x][2]:
            return board[x][1]
        if board[x][0] is not EMPTY and board[0][x] == board[1][x] == board[2][x]:
            return board[0][x]

    if board[0][0] is not EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[1][1]
    if board[2][0] is not EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (terminal(board)):
        wb = winner(board)
        if wb == X:
            return 1
        elif wb == 0:
            return -1
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    optimal_action = None
    current_Player = player(board)

    if board == initial_state():
        optimal_action = (random.randint(0, 2), random.randint(0, 2))
        return optimal_action

    if current_Player == X:
        best_score = -math.inf
        for action in actions(board):
            returned_score = minimaxRecurse(result(board, action))
            if returned_score > best_score:
                best_score = returned_score
                optimal_action = action

    elif current_Player == O:
        best_score = math.inf
        for action in actions(board):
            returned_score = minimaxRecurse(result(board, action))
            if returned_score < best_score:
                best_score = returned_score
                optimal_action = action

    return optimal_action


def minimaxRecurse(board):
    if terminal(board):
        return utility(board)

    current_player = player(board)
    if current_player == X:
        bestScore = -math.inf
        for action in actions(board):
            bestScore = max(bestScore, minimaxRecurse(result(board, action)))
        return bestScore
    elif current_player == O:
        bestScore = math.inf
        for action in actions(board):
            bestScore = min(bestScore, minimaxRecurse(result(board, action)))
        return bestScore
