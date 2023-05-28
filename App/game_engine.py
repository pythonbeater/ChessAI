'''
Responsible for rendering methods
'''
import pygame 
from utils import WIDTH, HEIGHT, B_DIMENSION, SQ_SIZE

class Game: 

    def __init__(self):
        pass

    def display_bg(self, surface): 
        '''
        Board rendering methods
        '''
        for col in range(B_DIMENSION):
            for row in range(B_DIMENSION):
                if (col + row) % 2 == 0: # if even board position
                    color = (232, 235, 239) # light square RGB color
                else: 
                    color = (125, 135, 150) # dark square RGB color

                # drawing board squares 
                square = (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)

                pygame.draw.rect(surface, color, square)
