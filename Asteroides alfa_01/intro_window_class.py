import pygame
from settings import *
from button_class import *

class IntroWindow:
    def __init__(self, game):
        self.game = game
        self.play_button = Button((10, 50), (100, 50), 'white', 'black', 'Play', 32 )

    def update(self):
        pass

    def draw(self):
        self.draw_intro_window()

    def draw_intro_window(self):
        self.game.screen.fill('grey')
        pygame.draw.rect(self.game.screen, 'black', INTRO_RECT)
