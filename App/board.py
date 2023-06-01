'''
Console board
'''

import time
import copy
from pieces import *
from square import Square
from move_piece import Place, Move
from utils import B_DIMENSION
from pieces import Pawn, Knight, Bishop, Rook, Queen, King

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

        en_passant_empty = self.squares[final.col][final.row].square_state(check_type='empty')
        # update console
        # initial position will be empty
        self.squares[initial.col][initial.row].piece = None
        # final will hace 
        self.squares[final.col][final.row].piece = piece
            
        # Pawn promotion and en passant
        if isinstance(piece, Pawn):
            # Capture by en passant
            difference = final.col - initial.col
            if difference != 0 and en_passant_empty:
                # initial position will be empty
                self.squares[initial.col + difference][initial.row].piece = None
                # final will hace 
                self.squares[final.col][final.row].piece = piece

        # Pawn promotion
                        
        # castling
        if isinstance(piece, King):
            if self.castling(initial, final):
                difference = final.col - initial.col
                rook = piece.left_rook if (difference < 0) else piece.right_rook
                if rook.valid_moves:
                    self.move(rook, rook.valid_moves[-1])
                
                
        # Movement        
        piece.moved = True

        # clear valid moves 
        piece.clear_moves()

        # save last move
        self.last_move = move

    def valid_move(self, piece, move):
        return move in piece.valid_moves

    def castling(self, initial, final):
        return abs(initial.col - final.col) == 2

    def en_passant_to_true(self, piece):
        # if this is not a final move then en passant is not possible
        if not isinstance(piece, Pawn):
            return
        
        for row in range(B_DIMENSION):
            for col in range(B_DIMENSION):
                if isinstance(self.squares[col][row].piece, Pawn):
                    self.squares[col][row].piece.en_passant = False

        piece.en_passant = True

    def check(self, piece, move):
        temporary_piece = copy.deepcopy(piece)
        temporary_board = copy.deepcopy(self)
        # move piece
        temporary_board.move(temporary_piece, move)

        # Check the check
        for row in range(B_DIMENSION):
            for col in range(B_DIMENSION):
                if temporary_board.squares[col][row].square_piece(piece.color, p_type='enemy'):
                    p = temporary_board.squares[col][row].piece
                    # Bool = False is the condition to dont run Check Moves = Not eat the king
                    temporary_board.check_moves(p, col, row, Confirmation=False)
                    for m in p.valid_moves:
                        # if the final place has a King is a check
                        if isinstance(m.final.piece, King):
                            return True
        
        return False

    def check_moves(self, piece, col, row, Confirmation=True): 
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
                        
                        #check 
                        if Confirmation:
                            if not self.check(piece, move):
                                # Append new move 
                                piece.add_valid_moves(move)
                        else:
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
                        check_piece = self.squares[move_col][move_row].piece
                        final_position = Square(move_col, move_row, check_piece)
                        # Create a new move
                        move = Place(initial_position, final_position)
                        #check 
                        if Confirmation:
                            if not self.check(piece, move):
                                # Append new move 
                                piece.add_valid_moves(move)
                        else:
                            # Append new move 
                            piece.add_valid_moves(move)
            
            # En Passant moves
            r = 3 if piece.color == 'white' else 4
            final_row = 2 if piece.color == 'white' else 5
            # Left 
            if Square.in_board_range(col-1) and row == r:
                if self.squares[col-1][row].square_piece(piece.color, p_type='enemy'):
                    p = self.squares[col-1][row].piece
                    if isinstance(p, Pawn):
                        if p.en_passant:
                            # Create intial and final move
                            initial_position = Square(col, row)
                            final_position = Square(col-1, final_row, p)
                            # Create a new move
                            move = Place(initial_position, final_position)
                            #check 
                            if Confirmation:
                                if not self.check(piece, move):
                                    # Append new move 
                                    piece.add_valid_moves(move)
                            else:
                                # Append new move 
                                piece.add_valid_moves(move)
            
            # Right 
            if Square.in_board_range(col+1) and row == r:
                if self.squares[col+1][row].square_piece(piece.color, p_type='enemy'):
                    p = self.squares[col+1][row].piece
                    if isinstance(p, Pawn):
                        if p.en_passant:
                            # Create intial and final move
                            initial_position = Square(col, row)
                            final_position = Square(col+1, final_row, p)
                            # Create a new move
                            move = Place(initial_position, final_position)
                            #check 
                            if Confirmation:
                                if not self.check(piece, move):
                                    # Append new move 
                                    piece.add_valid_moves(move)
                            else:
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

            for move in valid_moves: 
                move_col, move_row = move

                if Square.in_board_range(move_col, move_row): 
                    # checking if the square of valid move is empty or has enemy piece
                    if self.squares[move_col][move_row].empty_or_foe(piece.color): 
                        # squares of new move
                        initial = Square(col, row)
                        check_piece = self.squares[move_col][move_row].piece
                        final = Square(move_col, move_row, check_piece) #piece=piece
                        # new move
                        move = Place(initial, final)
                        #check 
                        if Confirmation:
                            if not self.check(piece, move):
                                # Append new move 
                                piece.add_valid_moves(move)
                            else: break # if the knight is in check
                        else:
                            # Append new move 
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
                        check_piece = self.squares[move_col][move_row].piece
                        final_position = Square(move_col, move_row, check_piece)
                        # Create a new move
                        move = Place(initial_position, final_position)
                        # Append new move 
                        
                        # empty
                        if self.squares[move_col][move_row].square_state(check_type = 'empty'):
                            #check 
                            if Confirmation:
                                if not self.check(piece, move):
                                    # Append new move 
                                    piece.add_valid_moves(move)
                            else:
                                # Append new move 
                                piece.add_valid_moves(move)
                        # has enemy piece
                        elif self.squares[move_col][move_row].square_piece(piece.color, p_type='enemy'):
                            #check 
                            if Confirmation:
                                if not self.check(piece, move):
                                    # Append new move 
                                    piece.add_valid_moves(move)
                            else:
                                # Append new move 
                                piece.add_valid_moves(move)
                            break
                        
                        # has team piece
                        elif self.squares[move_col][move_row].square_piece(piece.color, p_type='teammate'):
                            break
                        
                        
                    # not in range
                    else:
                        break
                    
                    # incrementing incrs        
                    move_row = move_row + incr_row
                    move_col = move_col + incr_col
        
        def king_moves():
            adjs = [
                (col+0,row-1), # up
                (col+1,row-1), # up-right
                (col+1,row+0), # right 
                (col+1,row+1), # down-right 
                (col+0,row+1), # down 
                (col-1,row+1), # down-left 
                (col-1,row+0), # left 
                (col-1,row-1) # up-left 
            ]
            
            for move in adjs:
                move_col, move_row = move
                
                if Square.in_board_range(move_col, move_row):
                    # checking if the square of valid move is empty or has enemy piece
                    if self.squares[move_col][move_row].empty_or_foe(piece.color): 
                        # squares of new move
                        initial = Square(col, row)
                        final = Square(move_col, move_row) #piece=piece
                        # new move
                        move = Place(initial, final)
                        #check 
                        if Confirmation:
                            if not self.check(piece, move):
                                # Append new move 
                                piece.add_valid_moves(move)
                            else: 
                                if not self.check(piece, move):
                                    break
                                else:piece.add_valid_moves(move) ## AQUI
                        else:
                            # Append new move 
                            piece.add_valid_moves(move)
                        
        
            # Castling
            if not piece.moved:
                
                # Queen castling
                left_rook = self.squares[0][row].piece
                if isinstance(left_rook, Rook):
                    if not left_rook.moved:
                        for c in range(1, 4):
                            # Check if any piece is between 
                            if self.squares[c][row].square_state(check_type='piece'):
                                break
                            
                            if c == 3:
                                piece.left_rook = left_rook 
                                
                                # Rook Movemento
                                initial = Square(0, row)
                                final = Square(3, row)
                                move_rook = Place(initial, final)
                                # king movement
                                initial = Square(col, row)
                                final = Square(2, row)
                                move_king = Place(initial, final)
            
                                #check 
                                if Confirmation:
                                    if not self.check(piece, move_king) and not self.check(left_rook, move_rook):
                                        # Append new move rook
                                        left_rook.add_valid_moves(move_rook)
                                        # Append new move king 
                                        piece.add_valid_moves(move_king)
                                else:
                                    # Append new move rook
                                    left_rook.add_valid_moves(move_rook)
                                    # Append new move king
                                    piece.add_valid_moves(move_king)
            
                # King side castle
                right_rook = self.squares[7][row].piece
                if isinstance(right_rook, Rook):
                    if not right_rook.moved:
                        for c in range(5, 7):
                            # Check if any piece is between 
                            if self.squares[c][row].square_state(check_type='piece'):
                                break
                                
                            if c == 6:
                                piece.right_rook = right_rook 
                                    
                                # Rook Movemento
                                initial = Square(7, row)
                                final = Square(5, row)
                                move_rook = Place(initial, final)
                                    
                                # king movement
                                initial = Square(col, row)
                                final = Square(6, row)
                                move_king = Place(initial, final)
                                
                                #check 
                                if Confirmation:
                                    if not self.check(piece, move_king) and not self.check(right_rook, move_rook):
                                        # Append new move rook
                                        right_rook.add_valid_moves(move_rook)
                                        # Append new move king 
                                        piece.add_valid_moves(move_king)
                                else:
                                    # Append new move rook
                                    right_rook.add_valid_moves(move_rook)
                                    # Append new move king
                                    piece.add_valid_moves(move_king)
                                
        
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
