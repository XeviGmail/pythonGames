import pygame, pymunk, sys, os.path
import random
from player import Player
from layout import Layout
from rock import Rock
from residuo import Residuo

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
        x = self.layout_play_rect['x'] + self.layout_play_rect['width'] / 2
        y = self.layout_play_rect['y'] + self.layout_play_rect['height']
        self.player_sprite = Player((x, y), player_speed, self.layout_play_rect, self.screen, self.get_player_image())
        self.player = pygame.sprite.GroupSingle(self.player_sprite)

        # Rocks (space, pos, velocity, radius, rect):
        self.rocks = pygame.sprite.Group()
        self.rock_radio_base = 20
        self.num_rocks = 8
        for _ in range(self.num_rocks):
            velocity = (random.uniform(-60, 60), random.uniform(-200, 0))
            radio = random.randint(1, 3) * self.rock_radio_base
            pos_x = random.uniform(self.layout_play_rect['x'] + radio,
                                   self.layout_play_rect['x'] + self.layout_play_rect['width'] - radio)
            pos_y = self.layout_play_rect['y'] - radio
            self.rock_sprite = Rock(self.space, (pos_x, pos_y), velocity, radio, self.layout_play_rect)
            self.rocks.add(self.rock_sprite)

        # residuos
        self.residuos = pygame.sprite.Group()

        # Puntuaciones
        self.asteroides = 0
        self.num_residuos = 0

    def collision_check(self):
        # player laser
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                laser_rocks_colision = pygame.sprite.spritecollide(laser, self.rocks, False)
                if laser_rocks_colision:
                    for rock in laser_rocks_colision:
                        radio = rock.radius - self.rock_radio_base
                        pos = (rock.rect.x, rock.rect.y)

                        if radio:
                            self.rock_sprite = Rock(self.space, pos, (random.uniform(-60, 60), random.uniform(-200, 0)), radio, self.layout_play_rect)
                            self.rocks.add(self.rock_sprite)
                            self.rock_sprite = Rock(self.space, pos, (random.uniform(-60, 60), random.uniform(-200, 0)), radio, self.layout_play_rect)
                            self.rocks.add(self.rock_sprite)
                        else:
                            self.asteroides += 1
                            residuo_sprite = Residuo((rock.rect.x, rock.rect.y), self.rock_radio_base, rock.body.velocity, self.layout_play_rect)
                            self.residuos.add(residuo_sprite)
                            if len(self.rocks) < self.num_rocks:
                                pos_x = random.uniform(self.layout_play_rect['x'] + radio,
                                                       self.layout_play_rect['x'] + self.layout_play_rect['width'] - radio)
                                pos_y = self.layout_play_rect['y'] - radio
                                radio = random.randint(1, 3) * self.rock_radio_base
                                self.rock_sprite = Rock(self.space, (pos_x, pos_y), (random.uniform(-60, 60), random.uniform(-200, 0)), radio, self.layout_play_rect)
                                self.rocks.add(self.rock_sprite)
                        rock.eliminar()
                        laser.kill()

        # Captura de residuos
        player_residuos_collision = pygame.sprite.spritecollide(self.player_sprite, self.residuos, False)
        if player_residuos_collision:
            for residuo in player_residuos_collision:
                residuo.kill()
                self.num_residuos += 1

    def write_info(self):
        score = 103
        tecnicos = 23
        ships = 5
        laser_cooldown = 600
        self.layout_info.write(0, 'General Information')
        self.layout_info.write(2, 'Points', str(score).zfill(5))
        self.layout_info.write(3, 'Rubidio', str(self.num_residuos).zfill(5))
        self.layout_info.write(4, 'Ships', str(ships).zfill(5))
        self.layout_info.write(5, 'Tecknics', str(tecnicos).zfill(5))
        self.layout_info.write(6, 'Ship Speed', str(tecnicos).zfill(5))
        self.layout_info.write(7, 'Laser Speed', str(tecnicos).zfill(5))
        self.layout_info.write(8, 'Laser Cooldown', str(laser_cooldown))
        self.layout_info.write(9, 'Laser Power', '15')
        self.layout_info.write(10, 'Asteroides', str(self.asteroides).zfill(5))

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

    def get_player_image(self):
        animacion_nave = []
        for i in range(15):
            archivo_nave = f'nave-1-{i:02d}.png'
            image_raw = pygame.image.load(os.path.join('../graphics/ship/01', archivo_nave))
            image = pygame.transform.scale(image_raw, (64, 32))
            animacion_nave.append(image)
        return animacion_nave

    def run(self):
        self.screen.fill('black')
        # Layout de Juego
        self.layout_play.update()
        self.player.update()
        self.player.draw(self.screen)
        # Rocas
        self.rocks.update()
        self.rocks.draw(self.screen)
        # Residuos
        self.residuos.update()
        self.residuos.draw(self.screen)
        # Layout de Informacion
        self.layout_info.update()
        self.write_info()
        self.bounds()
        self.collision_check()
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


