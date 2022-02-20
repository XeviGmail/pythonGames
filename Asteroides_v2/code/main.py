import random
import pygame, sys
import pymunk
from player import Player
from rock import Rock
from edge import Edge

def cc(point):
    return int(point[0]), screen_height-int(point[1])

class Game():
    def __init__(self, space, screen):
        # Edges
        self.space = space
        self.screen = screen

        # Rocks (space, pos_x, pos_y, velocity, radius)
        self.rocks = pygame.sprite.Group()
        for _ in range(8):
            velocity = (random.uniform(-60, 60), random.uniform(-200, 0))
            self.rock_sprite = Rock(self.space, random.uniform(50, 550), screen_height + 20, velocity, 20)
            self.rocks.add(self.rock_sprite)

        #Player
        self.player_sprite = Player((screen_width/2, screen_height-10), speed_player, (0, screen_width, 0, screen_height))
        self.player = pygame.sprite.GroupSingle(self.player_sprite)

    def collision_checks(self):
        # player laser
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                laser_rocks_colision = pygame.sprite.spritecollide(laser, self.rocks, False)
                if laser_rocks_colision:
                    for rock in laser_rocks_colision:
                        rock.eliminar()
                        velocity = (random.uniform(-60, 60), random.uniform(-200, 0))
                        self.rock_sprite = Rock(self.space, random.uniform(50, 550), screen_height + 20, velocity, 20)
                        self.rocks.add(self.rock_sprite)
                    laser.kill()
        # colision de rocas con player
        player_rocks_collision = pygame.sprite.spritecollide(self.player_sprite, self.rocks, False)
        if player_rocks_collision:
            for rock in player_rocks_collision:
                rock.eliminar()
                velocity = (random.uniform(-60, 60), random.uniform(-200, 0))
                self.rock_sprite = Rock(self.space, random.uniform(50, 550), screen_height + 20, velocity, 20)
                self.rocks.add(self.rock_sprite)

    def bounds(self):
        for rock in self.rocks:
            if rock.rect.x <= -50 or rock.rect.x >= 650 or rock.rect.y <= -50 or rock.rect.y >= 650 :
                rock.eliminar()
                velocity = (random.uniform(-60, 60), random.uniform(-200, 0))
                self.rock_sprite = Rock(self.space, random.uniform(50, 550), screen_height + 20, velocity, 20)
                self.rocks.add(self.rock_sprite)

    def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.rocks.update()
        self.rocks.draw(screen)
        self.bounds()
        self.collision_checks()

if __name__ == '__main__':
    pygame.init()
    FPS = 60
    speed_player = 5
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    space = pymunk.Space()

    game = Game(space, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('grey')
        game.run()

        pygame.display.flip()
        clock.tick(FPS)
        space.step(1/FPS)