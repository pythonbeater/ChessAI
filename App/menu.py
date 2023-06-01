import pygame
from utils import WIDTH, HEIGHT


class Menu:
    def __init__(self):
        # Initialize the game
        pygame.init()
        
        # Create the game window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Agent Selection')
        
        # Define Fonts
        self.font = pygame.font.SysFont('arialblack', 40)
        
        # Define colors
        self.TEXT_COLOR = (255, 255, 255)
        self.SELECTED_COLOR = (0, 255, 0)
        
        # Define agent options and initial selection
        self.agents = ['Agent 1', 'Agent 2', 'Agent 3']
        self.selected_agent = 0

        # Callback function for starting the game
        self.start_game_callback = None

    def draw_text(self, text, x, y, selected=False):
        if selected:
            color = self.SELECTED_COLOR
        else:
            color = self.TEXT_COLOR
        img = self.font.render(text, True, color)
        self.screen.blit(img, (x, y))
        
    def draw_menu(self):
        # Background color
        self.screen.fill((52, 78, 91))
        
        self.draw_text('Choose an Agent:', 100, 50)
        
        # Draw agents with highlighting for the selected agent
        for i in range(len(self.agents)):
            if i == self.selected_agent:
                self.draw_text(self.agents[i], 250, 150 + i * 100, selected=True)
            else:
                self.draw_text(self.agents[i], 250, 150 + i * 100)
        
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

