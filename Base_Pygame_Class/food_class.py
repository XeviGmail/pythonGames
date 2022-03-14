import random, copy
import pygame
from settings import *

class Food:
    def __init__(self, game):
        self.game = game
        self.game_window = self.game.game_window
        self.origin = copy.deepcopy(self.game_window.pos)
        self.pos = [random.randint(0, self.game.game_window.cols-1),
                    random.randint(0, self.game.game_window.rows-1)]

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.game.screen, FOOD_COLOR,
                         (self.origin[0] + (self.pos[0] * CELL_SIZE), self.origin[1] + (self.pos[1]*CELL_SIZE), CELL_SIZE, CELL_SIZE))