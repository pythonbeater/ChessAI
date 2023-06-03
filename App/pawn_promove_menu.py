import os
import pygame
from utils import WIDTH, HEIGHT
from pieces import Queen, Rook, Bishop, Knight


class PawnPromotionWindow:
    def __init__(self):
        self.selected_option = None
        self.window = None
        self.font = None
        
                # Create the game window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        

        # Define options and initial selection
        self.promotions = ["Queen", "Rook", "Bishop", "Knight"]
        self.selected_promotion = 0

        # Define Fonts
        font_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Assets', 'Font', '8bit_wonder','8-BIT WONDER.TTF')
        self.font_name = font_path
        
        # backgroung image
        background_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Assets', 'Images', 'Menu Background','chess-icon-set.jpg')
        self.background = pygame.image.load(background_path).convert()
        
        # Define colors
        self.BLACK, self.WHITE, self.SELECTED = (0, 0, 0), (255, 255, 255), (134, 189, 62)
                

    def draw_text_pawn(self, text, size, x, y, selected=False):
        if selected:
            font = pygame.font.Font(self.font_name, size)
            text_surface = font.render(text, True, self.SELECTED)
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y)
            self.screen.blit(text_surface, text_rect)
        else:
            font = pygame.font.Font(self.font_name, size)
            text_surface = font.render(text, True, self.WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y)
            self.screen.blit(text_surface, text_rect)
    
    def draw_menu_pawn(self):
        # Background color
        background_scaled = pygame.transform.scale(self.background, (800, 600))
        self.screen.blit(background_scaled, (0, 100))

        self.draw_text_pawn('Choose a Promotion', 30, WIDTH // 2, 150)

        # Draw promotions with highlighting for the selected option
        for i in range(len(self.promotions)):
            if i == self.selected_promotion:
                self.draw_text_pawn(self.promotions[i], 25, WIDTH // 2, 250 + i * 100, selected=True)
            else:
                self.draw_text_pawn(self.promotions[i], 25, WIDTH // 2, 250 + i * 100)

        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected_promotion = (self.selected_promotion + 1) % len(self.promotions)
                elif event.key == pygame.K_UP:
                    self.selected_promotion = (self.selected_promotion - 1) % len(self.promotions)
                elif event.key == pygame.K_RETURN:
                    self.selected_option = self.promotions[self.selected_promotion]
                    return False  # Exit the event loop and return the selected option

            elif event.type == pygame.QUIT:
                return False
        return True

    def handle_promotion(self, game, piece, target_col, target_row):
        # Create the appropriate piece object based on the selected promotion
        if self.selected_option == "Queen":
            promoted_piece = Queen(piece.color)
        elif self.selected_option == "Rook":
            promoted_piece = Rook(piece.color)
        elif self.selected_option == "Bishop":
            promoted_piece = Bishop(piece.color)
        elif self.selected_option == "Knight":
            promoted_piece = Knight(piece.color)

        # Update the game state with the promoted piece
        self.squares[target_col][target_row].piece = promoted_piece

        # Reset the selected option for future promotions
        self.selected_option = None
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.draw_menu_pawn()

        pygame.quit()