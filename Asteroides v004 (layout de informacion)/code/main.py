import os.path
import random
import pygame, sys
from layout import Layout
class Game():
    def __init__(self):
        self.FPS = 60
        self.clock = pygame.time.Clock()
        # Edges
        self.width = 1024
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Asteroides')

        # Layouts
        padding = 10
        self.layout_info = Layout(self.screen, padding, padding, int((self.width-padding) / 3) - 2 * padding, self.height - 2 * padding, 'grey')
        self.layout_play = Layout(self.screen, int((self.width-padding) / 3), padding, 2 * int((self.width-padding) / 3), self.height - (2 * padding), 'grey')

    def write_info(self):
        score = 103
        asteroider = 1
        tecnicos = 23
        ships = 5
        laser_cooldown = 600
        self.layout_info.write(0, 'General Information')
        self.layout_info.write(2, 'Points', str(score).zfill(5))
        self.layout_info.write(3, 'Rubidio', str(asteroider).zfill(5))
        self.layout_info.write(4, 'Ships', str(ships).zfill(5))
        self.layout_info.write(5, 'Tecknics', str(tecnicos).zfill(5))
        self.layout_info.write(6, 'Ship Speed', str(tecnicos).zfill(5))
        self.layout_info.write(7, 'Laser Speed', str(tecnicos).zfill(5))
        self.layout_info.write(8, 'Laser Cooldown', str(laser_cooldown))
        self.layout_info.write(9, 'Laser Power', '15')

    def run(self):
        self.screen.fill('black')
        # Layout de Informacion
        self.layout_info.update()
        self.write_info()
        # Layout de Juego
        self.layout_play.update()
        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
        game.run()


