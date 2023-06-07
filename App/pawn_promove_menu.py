import os
import pygame
from utils import WIDTH, HEIGHT
from pieces import Queen, Rook, Bishop, Knight

# To keep developing
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
                        return self.selected_option  # Return the selected option
                elif event.type == pygame.QUIT:
                    return None  # Return None to indicate quit event
            return True  # Return True to continue running

        def handle_promotion(self, piece):
            # Ensure piece has the color attribute
            if hasattr(piece, 'color'):
                piece_color = piece.color
            else:
                # Handle the case when piece.color is missing
                piece_color = "white"  # Provide a default color value

            # Create the appropriate piece object based on the selected promotion
            if self.selected_option == "Queen":
                promoted_piece = Queen(piece_color)
            elif self.selected_option == "Rook":
                promoted_piece = Rook(piece_color)
            elif self.selected_option == "Bishop":
                promoted_piece = Bishop(piece_color)
            elif self.selected_option == "Knight":
                promoted_piece = Knight(piece_color)
            else:
                # Handle the case when no option is selected
                promoted_piece = None

            # Return the promoted piece
            return promoted_piece
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.draw_menu_pawn()

        pygame.quit()