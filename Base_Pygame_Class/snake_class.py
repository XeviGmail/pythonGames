import random
import copy
import pygame
from settings import *
from food_class import *

class Snake:
    def __init__(self, game):
        self.game = game
        self.game_window = game.game_window
        self.origin = copy.deepcopy(self.game_window.pos)
        self.pos = [self.game_window.cols//2, self.game_window.rows//2]
        self.direction = [1, 0]
        self.body = []
        self.length = 1

    def update(self):
        if self.game.frame_count % (FPS//3) == 0:
            self.pos[0] += self.direction[0]
            self.pos[1] += self.direction[1]
            if self.pos[0] < 0 or self.pos[0] > self.game_window.cols - 1:
                self.die()
            if self.pos[1] < 0 or self.pos[1] > self.game_window.rows - 1:
                self.die()
            if self.pos == self.game.food.pos:
                self.eat()
            self.set_body()

    def draw(self):
        for pos in self.body:
            pygame.draw.rect(self.game.screen, BLACK,
                         (self.origin[0]+(pos[0]*CELL_SIZE), self.origin[1]+(pos[1]*CELL_SIZE), CELL_SIZE, CELL_SIZE))

    def set_body(self):
        self.body.insert(0, [self.pos[0], self.pos[1]])
        self.body = self.body[:self.length]

    def eat(self):
        self.length += 1
        self.game.food = Food(self.game)

    def die(self):
        self.game.state = 'dead'
        self.game.active_buttons = self.game.dead_buttons