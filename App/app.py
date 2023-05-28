'''
This is the main driver file. Responsible for
'''

import sys
import pygame
from game_engine import Game
from utils import WIDTH, HEIGHT, B_DIMENSION, SQ_SIZE

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # setting window dimensions
        pygame.display.set_caption('ChessAI') # window name
        self.game = Game()


    def mainloop(self):
        while True:
            self.game.display_bg(self.screen) # always display background

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # if user closes game window
                    pygame.quit()
                    sys.exit()

            pygame.display.update() # screen update


main = Main()
main.mainloop()