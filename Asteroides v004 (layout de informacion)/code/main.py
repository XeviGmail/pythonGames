import pygame, pymunk, sys
import random
from player import Player
from layout import Layout
from rock import Rock

class Game():
    def __init__(self):
        self.FPS = 60
        self.clock = pygame.time.Clock()
        # Edges
        self.width = 1024
        self.height = 800
        self.space = pymunk.Space()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Asteroides')

        # Layouts
        padding = 10
        layout_info_rect = {
            'x': padding,
            'y': padding,
            'width': int((self.width-padding) / 3) - 2 * padding,
            'height': self.height - 2 * padding
        }
        self.layout_info = Layout(self.screen, layout_info_rect, 'grey')
        self.layout_play_rect = {
            'x': int((self.width-padding) / 3),
            'y': padding,
            'width': 2 * int((self.width-padding) / 3),
            'height': self.height - (2 * padding)
        }
        self.layout_play = Layout(self.screen, self.layout_play_rect, 'grey')

        # Player
        player_speed = 5
        player = Player((500, 500), player_speed, self.layout_play_rect)
        self.player = pygame.sprite.GroupSingle(player)

        # Rocks (space, pos, velocity, radius, rect):
        self.rocks = pygame.sprite.Group()
        for _ in range(8):
            velocity = (random.uniform(-60, 60), random.uniform(-200, 0))
            radio = random.randint(1, 3) * 20
            pos_x = random.uniform(self.layout_play_rect['x'] + radio,
                                   self.layout_play_rect['x'] + self.layout_play_rect['width'] - radio)
            pos_y = self.layout_play_rect['y'] - radio
            self.rock_sprite = Rock(self.space, (pos_x, pos_y), velocity, radio, self.layout_play_rect)
            self.rocks.add(self.rock_sprite)

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

    def bounds(self):
        for rock in self.rocks:
            if rock.get_out_of_bounds():
                rock.set_out_of_bounds(False)
                rock.eliminar()
                velocity = (random.uniform(-60, 60), random.uniform(-200, 0))
                radio = random.randint(1, 3) * 20
                pos_x = random.uniform(self.layout_play_rect['x'] + radio, self.layout_play_rect['x'] + self.layout_play_rect['width'] - radio)
                pos_y = self.layout_play_rect['y'] - radio
                self.rock_sprite = Rock(self.space, (pos_x, pos_y), velocity, radio,  self.layout_play_rect)
                self.rocks.add(self.rock_sprite)

    def run(self):
        self.screen.fill('black')
        # Layout de Juego
        self.layout_play.update()
        self.player.update()
        self.player.draw(self.screen)
        # Rocas
        self.rocks.update()
        self.rocks.draw(self.screen)
        # Layout de Informacion
        self.layout_info.update()
        self.write_info()
        self.bounds()
        pygame.display.flip()
        self.clock.tick(self.FPS)
        self.space.step(1 / self.FPS)

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


