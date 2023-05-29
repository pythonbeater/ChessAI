'''
Calculation of all valid moves of a specific agent (piece) in a specific state (board position)
given a specific environment (board with other pieces) given chess dynamics
'''

from itertools import product
from pieces import Pawn, Knight, Bishop, Rook, Queen, King


def knight_moves(piece, col, row):
    valid_moves = [
        (col + 1, row - 2),
        (col - 1, row - 2)
        (col - 2, row - 1),
        (col + 2, row - 1),
        (col + 2, row + 1),
        (col - 2, row + 1),
        (col + 1, row + 2),
        (col - 1, row + 2)
    ]


def check_moves(piece, col, row): 
    '''
    Calculate all valid moves of a specific agent (piece) in a
    specific state (board position) given a specific environment 
    (board with other pieces)
    '''

    # check piece instance
    if isinstance(piece, Pawn): 
        pass

    elif isinstance(piece, Knight): 
        knight_moves()

    elif isinstance(piece, Bishop): 
        pass

    elif isinstance(piece, Rook): 
        pass

    elif isinstance(piece, Queen): 
        pass

    elif isinstance(piece, King): 
        pass


