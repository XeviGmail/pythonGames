import random
import pygame
import pymunk

class Rock(pygame.sprite.Sprite):
    def __init__(self, space, x, y, velocity, rock_radius, screen_width, screen_height):
        super().__init__()
        self.space = space
        self.rock_radius = rock_radius
        self.body = pymunk.Body()
        self.body.position = x, y
        self.body.velocity = velocity
        self.shape = pymunk.Circle(self.body, self.rock_radius)
        self.shape.elasticity = 1
        self.shape.density = 1
        self.space.add(self.body, self.shape)
        self.screen_width = screen_width
        self.screen_height = screen_height

        image_raw = pygame.image.load('../graphics/rocks/rock0.png')
        self.image = pygame.transform.scale(image_raw, (2 * self.rock_radius, 2 * self.rock_radius))
        self.rect = self.image.get_rect()

    def eliminar(self):
        self.kill()
        self.space.remove(self.body, self.shape)

    def cc(self, point):
        return int(point[0]), self.screen_height - int(point[1])

    def update(self):
        x, y = self.cc(self.body.position)
        self.rect.x = x-self.rock_radius
        self.rect.y = y-self.rock_radius
