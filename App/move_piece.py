'''
Responsible for piece movement blit
'''

import pygame
from utils import SQ_SIZE

class Move: 

    def __init__(self):
        self.piece = None
        self.moving = False
        self.x, self.y = 0, 0
        self.init_row, self.init_col  = 0, 0

    def update_blit(self, surface): 
        # piece icon increases size
        self.piece.set_img(size=128)
        img_url = self.piece.img_url

        # render picked piece
        img = pygame.image.load(img_url)
        img_centered = (self.x, self.y)
        self.piece.img_rect = img.get_rect(center=img_centered) # center image
        surface.blit(img, self.piece.img_rect)

    def update_coor(self, pos: tuple): 
        self.x, self.y = pos 
    
    def save_init(self, pos: tuple): 
        # convert coordinates to position in board
        self.initial_row = pos[1] // SQ_SIZE
        self.initial_col = pos[0] // SQ_SIZE

    def move_piece(self, piece): 
        self.piece = piece
        self.moving = True
    
    def drop_move(self):
        self.piece = None
        self.moving = False