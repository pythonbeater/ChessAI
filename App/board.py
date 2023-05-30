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
        self.last_move = None
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def move(self, piece, move): 
        initial = move.initial
        final = move.final

        # update console
        # initial position will be empty
        self.squares[initial.col][initial.row].piece = None
        # final will hace 
        self.squares[final.col][final.row].piece = piece

        piece.moved = True

        # clear valid moves 
        piece.clear_moves()

        # save last move
        self.last_move = move

    def valid_move(self, piece, move):
        return move in piece.valid_moves
        
    def check_moves(self, piece, col, row): 
        '''
        Calculate all valid moves of a specific agent (piece) in a
        specific state (board position) given a specific environment 
        (board with other pieces)
        '''

        def pawn_moves():
            # Steps moved
            steps = 1 if piece.moved else 2

            # vertical moves
            start = row + piece.dir # row -1
            end = row + (piece.dir * (1 + steps)) # row + (-1 * (1 + steps))
            for move_row in range(start, end, piece.dir):
                if Square.in_board_range(move_row):
                    if self.squares[col][move_row].square_state(check_type = 'empty'):
                        # Create intial and final move
                        initial_position = Square(col, row)
                        final_position = Square(col, move_row)
                        # Create a new move
                        move = Place(initial_position, final_position)
                        # Append new move 
                        piece.add_valid_moves(move)
                    # When move is blocked
                    else:
                        break
                # Not in range
                else:
                    break
                        
            # Diagonal moves when eat piece
                # Steps are not necessary because diagonal will be only 1 step 
            move_row = row + piece.dir 
            move_col = [col-1, col+1]
            for move_col in move_col:
                if Square.in_board_range(move_col, move_row):
                    if self.squares[move_col][move_row].square_piece(piece.color, p_type='enemy'):
                        # Create intial and final move
                        initial_position = Square(col, row)
                        final_position = Square(move_col, move_row)
                        # Create a new move
                        move = Place(initial_position, final_position)
                        # Append new move 
                        piece.add_valid_moves(move)
            
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

        def straight_moves(incrs):
            '''
            Increments values to straight moves in pieces that move in full lines
            '''
            for incr in incrs:
                incr_col, incr_row = incr
                move_row = row + incr_row
                move_col = col + incr_col

                while True:
                    if Square.in_board_range(move_col, move_row):
                        # Create intial and final move
                        initial_position = Square(col, row)
                        final_position = Square(move_col, move_row)
                        # Create a new move
                        move = Place(initial_position, final_position)
                        # Append new move 
                        
                        # empty
                        if self.squares[move_col][move_row].square_state(check_type = 'empty'):
                            # Append new move
                            piece.add_valid_moves(move)
                        # has enemy piece
                        if self.squares[move_col][move_row].square_piece(piece.color, p_type='enemy'):
                            # Append new move
                            piece.add_valid_moves(move)
                            break
                        
                        # has team piece
                        if self.squares[move_col][move_row].square_piece(piece.color, p_type='teammate'):
                            break
                        
                        
                    # not in range
                    else:
                        break
                    
                    # incrementing incrs        
                    move_row = move_row + incr_row
                    move_col = move_col + incr_col
        
        def king_moves():
            valid_moves = [
                (col+0,row-1), # up
                (col+1,row-1), # up-right
                (col+1,row+0), # right 
                (col+1,row+1), # down-right 
                (col+0,row+1), # down 
                (col-1,row+1), # down-left 
                (col-1,row+0), # left 
                (col-1,row-1) # up-left 
            ]
            
            for move in valid_moves:
                move_col, move_row = move
                
                if Square.in_board_range(move_col, move_row):
                    # checking if the square of valid move is empty or has enemy piece
                    if self.squares[move_col][move_row].empty_or_foe(piece.color): 
                        # squares of new move
                        initial = Square(col, row)
                        final = Square(move_col, move_row) #piece=piece
                        # new move
                        move = Place(initial, final)
                        # append new valid move
                        piece.add_valid_moves(move)
        
            # Castle
            
            # Queen side castle
            
            # King side castle
        
        # check piece instance
        if isinstance(piece, Pawn): 
            pawn_moves()
            
        elif isinstance(piece, Knight): 
            knight_moves()

        elif isinstance(piece, Bishop): 
            straight_moves([
                (1, -1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (-1, 1), # down-left   
            ])

        elif isinstance(piece, Rook): 
            straight_moves([
                (0, -1), # up
                (1, 0), # left
                (0, 1), # down
                (-1, 0), # right
            ])

        elif isinstance(piece, Queen): 
            straight_moves([
                (1, -1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (-1, 1), # down-left 
                (0, -1), # up
                (1, 0), # left
                (0, 1), # down
                (-1, 0), # right
                ])

        elif isinstance(piece, King): 
            king_moves()

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
