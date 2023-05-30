'''
Responsible for all rendering methods
'''

import pygame
from pygame.locals import *
from board import Board
from move_piece import Move
from utils import B_DIMENSION, SQ_SIZE, WIDTH, HEIGHT
from config import Config
from pieces import *
import sys


class Game: 

    def __init__(self) -> None:
        self.player_order = 'white'
        self.hovered_square = None
        self.board = Board()
        self.move = Move()
        self.config = Config()

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
                
                '''
                # Coordinates
                if col == 0:
                    label = self.config.font.render(str(B_DIMENSION - row), 1, color)
                    label_position = (5, 5 + row * SQ_SIZE)
                    
                    surface.blit(label, label_position)
                ''' 
                    
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
    
    def display_last_move(self, surface):
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final
                
            for position in [initial, final]:
                # color
                color = (244, 247, 116) if (position.row + position.col) % 2 == 0 else (172, 195, 51)
                # square rect
                rect = (position.col * SQ_SIZE, position.row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                # blit
                pygame.draw.rect(surface, color, rect)
                
    def display_hover(self, surface):
        if self.hovered_square:
            # color
            color = (180, 180, 180)
            # square rect
            rect = (self.hovered_square.col * SQ_SIZE, self.hovered_square.row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
            # blit
            pygame.draw.rect(surface, color, rect, width= 3)
                
    def next_turn(self):
        self.player_order = 'white' if self.player_order == 'black' else 'black'
        
    def set_hover(self, col, row):
        self.hovered_square = self.board.squares[col][row]
        
        
    def restart(self):
        self.__init__()
        
    
    def promotion_confirm(self, piece, final, surface):
        if final.row == 0 or final.row == 7:
            promotion_window_open = True
            while promotion_window_open:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = event.pos
                        window_x = (WIDTH - 200) // 2
                        window_y = (HEIGHT - 150) // 2
                        if (
                            window_x <= mouse_x <= window_x + 200 and
                            window_y <= mouse_y <= window_y + 150
                        ):
                            option_index = (mouse_y - window_y) // 30
                            promotion_options = ["Queen", "Rook", "Bishop", "Knight"]
                            promotion_piece = promotion_options[option_index]
                            if promotion_piece == "Queen":
                                self.squares[final.row][final.col].piece = Queen(piece.color)
                            elif promotion_piece == "Rook":
                                self.squares[final.row][final.col].piece = Rook(piece.color)
                            elif promotion_piece == "Bishop":
                                self.squares[final.row][final.col].piece = Bishop(piece.color)
                            elif promotion_piece == "Knight":
                                self.squares[final.row][final.col].piece = Knight(piece.color)
                            promotion_window_open = False
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
                # Update the screen to display the promotion window
                self.display_promotion_window(surface)
                pygame.display.update()
    
    def display_promotion_window(self, surface):
        # Background color of the promotion window
        color = (255, 255, 255)
        # Text color for the promotion options
        text_color = (0, 0, 0)
        # Font for the promotion options
        font = pygame.font.Font(None, 32)
        # Width and height of the promotion window
        window_width = 200
        window_height = 150
        # Position of the top-left corner of the promotion window
        window_x = (WIDTH - window_width) // 2
        window_y = (HEIGHT - window_height) // 2

        # Create promotion window
        window_surface = pygame.Surface((window_width, window_height))
        window_surface.fill(color)

        # Display the promotion options
        promotion_options = ["Queen", "Rook", "Bishop", "Knight"]
        option_y = 30
        
        for option in promotion_options:
            text_surface = font.render(option, True, text_color)
            text_rect = text_surface.get_rect(center=(window_width // 2, option_y))
            window_surface.blit(text_surface, text_rect)
            option_y += 30

        # Display the promotion window on the main screen
        surface.blit(window_surface, (window_x, window_y))


