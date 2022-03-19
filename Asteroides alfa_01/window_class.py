import pygame
from settings import *

class Window:
    def __init__(self, game, rect, color, bg_color):
        self.game = game
        self.rect = rect
        self.color = color
        self.bg_color = bg_color

    def update(self):
        pass

    def draw(self):
        self.draw_window()

    def draw_window(self):
        pygame.draw.rect(self.game.screen, self.color, self.rect)
        # Border
        pygame.draw.rect(self.game.screen, self.bg_color, (self.rect[0]-PADDING, self.rect[1]-PADDING, self.rect[2]+(2*PADDING), self.rect[3]+(2*PADDING)), PADDING)