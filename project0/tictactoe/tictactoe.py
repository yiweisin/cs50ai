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
    count = 0
    for i in board:
        for j in i:
            if j == EMPTY:
                count += 1
    if count %2 == 0:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ac = set()
    row = 0
    for i in board:
        cell = 0
        for j in i:
            if j == EMPTY:
                ac.add((row, cell))
            cell += 1
        row += 1
    return ac


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    b = [row[:] for row in board]
    if b[action[0]][action[1]] != EMPTY or action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise Exception
    else:
        b[action[0]][action[1]] = player(b)
    return b

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in board:
        if i[0] == i[1] == i[2] != EMPTY:
            return i[0]
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]
    if board[1][1] != EMPTY:
        if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
            return board[1][1]
    return None
    
            


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for i in board:
        if EMPTY in i:
            if winner(board) == None:
                return False
    return True
        


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    if terminal(board):
        return None
    return minimax2(board)[0]

def minimax2(board):  
    max = -float('inf')  
    opAction = None
    if player(board) == X:
        for action in actions(board):
            if terminal(result(board, action)):
                value = utility(result(board, action))
            else:
                value = minimax2(result(board, action))[1]
        
            if value > max:  
                max = value
                opAction = action
        value = max
    
    elif player(board) == O:
        min = float('inf')
        for action in actions(board):
            if terminal(result(board, action)):
                value = utility(result(board, action))
            else:
                value = minimax2(result(board, action))[1]
        
            if value < min:  
                min = value
                opAction = action
        value = min
  
    return opAction ,value

            

        
        
            
    
        
            
        
                    
                


        
