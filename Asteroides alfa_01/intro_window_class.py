import pygame
from settings import *

class IntroWindow:
    def __init__(self, game):
        self.game = game

    def update(self):
        pass

    def draw(self):
        self.draw_intro_window()

    def draw_intro_window(self):
        self.game.screen.fill('grey')
        pygame.draw.rect(self.game.screen, 'black', INTRO_RECT)