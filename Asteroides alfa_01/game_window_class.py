import pygame
from settings import *

class GameWindow:
    def __init__(self, game):
        self.game = game

    def update(self):
        pass

    def draw(self):
        self.draw_game_window()

    def draw_game_window(self):
        self.game.screen.fill('black')
        pygame.draw.rect(self.game.screen, 'grey', INFO_RECT)
        pygame.draw.rect(self.game.screen, 'grey', PLAY_RECT)

    def draw_intro_window(self):
        self.game.screen.fill('grey')
        pygame.draw.rect(self.game.screen, 'black', INTRO_RECT)