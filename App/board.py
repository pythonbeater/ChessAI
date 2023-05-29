'''
Console board
'''

from pieces import *
from square import Square
from utils import B_DIMENSION

class Board: 

    def __init__(self):
        # board 2d array
        self.squares = [[0]*B_DIMENSION for col in range(B_DIMENSION)]

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def _create(self): 
        # adding object to squares
        for col in range(B_DIMENSION):
            for row in range(B_DIMENSION):
                self.squares[col][row] = Square(col, row)

    def _add_pieces(self, color): 
        # pieces row based on color
        pawns_row, others_row = (B_DIMENSION-2, B_DIMENSION-1) if color == 'white' else (1, 0)

        # adding pawns to board
        for col in range(B_DIMENSION): 
            self.squares[col][pawns_row] = Square(col, pawns_row, Pawn(color))
            
        # adding rooks to board
        self.squares[0][others_row] = Square(0, others_row, Rook(color))
        self.squares[7][others_row] = Square(7, others_row, Rook(color))
        # adding knights to board
        self.squares[1][others_row] = Square(1, others_row, Knight(color))
        self.squares[6][others_row] = Square(6, others_row, Knight(color))
        # adding bishops to board
        self.squares[2][others_row] = Square(2, others_row, Bishop(color))
        self.squares[5][others_row] = Square(5, others_row, Bishop(color))
        # adding queen to board
        self.squares[3][others_row] = Square(3, others_row, Queen(color))
        # adding king to board
        self.squares[4][others_row] = Square(4, others_row, King(color))
