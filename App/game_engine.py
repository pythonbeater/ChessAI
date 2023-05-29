'''
Responsible for all rendering methods
'''

import pygame 
from board import Board
from move_piece import Move
from utils import WIDTH, HEIGHT, B_DIMENSION, SQ_SIZE

class Game: 

    def __init__(self):
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
