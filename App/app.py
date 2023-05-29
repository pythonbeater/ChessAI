'''
This is the main driver file. Responsible for running the App
'''

import sys
import pygame
from square import Square
from move_piece import Place
from game_engine import Game
from utils import WIDTH, HEIGHT, B_DIMENSION, SQ_SIZE, MAX_FPS

class App:

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # setting window dimensions
        pygame.display.set_caption('ChessAI') # window name
        self.game = Game()
        self.clock = pygame.time.Clock()


    def mainloop(self):

        screen = self.screen
        clock = self.clock
        game = self.game
        board = game.board
        move = game.move


        while True:
            game.display_bg(screen) # always display background
            game.display_valid_moves(screen) #DIFF
            game.display_pieces(screen)

            if move.moving: 
                move.update_blit(screen)

            clock.tick(MAX_FPS)

            for event in pygame.event.get():
                ### moving pieces ###
                # click event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    move.update_coor(event.pos)

                    # convert coordinates to position in board
                    clicked_row = move.y // SQ_SIZE
                    clicked_col = move.x // SQ_SIZE
                    
                    # if clicked square has piece
                    if board.squares[clicked_col][clicked_row].square_state():
                        
                        piece = board.squares[clicked_col][clicked_row].piece

                        # check available moves
                        board.check_moves(piece, clicked_col, clicked_row)

                        # save initial position to return if invalid move
                        move.save_init(event.pos)

                        # save piece representation
                        move.move_piece(piece)

                        game.display_bg(screen)
                        game.display_valid_moves(screen)
                        game.display_pieces(screen)
                        
                # mouse motion event
                elif event.type == pygame.MOUSEMOTION: 
                    if move.moving:
                        move.update_coor(event.pos)
                        game.display_bg(screen)
                        game.display_valid_moves(screen)
                        game.display_pieces(screen)
                        move.update_blit(screen)
            
                # release click event
                elif event.type == pygame.MOUSEBUTTONUP:
                                        
                    if move.moving:
                        move.update_coor(event.pos)

                        released_col = move.x // SQ_SIZE
                        released_row = move.y // SQ_SIZE

                        # create valid move
                        initial = Square(move.init_col, move.init_row)
                        final = Square(released_col, released_row)
                        place = Place(initial, final)

                        if board.valid_move(move.piece, place):
                            board.move(move.piece, place)

                            game.display_bg(screen)
                            game.display_pieces(screen)
                    
                    move.drop_move()

                ######################

                # moving window event: 
                elif event.type == pygame.ACTIVEEVENT:
                    clock.tick(MAX_FPS // 2)
                    
                # close app event
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update() # screen update


app = App()
app.mainloop()