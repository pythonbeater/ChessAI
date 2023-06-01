import os
import pygame
from utils import WIDTH, HEIGHT


class Menu:
    def __init__(self):
        # Initialize the game
        pygame.init()

        # Create the game window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('ChessAI')
        
        # Define Fonts
        font_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Assets', 'Font', '8bit_wonder','8-BIT WONDER.TTF')
        self.font_name = font_path
        
        # backgroung image
        background_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Assets', 'Images', 'Menu Background','chess-icon-set.jpg')
        self.background = pygame.image.load(background_path).convert()
        
        # Define colors
        self.BLACK, self.WHITE, self.SELECTED = (0, 0, 0), (255, 255, 255), (134, 189, 62)
                
        # Define agent options and initial selection
        self.agents = ['Agent 1', 'Agent 2', 'Agent 3']
        self.selected_agent = 0

        # Callback function for starting the game
        self.start_game_callback = None

    
    def draw_text(self, text, size, x, y, selected=False):
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
    
    def draw_menu(self):
        
        # Background color
        background_scaled = pygame.transform.scale(self.background, (800, 600))
        self.screen.blit(background_scaled, (0, 100))
        
        self.draw_text('Welcome to Chess AI',40, WIDTH//2 , 40)
        self.draw_text('Choose an Agent',30, WIDTH//2 , 150)
        self.draw_text('Created by Daniel Franco and Joao Malho',10, WIDTH//2, 750)
        
        # Draw agents with highlighting for the selected agent
        for i in range(len(self.agents)):
            if i == self.selected_agent:
                self.draw_text(self.agents[i], 25, WIDTH//2, 250 + i * 100, selected=True)
            else:
                self.draw_text(self.agents[i], 25, WIDTH//2, 250 + i * 100)
        
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected_agent = (self.selected_agent + 1) % len(self.agents)
                elif event.key == pygame.K_UP:
                    self.selected_agent = (self.selected_agent - 1) % len(self.agents)
                elif event.key == pygame.K_RETURN:
                    if self.start_game_callback is not None:
                        self.start_game_callback(self.agents[self.selected_agent])
                
            elif event.type == pygame.QUIT:
                return False

        return True

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.draw_menu()

        pygame.quit()

    def set_start_game_callback(self, callback):
        self.start_game_callback = callback

