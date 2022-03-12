import pygame
from settings import *

class GameWindow():
    def __init__(self, game):
        self.game = game
        self.pos = OFFSET
        self.width = SCREEN_WIDTH - OFFSET[0]*2
        self.height = SCREEN_HEIGHT - OFFSET[1] - OFFSET[0]
        self.rows = self.height // CELL_SIZE
        self.cols = self.width // CELL_SIZE

    def update(self):
        self.game.snake.update()
        self.game.food.update()

    def draw(self):
        self.draw_game_window()
        self.draw_grid()
        self.game.snake.draw()
        self.game.food.draw()

    def draw_grid(self):
        for x in range(self.width//CELL_SIZE):
            for y in range(self.height//CELL_SIZE):
                pygame.draw.line(self.game.screen, BLACK,
                                 (self.pos[0]+(CELL_SIZE*x), self.pos[1]),
                                 (self.pos[0]+(CELL_SIZE*x), self.pos[1]+self.height))
                pygame.draw.line(self.game.screen, BLACK,
                                 (self.pos[0], self.pos[1]+(CELL_SIZE*y)),
                                 (self.pos[0]+self.width, self.pos[1]+(CELL_SIZE*y)))

    def draw_game_window(self):
        pygame.draw.rect(self.game.screen, WHITE, (self.pos[0], self.pos[1], self.width, self.height))
        # Border
        pygame.draw.rect(self.game.screen, BLACK, (self.pos[0]-BORDER_THICKNESS, self.pos[1]-BORDER_THICKNESS, self.width+BORDER_THICKNESS, self.height+BORDER_THICKNESS), BORDER_THICKNESS)