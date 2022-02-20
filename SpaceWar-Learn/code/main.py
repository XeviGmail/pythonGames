import sys

import pygame
from sys import exit
from player import Player
from rock import Rock

class Game():
    def __init__(self):
        player_sprite = Player((screen_width/2, screen_height), speed_player, (0,screen_width))
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.rocks = pygame.sprite.Group()
        for i in range(4):
            rock_sprite = Rock(screen_width, screen_height)
            self.rocks.add(rock_sprite)

    def collision_checks(self):
        # player laser
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                if pygame.sprite.spritecollide(laser, self.rocks, True):
                    laser.kill()
                    rock_sprite = Rock(screen_width, screen_height)
                    self.rocks.add(rock_sprite)
        # rocks
        if self.rocks:
            for rock in self.rocks:
                rocas = self.rocks.copy()
                rocas.remove(rock)
                if pygame.sprite.spritecollide(rock, self.player, False):
                    rock.kill()
                    # pygame.quit()
                    # sys.exit()
                rocas_chocando = pygame.sprite.spritecollide(rock, rocas, False)
                if rocas_chocando:
                    pygame.quit()
                    sys.exit()

    def run(self):
        self.player.update()
        self.rocks.update()
        self.rocks.draw(screen)
        self.player.sprite.lasers.draw(screen)
        self.collision_checks()
        self.player.draw(screen)

if __name__ == '__main__':
    pygame.init()
    FPS = 60
    speed_player = 5
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Space War Learning')
    clock = pygame.time.Clock()
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill('grey')
        game.run()
        pygame.display.flip()
        clock.tick(FPS)