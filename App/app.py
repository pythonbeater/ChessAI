'''
This is the main driver file. Responsible for running the App
'''

import sys
import pygame
from config import Config
from square import Square
from menu import Menu
from move_piece import Place
from game_engine import Game
from utils import WIDTH, HEIGHT, SQ_SIZE, MAX_FPS
#from ai_agents_models import RandomAgent
from ai_agents_models import RandomAgent, BestMovementAgent
from checkmate import Checkmate

class App:

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # setting window dimensions
        pygame.display.set_caption('ChessAI') # window name
        self.game = Game()
        self.clock = pygame.time.Clock()
        self.config = Config()
        self.menu = None
        self.menu_active = False
        self.promotion_window = None
        self.checkmate = Checkmate(self.screen)
        
    def mainloop(self, selected_agent):
        running = True
        while running:
            # Run Menu
            if self.menu_active:
                running = self.menu.run()
            else:
                running = self.run_game(selected_agent)
            
    def run_game(self, selected_agent):
        
        screen = self.screen
        clock = self.clock
        game = self.game
        board = self.game.board
        move = self.game.move
        random_agent = RandomAgent('black')
        best_mov_agent = BestMovementAgent('black')
        
        
        game.display_bg(screen) # always display background
        game.display_last_move(screen)
        game.display_valid_moves(screen)
        game.display_pieces(screen)
        game.display_hover(screen)
        if move.moving: 
            move.update_blit(screen)

        clock.tick(MAX_FPS)
        
        for event in pygame.event.get():
            
            ### moving pieces ###
            # Agent implementation
            if game.player_order == 'white':
                # click event
                if event.type == pygame.MOUSEBUTTONDOWN:


                    move.update_coor(event.pos)
                    
                    # convert coordinates to position in board
                    clicked_row = move.y // SQ_SIZE
                    clicked_col = move.x // SQ_SIZE
                            
                    # if clicked square has piece
                    if board.squares[clicked_col][clicked_row].square_state(check_type='piece'):
                        # check- if has a piece
                        piece = board.squares[clicked_col][clicked_row].piece
                        # check valid piece color
                        if piece.color == game.player_order:
                            # check available moves
                            board.check_moves(piece, clicked_col, clicked_row, Confirmation=True)
                            # save initial position to return if invalid move
                            move.save_init(event.pos)
                            # save piece representation
                            move.move_piece(piece)
                            game.display_bg(screen)
                            game.display_last_move(screen)
                            game.display_valid_moves(screen)
                            game.display_pieces(screen)

                # mouse motion event
                elif event.type == pygame.MOUSEMOTION:
                    mot_row = event.pos[1] // SQ_SIZE
                    mot_col = event.pos[0] // SQ_SIZE
                        
                    game.set_hover(mot_col, mot_row)
                        
                    if move.moving:
                        move.update_coor(event.pos)
                        game.display_bg(screen)
                        game.display_last_move(screen)
                        game.display_valid_moves(screen)
                        game.display_pieces(screen)
                        game.display_hover(screen)
                        move.update_blit(screen)
                
                # release click event
                elif event.type == pygame.MOUSEBUTTONUP:
                        
                    if move.moving:
                        move.update_coor(event.pos)
                        board.en_passant_to_true(move.piece)
                        released_col = move.x // SQ_SIZE
                        released_row = move.y // SQ_SIZE

                        # create valid move
                        initial = Square(move.initial_col, move.initial_row)
                        final = Square(released_col, released_row)
                        place = Place(initial, final)
                        
                        if board.valid_move(move.piece, place):
                            captured = board.squares[released_col][released_row].square_state(check_type='piece')
                            board.move(move.piece, place)
                            game.sound_effect(captured)
                            game.display_bg(screen)
                            game.display_last_move(screen)
                            game.display_pieces(screen)
                            # next turn
                            game.next_turn()
                            
                        
                    move.drop_move()
                    
                    
                    # # Handle pawn promotion if the promotion window is active
                    # if self.promotion_window:
                    #     while True:
                    #         if not self.promotion_window.handle_events():
                    #             # Promotion option selected, update game state
                    #             selected_option = self.promotion_window.selected_option
                    #             if selected_option:
                    #                 self.promotion_window.handle_promotion(self.game, move.piece, released_col, released_row)
                    #                 self.promotion_window = None
                    #             break
                    #             ######################

                # moving window event: 
                elif event.type == pygame.ACTIVEEVENT:
                    clock.tick(MAX_FPS // 2)
                        
                # Keys Function
                elif event.type == pygame.KEYDOWN:
                        
                # Restart game
                    if event.key == pygame.K_r: # Key R
                        game.restart()
                        game = self.game
                        board = self.game.board
                        move = self.game.move
                                        
                # close app event
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            # Agent implementation
            elif game.player_order == 'black':
                if selected_agent == 'Random Ai Agent':
                    random_agent.make_move(board)
                
                elif selected_agent == 'Best Movement Agent':
                    best_mov_agent.make_move(board)
                
                else:
                    print('agent not implemented yet') 
                
                game.next_turn()  

            # Checkmate check
            elif self.checkmate.checkmate(board):
                self.checkmate.display_checkmate_message()
                            
            
        pygame.display.update() # screen update
        return True

    ### To keep developing
    
#    def open_promotion_window(self):
#        self.promotion_window = PawnPromotionWindow()
#        self.promotion_window.draw_menu_pawn()
    
    def start_menu(self):
        self.menu = Menu()
        self.menu.set_start_game_callback(self.start_game)
        self.menu_active = True
        
    def start_game(self, selected_agent):
        self.menu_active = False
        print('Selected Agent:', selected_agent)
        self.mainloop(selected_agent)

app = App()
app.start_menu()
selected_agent = 'Random Ai Agent'
app.mainloop(selected_agent)