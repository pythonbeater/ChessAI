'''
Console board
'''

from pieces import *
from square import Square
from move_piece import Place
from utils import B_DIMENSION
from pieces import Pieces, Pawn, Knight, Bishop, Rook, Queen, King

class Board: 

    def __init__(self) -> None:
        # board 2d array
        self.squares = [[0]*B_DIMENSION for col in range(B_DIMENSION)]

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

        
    def check_moves(self, piece, col, row): 
        '''
        Calculate all valid moves of a specific agent (piece) in a
        specific state (board position) given a specific environment 
        (board with other pieces)
        '''

        def knight_moves():
            valid_moves = [
                (col + 1, row - 2), 
                (col - 1, row - 2), 
                (col - 2, row - 1), 
                (col + 2, row - 1), 
                (col + 2, row + 1), 
                (col - 2, row + 1), 
                (col - 1, row + 2),
                (col + 1, row + 2)
            ]

            for valid in valid_moves: 
                valid_col, valid_row = valid

                if Square.in_board_range(valid_col, valid_row): 
                    # checking if the square of valid move is empty or has enemy piece
                    if self.squares[valid_col][valid_row].empty_or_foe(piece.color): 
                        # squares of new move
                        initial = Square(col, row)
                        final = Square(valid_col, valid_row) #piece=piece
                        # new move
                        move = Place(initial, final)
                        # append new valid move
                        piece.add_valid_moves(move)

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
