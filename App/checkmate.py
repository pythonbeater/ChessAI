import pygame
from utils import B_DIMENSION, WIDTH, HEIGHT

class Checkmate: 

    def __init__(self, screen) -> None:
        self.squares = [[0]*B_DIMENSION for col in range(B_DIMENSION)]
        self.screen = screen 
        
    def display_checkmate_message(self):
        font = pygame.font.SysFont(None, 60)
        text = font.render("Checkmate!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def checkmate(self, board):
        # Iterate over all the squares on the boarda
        for row in range(B_DIMENSION):
            for col in range(B_DIMENSION):
                square = board.squares[col][row]
                # Check if the square has a piece
                if square.piece is not None:
                    piece = square.piece

                # Calculate all valid moves for the piece
                board.check_moves(piece, col, row)

                # Get the list of valid moves for the piece
                possible_moves = piece.valid_moves
                
                if not possible_moves:
                    self.display_checkmate_message()                   
                
                else:
                    pass   