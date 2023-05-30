'''
Responsible for all game configurations and aspect
'''
import pygame
import os

class Config:
    
    def __init__(self) -> None:
        self.font = pygame.font.SysFont('monospace', 18, bold=True)