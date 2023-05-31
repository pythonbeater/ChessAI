'''
Responsible for all game configurations and aspect
'''
import os
import pygame
from theme import Theme
from sounds import Sound

class Config:
    
    def __init__(self) -> None:
        # theme
        self.themes = []
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        # font
        self.font = pygame.font.SysFont('monospace', 18, bold=True)
        # sounds
        self.move_sound = Sound(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Assets', 'Sounds', 'Move.wav'))
        self.capture_sound = Sound(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Assets', 'Sounds', 'Capture.wav'))

    def change_theme(self): 
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]

    def _add_themes(self): 
        blue = Theme(
            light_bg = (232, 235, 239), 
            dark_bg = (125, 135, 150),
            light_trace = (244, 247, 116), 
            dark_trace = (172, 195, 51), 
            light_moves = '#C86464',
            dark_moves = '#C84646'
        )
        self.themes = [blue]