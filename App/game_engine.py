'''
Responsible for all rendering methods
'''

import pygame 
from board import Board
from move_piece import Move
from utils import B_DIMENSION, SQ_SIZE

class Game: 

    def __init__(self) -> None:
        self.board = Board()
        self.move = Move()

    def display_bg(self, surface): 
        '''
        Board rendering methods
        '''
        for col in range(B_DIMENSION):
            for row in range(B_DIMENSION):
                # if even board position
                if (col + row) % 2 == 0: 
                    color = (232, 235, 239) # light square RGB color
                else:
                    color = (125, 135, 150) # dark square RGB color

                # drawing board squares rectangle 
                sq_rect = (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)

                pygame.draw.rect(surface, color, sq_rect)
    
    def display_pieces(self, surface): 
        for col in range(B_DIMENSION):
            for row in range(B_DIMENSION):
                current_pos = self.board.squares[col][row]
                # check current state per square
                if current_pos.square_state():
                    piece = current_pos.piece

                    # render pieces if not moving
                    if piece is not self.move.piece:
                        piece.set_img()
                        img = pygame.image.load(piece.img_url) # load piece image
                        img_centered = col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2
                        piece.img_rect = img.get_rect(center=img_centered) # center image
                        surface.blit(img, piece.img_rect) # rendering pixel data to board

    def display_valid_moves(self, surface): 
        # piece is grabbed
        if self.move.moving: 
            piece = self.move.piece

            # loop valid moves
            for move in piece.valid_moves: 
                # color
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                # square rect
                rect = (move.final.col * SQ_SIZE, move.final.row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                # blit
                pygame.draw.rect(surface, color, rect)