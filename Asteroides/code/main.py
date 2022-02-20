import random
import pygame, sys
import pymunk
from player import Player

def cc(point):
    return int(point[0]), screen_height-int(point[1])

class Rock(pygame.sprite.Sprite):
    def __init__(self, x, y, rock_radius):
        super().__init__()
        self.rock_radius = rock_radius
        self.body = pymunk.Body()
        self.body.position = x, y
        self.body.velocity = random.uniform(-200, 200), random.uniform(-200, 200)
        self.shape = pymunk.Circle(self.body, self.rock_radius)
        self.shape.elasticity = 1
        self.shape.density = 1
        space.add(self.body, self.shape)

        image_raw = pygame.image.load('../graphics/rocks/rock0.png')
        self.image = pygame.transform.scale(image_raw, (2 * self.rock_radius, 2 * self.rock_radius))
        self.rect = self.image.get_rect()

    def eliminar(self):
        space.remove(self.body, self.shape)
        self.kill()

    def update(self):
        x, y = cc(self.body.position)
        self.rect.x = x-self.rock_radius
        self.rect.y = y-self.rock_radius

class Edge():
    def __init__(self, pos_i, pos_f):
        self.pos_i = pos_i
        self.pos_f = pos_f
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, self.pos_i, self.pos_f, 1)
        self.shape.elasticity = 1
        space.add(self.body, self.shape)
    def draw(self):
        pygame.draw.line(screen, 'black', cc(self.pos_i), cc(self.pos_f))

class Game():
    def __init__(self):
        # Edges
        self.edge_bottom = Edge((10, 10), (585, 10))
        self.edge_top = Edge((10, 585), (585, 585))
        self.edge_left = Edge((10, 10), (10, 585))
        self.edge_right = Edge((585, 10), (585, 585))

        # Rocks
        rock_sprite = Rock(200, screen_height - 20, 20)
        self.rocks = pygame.sprite.Group()
        self.rocks.add(rock_sprite)
        rock_sprite = Rock(200, screen_height - 20, 20)
        self.rocks.add(rock_sprite)
        rock_sprite = Rock(200, screen_height - 20, 20)
        self.rocks.add(rock_sprite)
        rock_sprite = Rock(200, screen_height - 20, 20)
        self.rocks.add(rock_sprite)

        #Player
        self.player_sprite = Player((screen_width/2, screen_height-300), speed_player, (0, screen_width, 0, screen_height))
        self.player = pygame.sprite.GroupSingle(self.player_sprite)

    def collision_checks(self):
        # player laser
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                laser_rocks_colision = pygame.sprite.spritecollide(laser, self.rocks, False)
                if laser_rocks_colision:
                    for rock in laser_rocks_colision:
                        rock.eliminar()
                    laser.kill()
        player_rocks_collision = pygame.sprite.spritecollide(self.player_sprite, self.rocks, False)
        if player_rocks_collision:
            for rock in player_rocks_collision:
                rock.eliminar()




    def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.rocks.update()
        self.rocks.draw(screen)
        self.edge_bottom.draw()
        self.edge_top.draw()
        self.edge_left.draw()
        self.edge_right.draw()
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

    game = Game()

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